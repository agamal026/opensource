# Fourth accepted external project: JavaParser

Initial acceptance observation: November 3, 2026 in Europe/Vienna (November 2 UTC).
Ledger reconciliation: November 3, 2026.

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

## Accounting and synchronized continuation

JavaParser #5188 qualifies through its actual campaign-era upstream merge with
source linkage. The earlier rejected JavaParser #5175 remains excluded. Tests,
reviews, source revisions and this owned-hub record do not create additional
project credits.

The structured ledger now records #5188's acceptance, and the generated campaign
report shows **4 / 100**. The six qualified submitted-project records are still
six: replacing JavaParser's current contribution chain does not create another
distinct submitted project. The 99 other project records, all six historical
submissions and all benefit records are unchanged.

The earlier #5175 chain remains available in the immutable
[pre-reconciliation ledger](https://github.com/agamal026/opensource/blob/f1c4d528068d93c6ab3b1414e6fc4a9fe364c380/data/campaign.json)
and the existing dated #4074/#5175 evidence. It was rejected and receives no
acceptance credit. Appending the new merge to that old chain would misattribute
acceptance, so the current JavaParser chain now describes #5078/#5188 throughout.
It is not moved into the pre-campaign history because #5175 was submitted after
the campaign began.

The baseline-assessment milestone uses `characterized`, preserving the initial
`07afbca4` source and its original reported core-test command:

```sh
./mvnw -B --errors -pl javaparser-core-testing -am clean test --activate-profiles AlsoSlowTests
```

The [public PR description](https://github.com/javaparser/javaparser/pull/5188)
records 2,936 reported tests, zero failures/errors and eight existing skips for
that initial selected reactor. It also records 27 focused tests each on the
original and changed helper. These are recovered historical results, not new
executions. The profile belongs to an unselected module in that command, so no
additional slow-profile coverage is asserted. The characterization class was
subsequently removed as requested by the maintainer.

The validated and submitted milestones both identify final head `11f4b35d` and
use November 2. That submitted date describes the final source revision; the
PR was originally created October 21 at `21:06:08Z`. Final validation links the
two successful upstream workflow records above. The command was checked in
[`maven_tests.yml` at the final head](https://github.com/javaparser/javaparser/blob/11f4b35dffc4211636db7526767fbc55a6185955/.github/workflows/maven_tests.yml).
The initial local/AppVeyor test counts are not attached to the final head.

The README, roadmap and continuation pointer now identify the accepted state.
The broad registry report remains its explicitly dated October 18 snapshot;
this selected reconciliation is not a fresh collection of every registered PR.

The hub's existing offline tests, data validators and generated-report checks
passed for this reconciliation: 82 offline tests, both data validators, both
generated-report checks and the whitespace check. Exact results are recorded
with the hub PR.
The report was generated by the existing tool; no schema, implementation or
test changes were needed.

Other target-specific publishing restrictions and personal contributor
requirements remain separate. This merge does not prove that the connector can
publish to another upstream repository or that scheduled execution is repaired.

The initial acceptance observation used OpenAI ChatGPT assistance and serial
automated source/metadata review. The subsequent ledger reconciliation used a
coordinator and separate cloud agents for upstream review and accounting review.
This does not assert personal review by the contributor. Canonical upstream
maintainer review and merge evidence are linked above.
