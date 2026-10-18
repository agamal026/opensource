# October 18, 2026: existing contribution review and CI follow-through

This session prioritizes concrete feedback on the three submitted campaign
projects. **The campaign remains at 3/100 distinct qualified submissions, with
zero accepted campaign projects and no realized benefits.** No new project was
selected while the existing LZ4 failure and Jackson review requests were active.

The first observation window was **13:37:19–13:41:02 UTC**. It refreshed the three
active PRs, their discussions and submitted reviews, commit checks/statuses, and
actual workflow jobs. The LZ4 correction and its separate local validation came
after that initial observation. The [verification record](2026-10-18-review-followthrough-verification.json)
keeps those source revisions and observation scopes distinct. Corrected LZ4 CI
finished successfully at the **14:11:25–14:11:26 UTC** observation, followed by an
actual TSan log audit. Jackson now targets 3.1; both owned and upstream
four-build matrices passed all 74 contribution cases. Final upstream body/head/base
readback was verified at **15:25:01 UTC**. Hub gates are recorded separately below.

## LZ4 #1890: diagnose the completed upstream failure

All jobs on the originally submitted source
[`f83be8241c6042a0f9b500da927f68caa905fc92`](https://github.com/agamal026/lz4/commit/f83be8241c6042a0f9b500da927f68caa905fc92)
finished. **53 of 54 CheckRuns and actual jobs succeeded; ThreadSanitizer failed.**
The job IDs, statuses and conclusions were independently reconciled. Eight of
nine workflow runs succeeded; Sanitizers failed. AppVeyor's GitHub status
reported success, updated at **13:13:40 UTC**. Its underlying logs were not read.
The previous six pending jobs resolved to five successes and this one failure.
No issue comments, inline comments or submitted reviews were returned for LZ4.

The actual [ThreadSanitizer job](https://github.com/lz4/lz4/actions/runs/39130134533/job/117683433807)
completed at **13:16:11 UTC**. Its log reports an eight-byte write in
`LZ4IO_decompressBlockLegacy` racing with an eight-byte read in
`LZ4IO_writeDecodedChunk`. The separate decoder and writer workers access the
same legacy byte counter. The new regression decoded **27,262,976 bytes**, then
ThreadSanitizer reported one warning; `test-lz4-multiple-legacy` exited **66** and
the overall make command exited **2**. This was an executed source diagnostic,
not a pending admission result.

The [exact-base sanitizer workflow](https://github.com/lz4/lz4/blob/e7c36223415219c0a18ea75e3fe2eb5d267ee667/.github/workflows/sanitizers.yml)
matches the logged command:

```sh
make clean
CC=clang CPPFLAGS="-fsanitize=thread" make -j -C tests test-lz4 V=1
```

The complete 280,158-byte failed-job log is preserved without modification in
the later evidence archive. Its SHA-256 is
`1efe907904adbe8c9dc58b9ca162260ac8d046d9694bc4726bf10852a9da8532`.
Successful job conclusions establish those job outcomes; this observer did not
fetch their logs or infer individual test-case counts.

### Reproduce the race independently of the end-marker change

The coordinator reproduced the same race with **GCC 13 ThreadSanitizer on the
unchanged upstream base**
[`e7c36223415219c0a18ea75e3fe2eb5d267ee667`](https://github.com/lz4/lz4/commit/e7c36223415219c0a18ea75e3fe2eb5d267ee667).
That control used an **ordinary 26 MiB legacy stream without an end marker** and
exited **66** with a TSan warning. The separate
[baseline packet](https://github.com/agamal026/lz4/blob/a7f764a75f381654296c2d6e55d9c89478c21400/contribution-review/1889/tsan-baseline/README.md)
was published with five verified blobs. It establishes that the end-marker
regression exposed an existing counter-ownership problem. This classification
rests on the unchanged-source control, not on an assumption that failing CI is
unrelated to the contribution.

### Correct the writer's counter ownership

The correction is published at
[`0917e70420429ea2acab6aaac48cffdf4e827440`](https://github.com/agamal026/lz4/commit/0917e70420429ea2acab6aaac48cffdf4e827440),
tree `26cbd5018554777b0b36efd53e76616d9e006b1d`, and the coordinator verified that
[upstream PR #1890](https://github.com/lz4/lz4/pull/1890) now contains it. The PR
still targets the same upstream base. All three PR file blobs were reconciled;
the total PR scope is three files, 66 additions and four deletions across three
commits. This is follow-through on an existing submitted project, not another
distinct submission.

The incremental change is **two additions and two deletions in
`programs/lz4io.c`**. It moves the shared count increment from the decoder to the
existing sole writer, immediately before that writer's progress read. The
private pointer becomes mutable. The established decoder-then-writer completion
waits still precede the caller's final count read. This follows the modern frame
writer's existing ownership pattern without changing the regression script,
adding a sanitizer suppression, or introducing a new locking primitive.

The [independent automated review](https://github.com/agamal026/lz4/blob/a96c638dc9160f43544c8cd8414624cb2c166730/contribution-review/1889/tsan-followup/AUTOMATED_REVIEW.md)
found no required source correction. It checked the exact changed-file bytes,
the relevant pthread and Windows completion implementations, counter lifetime,
sparse/empty/test behavior, and the modern-writer comparison. The reviewer did
not execute tests or audit runtime logs; those are separately recorded below.

| Exact correction identity | Value |
| --- | --- |
| Changed-file Git blob | `64953a23bf10a09259b5d854d1c1c01a2cd9c69d` |
| Changed-file SHA-256 | `47f8169a9883ab1155d6783d4c09979b4b2edd822299f6c5cbaa376bf35c7f42` |
| Unchanged regression Git blob | `98c4a91c3430d556f7fa3e1151b5960ceaa7e19e` |
| Automated-review SHA-256 | `745b6ea960e670890d7becc0698ce973407935a931f7e8ed905394f4d810a533` |

### Validate the exact correction

The coordinator executed **eight commands, all exit 0**, on Linux x86-64 with
GCC 13.3.0, between **13:53:09.730460 and 13:53:50.855016 UTC**:

| Executed check | Result |
| --- | --- |
| TSan build with `CPPFLAGS=-fsanitize=thread` and `CFLAGS=-O1 -g -Werror` | Exit 0 |
| Same ordinary 26 MiB decode that failed on unchanged upstream | Exit 0, no TSan warning |
| Byte-for-byte comparison of the decoded fixture | Exit 0 |
| Complete unchanged legacy regression under TSan | Exit 0, no TSan warning |
| Normal threaded and nonthreaded builds with `CFLAGS=-O2 -Werror` | Exit 0 |
| Complete legacy regression with the normal threaded executable | Exit 0 |
| Complete legacy regression with the normal nonthreaded executable | Exit 0 |
| Source whitespace check | Exit 0 |

The [immutable validation packet](https://github.com/agamal026/lz4/blob/a96c638dc9160f43544c8cd8414624cb2c166730/contribution-review/1889/tsan-followup/README.md)
records the exact source, commands, executable selection, output/log hashes and
limits. Its seven direct files were verified. The 94,144-byte
[validation archive](https://github.com/agamal026/lz4/blob/a96c638dc9160f43544c8cd8414624cb2c166730/contribution-review/1889/tsan-followup/validation-logs.zip)
contains fifteen members, including the full old failed TSan log. Its SHA-256 is
`bf98d199171bb449b87ce3a2dcc553eae47240128b78bed8b8f7ec5ed3ad4609`.
Named archive members are inside the ZIP; they are not all direct GitHub files.

### Confirm the corrected upstream CI and actual regression

At **14:11:25–14:11:26 UTC**, all **54 CheckRuns, all 54 actual workflow jobs,
and all nine workflows succeeded** on corrected source
`0917e70420429ea2acab6aaac48cffdf4e827440`. Their source heads and check/job IDs
were reconciled. [AppVeyor build 54919870](https://ci.appveyor.com/project/YannCollet/lz4-1lndh/builds/54919870)
also reported success, updated at **14:04:10 UTC**; its underlying logs were not
inspected. The PR body update, current head/base and three-file scope were read
back, with its update time at **14:05:25 UTC**. Maintainer modification remains
disabled, and the PR is open and unmerged.

The final body update at **14:41:45 UTC** links the completed hosted packet and
reports the successful matrix. Canonical matching body/head/base/open-state
readback was verified; its exact clock was not captured. No comment was posted.
The full CI observation remains **14:11:25–14:11:26 UTC**.

The successful [ThreadSanitizer job 117694255444](https://github.com/lz4/lz4/actions/runs/39133845170/job/117694255444)
completed at **14:10:01 UTC**. The independent observer inspected its complete
decoded log. The actual checkout was merge commit
`9eb241584f5019e048346682cdd8bd2ac76b0100`; canonical Git objects establish that its
tree is the same `26cbd5018554777b0b36efd53e76616d9e006b1d` as the submitted
correction. The log shows instrumented Clang compilation and linkage, including
the multithreaded CLI path. The exact Clang version was not printed.

The legacy script started at **14:00:34 UTC**, reached its final successful
command at **14:01:24 UTC**, and completed cleanup. Its named cases supplied
specific runtime evidence:

| End-marker case | Decoded bytes | Listed compressed bytes |
| --- | ---: | ---: |
| Multi-block sparse-tail frame | 27,262,976 | 12,305,419 |
| Empty frame | 0 | 8 |
| Concatenated legacy/empty/skippable/modern frames | 27,430,912 | 12,388,233 |

The log contains **six byte-comparison assertions** and **six empty-stdout
assertions** across the file and piped forms of these cases, plus named byte
totals, listing-size checks, and the expected malformed-input failures. No TSan
warning, summary or fatal diagnostic, or make failure, appears. Concurrent make
output was interleaved, so the audit matched unique fixture names and assertions
instead of assigning arbitrary adjacent output to this script. Other successful
job results are supported by job/step metadata; their logs were not individually
audited.

The returned decoded log is **299,883 UTF-8 bytes**, SHA-256
`a468dff927a895b094d9a42c0444a600ab49905d8552063ad8144309c218207e`.
Its BOM and LF line endings are preserved. Original HTTP transport bytes were
unavailable; this digest identifies the returned decoded text encoded as UTF-8.
The verification record retains the compact audit and canonical job references;
the full private monitoring response is not copied into the hub.

The complete hosted evidence is now preserved in the
[published supplement](https://github.com/agamal026/lz4/blob/7751a987a7199b696902630b16d8e831880e9451/contribution-review/1889/tsan-hosted/README.md),
commit `7751a987a7199b696902630b16d8e831880e9451`, tree
`26c43584a573c3b0ec837f98b3c933d60aa43f89`, parent
`a96c638dc9160f43544c8cd8414624cb2c166730`. The coordinator verified the branch,
commit, tree and all **five direct Git blobs**. Its 258,638-byte
[archive](https://github.com/agamal026/lz4/blob/7751a987a7199b696902630b16d8e831880e9451/contribution-review/1889/tsan-hosted/lz4-1889-tsan-hosted-evidence.zip)
has SHA-256
`9375604c1dcf8f545a12c5b24ac4130fe2be3d1f6ec5b1d1b3ac594f7b86d265`.
The complete monitoring receipt and decoded TSan log are among its five archive
members; they are not direct Git blobs. Publishing this packet does not change
the source revision or the **14:11:25–14:11:26 UTC** observation time.

The previous failed source and its completed jobs remain historical evidence.
The earlier broader local CLI failure at `test-lz4-blocksize` was not rerun or
relabeled as passing. The completed hosted matrix and inspected regression do
not establish whole-program race freedom, maintainer approval, upstream
acceptance or reward qualification.

## Jackson #6302: published 3.1 backport and completed upstream validation

[Upstream PR #6302](https://github.com/FasterXML/jackson-databind/pull/6302) now
targets **3.1**, with source
[`38261628a27c109e6e49c916cdb0f7e8bf7bbf45`](https://github.com/agamal026/jackson-databind/commit/38261628a27c109e6e49c916cdb0f7e8bf7bbf45)
on base `5d64697ef018099e3d5f951668752ec9d4ffabf9`. All 12 changed Git blobs
were verified: four commits, 776 additions and no deletions. The source tree is
`861d2292ae59d0c91fd3b572cd044212e2580c00`.

The actual backport and `UnwrappedContainerSerializerHelper` respond to the
member's [branch request](https://github.com/FasterXML/jackson-databind/pull/6302#issuecomment-6250227789)
and [helper request](https://github.com/FasterXML/jackson-databind/pull/6302#discussion_r4307148911).
The existing [maintainer review](https://github.com/FasterXML/jackson-databind/pull/6302#pullrequestreview-5563125328)
is **COMMENTED**. The [CLA reminder](https://github.com/FasterXML/jackson-databind/pull/6302#issuecomment-6250307295)
remains unresolved as an acceptance gate. Automated source and fixture reviews
are recorded as automated reviews; no human approval or legal assent is inferred.

### Keep each executed attempt distinct

The owned [validation draft #2](https://github.com/agamal026/jackson-databind/pull/2)
provided four actual builds for each of these source revisions on the real 3.1
base. It remains open/draft and receives no additional campaign credit.

| Source and workflow | Actual outcome per build |
| --- | --- |
| Test-only `4a47e457`, [run 39135075480](https://github.com/agamal026/jackson-databind/actions/runs/39135075480) | 53 cases: **one failure, 32 errors, 20 passes**. No other class failed. |
| First fix `c2366f76`, [run 39136144887](https://github.com/agamal026/jackson-databind/actions/runs/39136144887) | Test compilation failed because `Reference.getFrom()` was unavailable. **Zero tests executed.** |
| API correction `60218d2e`, [run 39136668969](https://github.com/agamal026/jackson-databind/actions/runs/39136668969) | All 53 original cases passed; 21 compatibility cases had 19 passes/two assertion failures. Total: **74 executed, 72 passed, two failed**. |
| Fixture correction `38261628`, [run 39137464915](https://github.com/agamal026/jackson-databind/actions/runs/39137464915) | **All 74 cases passed**; full suites had zero failures/errors and one existing skip. |

The baseline reproduced empty root output instead of `[]` and 32 property-context
`StreamWriteException` errors. Its full totals were 5,862 on JDK 17 and 5,864 on
JDK 21/25, each with one failure, 32 errors and one skip. Android steps were
skipped after the failing builds. The larger earlier 3.x totals remain separate.

The two later compatibility mismatches concerned object-array suppression and
Iterable content type behavior. The separately reviewed
[fixture-only correction](https://github.com/agamal026/jackson-databind/blob/3e832d88429ddd257b144fb1a811eebb3a3a91e2/contribution-review/6299/3.1-followup/jackson-6299-3.1-compatibility-fixture-review.md)
compares actual unwrapped output with the existing wrapped path from the same
writer, retaining explicit value/empty assertions and all 53 original cases.
Production source was unchanged by this fixture correction. The two expectations
were not independently reproduced on unchanged 3.1; no such baseline is claimed.

Final owned validation completed at **14:49:22 UTC**, observed at
**14:50:34–14:50:35 UTC**, with all four full logs audited. Actual checkout
`086c5a281dbe8099cd3367d089ca97ce66bea449` has the final source tree. Linux JDK 17
also passed the static Android API compatibility check.

### Confirm actual upstream execution and publish the response

The first observation of [upstream run 39138054220](https://github.com/FasterXML/jackson-databind/actions/runs/39138054220)
at **14:56:13–14:56:43 UTC** found `action_required` and zero jobs. This remains
historical, alongside the older 13:40 admission gate on original `de533c21`/3.x.

**Attempt 2 completed successfully at 15:10:36 UTC.** Metadata was observed at
**15:13:35–15:13:36 UTC** and all four complete build logs retrieved by
**15:13:49 UTC**. Six actual jobs comprise four successful builds and two skipped
downstream triggers. Seven CheckRuns include those jobs and successful Gitar.
An empty legacy status collection does not represent a pending workflow.

| Executed build | Contribution cases | Full suite | Failures / errors / skips |
| --- | ---: | ---: | --- |
| Linux JDK 17 | 74 passed | 5,883 | 0 / 0 / 1 |
| Windows JDK 17 | 74 passed | 5,883 | 0 / 0 / 1 |
| Linux JDK 21 | 74 passed | 5,885 | 0 / 0 / 1 |
| Linux JDK 25 | 74 passed | 5,885 | 0 / 0 / 1 |

All 53 original and 21 compatibility cases passed in each job, and class totals
reconcile with the full-suite aggregates. Actual upstream checkout
`21d5d2915c92b1d3ffdd765567d0b3b2d55e00cf` has the submitted source tree. Linux
JDK 17's Android API check passed at **15:09:44–15:09:48 UTC**; this was Animal
Sniffer compatibility verification, not device execution. Gitar's functional
validation remained disabled; the actual build logs supply functional evidence.

The immutable [3.1 source and validation packet](https://github.com/agamal026/jackson-databind/blob/3e832d88429ddd257b144fb1a811eebb3a3a91e2/contribution-review/6299/3.1-followup/README.md)
has **16 verified direct files**. Its 597,940-byte archive holds 55 payload files
plus a manifest, including all four attempt audits and 16 complete build logs;
SHA-256 `7d6924376c82ccb8482b2fdb4d59e3cac2190545c8a08a3439c643c7eb74d7a4`.
The later [upstream supplement](https://github.com/agamal026/jackson-databind/blob/d4b18b11fea2be9088b7ad19c768ae31998e2aed/contribution-review/6299/3.1-upstream/README.md)
has **five verified direct files**, leaving the original 16 unchanged. Its
169,768-byte archive holds 16 payload files plus a manifest, including all four
upstream logs and the earlier admission-gate receipt; SHA-256
`a1cac99dd956709aaa7f9cc29b0b1bc61b9e6a61b4a4faff56528b8e3c391572`.
Archive-only members require extraction; they are not separate GitHub blobs.

One substantive [helper-thread reply](https://github.com/FasterXML/jackson-databind/pull/6302#discussion_r4307557870)
was posted at **15:16:02 UTC** and canonically verified at **15:16:13 UTC**.
It addresses the helper, backport, validation and evidence without repeating the
admission request. The final body update at **15:24:42 UTC** was verified at
**15:25:01 UTC**: unchanged source/base, open/non-draft, five issue comments and
two inline comments. Its CI paragraph links the completed upstream proof.

The original owned 3.x draft closed at **14:50:50 UTC**, retaining its body and
source on `archive/6299-original-3.x`. Owned draft #2's final body was updated at
**15:13:36 UTC** and verified at **15:14:03 UTC**. These owned records and this
follow-through add no distinct project, acceptance or realized benefit.

## JavaParser and the older portfolio

[JavaParser #5175](https://github.com/javaparser/javaparser/pull/5175) remained at
`2a437e500bf54024772dd9f3d6d4149506defed2`, based on
`dc6bc07155cb0d0d7a8a427b76411848eb862136`. Fresh discussion/review reads found only
the existing author admission request, with zero inline comments or submitted
reviews. At **13:40 UTC**, the [codegen/formatting run](https://github.com/javaparser/javaparser/actions/runs/39117999673)
and [Maven run](https://github.com/javaparser/javaparser/actions/runs/39117999726)
still required action and each returned **zero actual jobs**. AppVeyor's GitHub
status remained successful; its logs were not inspected. Reuse the existing
Linux/Java 17 proof and wait for substantive feedback or admission; do not post
the same request again.

The five historical open PRs received **metadata-only** reads at
**13:37:19 UTC**: [npm #9954](https://github.com/npm/cli/pull/9954),
[libavif #3413](https://github.com/AOMediaCodec/libavif/pull/3413),
[libevent #1916](https://github.com/libevent/libevent/pull/1916),
[nginx #1734](https://github.com/nginx/nginx/pull/1734), and
[libzip #576](https://github.com/nih-at/libzip/pull/576). No head/base/update-time
or comment-count delta appeared against their preceding live observations. Their
discussion bodies, reviews, checks, workflow jobs and reward evidence were not
refreshed. The historical merged libavif record was not queried.

All six historical snapshot/catalog/provenance rows remain unchanged, including
their **October 17, 20:01:04 UTC** check-observation dates. Only the three current
campaign PR records are eligible for this update. The top-level snapshot date
does not mean that every registered PR was refreshed.

## Accounting, workflow lesson and continuation

The stage counts remain **96 target, one validated and three submitted**, with
zero accepted campaign projects. All original campaign milestones, historical
submissions, benefit routes and realized-benefit lists are preserved. The
registry still contains nine PRs across eight projects: eight open and one
historical merge. The current next actions follow actual review and CI evidence.

The useful automated workflow lesson is to resolve new failures and review
requests before starting more projects: inspect the failed job itself, establish
the exact unchanged-source control, validate the scoped correction, and preserve
the prior failure instead of replacing it with a later passing label. Review
must also check supported target branches and shared implementation structure.
These are demonstrated workflow corrections, not evidence of personal human
learning, review, maintainer acceptance or income.

Preserve the hourly native cadence, the user's completion-only notification
rule, all other existing tasks, the October 13 baseline and November 12 review
anchor. The earliest libzip reward recheck remains **2026-10-22T13:12:13Z** and was
not performed. H2/libavif personal gates and current screening exclusions remain
in place. No new benefits or reward eligibility are established.

All **six required local gates passed**. The unit gate at
**15:32:19–15:32:20 UTC** passed **81 tests**, exit 0, on Python 3.12.14.
At **15:49:22–15:49:23 UTC**, snapshot validation, status-report consistency,
campaign validation, campaign-report consistency and `git diff --check` each
returned exit 0. Tools, tests and workflows are unchanged. The verification
record retains the actual command receipts and log hashes.

This is the evidence record prepared before publication. Its resulting commit,
parent, tree, all eight published file blobs, branch and hosted Actions jobs and
steps are verified separately and retained in the continuation checkpoint. This
record does not predict its own commit identity or a hosted CI result.
