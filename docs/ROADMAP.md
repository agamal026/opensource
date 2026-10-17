# Roadmap and improvements

This plan continues the existing open-source work. The October 13 baseline and
November 12 review date remain planning anchors, not promises of merges or awards.

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
| 1 | Resolve real issues or concrete feedback on owned tools. | Reproduction, focused regression, review, relevant CI, and a release containing the fix when appropriate. |
| 1 | Complete personal review of prepared libavif #2428. | Contributor review of exact parser, fixture, tests, and PR text; refreshed source/upstream preflight before submission. |
| 2 | Respond to substantive feedback on the five open upstream PRs. | Actual review request and validation of the resulting change; respect workflow admission and maintainer timing. |
| 2 | Support libzip Windows/CI work when needed. | Requested diagnosis or change, reproducible result, and maintainer disposition. |
| 3 | Resume Xcode investigation after workflow admission. | Real macOS/Xcode results for static/shared behavior and the libyuv-off duplicate-basename case. |

## Improvement rules

Extend the tools when real use exposes a missing capability. Keep refreshes
read-only and atomic, preserve curated context, and test missing or failed
evidence. Keep generated reports reviewable in Git.

Maintain original projects in their canonical repositories with supported-runtime
CI and focused release notes. Record external use only when directly observed.
Ownership and CI passes do not establish upstream responsibility or adoption.

No background schedule is installed. Private funding work stays in its original
workspace with its existing authorization and evidence rules.
