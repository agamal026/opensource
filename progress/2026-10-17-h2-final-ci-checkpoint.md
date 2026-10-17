# 2026-10-17 — H2 final CI, durable evidence and next action

The unchanged H2 #4456 proposal now has successful hosted Java 11 and Java 17
CI, with the completed results preserved alongside the original review evidence.
It remains a **validated proposal in the contributor's fork**, with no new
upstream submission or campaign submission credit. Documentation validation
still fails, and the personal contributor statement remains pending.

## Recover the exact source and evidence

Use these immutable references when recovering in a fresh cloud session:

| Record | Identity and public source |
| --- | --- |
| Upstream problem | [h2database/h2database #4456](https://github.com/h2database/h2database/issues/4456) |
| Upstream base | [f2922a7766ec2472bc65d5e5ab4086390a76a42c](https://github.com/h2database/h2database/commit/f2922a7766ec2472bc65d5e5ab4086390a76a42c) |
| Unchanged proposal | [9d7a0ad26f8a53654e0ce106a80f702ae5840a28](https://github.com/agamal026/h2database/commit/9d7a0ad26f8a53654e0ce106a80f702ae5840a28), tree `07172cddd8b11fa8a5325ccb40072de775f3eaa7` |
| Original review packet | [README at 0feb07c57de0641cda13ad69de24ecf88fc4c917](https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/README.md) |
| Completed CI and documentation supplement | [README at f190120801a23792717d6a2f0690b61398a5bafc](https://github.com/agamal026/h2database/blob/f190120801a23792717d6a2f0690b61398a5bafc/contribution-review/4456-follow-up/README.md), commit tree `01e007eba7a8a776ae4b564d04dca9d83c8fc443` |

The supplement's 15 files were published with the reference, tree and parent
read back. The original 49-file packet, including its checksum inventories,
remains unchanged. Source and workflow files were not changed for this follow-up.

The four-file patch still has SHA-256
`12214cbedb78209380b7b4d6c7402752de14b96bb464abe9a10ab224abcf3e98`.
It prevents an unsafe conversion of differently typed `ANY(?)` bindings into
VARCHAR index keys and resets reused cursor state between executions. The
original packet retains the reproduction, discarded-draft negative control,
regressions, safe-index controls and scoped coverage evidence.

The portable `h2-4456-complete-review-package.zip` contains **67 entries**, is
**203,483 bytes**, and has SHA-256
`8cb6378143b7b6f4f881cf816fc6012eaf6e320f4288c4d633a43f284c9442a3`.
Archive integrity and hash checks passed. Its contents and immutable GitHub
references allow recovery without the previous checkout or a connected PC.

## What the completed CI establishes

[Run 39073428774](https://github.com/agamal026/h2database/actions/runs/39073428774)
executed the unchanged upstream workflow at the exact proposal commit. Attempt
1 succeeded on both JDKs using `./build.sh jar testCI` from `h2`, with the
workflow's `JAVA_OPTS=-Xmx512m`.

| Job | Runtime | Successful Test-step completion, UTC |
| --- | --- | --- |
| [Java 11](https://github.com/agamal026/h2database/actions/runs/39073428774/job/117515577514) | Temurin 11.0.32.1+1 | 22:23:10 |
| [Java 17](https://github.com/agamal026/h2database/actions/runs/39073428774/job/117515577740) | Temurin 17.0.20.1+1 | 22:23:58 |

This is the complete **CI-selected suite**: six database configurations plus
additional/utility tests. `TestPreparedStatement` completed in all six
configurations on each JDK. Both logs report five unexecuted classes:
`TestDefrag`, `TestMVStoreBenchmark`, `TestSubqueryPerformanceOnLazyExecutionMode`,
`TestSpatial` and `TestLargeBlob`. The result does not cover every slower non-CI
mode or the full documentation/release process.

The successful Java 11 job retains one error annotation: a background MVStore
`OutOfMemoryError` during `TestOutOfMemory`. That test deliberately creates memory
pressure and subsequently records normal completion. **The exact diagnostic
remains unexplained**; it was absent from the retrieved successful exact-base
Java 11 log. Neither final log contains a framework `ERROR: FAIL` or a
durability-failure line. The supplement preserves the diagnostic and baseline
comparison without calling it expected or baseline-reproduced.

## Failures and contributor requirements remain explicit

The isolated final-source `./build.sh docs` attempt exited 1 because prerequisite
compiled classes were missing. `./build.sh jar docs` then completed the JAR build
and Javadoc but exited 1 during `CheckTextFiles`, reporting an automatic
`TestRecovery.java` rewrite and the 131-character line at
`RandomAccessStore.java:271`. Later documentation/link checks were not reached.

The blocking `RandomAccessStore.java` is byte-identical to the pinned upstream
base, and the original baseline evidence contains the same formatting finding.
This identifies unchanged blocking code; the documentation command remains
failed. Formatter edits stayed in the isolated copy, and the four original
proposal files still match publication. Earlier failed/interrupted non-CI broad
runs remain historical failures, rather than being replaced by this CI pass.

[H2's contribution guide](https://h2database.com/html/build.html#providing_patches)
requires a truthful authorship/licensing statement. It remains pending; automated
review and CI do not provide a personal statement or human approval. The
[own-fork draft PR #1](https://github.com/agamal026/h2database/pull/1) now includes
the final CI and documentation limitations. Canonical read-back verified its
body update at **22:39:57 UTC**, `draft: true`, and the unchanged source head.
It is not an upstream PR, acceptance or merge.

## Campaign state and existing follow-ups

The [campaign](CAMPAIGN.md) contains **100 distinct targets**: H2 is validated
and 99 remain at target stage. There are **zero new qualified submissions**.
Six historical PRs across five projects remain separate. No verified earnings
or new granted/activated benefits are recorded for this campaign.

The previously delivered [npm/cli #9954 comment](https://github.com/npm/cli/pull/9954#issuecomment-6241492647)
and [libavif #3413 comment](https://github.com/AOMediaCodec/libavif/pull/3413#issuecomment-6241498834)
remain the follow-up records. This checkpoint added no duplicate or new comments
to those threads. Their requests do not themselves establish workflow admission
or CLA clearance.

The [bounded candidate screen](../docs/CANDIDATE-SCREENING-2026-10-17.md), conducted
22:16:57–22:24:32 UTC, selected zero candidates. Preserve its competing-fix,
assignment and sponsor-policy exclusions when choosing the next task.

## Resume sustainable work

Read [GOAL.md](../GOAL.md), [opportunities](../docs/OPPORTUNITIES.md), this latest
checkpoint and [cloud operation](../docs/CLOUD-OPERATION.md). Recover the exact
proposal and both evidence packets before interpreting older pending-CI notes.
Do not repeat unchanged successful CI or implement an already competing fix.

If H2 is blocked by its personal contributor statement or an access dependency,
park it with the concrete review package queued for personal review and advance
the next useful unblocked task. Keep at most one main upstream implementation
and one owned-tool improvement active. Require current policy, selection and
benefit evidence before committing to new paid work.

The native **Advance open-source contributions** task is enabled daily at
**08:00 Europe/Vienna**, first scheduled for **October 18**. Its unchanged
prompt recovers the latest repository records. A final check found that its
cadence had changed back to hourly; the intended daily schedule was restored.
Independent read-back at **22:45:21 UTC** confirmed the daily cadence, enabled
state, unchanged prompt and no execution yet. The cause of the later cadence
change is not established. The two other tasks were unchanged. Review actual
schedule/run history during the first executions; future runs must record their
actual work.

Preserve the **October 13 baseline** and **November 12 review anchor**. The
libzip retention recheck remains **2026-10-22T13:12:13Z**; the date alone does not
establish a qualifying month, reward eligibility or payment. Private research
applications remain separate.

The preceding hub commit
[afa0dbaf3ffb1cfb0d7861817b47fbff8e6ebc6b](https://github.com/agamal026/opensource/commit/afa0dbaf3ffb1cfb0d7861817b47fbff8e6ebc6b)
passed all four jobs in [run 39074080118](https://github.com/agamal026/opensource/actions/runs/39074080118).
Use the [final verification receipt](2026-10-17-final-verification.json) for the
commands and outcomes associated with this new checkpoint.
