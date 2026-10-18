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
| 1 | Follow through on submitted [JavaParser #5175](https://github.com/javaparser/javaparser/pull/5175). | [Exact published source, reused validation and submission read-back](../progress/2026-10-18-javaparser-5175-submission.md); follow GitHub Actions authorization/results and substantive review; AppVeyor reported success without underlying log inspection. Reuse unchanged passing tests. Submission does not establish acceptance or a reward. |
| 1 | Resolve the prepared H2 #4456 contribution's remaining gates. | [Exact source and completed Java 11/17 CI evidence](../progress/2026-10-17-h2-final-ci-checkpoint.md), truthful contributor statement, and disposition of the documented docs/non-CI limits. Park personal/access dependencies while advancing useful unblocked work. |
| 2 | Respond to substantive feedback on the six open upstream PRs. | Actual review request and validation of the resulting change; respect workflow admission and maintainer timing. |
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
[cloud operation](CLOUD-OPERATION.md#schedule-and-notifications). Read its actual
run history to verify execution. Private funding work stays in its original
workspace with its existing authorization and evidence rules.
