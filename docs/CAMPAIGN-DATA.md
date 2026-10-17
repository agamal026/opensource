# Contribution campaign data

`tools/contribution_campaign.py` validates a deliberately curated campaign and
renders an offline Markdown report. The initial goal is **100 distinct external
repositories with qualified submissions**. A target, a screened opportunity, a
passing test, an accepted contribution and a paid benefit have separate counts.
There is no requirement to fill the file with 100 entries before starting work.
The goal is not a limit on the number of repositories that may be researched.

This tool does not browse, run tests, change Git state, submit PRs, apply for
benefits or schedule work. Its evidence checks establish structure and internal
consistency. Verify the linked evidence, upstream policies, external ownership
and actual eligibility before advancing a record. The tool
cannot establish that a URL is truthful, available, public or an approval.

## Commands

Run from the repository root with Python 3.10+; no packages are needed:

```sh
python3 tools/contribution_campaign.py validate --input data/campaign.json
python3 tools/contribution_campaign.py report --input data/campaign.json --output progress/CAMPAIGN.md
python3 tools/contribution_campaign.py report --input data/campaign.json --output progress/CAMPAIGN.md --check
python3 tools/contribution_campaign.py report --input data/campaign.json --batch 1
```

`data/campaign.json` is the default input. `report` writes to stdout when no
`--output` is supplied. `--batch` filters the displayed queue, stages and benefit
totals; the headline goal always covers the whole campaign. All input records
are validated, including records outside the requested batch. A batch with no
records produces an empty batch report.

Successful commands return 0. `--check` returns 1 if the report is missing or its
bytes differ and never writes it. Invalid input or an I/O failure returns 2.
`--check` requires `--output`. An output path cannot overwrite the input,
including an existing alias to that file.

A report is fully validated and rendered before output directories or files are
created. File output uses a temporary file in the destination directory, flushes
and syncs its contents, then replaces the destination atomically. An invalid
record or failed replacement preserves the previous report. Reports are UTF-8
with LF line endings and contain no generated current timestamp: the same
reviewed data produces the same report.

## Schema version 1

The top-level object requires `schema_version` (integer 1), `owner` (GitHub
account), `started_on`, `updated_on`, `target_count` (positive integer), and
`projects` (array). `historical_submissions` is optional and defaults to an empty
array. Dates are real `YYYY-MM-DD` calendar dates; `updated_on` cannot precede
`started_on`.

Each project requires `repository`, `batch` (positive integer), `summary`,
`next_action`, `benefit_route`, `milestones`, and `benefits`. Repositories are
GitHub `OWNER/REPO` coordinates and are unique across batches without regard to
case. The contributor's own account is excluded. Ownership through an
organization and whether a repository is an external upstream must be checked
manually; a different account name alone does not establish external ownership.

The following is **illustrative syntax**, not a researched opportunity or
contribution record:

```json
{
  "schema_version": 1,
  "owner": "contributor",
  "started_on": "2026-10-17",
  "updated_on": "2026-10-17",
  "target_count": 100,
  "historical_submissions": [],
  "projects": [
    {
      "repository": "upstream/library",
      "batch": 1,
      "summary": "A public repository to investigate for a useful contribution.",
      "next_action": "Read the contribution policy and check for a selectable issue.",
      "benefit_route": {
        "kind": "unconfirmed",
        "qualification": "unverified",
        "checked_on": "2026-10-17",
        "summary": "No direct benefit route has been established.",
        "refs": []
      },
      "milestones": [
        {
          "stage": "target",
          "date": "2026-10-17",
          "refs": ["https://github.com/upstream/library"]
        }
      ],
      "benefits": []
    }
  ]
}
```

Unknown or missing fields, duplicate JSON keys, non-finite JSON numbers and
inputs larger than 4 MiB are rejected. Strings must be nonempty, bounded and
single-line without control characters. Evidence references are HTTPS URLs
without embedded credentials; reference arrays cannot contain duplicates.
These syntax rules are not a privacy filter. Publish only deliberately selected
public material and inspect the complete diff.

## Contribution milestones

`milestones` is a nonempty, cumulative prefix of the sequence below. A stage
cannot be skipped, repeated or reordered. Each milestone requires `stage`,
`date` and a nonempty `refs` array, plus the stage-specific fields in the table.
Dates cannot decrease, precede `started_on` or follow `updated_on`.

| Stage | Additional fields | What the evidence must establish |
| --- | --- | --- |
| `target` | None | A real external repository and a plausible reason to investigate. |
| `screened` | `policy_ref` | Applicable contribution and AI-use policy; an assessed task or gap. |
| `selected` | `selection_ref` | A concrete useful task, current selectability and any required maintainer assignment or permission. |
| `reproduced` | `source_commit`, `source_ref`, `validation` | A baseline defect or demonstrated shortfall in a supported workflow, at an exact revision. |
| `validated` | `source_commit`, `source_ref`, `validation`, `review_ref` | Meaningful passing validation and review of the proposed revision. |
| `submitted` | `pr_url`, `source_commit` | An actual upstream PR containing the validated revision. |
| `accepted` | `acceptance_ref` | Actual upstream acceptance, independently of tests or submission. |

`source_commit` is a full lowercase 40-character Git SHA. `source_ref` is a
GitHub commit URL ending in that exact SHA; a contributor fork is valid for the
proposed source. At submission, the SHA must equal the preceding validated SHA.
The submitter must check that the upstream PR actually contains that revision.
The validator does not query the PR head.

`validation` has exactly three fields:

```json
{
  "command": "python3 -m unittest discover -s tests -v",
  "result": "passed",
  "ref": "https://github.com/contributor/evidence/blob/cccccccccccccccccccccccccccccccccccccccc/validation.md#fixed"
}
```

Use `result: "reproduced"` for the baseline milestone and `result: "passed"` for
the validated milestone. A reproduced wrong result need not have a nonzero
process exit code. The linked record must describe the exact commands and
configuration, revision, observed result, test counts, skips and remaining scope
limits. Prefer immutable commit permalinks and exact run/attempt links.
`review_ref` must identify the review of this revision and any required personal
review. Agent output alone cannot establish human review or independently
learned human skills. Useful documentation or workflow changes may demonstrate
a specific baseline shortfall; do not invent a failing software test for them.

`pr_url` must be the canonical `https://github.com/OWNER/REPO/pull/NUMBER` in the
project's upstream repository. An acceptance reference must identify that PR,
an acceptance comment or review on it (`#issuecomment-NUMBER` or
`#pullrequestreview-NUMBER`), or an exact commit in the same upstream repository.
The author must confirm that the link establishes acceptance; a PR link alone
does not prove a merge. Partial incorporation must be described precisely and
must not be labeled a full PR merge.

**Goal credit is one per distinct repository reaching `submitted` during this
campaign**, including those that later reach `accepted`. Qualified here means
the recorded contribution evidence meets this schema. It does not mean the
work earned money or that the benefit program found the contributor eligible.
Additional PRs to the same repository do not increase the distinct-project
numerator. Retain detailed follow-up work in dated progress records. Keep
screened or parked targets with an accurate next action; research does not
create submission credit.

Append a milestone only when its evidence exists. If the proposed revision
changes, revalidate and retain the earlier evidence in dated progress records
before updating the current revision. This tool validates a current record; it
does not reconcile previous file versions or perform automatic transitions.

## Historical submissions

`historical_submissions` preserves earlier PRs without inventing missing
reproduction, validation or review history. Each item requires `repository`,
`pr_url`, `submitted_on` and nonempty `refs`. Its submission date must predate
`started_on`. To record acceptance, add both `accepted_on` and `acceptance_ref`;
the acceptance date must lie between submission and `updated_on`.

Historical PR URLs are unique and cannot also occur as new campaign
submissions. They never count toward the campaign submission goal, even if
accepted after the campaign starts. They remain visible in a separate report
section, including in batch reports. An upstream may have both an older PR in
history and a different new campaign PR. Existing catalog and baseline
accounting remain separate and are not modified by this tool.

## Benefit routes and realized benefits

Every project has a `benefit_route` object with exactly `kind`, `qualification`,
`checked_on`, `summary` and `refs`. Route kinds are `cash`, `subscription`,
`credits`, `indirect` or `unconfirmed`. Qualifications are `unverified`,
`conditional`, `eligible`, `ineligible` or `not_applicable`.

`checked_on` cannot follow `updated_on`. An `unconfirmed` route must be
`unverified`; only that pair permits empty references. `not_applicable` is
reserved for indirect benefits. All other routes require source references.
A program advertising rewards can be `conditional` while issue fit, assignment,
contributor eligibility or an application decision remains unresolved. An
`eligible` claim needs evidence specific to the program's requirements and the
contributor. Neither status establishes a grant or payment. Keep application
and detailed eligibility evidence in the existing opportunity records; the
campaign tool does not submit or infer applications.

`benefits` is a list of evidenced benefit records. An empty list is appropriate
when nothing has been advertised for the particular opportunity or realized.
Each record requires:

| Field | Contract |
| --- | --- |
| `id` | A lowercase identifier, unique across the campaign; use letters, numbers and internal `-`, `_` or `.` separators. |
| `kind` | `cash`, `subscription` or `credits`. |
| `state` | `advertised`, `granted`, `activated` or `paid`. |
| `date` | The date of this state, no later than `updated_on`. |
| `summary` | What this evidence establishes, with any limitations. |
| `refs` | Nonempty public evidence links. |

`granted` additionally requires `grant_ref`; `activated` requires
`activation_ref`; and `paid` requires `receipt_ref`. These are HTTPS evidence
links, and earlier grant/activation links may be retained as a benefit advances.
Cash cannot be `activated`; subscriptions and credits cannot be `paid`.

Cash amounts use the paired `amount` and `currency` fields. `amount` is a
positive exact decimal string, with up to 18 integral and eight fractional
digits; floats, exponents and non-finite values are rejected. `currency` is a
three-letter uppercase code; its real-world validity is a manual evidence
check. Other benefit kinds cannot carry monetary amount fields. Paid cash
requires both fields and a payment receipt reference. Optional advertised or
granted cash amounts must be supported by their linked evidence.

A payment reference should identify one particular received payment. Avoid
recording the same payment under different IDs or repositories. Public evidence
may be a carefully redacted receipt or an attestation identifying retained
private proof; never publish account numbers, payment credentials, private
correspondence or an unredacted receipt. The tool checks the presence and shape
of a receipt reference, not whether money actually arrived.

Reports add only `paid` cash dated on or after `started_on`, using exact decimal
arithmetic and a separate total for each currency. They do not convert
currencies or assign cash values to subscriptions or credits. Benefit-state
counts also exclude earlier dates. Earlier benefit records may remain in the
project's evidence detail. Advertised amounts and unpaid grants remain visible
in their own states and do not enter paid totals.

## Continuing the campaign

Use a small batch to select the next supported, useful task, then perform the
work in an isolated checkout. The report can be produced in a cloud workspace
or on any supported machine. Review current upstream feedback and paid-work
selectability during each active session. Update public evidence and the next
action, validate the campaign, regenerate the report and publish the reviewed
changes through the normal repository process. The queue and evidence make the
work resumable; they do not imply unattended or guaranteed future execution.
