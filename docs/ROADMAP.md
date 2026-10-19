# Roadmap and improvements

This plan continues the existing open-source work. The October 13 baseline and
November 12 review date remain planning anchors, not promises of merges or awards.

Select work against [the goal](../GOAL.md) and
[the opportunity notes](OPPORTUNITIES.md). Read both and the latest dated entry
in [progress](../progress/) at the start of every resumed session.

## First iteration

| Improvement | Result |
| --- | --- |
| Recover the workstation checkpoint | Verify the migrated workspace and exact prepared libavif patch hashes. |
| Create a public home for continued work | Organize tools, skill, contribution registry, generated status, and dated progress. |
| Replace manual status reconstruction | Add read-only PR refreshes and reports that expose pending, failed, and unknown checks. |
| Capture useful local Git state | Record branches, revisions, and change counts without copying checkout contents. |
| Make continuation repeatable | Version the workflow skill and validation/publication process. |

## Next actions

| Priority | Action | Evidence needed to finish |
| --- | --- | --- |
| 1 | Recheck the existing libzip reward evidence at or after 2026-10-22T13:12:13Z (15:12 Europe/Vienna on October 22). | Fresh evidence of continuing upstream incorporation and current program rules. This date does not establish a qualifying month of retention or payout eligibility. |
| 1 | Investigate a paid issue with current sponsor evidence that is unassigned or explicitly selectable. | Current sponsor offer, assignment availability, acceptance/payment terms, a reproduction, and a scoped implementation opportunity. |
| 1 | Resolve real issues or concrete feedback on owned tools. | Reproduction, focused regression, review, relevant CI, and a release containing the fix when appropriate. |
| 1 | Complete personal review of prepared libavif #2428. | Contributor review of exact parser, fixture, tests, and PR text; refreshed source/upstream preflight before submission. |
| 1 | Follow through on submitted [JavaParser #5175](https://github.com/javaparser/javaparser/pull/5175). | [October 19 maintainer direction and exact-head review](../progress/2026-10-19-review-routing.md): keep the PR open and preserve the regression tests while the maintainer investigates generic alignment. Related #5179 currently changes the CsmMix annotation path; no applicable import-list fix is verified. Adapt tests only when the relevant patch/request exists. Reuse unchanged passing tests and retain admission limits. |
| 1 | Follow through on submitted [Jackson databind #6302](https://github.com/FasterXML/jackson-databind/pull/6302). | The requested 3.1 backport/helper work and four upstream builds are complete at source 38261628a27c109e6e49c916cdb0f7e8bf7bbf45. Reuse [the completed upstream evidence](https://github.com/agamal026/jackson-databind/blob/d4b18b11fea2be9088b7ad19c768ae31998e2aed/contribution-review/6299/3.1-upstream/README.md). Follow substantive reviews and actual CLA/acceptance evidence; the earlier admission blocker is historical. |
| 1 | Follow through on submitted [LZ4 #1890](https://github.com/lz4/lz4/pull/1890). | Current head 0917e70420429ea2acab6aaac48cffdf4e827440 has 54 successful CheckRuns and successful hosted TSan in [the completed supplement](https://github.com/agamal026/lz4/blob/7751a987a7199b696902630b16d8e831880e9451/contribution-review/1889/tsan-hosted/README.md). Respond to substantive feedback or a new regression; retain the earlier broader baseline limitation without repeating successful unchanged tests. Acceptance and patch-specific benefits remain unverified. |
| 1 | Follow through on [Commons Compress #825](https://github.com/apache/commons-compress/pull/825) and [Commons Lang #1826](https://github.com/apache/commons-lang/pull/1826). | [Latest verified checkpoint](../progress/2026-10-18-commons-lang-1826.md), actual admitted jobs and substantive reviews. Owned validation is complete within its documented scope; both Jira backlinks exist. Preserve the single admission comment per PR and reuse unchanged successful tests. |
| 1 | Advance the next eligible contribution once actionable reviews are handled. | Read [data/continuation.json](../data/continuation.json), screen at most three candidates, reproduce one supported issue and establish a publication route. Review waiting alone does not hold the main implementation slot. |
| 1 | Resolve the prepared H2 #4456 contribution's remaining gates. | [Exact source and completed Java 11/17 CI evidence](../progress/2026-10-17-h2-final-ci-checkpoint.md), truthful contributor statement, and disposition of the documented docs/non-CI limits. Park personal/access dependencies while advancing useful unblocked work. |
| 2 | Respond to substantive feedback on the registered open upstream PRs. | Actual review request and validation of the resulting change; respect workflow admission and maintainer timing. |
| 2 | Support libzip Windows/CI work when needed. | Requested diagnosis or change, reproducible result, and maintainer disposition. |
| 2 | Pursue a fitting subscription or credit program for an actual project need. | Verified current criteria and project fit; record application, grant, and activated access separately. |
| 3 | Resume Xcode investigation after workflow admission. | Real macOS/Xcode results for static/shared behavior and the libyuv-off duplicate-basename case. |

## Improvement rules

Keep one main upstream implementation and one owned-tool improvement active.
Verify a usable publication route before starting another implementation that
needs a new fork. The successful JavaParser browser submission does not establish
connector permission for external PRs or future forks; prefer already writable
contributor forks when practical.
Timebox crowded unpaid proposal screening and park investigations without a
supported route to selection. Use `GOAL.md` to distinguish technical results,
realized benefits, and evidence of the contributor's personal learning.

Extend the tools when real use exposes a missing capability. Keep refreshes
read-only and atomic, preserve curated context, and test missing or failed
evidence. Keep generated reports reviewable in Git.

Maintain original projects in their canonical repositories with supported-runtime
CI and focused release notes. Record external use only when directly observed.
Ownership and CI passes do not establish upstream responsibility or adoption.

Hosted continuation is configured through the hourly task documented in
[cloud operation](CLOUD-OPERATION.md#schedule-and-notifications). Inspect available native run metadata and actual repository checkpoints to verify
execution; a last-run timestamp alone does not prove completion. Private funding work stays in its original
workspace with its existing authorization and evidence rules.
