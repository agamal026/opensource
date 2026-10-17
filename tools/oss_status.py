#!/usr/bin/env python3
"""Validate, refresh, and render the public open-source contribution registry.

Python 3.10+; no dependencies. Only ``refresh`` accesses GitHub, using the local
authenticated gh CLI. It requests a fixed list of public metadata fields.

API transport: https://cli.github.com/manual/gh_api
Check states: https://docs.github.com/en/graphql/reference/checks
Commit statuses: https://docs.github.com/en/graphql/reference/commits
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime, timezone
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import quote, urlsplit


GH_FIELDS = (
    "number,title,url,state,isDraft,updatedAt,mergedAt,headRefOid,baseRefOid,"
    "statusCheckRollup,reviewDecision"
)
# Use gh's generic transport, available in gh 2.46, rather than its versioned
# `pr view --json` field registry (which did not yet expose baseRefOid there).
# Variables go in a JSON request body; no value is interpolated into this query.
GRAPHQL_QUERY = """query ContributionStatus(
  $owner: String!, $name: String!, $number: Int!, $cursor: String
) {
  repository(owner: $owner, name: $name) {
    isPrivate
    pullRequest(number: $number) {
      number title url state isDraft updatedAt mergedAt
      headRefOid baseRefOid reviewDecision
      commits(last: 1) {
        nodes {
          commit {
            oid
            statusCheckRollup {
              contexts(first: 100, after: $cursor) {
                totalCount
                pageInfo { hasNextPage endCursor }
                nodes {
                  __typename
                  ... on CheckRun { id name status conclusion detailsUrl }
                  ... on StatusContext { id context state targetUrl }
                }
              }
            }
          }
        }
      }
    }
  }
}"""
MAX_CHECK_PAGES = 100  # Abort explicitly above 10,000 contexts; never truncate.
CATALOG_FIELDS = {"schema_version", "owner", "baseline_date", "projects", "contributions", "candidates"}
PROJECT_FIELDS = {"id", "repository", "description", "license", "release_tag", "release_url", "ci_url"}
CONTRIBUTION_FIELDS = {"id", "repository", "number", "url", "summary", "notes"}
CANDIDATE_FIELDS = {"id", "repository", "issue", "url", "title", "stage", "next_action"}
SNAPSHOT_FIELDS = {"schema_version", "observed_at", "pull_requests"}
PR_FIELDS = {
    "id", "repository", "number", "url", "title", "state", "is_draft", "updated_at",
    "merged_at", "head_sha", "base_sha", "review_decision", "checks",
}
CHECK_FIELDS = {"kind", "name", "status", "conclusion", "url"}
HANDLE = r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?"
REPOSITORY = re.compile(rf"{HANDLE}/[A-Za-z0-9_.-]+\Z")
IDENTIFIER = re.compile(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*\Z")
SHA = re.compile(r"[0-9a-f]{40}\Z")
TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z\Z")
REVIEW_DECISIONS = {"", "APPROVED", "CHANGES_REQUESTED", "REVIEW_REQUIRED"}
OUTCOME_ORDER = ("failed", "action_required", "pending", "unknown", "passed", "neutral", "skipped")


class ValidationError(ValueError):
    """Input cannot support a trustworthy public report."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def fields(value: object, expected: set[str], where: str) -> dict:
    require(isinstance(value, dict), f"{where}: expected an object")
    require(set(value) == expected, f"{where}: missing or unexpected fields")
    return value


def required_fields(value: object, expected: set[str], where: str) -> dict:
    """Validate API structure without preserving any unrequested fields."""
    require(isinstance(value, dict), f"{where}: expected an object")
    require(expected <= set(value), f"{where}: missing requested fields")
    return value


def text(value: object, where: str, *, empty: bool = False, limit: int = 4000) -> str:
    require(isinstance(value, str), f"{where}: expected a string")
    require((empty or bool(value.strip())) and len(value) <= limit, f"{where}: invalid length")
    require(not any(ord(c) < 32 or ord(c) == 127 for c in value), f"{where}: control characters are not allowed")
    return value


def array(value: object, where: str) -> list:
    require(isinstance(value, list), f"{where}: expected an array")
    return value


def integer(value: object, where: str) -> int:
    require(type(value) is int and value > 0, f"{where}: expected a positive integer")
    return value


def timestamp(value: object, where: str) -> datetime:
    value = text(value, where, limit=40)
    require(bool(TIMESTAMP.fullmatch(value)), f"{where}: expected a UTC timestamp ending in Z")
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise ValidationError(f"{where}: invalid calendar date or time") from exc


def baseline_date(value: object) -> date:
    value = text(value, "catalog.baseline_date", limit=10)
    require(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)), "catalog.baseline_date: expected YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError("catalog.baseline_date: invalid calendar date") from exc


def repository(value: object, where: str) -> str:
    value = text(value, where, limit=140)
    require(bool(REPOSITORY.fullmatch(value)), f"{where}: expected OWNER/REPO")
    require(value.split("/")[1] not in {".", ".."}, f"{where}: invalid repository name")
    return value


def https_url(value: object, where: str, *, nullable: bool = False) -> str | None:
    if value is None and nullable:
        return None
    value = text(value, where, limit=2048)
    require(not any(c.isspace() or c in '<>\\"' for c in value), f"{where}: invalid URL characters")
    try:
        parts = urlsplit(value)
        valid = parts.scheme == "https" and bool(parts.hostname) and not parts.username and not parts.password
        # Accessing port also validates malformed ports.
        valid = valid and parts.port in {None, 443}
    except ValueError as exc:
        raise ValidationError(f"{where}: invalid HTTPS URL") from exc
    require(valid, f"{where}: expected an HTTPS URL without credentials")
    return value


def github_url(value: object, repo: str, kind: str, number: int, where: str) -> str:
    value = https_url(value, where)
    expected = f"https://github.com/{repo}/{kind}/{number}"
    require(value.casefold() == expected.casefold(), f"{where}: URL does not match repository and number")
    return value


def validate_catalog(catalog: object) -> dict:
    catalog = fields(catalog, CATALOG_FIELDS, "catalog")
    require(type(catalog["schema_version"]) is int and catalog["schema_version"] == 1, "catalog: unsupported schema_version")
    owner = text(catalog["owner"], "catalog.owner", limit=39)
    require(bool(re.fullmatch(HANDLE, owner)), "catalog.owner: invalid GitHub owner")
    baseline_date(catalog["baseline_date"])
    ids: set[str] = set()
    coordinates: set[tuple] = set()
    project_repos: set[str] = set()
    for group, expected in (("projects", PROJECT_FIELDS), ("contributions", CONTRIBUTION_FIELDS), ("candidates", CANDIDATE_FIELDS)):
        for index, item in enumerate(array(catalog[group], f"catalog.{group}")):
            where = f"catalog.{group}[{index}]"
            item = fields(item, expected, where)
            identifier = text(item["id"], where + ".id", limit=100)
            require(bool(IDENTIFIER.fullmatch(identifier)), f"{where}.id: invalid identifier")
            require(identifier not in ids, f"{where}: duplicate id")
            ids.add(identifier)
            repo = repository(item["repository"], where + ".repository")
            if group == "projects":
                require(repo.split("/")[0].casefold() == owner.casefold(), f"{where}: own project must belong to catalog.owner")
                require(repo.casefold() not in project_repos, f"{where}: duplicate project repository")
                project_repos.add(repo.casefold())
                text(item["description"], where + ".description")
                text(item["license"], where + ".license", limit=150)
                https_url(item["ci_url"], where + ".ci_url", nullable=True)
                tag, release = item["release_tag"], item["release_url"]
                require((tag is None) == (release is None), f"{where}: release tag and URL must both be supplied or both be null")
                if tag is not None:
                    text(tag, where + ".release_tag", limit=200)
                    https_url(release, where + ".release_url")
                    expected_release = f"https://github.com/{repo}/releases/tag/{quote(tag, safe='/')}"
                    require(release == expected_release, f"{where}: release URL does not match repository and tag")
            else:
                number_key, kind = ("number", "pull") if group == "contributions" else ("issue", "issues")
                number = integer(item[number_key], where + "." + number_key)
                coord = (repo.casefold(), kind, number)
                require(coord not in coordinates, f"{where}: duplicate repository and number")
                coordinates.add(coord)
                github_url(item["url"], repo, kind, number, where + ".url")
                if group == "contributions":
                    require(repo.split("/")[0].casefold() != owner.casefold(), f"{where}: upstream contributions cannot be own repositories")
                    text(item["summary"], where + ".summary")
                    for note in array(item["notes"], where + ".notes"):
                        text(note, where + ".notes[]")
                else:
                    for name in ("title", "stage", "next_action"):
                        text(item[name], where + "." + name)
    return catalog


def validate_check(check: object, where: str) -> dict:
    check = fields(check, CHECK_FIELDS, where)
    kind = text(check["kind"], where + ".kind", limit=30)
    require(kind in {"check_run", "status_context", "unknown"}, f"{where}: invalid kind")
    text(check["name"], where + ".name")
    for key in ("status", "conclusion"):
        value = text(check[key], where + "." + key, empty=True, limit=100)
        require(not value or bool(re.fullmatch(r"[A-Z0-9_]+", value)), f"{where}.{key}: expected an uppercase state code")
    require(check["kind"] != "status_context" or check["conclusion"] == "", f"{where}: status contexts do not have conclusions")
    https_url(check["url"], where + ".url", nullable=True)
    return check


def validate_snapshot(catalog: dict, snapshot: object) -> dict:
    validate_catalog(catalog)
    snapshot = fields(snapshot, SNAPSHOT_FIELDS, "snapshot")
    require(type(snapshot["schema_version"]) is int and snapshot["schema_version"] == 1, "snapshot: unsupported schema_version")
    observed = timestamp(snapshot["observed_at"], "snapshot.observed_at")
    registered = {item["id"]: item for item in catalog["contributions"]}
    seen: set[str] = set()
    for index, item in enumerate(array(snapshot["pull_requests"], "snapshot.pull_requests")):
        where = f"snapshot.pull_requests[{index}]"
        item = fields(item, PR_FIELDS, where)
        identifier = text(item["id"], where + ".id", limit=100)
        require(identifier in registered, f"{where}: unregistered contribution")
        require(identifier not in seen, f"{where}: duplicate contribution")
        seen.add(identifier)
        source = registered[identifier]
        require(item["repository"] == source["repository"], f"{where}: repository does not match catalog")
        integer(item["number"], where + ".number")
        require(item["number"] == source["number"], f"{where}: number does not match catalog")
        github_url(item["url"], source["repository"], "pull", source["number"], where + ".url")
        text(item["title"], where + ".title")
        state = text(item["state"], where + ".state", limit=30)
        require(state in {"OPEN", "CLOSED", "MERGED"}, f"{where}: invalid state")
        require(type(item["is_draft"]) is bool, f"{where}: is_draft must be boolean")
        updated = timestamp(item["updated_at"], where + ".updated_at")
        require(updated <= observed, f"{where}: update is later than observation")
        if item["state"] == "MERGED":
            merged = timestamp(item["merged_at"], where + ".merged_at")
            require(merged <= updated, f"{where}: merge is later than update")
        else:
            require(item["merged_at"] is None, f"{where}: non-merged PR must have null merged_at")
        for key in ("head_sha", "base_sha"):
            value = text(item[key], where + "." + key, limit=40)
            require(bool(SHA.fullmatch(value)), f"{where}.{key}: expected a full lowercase 40-character commit SHA")
        review = text(item["review_decision"], where + ".review_decision", empty=True, limit=40)
        require(review in REVIEW_DECISIONS, f"{where}: invalid review_decision")
        for check_index, check in enumerate(array(item["checks"], where + ".checks")):
            validate_check(check, f"{where}.checks[{check_index}]")
    require(seen == set(registered), "snapshot: missing registered contributions")
    return snapshot


def check_outcome(check: dict) -> str:
    """Unknown states never become passing; neutral/skipped remain distinct."""
    if check["kind"] == "status_context":
        return {"SUCCESS": "passed", "FAILURE": "failed", "ERROR": "failed", "PENDING": "pending", "EXPECTED": "pending"}.get(check["status"], "unknown")
    if check["kind"] != "check_run":
        return "unknown"
    if check["status"] in {"IN_PROGRESS", "PENDING", "QUEUED", "REQUESTED", "WAITING"}:
        return "pending"
    if check["status"] != "COMPLETED":
        return "unknown"
    conclusion = check["conclusion"]
    if conclusion in {"FAILURE", "CANCELLED", "TIMED_OUT", "STALE", "STARTUP_FAILURE"}:
        return "failed"
    return {"SUCCESS": "passed", "ACTION_REQUIRED": "action_required", "NEUTRAL": "neutral", "SKIPPED": "skipped"}.get(conclusion, "unknown")


def summarize_checks(checks: list[dict]) -> str:
    if not checks:
        return "unknown (no checks returned)"
    counts = Counter(check_outcome(check) for check in checks)
    return "; ".join(f"{counts[state]} {state.replace('_', ' ')}" for state in OUTCOME_ORDER if counts[state])


def _state_code(value: object, where: str) -> str:
    if value is None:
        return ""
    return text(value, where, empty=True, limit=100).upper()


def normalize_check(raw: object) -> dict:
    require(isinstance(raw, dict), "GitHub check: expected an object")
    typename = raw.get("__typename")
    if typename == "CheckRun":
        check = {"kind": "check_run", "name": raw.get("name"), "status": _state_code(raw.get("status"), "check.status"), "conclusion": _state_code(raw.get("conclusion"), "check.conclusion"), "url": raw.get("detailsUrl") or None}
    elif typename == "StatusContext":
        check = {"kind": "status_context", "name": raw.get("context"), "status": _state_code(raw.get("state"), "check.state"), "conclusion": "", "url": raw.get("targetUrl") or None}
    else:
        # Retain the existence of an unrecognized object without publishing its
        # arbitrary fields or guessing that it is a successful check.
        check = {"kind": "unknown", "name": "Unrecognized GitHub check", "status": "", "conclusion": "", "url": None}
    return validate_check(check, "GitHub check")


def normalize_pr(source: dict, raw: object) -> dict:
    raw = required_fields(raw, set(GH_FIELDS.split(",")), "GitHub PR")
    checks = raw["statusCheckRollup"]
    # A null rollup is legitimate when no checks are available. Missing fields
    # are rejected above; a null or empty rollup remains unknown, never passing.
    if checks is None:
        checks = []
    array(checks, "GitHub PR.statusCheckRollup")
    review = raw["reviewDecision"]
    require(review is None or isinstance(review, str), "GitHub PR.reviewDecision: expected a string or null")
    result = {
        "id": source["id"], "repository": source["repository"], "number": raw["number"],
        "url": raw["url"], "title": raw["title"], "state": raw["state"], "is_draft": raw["isDraft"],
        "updated_at": raw["updatedAt"], "merged_at": raw["mergedAt"], "head_sha": raw["headRefOid"],
        "base_sha": raw["baseRefOid"], "review_decision": review or "",
        "checks": [normalize_check(check) for check in checks],
    }
    result["checks"].sort(key=lambda check: tuple(str(check[key] or "") for key in ("kind", "name", "status", "conclusion", "url")))
    return result


def _unique_pairs(pairs: list[tuple]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"JSON: duplicate key {key!r}")
        result[key] = value
    return result


def parse_json(value: str) -> object:
    def invalid_constant(token: str) -> None:
        raise ValidationError("JSON: non-finite numbers are not allowed")
    try:
        return json.loads(value, object_pairs_hook=_unique_pairs, parse_constant=invalid_constant)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON at line {exc.lineno}, column {exc.colno}") from exc


def read_json(path: Path) -> object:
    return parse_json(path.read_text(encoding="utf-8"))


def atomic_write(path: Path, content: str) -> None:
    """Replace one file only after its full content is ready; clean up on failure."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def query_pr_page(source: dict, cursor: str | None) -> dict:
    owner, name = source["repository"].split("/")
    body = {"query": GRAPHQL_QUERY, "variables": {
        "owner": owner, "name": name, "number": source["number"], "cursor": cursor,
    }}
    command = ["gh", "api", "graphql", "--hostname", "github.com", "--method", "POST", "--input", "-"]
    label = f"{source['repository']}#{source['number']}"
    try:
        response = subprocess.run(
            command, input=json.dumps(body), capture_output=True, text=True,
            encoding="utf-8", timeout=30, check=False,
        )
    except FileNotFoundError as exc:
        raise ValidationError("refresh requires the authenticated GitHub CLI (gh)") from exc
    except subprocess.TimeoutExpired as exc:
        raise ValidationError(f"GitHub query timed out for {label}; snapshot unchanged") from exc
    require(response.returncode == 0, f"GitHub query failed for {label} (exit {response.returncode}); snapshot unchanged")
    payload = required_fields(parse_json(response.stdout), {"data"}, "GitHub response")
    errors = payload.get("errors", [])
    require(isinstance(errors, list) and not errors, f"GitHub query returned errors for {label}; snapshot unchanged")
    # Error messages and unrequested raw metadata are never copied to output.
    data = required_fields(payload["data"], {"repository"}, "GitHub data")
    repo = required_fields(data["repository"], {"isPrivate", "pullRequest"}, "GitHub repository")
    require(repo["isPrivate"] is False, "GitHub repository is not public; snapshot unchanged")
    return required_fields(repo["pullRequest"], set(GH_FIELDS.split(",")) - {"statusCheckRollup"} | {"commits"}, "GitHub PR")


def check_page(raw: dict) -> tuple[list[dict], int, str | None]:
    commits = required_fields(raw["commits"], {"nodes"}, "GitHub PR.commits")
    nodes = array(commits["nodes"], "GitHub PR.commits.nodes")
    require(len(nodes) == 1, "GitHub PR: expected exactly one last commit")
    last = required_fields(nodes[0], {"commit"}, "GitHub last commit")
    commit = required_fields(last["commit"], {"oid", "statusCheckRollup"}, "GitHub commit")
    require(commit["oid"] == raw["headRefOid"], "GitHub PR: check commit does not match head SHA; rerun refresh")
    rollup = commit["statusCheckRollup"]
    if rollup is None:
        return [], 0, None
    rollup = required_fields(rollup, {"contexts"}, "GitHub check rollup")
    contexts = required_fields(rollup["contexts"], {"nodes", "pageInfo", "totalCount"}, "GitHub contexts")
    checks = array(contexts["nodes"], "GitHub contexts.nodes")
    total = contexts["totalCount"]
    require(type(total) is int and 0 <= total <= 100 * MAX_CHECK_PAGES, "GitHub contexts: invalid or excessive totalCount")
    require(len(checks) <= 100, "GitHub contexts: page exceeds requested size")
    info = required_fields(contexts["pageInfo"], {"hasNextPage", "endCursor"}, "GitHub pageInfo")
    require(type(info["hasNextPage"]) is bool, "GitHub pageInfo: hasNextPage must be boolean")
    cursor = info["endCursor"]
    if cursor is not None:
        text(cursor, "GitHub pageInfo.endCursor", limit=4096)
    require(not info["hasNextPage"] or (bool(checks) and cursor is not None), "GitHub pagination made no progress")
    return checks, total, cursor if info["hasNextPage"] else None


def fetch_pr(source: dict) -> dict:
    metadata = None
    expected_total = None
    checks: list[dict] = []
    cursor = None
    seen_cursors: set[str] = set()
    seen_checks: set[str] = set()
    for _ in range(MAX_CHECK_PAGES):
        raw = query_pr_page(source, cursor)
        current = {key: raw[key] for key in GH_FIELDS.split(",") if key != "statusCheckRollup"}
        if metadata is None:
            metadata = current
        require(current == metadata, "GitHub PR changed while fetching check pages; rerun refresh")
        page, total, next_cursor = check_page(raw)
        if expected_total is None:
            expected_total = total
        require(total == expected_total, "GitHub check count changed during pagination; rerun refresh")
        for node in page:
            node = required_fields(node, {"__typename"}, "GitHub check node")
            typename = text(node["__typename"], "GitHub check typename", limit=100)
            if typename in {"CheckRun", "StatusContext"}:
                node = required_fields(node, {"id"}, "GitHub check node")
                identifier = text(node["id"], "GitHub check id", limit=4096)
                require(identifier not in seen_checks, "GitHub check appeared twice during pagination; rerun refresh")
                seen_checks.add(identifier)
            checks.append(normalize_check(node))
        require(len(checks) <= total, "GitHub contexts exceed totalCount")
        if next_cursor is None:
            require(len(checks) == total, "GitHub contexts are incomplete; snapshot unchanged")
            result = normalize_pr(source, {**metadata, "statusCheckRollup": []})
            result["checks"] = sorted(checks, key=lambda item: tuple(str(item[key] or "") for key in ("kind", "name", "status", "conclusion", "url")))
            return result
        require(len(checks) < total, "GitHub pagination contradicts totalCount")
        require(next_cursor not in seen_cursors, "GitHub pagination cursor repeated; snapshot unchanged")
        seen_cursors.add(next_cursor)
        cursor = next_cursor
    raise ValidationError("GitHub check pagination limit exceeded; snapshot unchanged")


def refresh(catalog: dict, output: Path) -> dict:
    validate_catalog(catalog)
    pull_requests = [fetch_pr(source) for source in sorted(catalog["contributions"], key=lambda item: item["id"])]
    snapshot = {"schema_version": 1, "observed_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"), "pull_requests": pull_requests}
    validate_snapshot(catalog, snapshot)
    atomic_write(output, json.dumps(snapshot, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
    return snapshot


def md(value: str) -> str:
    """Escape metadata as literal Markdown text, including table delimiters."""
    value = html.escape(value, quote=False)
    return re.sub(r"([\\`*_{}\[\]()#+.!|~-])", r"\\\1", value)


def link(label: str, url: str) -> str:
    return f"[{md(label)}](<{url}>)"


def render(catalog: dict, snapshot: dict) -> str:
    validate_snapshot(catalog, snapshot)
    prs = sorted(snapshot["pull_requests"], key=lambda item: (item["repository"].casefold(), item["number"]))
    metadata = {item["id"]: item for item in catalog["contributions"]}
    baseline = baseline_date(catalog["baseline_date"])
    state_counts = Counter(pr["state"] for pr in prs)
    since = [pr for pr in prs if pr["state"] == "MERGED" and timestamp(pr["merged_at"], "merged_at").date() >= baseline]
    lines = [
        "# Open-source progress", "",
        f"Observed at: {snapshot['observed_at']}. Baseline date: {catalog['baseline_date']} (UTC).", "",
        "This report is generated from the public catalog and a dated GitHub snapshot. It is not a live status page.", "",
        "## Upstream contributions", "",
        f"Registered pull requests: {len(prs)}; open: {state_counts['OPEN']}; merged: {state_counts['MERGED']}; closed without merge: {state_counts['CLOSED']}.", "",
        f"Registered PRs with a recorded merge on or after {catalog['baseline_date']}: {len(since)}.", "",
        "This date comparison does not establish an additional independently tested contribution or completion of a project goal. Partial integrations in otherwise open PRs require separate evidence. Own-project releases are listed separately and do not enter these counts.", "",
        "Check results describe only the rollup returned by GitHub for each recorded head. Missing checks and unrecognized states remain unknown. Success does not establish review approval, complete test coverage, or readiness to merge.", "",
        "| Pull request | State | Returned checks | Review decision | Updated (UTC) |",
        "| --- | --- | --- | --- | --- |",
    ]
    for pr in prs:
        label = f"{pr['repository']} #{pr['number']}"
        state = pr["state"].lower() + (" (draft)" if pr["is_draft"] else "")
        review = pr["review_decision"].lower().replace("_", " ") or "not reported"
        lines.append(f"| {link(label, pr['url'])} | {state} | {summarize_checks(pr['checks'])} | {review} | {pr['updated_at']} |")
    if not prs:
        lines.extend(["", "No upstream pull requests are registered."])
    for pr in prs:
        item = metadata[pr["id"]]
        lines.extend(["", f"### {md(pr['repository'])} #{pr['number']}: {md(pr['title'])}", "", md(item["summary"]), "", f"- Source: {link('pull request', pr['url'])}", f"- Head commit: `{pr['head_sha']}`", f"- Base commit: `{pr['base_sha']}`"])
        if pr["merged_at"]:
            lines.append(f"- Recorded merge: {pr['merged_at']}")
        for note in item["notes"]:
            lines.append(f"- Catalog note: {md(note)}")
        if pr["checks"]:
            lines.extend(["", "| Check | Kind | Raw status | Conclusion | Interpretation |", "| --- | --- | --- | --- | --- |"])
            for check in sorted(pr["checks"], key=lambda check: (check["name"], check["kind"], check["status"], check["conclusion"], check["url"] or "")):
                name = link(check["name"], check["url"]) if check["url"] else md(check["name"])
                lines.append(f"| {name} | {check['kind'].replace('_', ' ')} | {md(check['status']) or 'not reported'} | {md(check['conclusion']) or 'not reported'} | {check_outcome(check).replace('_', ' ')} |")
    lines.extend(["", "## Maintained projects", "", "Cataloged release and CI links are references. This command refreshes pull requests only; it does not verify a release or run project tests.", "", "| Project | Description | Declared license | Release | CI |", "| --- | --- | --- | --- | --- |"])
    for item in sorted(catalog["projects"], key=lambda item: item["id"]):
        release = link(item["release_tag"], item["release_url"]) if item["release_url"] else "not registered"
        ci = link("CI", item["ci_url"]) if item["ci_url"] else "not registered"
        lines.append(f"| {link(item['repository'], 'https://github.com/' + item['repository'])} | {md(item['description'])} | {md(item['license'])} | {release} | {ci} |")
    lines.extend(["", "## Candidate work", "", "Stages and next actions below are curated catalog notes, not GitHub readiness decisions.", "", "| Candidate | Stage | Next action |", "| --- | --- | --- |"])
    for item in sorted(catalog["candidates"], key=lambda item: item["id"]):
        label = f"{item['repository']} #{item['issue']}: {item['title']}"
        lines.append(f"| {link(label, item['url'])} | {md(item['stage'])} | {md(item['next_action'])} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "refresh", "render"):
        command = commands.add_parser(name)
        command.add_argument("--catalog", type=Path, default=Path("data/catalog.json"))
        if name != "refresh":
            command.add_argument("--snapshot", type=Path, default=Path("data/github.json"))
        if name == "refresh":
            command.add_argument("--output", type=Path, default=Path(".local/github.json"), help="snapshot destination; tracked data/github.json requires this explicit option")
        if name == "render":
            command.add_argument("--output", type=Path, help="write Markdown atomically; default: stdout")
            command.add_argument("--check", action="store_true", help="exit 1 if --output is missing or differs; never write")
    args = parser.parse_args(argv)
    if args.command == "render" and args.check and args.output is None:
        parser.error("render --check requires --output")
    try:
        catalog = validate_catalog(read_json(args.catalog))
        if args.command == "refresh":
            snapshot = refresh(catalog, args.output)
            print(f"Refreshed {len(snapshot['pull_requests'])} pull requests into {args.output}")
            return 0
        snapshot = validate_snapshot(catalog, read_json(args.snapshot))
        if args.command == "validate":
            print(f"Valid: {len(catalog['projects'])} projects, {len(snapshot['pull_requests'])} pull requests, {len(catalog['candidates'])} candidates")
            return 0
        report = render(catalog, snapshot)
        if args.check:
            if not args.output.is_file() or args.output.read_bytes() != report.encode("utf-8"):
                print(f"Out of date: {args.output}", file=sys.stderr)
                return 1
            print(f"Up to date: {args.output}")
        elif args.output:
            atomic_write(args.output, report)
            print(f"Wrote {args.output}")
        else:
            sys.stdout.write(report)
        return 0
    except (ValidationError, OSError, UnicodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
