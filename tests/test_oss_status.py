"""Offline behavioral tests for the public status tool; no credentials needed."""

import contextlib
from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock


SPEC = importlib.util.spec_from_file_location("oss_status", Path(__file__).resolve().parents[1] / "tools" / "oss_status.py")
status = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(status)


def catalog():
    return {
        "schema_version": 1,
        "owner": "maintainer",
        "baseline_date": "2026-10-13",
        "projects": [{
            "id": "own-tool", "repository": "maintainer/tool", "description": "A useful tool",
            "license": "MIT", "release_tag": "v1.0.0", "release_url": "https://github.com/maintainer/tool/releases/tag/v1.0.0",
            "ci_url": "https://github.com/maintainer/tool/actions",
        }],
        "contributions": [{
            "id": "upstream-10", "repository": "upstream/library", "number": 10,
            "url": "https://github.com/upstream/library/pull/10", "summary": "Fix handling of inputs",
            "notes": ["Additional tests are awaiting maintainer workflow approval."],
        }],
        "candidates": [{
            "id": "candidate-20", "repository": "upstream/library", "issue": 20,
            "url": "https://github.com/upstream/library/issues/20", "title": "Candidate change",
            "stage": "human review required", "next_action": "Review the prepared patch before submission.",
        }],
    }


def check(kind="check_run", status_code="COMPLETED", conclusion="SUCCESS", name="Linux", url=None):
    return {"kind": kind, "name": name, "status": status_code, "conclusion": conclusion, "url": url}


def snapshot():
    return {
        "schema_version": 1,
        "observed_at": "2026-10-17T12:30:00Z",
        "pull_requests": [{
            "id": "upstream-10", "repository": "upstream/library", "number": 10,
            "url": "https://github.com/upstream/library/pull/10", "title": "Fix inputs",
            "state": "OPEN", "is_draft": False, "updated_at": "2026-10-16T12:00:00Z",
            "merged_at": None, "head_sha": "a" * 40, "base_sha": "b" * 40,
            "review_decision": "", "checks": [check()],
        }],
    }


def raw_pr():
    return {
        "number": 10, "title": "Fix inputs", "url": "https://github.com/upstream/library/pull/10",
        "state": "OPEN", "isDraft": False, "updatedAt": "2020-01-01T00:00:00Z",
        "mergedAt": None, "headRefOid": "a" * 40, "baseRefOid": "b" * 40,
        "reviewDecision": "", "statusCheckRollup": [{
            "__typename": "CheckRun", "name": "Linux", "status": "COMPLETED", "conclusion": "SUCCESS",
            "detailsUrl": "https://github.com/upstream/library/actions/runs/1",
            "workflowName": "Unrequested workflow metadata",
        }, {
            "__typename": "StatusContext", "context": "Contributor agreement", "state": "FAILURE",
            "targetUrl": "https://example.org/status/1", "description": "Unrequested description",
        }],
    }


def graphql_page(raw=None, *, checks=None, total=None, next_cursor=None):
    """Shape returned by the fixed query, independent of gh pr view's exporter."""
    raw = deepcopy(raw if raw is not None else raw_pr())
    original_checks = raw.pop("statusCheckRollup")
    if checks is None:
        checks = original_checks
    if checks is None:
        rollup = None
    else:
        checks = deepcopy(checks)
        for index, node in enumerate(checks):
            if isinstance(node, dict) and node.get("__typename") in {"CheckRun", "StatusContext"}:
                node.setdefault("id", f"node-{index}")
        rollup = {"contexts": {
            "nodes": checks, "totalCount": len(checks) if total is None else total,
            "pageInfo": {"hasNextPage": next_cursor is not None, "endCursor": next_cursor},
        }}
    raw["commits"] = {"nodes": [{"commit": {"oid": raw["headRefOid"], "statusCheckRollup": rollup}}]}
    return {"data": {"repository": {"isPrivate": False, "pullRequest": raw}}}


def response(payload):
    return subprocess.CompletedProcess([], 0, json.dumps(payload), "")


def two_contributions():
    data = catalog()
    second = deepcopy(data["contributions"][0])
    second.update(id="upstream-11", number=11, url="https://github.com/upstream/library/pull/11")
    data["contributions"].append(second)
    return data


class CheckInterpretationTests(unittest.TestCase):
    def test_mixed_success_failure_and_required_action_remain_visible(self):
        checks = [check(), check(conclusion="ACTION_REQUIRED"), check("status_context", "FAILURE", "", "CLA"), check(status_code="QUEUED", conclusion="")]
        self.assertEqual(status.summarize_checks(checks), "1 failed; 1 action required; 1 pending; 1 passed")

    def test_unknown_and_no_checks_never_report_success(self):
        cases = [check(status_code="FUTURE_STATUS"), check(conclusion="FUTURE_CONCLUSION"), check(conclusion=""), check("unknown"), check("status_context", "FUTURE_STATE", "")]
        for item in cases:
            with self.subTest(item=item):
                self.assertEqual(status.check_outcome(item), "unknown")
        self.assertEqual(status.summarize_checks([]), "unknown (no checks returned)")
        self.assertEqual(status.summarize_checks([check(), cases[0]]), "1 unknown; 1 passed")

    def test_non_passing_conclusions_are_not_successes(self):
        for conclusion in ("FAILURE", "CANCELLED", "TIMED_OUT", "STALE", "STARTUP_FAILURE"):
            with self.subTest(conclusion=conclusion):
                self.assertEqual(status.check_outcome(check(conclusion=conclusion)), "failed")
        self.assertEqual(status.check_outcome(check(conclusion="SKIPPED")), "skipped")
        self.assertEqual(status.check_outcome(check(conclusion="NEUTRAL")), "neutral")

    def test_incomplete_run_does_not_pass_from_a_success_conclusion(self):
        for state in ("IN_PROGRESS", "PENDING", "QUEUED", "REQUESTED", "WAITING"):
            with self.subTest(state=state):
                self.assertEqual(status.check_outcome(check(status_code=state)), "pending")

    def test_commit_statuses_are_independent_of_checkrun_conclusions(self):
        for state, expected in (("SUCCESS", "passed"), ("ERROR", "failed"), ("FAILURE", "failed"), ("EXPECTED", "pending"), ("PENDING", "pending")):
            with self.subTest(state=state):
                self.assertEqual(status.check_outcome(check("status_context", state, "")), expected)


class ValidationTests(unittest.TestCase):
    def test_valid_catalog_and_complete_snapshot(self):
        self.assertEqual(status.validate_snapshot(catalog(), snapshot()), snapshot())

    def test_duplicate_ids_and_coordinates_are_rejected(self):
        for change in ("id", "coordinates"):
            data = two_contributions()
            if change == "id":
                data["contributions"][1]["id"] = "upstream-10"
            else:
                data["contributions"][1].update(number=10, url="https://github.com/upstream/library/pull/10")
            with self.subTest(change=change), self.assertRaises(status.ValidationError):
                status.validate_catalog(data)

    def test_snapshot_must_match_all_registered_pull_requests_exactly(self):
        for mutation in ("missing", "extra", "duplicate", "repository", "number", "url"):
            data = snapshot()
            if mutation == "missing":
                data["pull_requests"] = []
            elif mutation == "extra":
                data["pull_requests"][0]["id"] = "unregistered"
            elif mutation == "duplicate":
                data["pull_requests"].append(deepcopy(data["pull_requests"][0]))
            elif mutation == "repository":
                data["pull_requests"][0]["repository"] = "other/library"
            elif mutation == "number":
                data["pull_requests"][0]["number"] = 11
            else:
                data["pull_requests"][0]["url"] = "https://github.com/upstream/library/pull/11"
            with self.subTest(mutation=mutation), self.assertRaises(status.ValidationError):
                status.validate_snapshot(catalog(), data)

    def test_dates_are_real_and_temporally_consistent(self):
        for invalid in ("2026-02-30", "20261013", "2026-1-3"):
            data = catalog()
            data["baseline_date"] = invalid
            with self.subTest(date=invalid), self.assertRaises(status.ValidationError):
                status.validate_catalog(data)
        for invalid in ("2026-02-30T12:00:00Z", "2026-10-17T12:30:00", "2026-10-17T12:30:00+00:00"):
            data = snapshot()
            data["observed_at"] = invalid
            with self.subTest(timestamp=invalid), self.assertRaises(status.ValidationError):
                status.validate_snapshot(catalog(), data)
        data = snapshot()
        data["pull_requests"][0]["updated_at"] = "2026-10-18T00:00:00Z"
        with self.assertRaisesRegex(status.ValidationError, "later than observation"):
            status.validate_snapshot(catalog(), data)

    def test_merge_metadata_cannot_contradict_state_or_update(self):
        for state, merged in (("OPEN", "2026-10-14T00:00:00Z"), ("MERGED", None), ("MERGED", "2026-10-17T00:00:00Z")):
            data = snapshot()
            data["pull_requests"][0].update(state=state, merged_at=merged)
            with self.subTest(state=state, merged=merged), self.assertRaises(status.ValidationError):
                status.validate_snapshot(catalog(), data)

    def test_mismatched_or_unsafe_urls_are_rejected(self):
        for url in ("http://github.com/upstream/library/pull/10", "https://example.com/upstream/library/pull/10", "https://github.com/upstream/library/pull/10?extra=1", "https://user:secret@github.com/upstream/library/pull/10", "https://github.com/upstream/library/pull/10\n"):
            data = catalog()
            data["contributions"][0]["url"] = url
            with self.subTest(url=url), self.assertRaises(status.ValidationError):
                status.validate_catalog(data)
        data = catalog()
        data["projects"][0]["release_url"] = "https://github.com/maintainer/tool/releases/tag/v2.0.0"
        with self.assertRaisesRegex(status.ValidationError, "release URL"):
            status.validate_catalog(data)

    def test_partial_releases_and_duplicate_own_projects_are_rejected(self):
        data = catalog()
        data["projects"][0]["release_tag"] = None
        with self.assertRaises(status.ValidationError):
            status.validate_catalog(data)
        data = catalog()
        second = deepcopy(data["projects"][0])
        second["id"] = "other-id"
        data["projects"].append(second)
        with self.assertRaisesRegex(status.ValidationError, "duplicate project"):
            status.validate_catalog(data)

    def test_own_projects_cannot_inflate_upstream_contribution_counts(self):
        data = catalog()
        data["contributions"][0].update(repository="maintainer/tool", url="https://github.com/maintainer/tool/pull/10")
        with self.assertRaisesRegex(status.ValidationError, "own repositories"):
            status.validate_catalog(data)

    def test_commit_ids_require_exact_full_sha(self):
        for sha in ("abcdef1", "A" * 40, "z" * 40, "a" * 39, "a" * 41):
            data = snapshot()
            data["pull_requests"][0]["head_sha"] = sha
            with self.subTest(sha=sha), self.assertRaises(status.ValidationError):
                status.validate_snapshot(catalog(), data)

    def test_types_unknown_fields_and_duplicate_json_keys_are_rejected(self):
        mutations = [("state", []), ("review_decision", {}), ("number", True), ("is_draft", "false")]
        for key, value in mutations:
            data = snapshot()
            data["pull_requests"][0][key] = value
            with self.subTest(key=key), self.assertRaises(status.ValidationError):
                status.validate_snapshot(catalog(), data)
        data = snapshot()
        data["pull_requests"][0]["body"] = "not permitted in a public snapshot"
        with self.assertRaises(status.ValidationError):
            status.validate_snapshot(catalog(), data)
        with self.assertRaisesRegex(status.ValidationError, "duplicate key"):
            status.parse_json('{"schema_version": 1, "schema_version": 2}')
        with self.assertRaises(status.ValidationError):
            status.parse_json('{"value": NaN}')


class RefreshTests(unittest.TestCase):
    def test_normalizes_both_check_types_and_drops_unrequested_fields(self):
        raw = raw_pr()
        raw.update(body="PRIVATE BODY", comments=["PRIVATE COMMENT"], author={"login": "PRIVATE IDENTITY"})
        normalized = status.normalize_pr(catalog()["contributions"][0], raw)
        self.assertEqual(set(normalized), status.PR_FIELDS)
        self.assertEqual({item["kind"] for item in normalized["checks"]}, {"check_run", "status_context"})
        self.assertEqual(status.summarize_checks(normalized["checks"]), "1 failed; 1 passed")
        encoded = json.dumps(normalized)
        for forbidden in ("PRIVATE", "workflowName", "description", "comments", "author"):
            self.assertNotIn(forbidden, encoded)

    def test_missing_rollup_field_is_error_but_null_is_unknown(self):
        raw = raw_pr()
        raw["statusCheckRollup"] = None
        self.assertEqual(status.normalize_pr(catalog()["contributions"][0], raw)["checks"], [])
        del raw["statusCheckRollup"]
        with self.assertRaisesRegex(status.ValidationError, "missing requested fields"):
            status.normalize_pr(catalog()["contributions"][0], raw)

    def test_unknown_union_member_is_retained_conservatively(self):
        normalized = status.normalize_check({"__typename": "FutureCheck", "name": "secret", "body": "secret", "state": "SUCCESS"})
        self.assertEqual(status.check_outcome(normalized), "unknown")
        self.assertNotIn("secret", json.dumps(normalized))

    def test_gh_2_46_transport_avoids_unsupported_pr_view_field_registry(self):
        def gh_2_46(command, **kwargs):
            if command[:3] == ["gh", "pr", "view"]:
                return subprocess.CompletedProcess(command, 1, "", 'Unknown JSON field: "baseRefOid"')
            self.assertEqual(command, ["gh", "api", "graphql", "--hostname", "github.com", "--method", "POST", "--input", "-"])
            request = json.loads(kwargs["input"])
            self.assertEqual(request["variables"], {"owner": "upstream", "name": "library", "number": 10, "cursor": None})
            self.assertEqual(request["query"], status.GRAPHQL_QUERY)
            self.assertIn("baseRefOid", request["query"])
            self.assertIn("commits(last: 1)", request["query"])
            self.assertIn("contexts(first: 100, after: $cursor)", request["query"])
            for unrequested in ("mutation", "author", "body", "comments", "creator", "description"):
                self.assertNotIn(unrequested, request["query"])
            return response(graphql_page())

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "nested" / "github.json"
            with mock.patch.object(status.subprocess, "run", side_effect=gh_2_46) as run:
                refreshed = status.refresh(catalog(), output)
            self.assertEqual(run.call_count, 1)
            self.assertFalse(run.call_args.kwargs.get("shell", False))
            self.assertEqual(run.call_args.kwargs["timeout"], 30)
            self.assertEqual(status.read_json(output), refreshed)
            self.assertEqual(refreshed["pull_requests"][0]["base_sha"], "b" * 40)
            self.assertEqual(refreshed["pull_requests"][0]["head_sha"], "a" * 40)
            status.validate_snapshot(catalog(), refreshed)
            self.assertEqual(list(output.parent.iterdir()), [output])

    def test_later_query_failure_preserves_old_snapshot_and_omits_error_body(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "github.json"
            output.write_bytes(b"EXISTING SNAPSHOT\n")
            responses = [response(graphql_page()), subprocess.CompletedProcess([], 1, "PRIVATE OUTPUT", "PRIVATE TOKEN")]
            with mock.patch.object(status.subprocess, "run", side_effect=responses):
                with self.assertRaises(status.ValidationError) as raised:
                    status.refresh(two_contributions(), output)
            self.assertIn("upstream/library#11", str(raised.exception))
            self.assertNotIn("PRIVATE", str(raised.exception))
            self.assertEqual(output.read_bytes(), b"EXISTING SNAPSHOT\n")
            self.assertEqual(list(output.parent.iterdir()), [output])

    def test_later_invalid_response_preserves_old_snapshot(self):
        second = raw_pr()
        second.update(number=11, url="https://github.com/upstream/library/pull/11", headRefOid="short")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "github.json"
            output.write_bytes(b"OLD\n")
            responses = [response(graphql_page()), response(graphql_page(second))]
            with mock.patch.object(status.subprocess, "run", side_effect=responses), self.assertRaises(status.ValidationError):
                status.refresh(two_contributions(), output)
            self.assertEqual(output.read_bytes(), b"OLD\n")

    def test_missing_cli_timeout_and_invalid_json_do_not_create_output(self):
        for failure in (FileNotFoundError(), subprocess.TimeoutExpired(["gh"], 30), subprocess.CompletedProcess([], 0, "not JSON", "")):
            with self.subTest(failure=type(failure).__name__), tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / "github.json"
                options = {"side_effect": failure} if isinstance(failure, Exception) else {"return_value": failure}
                with mock.patch.object(status.subprocess, "run", **options), self.assertRaises(status.ValidationError):
                    status.refresh(catalog(), output)
                self.assertFalse(output.exists())

    def test_failed_replace_cleans_temporary_file_and_keeps_existing_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.md"
            output.write_bytes(b"OLD\n")
            with mock.patch.object(status.os, "replace", side_effect=OSError("simulated filesystem failure")), self.assertRaises(OSError):
                status.atomic_write(output, "NEW\n")
            self.assertEqual(output.read_bytes(), b"OLD\n")
            self.assertEqual(list(output.parent.iterdir()), [output])

    def test_fetches_more_than_100_contexts_and_keeps_late_failure(self):
        checks = [{"__typename": "CheckRun", "id": f"check-{index}", "name": f"job-{index:03}", "status": "COMPLETED", "conclusion": "SUCCESS", "detailsUrl": None} for index in range(101)]
        checks[-1]["conclusion"] = "FAILURE"
        pages = [response(graphql_page(checks=checks[:100], total=101, next_cursor="cursor-100")), response(graphql_page(checks=checks[100:], total=101))]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "github.json"
            with mock.patch.object(status.subprocess, "run", side_effect=pages) as run:
                refreshed = status.refresh(catalog(), output)
            self.assertEqual(run.call_count, 2)
            self.assertEqual(json.loads(run.call_args_list[0].kwargs["input"])["variables"]["cursor"], None)
            self.assertEqual(json.loads(run.call_args_list[1].kwargs["input"])["variables"]["cursor"], "cursor-100")
            normalized = refreshed["pull_requests"][0]["checks"]
            self.assertEqual(len(normalized), 101)
            self.assertEqual(status.summarize_checks(normalized), "1 failed; 100 passed")
            self.assertTrue(all(set(item) == status.CHECK_FIELDS for item in normalized))

    def test_null_graphql_rollup_and_empty_contexts_remain_unknown(self):
        raw = raw_pr()
        raw["statusCheckRollup"] = None
        for payload in (graphql_page(raw), graphql_page(checks=[])):
            with self.subTest(payload=payload), tempfile.TemporaryDirectory() as directory:
                with mock.patch.object(status.subprocess, "run", return_value=response(payload)):
                    refreshed = status.refresh(catalog(), Path(directory) / "github.json")
                self.assertEqual(status.summarize_checks(refreshed["pull_requests"][0]["checks"]), "unknown (no checks returned)")

    def test_missing_rollup_or_commit_and_mismatched_head_fail_closed(self):
        for mutation in ("missing_rollup", "missing_commits", "empty_commits", "different_head", "null_contexts", "missing_page_info"):
            payload = graphql_page()
            pr = payload["data"]["repository"]["pullRequest"]
            commit = pr["commits"]["nodes"][0]["commit"]
            if mutation == "missing_rollup":
                del commit["statusCheckRollup"]
            elif mutation == "missing_commits":
                del pr["commits"]
            elif mutation == "empty_commits":
                pr["commits"]["nodes"] = []
            elif mutation == "different_head":
                commit["oid"] = "c" * 40
            elif mutation == "null_contexts":
                commit["statusCheckRollup"]["contexts"] = None
            else:
                del commit["statusCheckRollup"]["contexts"]["pageInfo"]
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / "github.json"
                output.write_bytes(b"OLD\n")
                with mock.patch.object(status.subprocess, "run", return_value=response(payload)), self.assertRaises(status.ValidationError):
                    status.refresh(catalog(), output)
                self.assertEqual(output.read_bytes(), b"OLD\n")

    def test_pagination_inconsistency_preserves_previous_snapshot(self):
        checks = [{"__typename": "CheckRun", "id": "first", "name": "first", "status": "COMPLETED", "conclusion": "SUCCESS", "detailsUrl": None}]
        for mutation in ("changed_head", "changed_base", "changed_state", "changed_total", "duplicate_check", "repeated_cursor", "incomplete", "empty_page", "null_later_rollup"):
            first = graphql_page(checks=checks, total=3, next_cursor="cursor-one")
            later_check = {**checks[0], "id": "second", "name": "second"}
            later = graphql_page(checks=[later_check], total=3, next_cursor="cursor-two")
            pr = later["data"]["repository"]["pullRequest"]
            commit = pr["commits"]["nodes"][0]["commit"]
            contexts = commit["statusCheckRollup"]["contexts"]
            if mutation == "changed_head":
                pr["headRefOid"] = commit["oid"] = "c" * 40
            elif mutation == "changed_base":
                pr["baseRefOid"] = "c" * 40
            elif mutation == "changed_state":
                pr["state"] = "CLOSED"
            elif mutation == "changed_total":
                contexts["totalCount"] = 4
            elif mutation == "duplicate_check":
                contexts["nodes"][0]["id"] = "first"
            elif mutation == "repeated_cursor":
                contexts["pageInfo"]["endCursor"] = "cursor-one"
            elif mutation == "incomplete":
                contexts["pageInfo"]["hasNextPage"] = False
            elif mutation == "empty_page":
                contexts["nodes"] = []
            else:
                commit["statusCheckRollup"] = None
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / "github.json"
                output.write_bytes(b"OLD\n")
                with mock.patch.object(status.subprocess, "run", side_effect=[response(first), response(later)]), self.assertRaises(status.ValidationError):
                    status.refresh(catalog(), output)
                self.assertEqual(output.read_bytes(), b"OLD\n")

    def test_graphql_errors_null_objects_and_private_repository_are_not_published(self):
        payloads = [
            {"data": None, "errors": [{"message": "PRIVATE ERROR CONTENT"}]},
            {"data": {"repository": None}},
            {"data": {"repository": {"isPrivate": False, "pullRequest": None}}},
        ]
        private = graphql_page()
        private["data"]["repository"]["isPrivate"] = True
        payloads.append(private)
        partial = graphql_page()
        partial["errors"] = [{"message": "PRIVATE PARTIAL RESPONSE"}]
        payloads.append(partial)
        for payload in payloads:
            with self.subTest(payload=payload), tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / "github.json"
                with mock.patch.object(status.subprocess, "run", return_value=response(payload)), self.assertRaises(status.ValidationError) as raised:
                    status.refresh(catalog(), output)
                self.assertFalse(output.exists())
                self.assertNotIn("PRIVATE", str(raised.exception))


class RenderingTests(unittest.TestCase):
    def test_report_is_deterministic_under_input_order_changes(self):
        data = two_contributions()
        observed = snapshot()
        second = deepcopy(observed["pull_requests"][0])
        second.update(id="upstream-11", number=11, url="https://github.com/upstream/library/pull/11")
        observed["pull_requests"].append(second)
        observed["pull_requests"][0]["checks"].extend([check(name="zeta"), check(name="alpha", conclusion="ACTION_REQUIRED")])
        expected = status.render(data, observed)
        data["contributions"].reverse()
        observed["pull_requests"].reverse()
        for pr in observed["pull_requests"]:
            pr["checks"].reverse()
        self.assertEqual(status.render(data, observed), expected)
        self.assertTrue(expected.endswith("\n"))

    def test_merge_date_comparison_excludes_old_merge_and_does_not_claim_goal_completion(self):
        data = two_contributions()
        observed = snapshot()
        old = observed["pull_requests"][0]
        old.update(state="MERGED", merged_at="2026-09-09T23:21:10Z")
        new = deepcopy(old)
        new.update(id="upstream-11", number=11, url="https://github.com/upstream/library/pull/11", merged_at="2026-10-13T00:00:00Z")
        observed["pull_requests"].append(new)
        report = status.render(data, observed)
        self.assertIn("Registered pull requests: 2; open: 0; merged: 2; closed without merge: 0.", report)
        self.assertIn("recorded merge on or after 2026-10-13: 1.", report)
        self.assertIn("does not establish an additional independently tested contribution", report)
        self.assertIn("Own-project releases are listed separately and do not enter these counts", report)

    def test_markdown_escapes_metadata_and_preserves_exact_commit_ids(self):
        data, observed = catalog(), snapshot()
        data["contributions"][0]["summary"] = "Literal [link](https://unexpected.example) | <script>"
        report = status.render(data, observed)
        self.assertIn(r"Literal \[link\]\(https://unexpected\.example\) \| &lt;script&gt;", report)
        self.assertNotIn("<script>", report)
        self.assertIn("`" + "a" * 40 + "`", report)
        self.assertIn("`" + "b" * 40 + "`", report)

    def test_cli_render_check_detects_staleness_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog_path, snapshot_path, report_path = root / "catalog.json", root / "github.json", root / "progress.md"
            catalog_path.write_text(json.dumps(catalog()), encoding="utf-8")
            snapshot_path.write_text(json.dumps(snapshot()), encoding="utf-8")
            argv = ["render", "--catalog", str(catalog_path), "--snapshot", str(snapshot_path), "--output", str(report_path)]
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(status.main(argv + ["--check"]), 1)
                self.assertFalse(report_path.exists())
                self.assertEqual(status.main(argv), 0)
                self.assertEqual(status.main(argv + ["--check"]), 0)
                report_path.write_bytes(b"STALE\n")
                self.assertEqual(status.main(argv + ["--check"]), 1)
            self.assertEqual(report_path.read_bytes(), b"STALE\n")

    def test_refresh_cli_defaults_to_untracked_local_snapshot(self):
        with mock.patch.object(status, "read_json", return_value=catalog()), mock.patch.object(status, "refresh", return_value={"pull_requests": []}) as refresh, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(status.main(["refresh"]), 0)
        self.assertEqual(refresh.call_args.args[1], Path(".local/github.json"))


if __name__ == "__main__":
    unittest.main()
