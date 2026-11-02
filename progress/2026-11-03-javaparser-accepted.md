# Fourth accepted external project: JavaParser

Observed November 3, 2026 in Europe/Vienna (November 2 UTC).

**Verified acceptance total: 4 / 100 distinct external projects; 96 remain.**
The retained three-project baseline is Commons Lang, LZ4 and Commons CSV.
JavaParser adds one project. This record verifies an upstream acceptance that
already occurred; this observation session did not perform the final source
revision or upstream merge. No payment, activated benefit or release is asserted.

## Canonical acceptance

- [PR #5188](https://github.com/javaparser/javaparser/pull/5188), authored by
  `agamal026`, is closed and merged. It was created October 21 and merged
  **2026-11-02T22:34:06Z** (November 2 at 23:34:06 in Vienna).
- Final PR head: `11f4b35dffc4211636db7526767fbc55a6185955`.
- [Accepted squash](https://github.com/javaparser/javaparser/commit/71544cb30b8857f32282d2edbd23e9d0a581d6a9):
  `71544cb30b8857f32282d2edbd23e9d0a581d6a9`.
- Accepted tree: `91ec7ca18daab54ea83fbb2008a86f1b554d7c81`;
  parent: `34e9de6767832089fa417b9db333cf5279f93bcf`.
- [Issue #5078](https://github.com/javaparser/javaparser/issues/5078) is
  closed as completed at `2026-11-02T22:34:08Z`.

The final change touches only
`javaparser-core-testing/src/test/java/com/github/javaparser/utils/TestParser.java`:
22 additions and 19 deletions. It delegates parsing to independently configured
`JavaParserAdapter` instances while preserving the helper's public API and JUnit
assertion-failure messages. The private wrapper is named `failOnParseProblem`,
and the original `ParseProblemException` is retained as the cause.

The [maintainer's review](https://github.com/javaparser/javaparser/pull/5188#issuecomment-6584405403)
requested removal of the additional `TestParserTest`, a clearer wrapper name and
a single commit, and suggested retaining the exception cause. The accepted diff
reflects those changes. The earlier two-file submission and its validation are
historical; do not describe the removed test class as part of the accepted patch.

## Retention and final-head checks

Observed upstream `master` is `338feab92ee15d7365e2b6dc5ff8f51b14fd9896`.
The [comparison from the accepted squash](https://github.com/javaparser/javaparser/compare/71544cb30b8857f32282d2edbd23e9d0a581d6a9...338feab92ee15d7365e2b6dc5ff8f51b14fd9896)
is one commit ahead, zero behind, and has the accepted squash as merge base.
Only `pom.xml` changes afterward, so the accepted helper remains in this observed
upstream revision.

GitHub's workflow metadata for final head `11f4b35d` reports both workflows
completed successfully:

- [Build and test using Maven, run 41506819484](https://github.com/javaparser/javaparser/actions/runs/41506819484).
- [Code generation and formatting, run 41506820123](https://github.com/javaparser/javaparser/actions/runs/41506820123).

This supersedes the earlier approval-pending observation for this submission.
No workflow was rerun for this record. Individual job logs, exact test counts,
platform coverage and skips were not audited here. Historical local/AppVeyor
results for `07afbca4` must not be relabeled as final-head results.

## Accounting and pending synchronization

JavaParser #5188 qualifies through its actual campaign-era upstream merge with
source linkage. The earlier rejected JavaParser #5175 remains excluded. Tests,
reviews, source revisions and this owned-hub record do not create additional
project credits.

**The structured ledger and generated campaign report have not been updated by
this record.** Their dated three-project export remains an older snapshot, not
the latest verified total. Reconciliation must retain the rejected history,
record #5188's distinct acceptance, and regenerate the report with the existing
validator. Do not hand-edit the generated report or invent missing final-head
local validation history.

Other target-specific publishing restrictions and personal contributor
requirements remain separate. This merge does not prove that the connector can
publish to another upstream repository or that scheduled execution is repaired.

This record was prepared with OpenAI ChatGPT assistance and serial automated
source/metadata review. It does not assert a new independent-agent or personal
human review. Canonical upstream maintainer review and merge evidence are linked
above.
