"""Offline campaign accounting and evidence regressions (Python 3.10+)."""

import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock


SPEC = importlib.util.spec_from_file_location(
    "contribution_campaign", Path(__file__).resolve().parents[1] / "tools" / "contribution_campaign.py")
campaign = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(campaign)

BASE = "a" * 40
FIXED = "b" * 40
EVIDENCE = "https://github.com/contributor/evidence/blob/" + "c" * 40 + "/validation.md"


def project(stage="target", repository="upstream/library", batch=1):
    milestones = [
        {"stage": "target", "date": "2026-10-17", "refs": ["https://github.com/" + repository]},
        {"stage": "screened", "date": "2026-10-17", "refs": [EVIDENCE],
         "policy_ref": "https://github.com/" + repository + "/blob/main/CONTRIBUTING.md"},
        {"stage": "selected", "date": "2026-10-17", "refs": [EVIDENCE],
         "selection_ref": "https://github.com/" + repository + "/issues/7"},
        {"stage": "reproduced", "date": "2026-10-17", "refs": [EVIDENCE],
         "source_commit": BASE, "source_ref": "https://github.com/" + repository + "/commit/" + BASE,
         "validation": {"command": "python3 regression.py", "result": "reproduced", "ref": EVIDENCE + "#baseline"}},
        {"stage": "validated", "date": "2026-10-17", "refs": [EVIDENCE],
         "source_commit": FIXED, "source_ref": "https://github.com/contributor/library/commit/" + FIXED,
         "validation": {"command": "python3 -m unittest discover -s tests -v", "result": "passed", "ref": EVIDENCE + "#fixed"},
         "review_ref": EVIDENCE + "#review"},
        {"stage": "submitted", "date": "2026-10-17", "refs": [EVIDENCE],
         "pr_url": "https://github.com/" + repository + "/pull/8", "source_commit": FIXED},
        {"stage": "accepted", "date": "2026-10-17", "refs": [EVIDENCE],
         "acceptance_ref": "https://github.com/" + repository + "/pull/8#issuecomment-123"},
    ]
    return {
        "repository": repository, "batch": batch, "summary": "A supported workflow defect.",
        "next_action": "Review the next actionable upstream response.",
        "benefit_route": {"kind": "unconfirmed", "qualification": "unverified", "checked_on": "2026-10-17",
                          "summary": "No direct benefit route has been established.", "refs": []},
        "milestones": milestones[:campaign.STAGES.index(stage) + 1], "benefits": [],
    }


def fixture(*projects):
    return {"schema_version": 1, "owner": "contributor", "started_on": "2026-10-17", "updated_on": "2026-10-18",
            "target_count": 100, "projects": list(projects), "historical_submissions": []}


def benefit(identifier="cash-one", state="paid", kind="cash", amount="0.10", currency="USD", date="2026-10-17"):
    result = {"id": identifier, "kind": kind, "state": state, "date": date, "summary": "Evidence for this benefit state.", "refs": [EVIDENCE]}
    if state != "advertised":
        result[{"granted": "grant_ref", "activated": "activation_ref", "paid": "receipt_ref"}[state]] = EVIDENCE + "#" + identifier
    if kind == "cash":
        result.update(amount=amount, currency=currency)
    return result


class CampaignValidationTests(unittest.TestCase):
    def assert_invalid(self, data, message=None):
        with self.assertRaises(campaign.ValidationError) as caught:
            campaign.validate_campaign(data)
        if message:
            self.assertIn(message, str(caught.exception))

    def test_empty_campaign_does_not_invent_progress(self):
        report = campaign.render_campaign(fixture())
        self.assertIn("0 / 100 distinct external repositories", report)
        self.assertIn("Full research queue: 0 repositories", report)
        self.assertIn("Recorded paid cash: none.", report)

    def test_complete_history_counts_submission_and_acceptance_separately(self):
        data = fixture(project("submitted"), project("accepted", "other/project", 2), project("screened", "third/project", 2))
        report = campaign.render_campaign(data)
        self.assertIn("2 / 100 distinct external repositories", report)
        self.assertIn("| submitted | 1 | 2 |", report)
        self.assertIn("| accepted | 1 | 1 |", report)
        self.assertIn(FIXED, report)
        self.assertIn(EVIDENCE + "#fixed", report)
        self.assertIn(EVIDENCE + "#review", report)

    def test_case_insensitive_duplicate_targets_across_batches_are_rejected(self):
        self.assert_invalid(fixture(project(), project(repository="UPSTREAM/Library", batch=2)), "duplicate target")

    def test_owned_repositories_cannot_inflate_external_goal(self):
        self.assert_invalid(fixture(project(repository="Contributor/owned")), "not external")

    def test_goal_is_not_a_cap_on_research_queue(self):
        data = fixture(project(), project(repository="other/library"))
        data["target_count"] = 1
        self.assertEqual(len(campaign.validate_campaign(data)["projects"]), 2)

    def test_unsupported_skipped_and_repeated_stages_are_rejected(self):
        for milestones in ([{"stage": "published"}], [{"stage": "submitted"}],
                           [project()["milestones"][0], project()["milestones"][0]]):
            with self.subTest(milestones=milestones):
                data = fixture(project())
                data["projects"][0]["milestones"] = milestones
                self.assert_invalid(data, "stage")

    def test_selection_requires_policy_and_selection_evidence(self):
        for index, key in ((1, "policy_ref"), (2, "selection_ref")):
            with self.subTest(key=key):
                data = fixture(project("selected"))
                del data["projects"][0]["milestones"][index][key]
                self.assert_invalid(data)

    def test_validation_requires_exact_source_test_and_review_records(self):
        for index, key in ((3, "source_commit"), (3, "validation"), (4, "source_ref"), (4, "review_ref")):
            with self.subTest(key=key):
                data = fixture(project("validated"))
                del data["projects"][0]["milestones"][index][key]
                self.assert_invalid(data)
        for key, value in (("source_commit", "short"), ("source_ref", "https://github.com/upstream/library/commit/" + BASE)):
            with self.subTest(key=key):
                data = fixture(project("validated"))
                data["projects"][0]["milestones"][4][key] = value
                self.assert_invalid(data)
        data = fixture(project("validated"))
        data["projects"][0]["milestones"][4]["validation"]["result"] = "failed"
        self.assert_invalid(data, "does not establish")

    def test_submission_requires_matching_pr_evidence_and_validated_revision(self):
        for key, value in (("pr_url", None), ("refs", []), ("source_commit", BASE),
                           ("pr_url", "https://github.com/contributor/library/pull/8")):
            with self.subTest(key=key, value=value):
                data = fixture(project("submitted"))
                if value is None:
                    del data["projects"][0]["milestones"][5][key]
                else:
                    data["projects"][0]["milestones"][5][key] = value
                self.assert_invalid(data)

    def test_acceptance_requires_upstream_acceptance_for_the_submission(self):
        for reference in (None, EVIDENCE, "https://github.com/upstream/library/pull/9",
                          "https://github.com/contributor/library/commit/" + FIXED):
            with self.subTest(reference=reference):
                data = fixture(project("accepted"))
                if reference is None:
                    del data["projects"][0]["milestones"][6]["acceptance_ref"]
                else:
                    data["projects"][0]["milestones"][6]["acceptance_ref"] = reference
                self.assert_invalid(data)
        for reference in ("https://github.com/upstream/library/pull/8",
                          "https://github.com/upstream/library/commit/" + FIXED):
            data = fixture(project("accepted"))
            data["projects"][0]["milestones"][6]["acceptance_ref"] = reference
            campaign.validate_campaign(data)

    def test_history_is_preserved_without_fabricated_validation_or_new_credit(self):
        data = fixture(project())
        data["historical_submissions"] = [{"repository": "upstream/library", "pr_url": "https://github.com/upstream/library/pull/8",
                                           "submitted_on": "2026-10-01", "refs": [EVIDENCE], "accepted_on": "2026-10-18",
                                           "acceptance_ref": "https://github.com/upstream/library/pull/8"}]
        report = campaign.render_campaign(data)
        self.assertIn("0 / 100 distinct", report)
        self.assertIn("Historical submissions: 1; excluded", report)
        self.assertIn("Accepted 2026-10-18", report)
        data["projects"][0] = project("submitted")
        self.assert_invalid(data, "historical PR cannot also count")

    def test_dates_cannot_invent_history_or_future_milestones(self):
        for value in ("2026-02-30", "2026-10-16", "2026-10-19"):
            data = fixture(project())
            data["projects"][0]["milestones"][0]["date"] = value
            self.assert_invalid(data)
        data = fixture(project("screened"))
        data["projects"][0]["milestones"][0]["date"] = "2026-10-18"
        self.assert_invalid(data, "earlier than")

    def test_claimed_benefit_route_requires_qualification_sources(self):
        data = fixture(project())
        route = data["projects"][0]["benefit_route"]
        route.update(kind="cash", qualification="conditional")
        self.assert_invalid(data, "references")
        route["refs"] = [EVIDENCE]
        campaign.validate_campaign(data)
        route["qualification"] = "guaranteed"
        self.assert_invalid(data, "qualification")

    def test_paid_cash_requires_receipt_and_exact_amount(self):
        for key in ("receipt_ref", "amount", "currency", "refs"):
            with self.subTest(key=key):
                item = benefit()
                del item[key]
                data = fixture(project())
                data["projects"][0]["benefits"] = [item]
                self.assert_invalid(data)

    def test_grants_and_activations_require_their_own_evidence(self):
        for state, kind, key in (("granted", "cash", "grant_ref"), ("activated", "subscription", "activation_ref")):
            data = fixture(project())
            data["projects"][0]["benefits"] = [benefit(state=state, kind=kind)]
            campaign.validate_campaign(data)
            del data["projects"][0]["benefits"][0][key]
            self.assert_invalid(data)
        for state, kind in (("activated", "cash"), ("paid", "credits")):
            data = fixture(project())
            data["projects"][0]["benefits"] = [benefit(state=state, kind=kind)]
            self.assert_invalid(data)

    def test_nonexact_and_nonpositive_financial_values_are_rejected(self):
        for amount in (1.25, True, "1e3", "NaN", "Infinity", "-1", "0", "00.10", "1,000", "0.123456789"):
            with self.subTest(amount=amount):
                data = fixture(project())
                data["projects"][0]["benefits"] = [benefit(amount=amount)]
                self.assert_invalid(data)

    def test_paid_totals_exclude_ads_grants_history_and_non_cash(self):
        data = fixture(project())
        data["projects"][0]["benefits"] = [
            benefit("usd-one", amount="0.10"), benefit("usd-two", amount="0.20"),
            benefit("eur", amount="2.50", currency="EUR"), benefit("advert", state="advertised", amount="99999"),
            benefit("grant", state="granted", amount="12345"), benefit("old", date="2026-10-16", amount="777"),
            benefit("access", state="activated", kind="subscription"), benefit("credits", state="granted", kind="credits"),
        ]
        report = campaign.render_campaign(data)
        self.assertIn("Recorded paid cash: EUR 2.50; USD 0.30.", report)
        self.assertIn("| cash | 1 | 1 | 0 | 3 |", report)
        self.assertIn("| subscription | 0 | 0 | 1 | 0 |", report)
        self.assertIn("| credits | 0 | 1 | 0 | 0 |", report)

    def test_duplicate_benefit_ids_cannot_double_count_across_targets(self):
        data = fixture(project(), project(repository="other/project"))
        for item in data["projects"]:
            item["benefits"] = [benefit()]
        self.assert_invalid(data, "duplicate benefit identifier")

    def test_batch_report_keeps_full_goal_and_validates_unshown_records(self):
        data = fixture(project("submitted"), project("submitted", "other/project", 2))
        report = campaign.render_campaign(data, batch=1)
        self.assertIn("2 / 100 distinct", report)
        self.assertIn("| submitted | 1 | 1 |", report)
        self.assertNotIn("https://github.com/other/project", report)
        data["projects"][1]["milestones"][5]["refs"] = []
        with self.assertRaises(campaign.ValidationError):
            campaign.render_campaign(data, batch=1)

    def test_render_is_deterministic_and_escapes_user_text(self):
        data = fixture(project(repository="zebra/project"), project(repository="alpha/project"))
        data["projects"][0]["summary"] = "<script>alert(1)</script> | [misleading](https://example.org)"
        reversed_data = copy.deepcopy(data)
        reversed_data["projects"].reverse()
        report = campaign.render_campaign(data)
        self.assertEqual(report, campaign.render_campaign(reversed_data))
        self.assertNotIn("<script>", report)
        self.assertIn("&lt;script&gt;", report)
        self.assertIn("\\| \\[misleading\\]", report)

    def test_boolean_numbers_unknown_fields_and_credential_urls_fail(self):
        data = fixture(project())
        data["target_count"] = True
        self.assert_invalid(data)
        data = fixture(project())
        data["projects"][0]["private_path"] = "private-path-must-not-echo"
        self.assert_invalid(data, "unexpected fields")
        data = fixture(project())
        data["projects"][0]["milestones"][0]["refs"] = ["https://user:password@example.org/evidence"]
        self.assert_invalid(data, "without credentials")


class CampaignOutputTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.input = self.root / "campaign.json"
        self.output = self.root / "report.md"
        self.input.write_text(json.dumps(fixture(project("submitted"))), encoding="utf-8")

    def invoke(self, *args):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = campaign.main(list(args))
        return result, stdout.getvalue(), stderr.getvalue()

    def test_successful_atomic_report_and_check_preserve_exact_bytes(self):
        args = ("report", "--input", str(self.input), "--output", str(self.output))
        self.assertEqual(self.invoke(*args)[0], 0)
        expected = campaign.render_campaign(campaign.load_campaign(self.input)).encode("utf-8")
        self.assertEqual(self.output.read_bytes(), expected)
        self.assertEqual(self.invoke(*args, "--check")[0], 0)
        self.output.write_bytes(b"previous report\r\n")
        self.assertEqual(self.invoke(*args, "--check")[0], 1)
        self.assertEqual(self.output.read_bytes(), b"previous report\r\n")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["campaign.json", "report.md"])

    def test_invalid_input_preserves_report_without_creating_output_directories(self):
        self.output.write_text("last valid report", encoding="utf-8")
        data = fixture(project("submitted"))
        del data["projects"][0]["milestones"][5]["pr_url"]
        self.input.write_text(json.dumps(data), encoding="utf-8")
        with mock.patch.object(campaign, "atomic_write", side_effect=AssertionError("must not write invalid input")):
            self.assertEqual(self.invoke("report", "--input", str(self.input), "--output", str(self.output))[0], 2)
            nested = self.root / "new" / "report.md"
            self.assertEqual(self.invoke("report", "--input", str(self.input), "--output", str(nested))[0], 2)
        self.assertEqual(self.output.read_text(encoding="utf-8"), "last valid report")
        self.assertFalse((self.root / "new").exists())

    def test_duplicate_json_keys_and_nonfinite_numbers_preserve_output(self):
        data = self.input.read_text(encoding="utf-8")
        invalid_inputs = [
            data.replace('"projects":', '"projects": [], "projects":', 1),
            data.replace('"repository":', '"repository": "hidden/target", "repository":', 1),
            data.replace('"target_count": 100', '"target_count": NaN'),
        ]
        self.output.write_bytes(b"previous report")
        for invalid in invalid_inputs:
            with self.subTest(invalid=invalid[:40]):
                self.input.write_text(invalid, encoding="utf-8")
                result, stdout, _ = self.invoke("report", "--input", str(self.input), "--output", str(self.output))
                self.assertEqual(result, 2)
                self.assertEqual(stdout, "")
                self.assertEqual(self.output.read_bytes(), b"previous report")

    def test_unpaired_json_surrogates_fail_before_stdout_or_file_output(self):
        self.output.write_bytes(b"previous report")
        nested = self.root / "new" / "report.md"
        commands = (("validate",), ("report",),
                    ("report", "--output", str(self.output)),
                    ("report", "--output", str(nested)))
        for surrogate in (0xD800, 0xDFFF):
            data = fixture(project())
            data["projects"][0]["summary"] = "Unpaired surrogate: " + chr(surrogate)
            # JSON escapes are valid UTF-8 bytes, but decode into a string that
            # cannot itself be encoded as UTF-8 for a report.
            self.input.write_text(json.dumps(data), encoding="utf-8")
            for command in commands:
                with self.subTest(surrogate=hex(surrogate), command=command[0], output=command[1:]):
                    buffer, stderr = io.BytesIO(), io.StringIO()
                    with io.TextIOWrapper(buffer, encoding="utf-8", errors="strict") as stdout:
                        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                            result = campaign.main([*command, "--input", str(self.input)])
                        stdout.flush()
                        self.assertEqual(buffer.getvalue(), b"")
                    self.assertEqual(result, 2)
                    self.assertIn("surrogate code points", stderr.getvalue())
                    self.assertNotIn("Traceback", stderr.getvalue())
                    self.assertEqual(self.output.read_bytes(), b"previous report")
                    self.assertFalse(nested.parent.exists())
                    self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["campaign.json", "report.md"])

    def test_valid_supplementary_unicode_survives_json_and_utf8_output(self):
        data = fixture(project())
        data["projects"][0]["summary"] = "A valid supplementary character: " + chr(0x1F680)
        self.input.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(self.invoke("validate", "--input", str(self.input))[0], 0)
        self.assertEqual(self.invoke("report", "--input", str(self.input), "--output", str(self.output))[0], 0)
        self.assertIn(chr(0x1F680).encode("utf-8"), self.output.read_bytes())

    def test_replace_failure_preserves_prior_report_and_removes_temporary_file(self):
        self.output.write_bytes(b"previous report")
        with mock.patch.object(campaign.os, "replace", side_effect=OSError("private-path-must-not-echo")):
            result, stdout, stderr = self.invoke("report", "--input", str(self.input), "--output", str(self.output))
        self.assertEqual(result, 2)
        self.assertEqual(stdout, "")
        self.assertNotIn("private-path-must-not-echo", stderr)
        self.assertEqual(self.output.read_bytes(), b"previous report")
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["campaign.json", "report.md"])

    def test_output_cannot_overwrite_input(self):
        original = self.input.read_bytes()
        result, _, stderr = self.invoke("report", "--input", str(self.input), "--output", str(self.input))
        self.assertEqual(result, 2)
        self.assertIn("must not overwrite", stderr)
        self.assertEqual(self.input.read_bytes(), original)

    def test_check_missing_report_does_not_create_it(self):
        nested = self.root / "missing" / "report.md"
        result, _, _ = self.invoke("report", "--input", str(self.input), "--output", str(nested), "--check")
        self.assertEqual(result, 1)
        self.assertFalse(nested.parent.exists())

    def test_validate_and_stdout_report_are_offline_and_leave_no_files(self):
        result, stdout, stderr = self.invoke("validate", "--input", str(self.input))
        self.assertEqual((result, stderr), (0, ""))
        self.assertIn("1 / 100 qualified submitted", stdout)
        result, stdout, stderr = self.invoke("report", "--input", str(self.input))
        self.assertEqual((result, stderr), (0, ""))
        self.assertIn("# Contribution campaign", stdout)
        self.assertEqual([p.name for p in self.root.iterdir()], ["campaign.json"])


if __name__ == "__main__":
    unittest.main()
