# Commons Compress #825: framed stream counters

Observed through **2026-10-18 17:18:51 UTC**. The campaign now records **4 of
100 distinct external projects submitted**, **0 accepted campaign projects**,
and **0 verified realized benefits**. The six historical submissions remain
separate. The [submission receipt](2026-10-18-commons-compress-825-verification.json)
records the exact sources, publication readbacks, CI admission, and evidence.

## Published contribution

[Apache Commons Compress PR #825](https://github.com/apache/commons-compress/pull/825)
was created at **17:15:07 UTC** and read back at **17:15:56 UTC**. It is open,
ready for review, and unmerged. Its title is
`[COMPRESS-726] Count returned bytes in framed LZ4 and Snappy streams`.

| Identity | Verified value |
| --- | --- |
| Submitted head | `7e6477880259d60d4dfa60a5e34e4ea7875176b1` |
| Source tree | `9c0430eb9a40f5f493132589e6fef3b7ffcbe494` |
| Upstream master base | `611cad06b66842692870c6ae98f50de7ce4f25d5` |
| Change | 6 files, 190 additions, 3 deletions |
| Production scope | Two framed readers; 20 added lines |

The two readers inherited an output-count result that included framing or
compressed input accounting. The patch gives each reader a separate counter
and increments it only after a successful read returns bytes to the caller.
Empty streams start at zero; single-byte reads and read-based skips share the
same accounting. Existing compressed counts, legacy counts, pushback,
checksums, and decoding remain byte-for-byte unchanged apart from the three
counter insertions in each reader. The
[independent automated source review](https://github.com/agamal026/commons-compress/blob/6505ee953046ebda57a40d91d520214c1cf6b1bd/contribution-review/framed-statistics/local-verification/source-review.json)
records that comparison and its limits.

The change addresses the counter defect reported in
[COMPRESS-726](https://issues.apache.org/jira/browse/COMPRESS-726?focusedCommentId=18092163&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel).
The broader decompression-size-limit proposal remains separate in
[PR #777](https://github.com/apache/commons-compress/pull/777).
The counter patch does not implement or close that proposal.

## Before-and-after validation

| Execution | Actual result | Evidence and limit |
| --- | --- | --- |
| New and updated tests over unchanged upstream production | 89 tests, 39 failures, 0 errors, 0 skips | All 10 shared counter invocations failed; 50 selected existing cases passed. |
| Same tests with the prepared fix | 89 tests, 0 failures, 0 errors, 0 skips | All six file hashes match the later published source; the working tree had not yet been committed during this run. |
| Local default Maven build on published source | 4,791 tests, 2 failures, 0 errors, 26 skips | Existing TAR fixture UID/GID assertions failed under root ownership; later verification goals were not reached. |
| Those two tests over unchanged upstream source | 2 tests, the same 2 failures, 0 errors, 0 skips | Confirms the local fixture limitation; no source edits were applied. |
| Owned hosted default Maven matrix | All 19 jobs succeeded | Every job reported 4,791 tests, 0 failures and 0 errors; details below. |

The shared regression class contains five parameterized methods, executed for
both formats. Coverage includes empty streams, zero-length reads, single and
offset bulk reads, skipping, compressed and raw chunks, multiple chunks,
concatenated empty frames, metadata, and retained output counts after a later
framing exception. Existing format tests also cover the iWork dialect.

The [immutable baseline](https://github.com/agamal026/commons-compress/blob/191c9e8ce0fb7c478f64bd8912fc56d9747eca5d/contribution-review/framed-statistics/baseline/README.md)
preserves the failing output and test bytes. The
[local verification packet](https://github.com/agamal026/commons-compress/blob/6505ee953046ebda57a40d91d520214c1cf6b1bd/contribution-review/framed-statistics/local-verification/README.md)
preserves the focused pass, full local failure, unchanged-source control,
automated review, and CI setup. Attempts to prepare a non-root execution were
blocked by the runtime's UID/GID mapping before tests ran. They are not counted
as validation and were not an automatic approval rejection.

### Complete owned hosted validation

[Maven run 39147450534](https://github.com/agamal026/commons-compress/actions/runs/39147450534)
completed on attempt 1, with its last status updated at **17:06:21 UTC**.
All 19 complete job logs were read and independently audited. This includes
Java 8, 11, 17, 21, 25 and 27 on Ubuntu, Windows and macOS, plus the experimental
Ubuntu Java 28-ea job. Every job ran the unchanged default command:

```sh
mvn --errors --show-version --batch-mode --no-transfer-progress
```

Each job passed all 89 relevant tests without skips. Full-suite skips were
26 on Ubuntu, 30 on Windows and 28 on macOS. Build-plan checks, RAT, Checkstyle,
PMD and japicmp succeeded in all 19 jobs. Javadoc executed successfully in 16
jobs; the project's existing Java 8 profile omits it in the other three.

The tested merge was `76d0130283eb142314cf11bb42825798e9279a05`, tree
`75180283dda44c16550c644a7df3f88545424ac4`. A complete Git comparison against
submitted source `7e6477880259d60d4dfa60a5e34e4ea7875176b1` found only four
schedule-line deletions in two owned-fork security workflow files. These
deletions were made before enabling Actions to avoid starting additional
recurring work. Source, tests, build inputs, and the Maven workflow are
otherwise identical. The upstream PR contains no workflow edits.

CodeQL completed analysis and uploaded results. Its skipped-test build is
recorded separately. Dependency Review first failed because the owned fork's
dependency graph was disabled; after enabling that capability, retrying the
failed job produced a successful second attempt. Both logs are retained.

The [hosted verification packet](https://github.com/agamal026/commons-compress/blob/078e0a6a958ba1cf74387031867ae3eeb4450c8d/contribution-review/framed-statistics/hosted-verification/README.md)
contains the complete audit and a 439,350-byte ZIP with 22 decoded job logs and
their hash manifest. Its SHA-256 is
`218eee795b29e8aa44c5868921f2ffb588046d03b67e4a1719e35eba36d2f1de`.
All text, archive bytes, tree entries, parents and evidence branch references
were read back; the last hosted publication verification was at **17:14:27 UTC**.
The owned validation draft and evidence branches receive no external campaign
credit.

## Upstream review and admission

The upstream CodeQL, Dependency Review and Java CI runs each returned
`action_required`. Their actual job collections each contained **zero jobs**.
There were zero CheckRuns and zero legacy StatusContexts. The empty legacy
endpoint's combined `pending` value does not establish an executing build.

After reading all three discussion collections, one
[CI admission request](https://github.com/apache/commons-compress/pull/825#issuecomment-6252813089)
was posted at **17:18:39 UTC** and verified at **17:18:51 UTC**. Do not duplicate
it. At that observation the PR had one issue comment, zero inline comments,
and no submitted review in the earlier complete review collection. Upstream
execution, approval and acceptance remain outstanding.

The [contribution guide](https://github.com/apache/commons-compress/blob/611cad06b66842692870c6ae98f50de7ce4f25d5/CONTRIBUTING.md)
and [PR template](https://github.com/apache/commons-compress/blob/611cad06b66842692870c6ae98f50de7ce4f25d5/.github/pull_request_template.md)
were checked before submission. The existing Jira report supplies the issue
reference; typical bug fixes are within the guide's small-patch CLA exception.
The PR discloses AI tools and scope under the
[ASF guidance](https://www.apache.org/legal/generative-tooling.html).
Automated review is not recorded as personal human review or legal assent.

The requested Jira backlink is still pending. A post-submission public read at
**17:17:03 UTC** returned all four comments and no PR #825 backlink. Add the
link when the Jira write capability becomes available.

## Existing work and screening

The [bounded screen and follow-through receipt](2026-10-18-1608-screen-followthrough.json)
preserves the 16:08–16:11 UTC collection scopes and prior evidence references.
Jackson #6302, LZ4 #1890 and JavaParser #5175 had unchanged source revisions
and no new actionable discussion. Jackson's four build results, LZ4's 54 actual
successful jobs and audited TSan log, and JavaParser's two admission-gated runs
remain attributed to their original observations. Five historical open PRs
received metadata-only checks. The older merged libavif #3350 was not re-read.
No repeated comment or rerun was sent to those projects.

This cycle screened Commons Compress, Commons IO and jsoup. Commons Compress
advanced through submission. Commons IO IO-754 remains a researched reserve
outside the current 100 targets, with no implementation or reproduction.
jsoup's current policy rejects AI-generated code and AI-written issues, PRs
and discussions; its queue entry retains the evidence and excludes this
automated submission route. All 100 target histories remain in the queue.

## Benefits, workflow and next action

No selectable paid assignment, patch-specific reward qualification, participant
eligibility, award, activated subscription, credit allocation or payment was
established for this change. Conditional project scope is not a benefit earned.
Keep the existing libzip retention recheck at or after **2026-10-22T13:12:13Z**.
H2 and libavif retain their documented personal-review or legal dependencies.

The useful workflow result is a recoverable chain from failing tests through a
minimal fix, independent automated review, exact-source controls and complete
hosted job logs. Personal learning remains unverified until the contributor
reviews or practices the work. No additional tool change was needed this cycle.

Resume substantive maintainer feedback and the recorded CI admission gates
first. Reuse this proof while source, base, feedback and actual CI remain
unchanged. Restore source and evidence from the immutable links above in a
fresh cloud session. The existing hourly task remains the continuation channel;
do not add another worker. An enabled schedule is separate from actual run
history. Publish the final hub record, verify its own CI, and refresh the native
handoff with that exact commit before ending this cycle.
