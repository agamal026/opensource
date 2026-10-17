#!/usr/bin/env python3
"""Validate and report a manually reviewed contribution campaign, offline.

Python 3.10+; standard library only. This tool never queries Git/GitHub or submits
work. Evidence requirements validate the record's structure, not external facts.
See docs/CAMPAIGN-DATA.md for the schema and accounting rules.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
from decimal import Decimal, localcontext
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import urlsplit


STAGES = ("target", "screened", "selected", "reproduced", "validated", "submitted", "accepted")
STAGE_FIELDS = {
    "target": set(),
    "screened": {"policy_ref"},
    "selected": {"selection_ref"},
    "reproduced": {"source_commit", "source_ref", "validation"},
    "validated": {"source_commit", "source_ref", "validation", "review_ref"},
    "submitted": {"pr_url", "source_commit"},
    "accepted": {"acceptance_ref"},
}
HANDLE = r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?"
REPOSITORY = re.compile(rf"{HANDLE}/[A-Za-z0-9_.-]+\Z")
SHA = re.compile(r"[0-9a-f]{40}\Z")
AMOUNT = re.compile(r"(?:0|[1-9][0-9]{0,17})(?:\.[0-9]{1,8})?\Z")
MAX_INPUT_BYTES = 4 * 1024 * 1024


class ValidationError(ValueError):
    """A campaign record cannot support the requested report."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def fields(value: object, required: set[str], where: str, optional: set[str] | None = None) -> dict:
    require(isinstance(value, dict), f"{where}: expected an object")
    require(required <= value.keys() <= required | (optional or set()),
            f"{where}: missing or unexpected fields")
    return value


def text(value: object, where: str, limit: int = 4000) -> str:
    require(isinstance(value, str) and bool(value.strip()) and len(value) <= limit,
            f"{where}: expected a nonempty bounded string")
    require(not any(ord(c) < 32 or ord(c) == 127 for c in value),
            f"{where}: control characters are not allowed")
    require(not any(0xD800 <= ord(c) <= 0xDFFF for c in value),
            f"{where}: surrogate code points are not allowed")
    return value


def integer(value: object, where: str) -> int:
    require(type(value) is int and value > 0, f"{where}: expected a positive integer")
    return value


def day(value: object, where: str) -> date:
    value = text(value, where, 10)
    require(bool(re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value)),
            f"{where}: expected YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{where}: invalid calendar date") from exc


def repository(value: object, owner: str, where: str) -> str:
    value = text(value, where, 140)
    require(bool(REPOSITORY.fullmatch(value)) and value.split("/")[-1] not in {".", ".."},
            f"{where}: expected a GitHub OWNER/REPO")
    require(value.split("/")[0].casefold() != owner.casefold(),
            f"{where}: owner-account repositories are not external contributions")
    return value


def url(value: object, where: str) -> str:
    value = text(value, where, 2048)
    require(not any(c.isspace() or c in '<>\\"' for c in value), f"{where}: invalid URL characters")
    try:
        parts = urlsplit(value)
        valid = (parts.scheme == "https" and bool(parts.hostname)
                 and parts.username is None and parts.password is None
                 and parts.port in {None, 443})
    except ValueError:
        valid = False
    require(valid, f"{where}: expected an HTTPS evidence URL without credentials")
    return value


def refs(value: object, where: str, *, empty: bool = False) -> list[str]:
    require(isinstance(value, list) and (empty or bool(value)), f"{where}: expected evidence references")
    for index, item in enumerate(value):
        url(item, f"{where}[{index}]")
    require(len(set(value)) == len(value), f"{where}: duplicate evidence reference")
    return value


def commit(value: object, where: str) -> str:
    value = text(value, where, 40)
    require(bool(SHA.fullmatch(value)), f"{where}: expected a full lowercase 40-character Git SHA")
    return value


def pr_url(value: object, repo: str, where: str) -> str:
    value = url(value, where)
    require(bool(re.fullmatch(rf"https://github\.com/{re.escape(repo)}/pull/[1-9][0-9]*", value, re.I)),
            f"{where}: expected a canonical pull request URL in this upstream repository")
    return value


def acceptance_ref(value: object, repo: str, pull: str, where: str) -> str:
    value = url(value, where)
    pull_pattern = re.escape(pull) + r"(?:#(?:issuecomment-|pullrequestreview-)[1-9][0-9]*)?"
    commit_pattern = rf"https://github\.com/{re.escape(repo)}/commit/[0-9a-f]{{40}}"
    require(bool(re.fullmatch(rf"(?:{pull_pattern}|{commit_pattern})", value, re.I)),
            f"{where}: expected the submitted PR, its acceptance comment/review, or an upstream commit")
    return value


def validate_route(value: object, updated: date, where: str) -> None:
    route = fields(value, {"kind", "qualification", "checked_on", "summary", "refs"}, where)
    require(route["kind"] in ("cash", "subscription", "credits", "indirect", "unconfirmed"),
            f"{where}.kind: unsupported benefit route")
    require(route["qualification"] in ("unverified", "conditional", "eligible", "ineligible", "not_applicable"),
            f"{where}.qualification: unsupported qualification")
    require(day(route["checked_on"], where + ".checked_on") <= updated,
            f"{where}.checked_on: after updated_on")
    text(route["summary"], where + ".summary")
    unknown = route["kind"] == "unconfirmed" and route["qualification"] == "unverified"
    require(route["kind"] != "unconfirmed" or unknown,
            f"{where}: an unconfirmed route must be unverified")
    require(route["qualification"] != "not_applicable" or route["kind"] == "indirect",
            f"{where}: not_applicable is only for indirect benefits")
    refs(route["refs"], where + ".refs", empty=unknown)


def validate_milestones(value: object, repo: str, started: date, updated: date, where: str) -> None:
    require(isinstance(value, list) and 1 <= len(value) <= len(STAGES),
            f"{where}: expected a nonempty ordered milestone history")
    previous = started
    for index, item in enumerate(value):
        location = f"{where}[{index}]"
        require(isinstance(item, dict), f"{location}: expected an object")
        stage = item.get("stage")
        require(stage == STAGES[index], f"{location}.stage: unsupported, skipped, repeated, or out-of-order stage")
        fields(item, {"stage", "date", "refs"} | STAGE_FIELDS[stage], location)
        observed = day(item["date"], location + ".date")
        require(previous <= observed <= updated,
                f"{location}.date: outside campaign dates or earlier than the preceding milestone")
        previous = observed
        refs(item["refs"], location + ".refs")
        for key in ("policy_ref", "selection_ref", "review_ref"):
            if key in item:
                url(item[key], location + "." + key)
        if "source_commit" in item:
            commit(item["source_commit"], location + ".source_commit")
        if stage in {"reproduced", "validated"}:
            source = url(item["source_ref"], location + ".source_ref")
            require(bool(re.fullmatch(rf"https://github\.com/{HANDLE}/[A-Za-z0-9_.-]+/commit/{item['source_commit']}", source, re.I)),
                    f"{location}.source_ref: expected a GitHub commit URL matching source_commit")
            validation = fields(item["validation"], {"command", "result", "ref"}, location + ".validation")
            text(validation["command"], location + ".validation.command")
            require(validation["result"] == ("reproduced" if stage == "reproduced" else "passed"),
                    f"{location}.validation.result: does not establish this milestone")
            url(validation["ref"], location + ".validation.ref")
        if stage == "submitted":
            pr_url(item["pr_url"], repo, location + ".pr_url")
            require(item["source_commit"] == value[index - 1]["source_commit"],
                    f"{location}.source_commit: submission differs from the validated source")
        if stage == "accepted":
            acceptance_ref(item["acceptance_ref"], repo, value[index - 1]["pr_url"], location + ".acceptance_ref")


def validate_benefits(value: object, updated: date, seen: set[str], where: str) -> None:
    require(isinstance(value, list), f"{where}: expected an array")
    for index, item in enumerate(value):
        location = f"{where}[{index}]"
        fields(item, {"id", "kind", "state", "date", "summary", "refs"}, location,
               {"amount", "currency", "grant_ref", "activation_ref", "receipt_ref"})
        identifier = text(item["id"], location + ".id", 100)
        require(bool(re.fullmatch(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*", identifier)),
                f"{location}.id: expected a lowercase identifier")
        require(identifier not in seen, f"{location}.id: duplicate benefit identifier")
        seen.add(identifier)
        require(item["kind"] in ("cash", "subscription", "credits"), f"{location}.kind: unsupported benefit kind")
        state = item["state"]
        require(state in ("advertised", "granted", "activated", "paid"), f"{location}.state: unsupported benefit state")
        require(day(item["date"], location + ".date") <= updated, f"{location}.date: after updated_on")
        text(item["summary"], location + ".summary")
        refs(item["refs"], location + ".refs")
        for key in ("grant_ref", "activation_ref", "receipt_ref"):
            if key in item:
                url(item[key], location + "." + key)
        if state in {"granted", "activated", "paid"}:
            key = {"granted": "grant_ref", "activated": "activation_ref", "paid": "receipt_ref"}[state]
            require(key in item, f"{location}: missing evidence for benefit state")
        require(state != "paid" or item["kind"] == "cash", f"{location}: paid is only for cash")
        require(state != "activated" or item["kind"] != "cash", f"{location}: cash cannot be activated")
        require(("amount" in item) == ("currency" in item), f"{location}: amount and currency must occur together")
        if "amount" in item:
            require(item["kind"] == "cash", f"{location}: monetary amounts are only for cash")
            amount = text(item["amount"], location + ".amount", 27)
            require(bool(AMOUNT.fullmatch(amount)) and Decimal(amount) > 0,
                    f"{location}.amount: expected a positive exact decimal string")
            require(isinstance(item["currency"], str) and bool(re.fullmatch(r"[A-Z]{3}", item["currency"])),
                    f"{location}.currency: expected a three-letter uppercase currency code")
        require(state != "paid" or "amount" in item, f"{location}: paid cash requires an amount and currency")


def validate_campaign(value: object) -> dict:
    data = fields(value, {"schema_version", "owner", "started_on", "updated_on", "target_count", "projects"},
                  "campaign", {"historical_submissions"})
    require(type(data["schema_version"]) is int and data["schema_version"] == 1, "campaign: unsupported schema_version")
    owner = text(data["owner"], "campaign.owner", 39)
    require(bool(re.fullmatch(HANDLE, owner)), "campaign.owner: expected a GitHub account name")
    started = day(data["started_on"], "campaign.started_on")
    updated = day(data["updated_on"], "campaign.updated_on")
    require(started <= updated, "campaign.updated_on: before started_on")
    integer(data["target_count"], "campaign.target_count")
    require(isinstance(data["projects"], list), "campaign.projects: expected an array")
    seen_repositories: set[str] = set()
    seen_benefits: set[str] = set()
    for index, project in enumerate(data["projects"]):
        where = f"campaign.projects[{index}]"
        fields(project, {"repository", "batch", "summary", "next_action", "benefit_route", "milestones", "benefits"}, where)
        repo = repository(project["repository"], owner, where + ".repository")
        require(repo.casefold() not in seen_repositories, f"{where}.repository: duplicate target repository")
        seen_repositories.add(repo.casefold())
        integer(project["batch"], where + ".batch")
        text(project["summary"], where + ".summary")
        text(project["next_action"], where + ".next_action")
        validate_route(project["benefit_route"], updated, where + ".benefit_route")
        validate_milestones(project["milestones"], repo, started, updated, where + ".milestones")
        validate_benefits(project["benefits"], updated, seen_benefits, where + ".benefits")
    history = data.get("historical_submissions", [])
    require(isinstance(history, list), "campaign.historical_submissions: expected an array")
    seen_pulls: set[str] = set()
    for index, item in enumerate(history):
        where = f"campaign.historical_submissions[{index}]"
        fields(item, {"repository", "pr_url", "submitted_on", "refs"}, where, {"accepted_on", "acceptance_ref"})
        repo = repository(item["repository"], owner, where + ".repository")
        pull = pr_url(item["pr_url"], repo, where + ".pr_url")
        require(pull.casefold() not in seen_pulls, f"{where}.pr_url: duplicate historical submission")
        seen_pulls.add(pull.casefold())
        submitted = day(item["submitted_on"], where + ".submitted_on")
        require(submitted < started, f"{where}.submitted_on: historical submissions must predate the campaign")
        refs(item["refs"], where + ".refs")
        require(("accepted_on" in item) == ("acceptance_ref" in item), f"{where}: acceptance requires its date and upstream evidence")
        if "accepted_on" in item:
            require(submitted <= day(item["accepted_on"], where + ".accepted_on") <= updated,
                    f"{where}.accepted_on: outside submission/updated dates")
            acceptance_ref(item["acceptance_ref"], repo, pull, where + ".acceptance_ref")
    for project in data["projects"]:
        for item in project["milestones"]:
            require(item.get("pr_url", "").casefold() not in seen_pulls,
                    "campaign: a historical PR cannot also count as a new campaign submission")
    return data


def unique_pairs(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, "campaign JSON: duplicate object key")
        result[key] = value
    return result


def invalid_constant(_: str) -> None:
    raise ValidationError("campaign JSON: non-finite numbers are not allowed")


def load_campaign(path: Path) -> dict:
    try:
        with path.open("rb") as handle:
            raw = handle.read(MAX_INPUT_BYTES + 1)
        require(len(raw) <= MAX_INPUT_BYTES, "campaign JSON: input exceeds 4 MiB")
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs, parse_constant=invalid_constant)
    except OSError as exc:
        raise ValidationError("campaign JSON: could not read input") from exc
    except (ValueError, RecursionError) as exc:
        if isinstance(exc, ValidationError):
            raise
        raise ValidationError("campaign JSON: invalid JSON or encoding") from exc
    return validate_campaign(value)


def md(value: str) -> str:
    value = html.escape(value, quote=True)
    return re.sub(r"([\\`*_{}\[\]()#+.!|~-])", r"\\\1", value)


def link(label: str, reference: str) -> str:
    return f"[{md(label)}](<{reference}>)"


def reached(project: dict, stage: str) -> bool:
    return len(project["milestones"]) > STAGES.index(stage)


def paid_totals(projects: list[dict], started_on: str) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    with localcontext() as context:
        context.prec = 60  # Exact addition for the bounded input and amount sizes.
        for project in projects:
            for benefit in project["benefits"]:
                if benefit["state"] == "paid" and benefit["date"] >= started_on:
                    currency = benefit["currency"]
                    totals[currency] = totals.get(currency, Decimal(0)) + Decimal(benefit["amount"])
    return totals


def render_campaign(data: dict, batch: int | None = None) -> str:
    # Public callers get the same validation guarantees as the CLI, including
    # invalid records outside a requested batch.
    validate_campaign(data)
    if batch is not None:
        integer(batch, "report.batch")
    projects = sorted((p for p in data["projects"] if batch is None or p["batch"] == batch),
                      key=lambda p: (p["batch"], p["repository"].casefold()))
    submitted = sum(reached(p, "submitted") for p in data["projects"])
    history = data.get("historical_submissions", [])
    lines = ["# Contribution campaign", "",
             f"Started: {data['started_on']}. Records reviewed through: {data['updated_on']}.", "",
             f"**Goal progress: {submitted} / {data['target_count']} distinct external repositories with qualified campaign submissions.**", "",
             f"Full research queue: {len(data['projects'])} repositories. Historical submissions: {len(history)}; excluded from this goal.", "",
             "A qualified submission has the policy, selection, reproduction, exact source, passing validation, review and upstream PR evidence required by the schema. It does not establish acceptance or benefit eligibility.", "",
             "This offline report checks record structure and consistency. Verify what the linked evidence establishes, current policies, ownership and benefit eligibility. This offline tool does not start background work.", ""]
    if batch is not None:
        lines += [f"## Batch {batch}", "", "Stage and benefit totals below cover this batch only; goal progress above covers the full campaign.", ""]
    lines += ["## Contribution stages", "", "| Stage | Currently at stage | Reached in displayed queue |", "| --- | ---: | ---: |"]
    current = Counter(p["milestones"][-1]["stage"] for p in projects)
    for stage in STAGES:
        lines.append(f"| {stage} | {current[stage]} | {sum(reached(p, stage) for p in projects)} |")
    lines += ["", "## Batches", "", "| Batch | Targets | Screened | Selected | Qualified submitted | Accepted |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for number in sorted({p["batch"] for p in projects}):
        group = [p for p in projects if p["batch"] == number]
        counts = [len(group)] + [sum(reached(p, s) for p in group) for s in ("screened", "selected", "submitted", "accepted")]
        lines.append(f"| {number} | " + " | ".join(str(n) for n in counts) + " |")
    lines += ["", "## Benefits", "", "Only dated benefit records within this campaign appear in these totals. Advertised amounts, unpaid grants, subscriptions and credits are never converted into paid cash.", "",
              "| Kind | Advertised | Granted | Activated | Paid |", "| --- | ---: | ---: | ---: | ---: |"]
    benefits = Counter((b["kind"], b["state"]) for p in projects for b in p["benefits"] if b["date"] >= data["started_on"])
    for kind in ("cash", "subscription", "credits"):
        lines.append(f"| {kind} | " + " | ".join(str(benefits[kind, s]) for s in ("advertised", "granted", "activated", "paid")) + " |")
    totals = paid_totals(projects, data["started_on"])
    lines += ["", "Recorded paid cash: " + ("; ".join(f"{currency} {format(amount, 'f')}" for currency, amount in sorted(totals.items())) if totals else "none") + ".", "", "## Queue and evidence", ""]
    for project in projects:
        repo = project["repository"]
        route = project["benefit_route"]
        lines += [f"### {link(repo, 'https://github.com/' + repo)}", "",
                  f"Batch {project['batch']} · current stage: **{project['milestones'][-1]['stage']}**.", "",
                  md(project["summary"]), "", "Next action: " + md(project["next_action"]), "",
                  f"Benefit route: **{route['kind']} / {route['qualification']}**, checked {route['checked_on']}. " + md(route["summary"]), ""]
        if route["refs"]:
            lines += ["Route evidence: " + ", ".join(link(str(i + 1), r) for i, r in enumerate(route["refs"])) + ".", ""]
        for milestone in project["milestones"]:
            evidence = [link(f"evidence {i + 1}", r) for i, r in enumerate(milestone["refs"])]
            for key in ("policy_ref", "selection_ref", "review_ref", "pr_url", "acceptance_ref"):
                if key in milestone:
                    evidence.append(link(key, milestone[key]))
            if "source_ref" in milestone:
                evidence.append(link("source " + milestone["source_commit"], milestone["source_ref"]))
            elif "source_commit" in milestone:
                evidence.append("validated source " + milestone["source_commit"])
            lines.append(f"- {milestone['date']} **{milestone['stage']}**: " + "; ".join(evidence) + ".")
            if "validation" in milestone:
                validation = milestone["validation"]
                lines.append("  Validation command: " + md(validation["command"]) + "; result: **" + validation["result"] + "**; " + link("validation record", validation["ref"]) + ".")
        lines.append("")
        for benefit in project["benefits"]:
            detail = f"- Benefit {md(benefit['id'])}: **{benefit['kind']} / {benefit['state']}** on {benefit['date']}. " + md(benefit["summary"])
            if "amount" in benefit:
                detail += f" Amount in this state: {benefit['currency']} {benefit['amount']}."
            evidence = [link(f"evidence {i + 1}", r) for i, r in enumerate(benefit["refs"])]
            evidence += [link(k, benefit[k]) for k in ("grant_ref", "activation_ref", "receipt_ref") if k in benefit]
            lines.append(detail + " " + "; ".join(evidence) + ".")
        if project["benefits"]:
            lines.append("")
    lines += ["## Historical submissions (excluded from campaign progress)", ""]
    if not history:
        lines.append("None imported. Existing contribution history elsewhere in the hub remains separate.")
    else:
        for item in sorted(history, key=lambda h: (h["submitted_on"], h["pr_url"].casefold())):
            detail = "- " + link(item["repository"], item["pr_url"]) + f": submitted {item['submitted_on']}."
            if "accepted_on" in item:
                detail += " Accepted " + item["accepted_on"] + "; " + link("upstream acceptance", item["acceptance_ref"]) + "."
            lines.append(detail + " " + "; ".join(link(f"evidence {i + 1}", r) for i, r in enumerate(item["refs"])) + ".")
    return "\n".join(lines).rstrip() + "\n"


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "report"):
        sub = commands.add_parser(command)
        sub.add_argument("--input", type=Path, default=Path("data/campaign.json"))
        if command == "report":
            sub.add_argument("--batch", type=int)
            sub.add_argument("--output", type=Path)
            sub.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "report" and args.check and args.output is None:
        parser.error("--check requires --output")
    try:
        data = load_campaign(args.input)
        if args.command == "validate":
            submitted = sum(reached(p, "submitted") for p in data["projects"])
            print(f"Campaign is valid: {len(data['projects'])} targets; {submitted} / {data['target_count']} qualified submitted repositories.")
        else:
            content = render_campaign(data, args.batch)
            if args.output is None:
                sys.stdout.write(content)
            else:
                same_path = args.output.resolve() == args.input.resolve()
                if args.output.exists():
                    same_path = same_path or args.output.samefile(args.input)
                require(not same_path, "report: output must not overwrite campaign input")
                if args.check:
                    try:
                        current = args.output.read_bytes()
                    except FileNotFoundError:
                        current = None
                    if current != content.encode("utf-8"):
                        print("Campaign report is missing or out of date.", file=sys.stderr)
                        return 1
                else:
                    atomic_write(args.output, content)
        return 0
    except ValidationError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except OSError:
        print("Error: could not read or replace campaign report.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
