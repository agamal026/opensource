# Accepted contribution accounting and libzip review reconciliation

Reviewed **November 1, 2026, Europe/Vienna**, during a manual continuation.
The underlying GitHub/source observations occurred on October 31 UTC. This
is a selected review, not a refresh of every project or the historical
October 18 registry snapshot.

## Result and owned-tool correction

The independently verified accepted count remains **3 / 100**, with **zero new
accepted projects in this continuation**. The public tracker had not incorporated
the later acceptance records, and its renderer incorrectly used submitted PRs
as the goal numerator. That differed from the accepted-project objective.

`contribution_campaign.py` now counts only accepted projects toward the goal in
both the report and CLI validation summary. Qualified submissions remain a
separate measure. A filtered batch retains the whole-campaign headline while
its stage table shows only that batch. Historical submissions remain excluded,
even when accepted after the campaign started.

The existing baseline milestone now permits an explicitly `characterized`
result for supported-behavior test coverage. Its stored stage identifier remains
`reproduced` for compatibility, but reports label that slot **baseline assessed**
and display the actual result. Proposed-revision validation still requires
`passed`; exact source, evidence, review, submission and acceptance requirements
remain. This prevents the CSV record from implying a failing parser baseline.

The generated report records six distinct qualified submission histories and
three accepted projects. That submission metric is limited to the complete
histories currently entered, not a complete inventory of every later PR or
revision. BeanUtils #444 and the later JavaParser #5188 are linked below; their
full historical milestone backfill is outside this correction. Earlier records
and failed/rejected work are not erased.

## Acceptance evidence

| Project | Accepted result | Source and linkage |
| --- | --- | --- |
| Commons Lang | PR #1826 merged October 19 at 22:29:43 UTC. | [Merge `d6264649`](https://github.com/apache/commons-lang/commit/d626464952b57e665a83bf556cd0f0e7fd9983fb), [original PR](https://github.com/apache/commons-lang/pull/1826). Current inspected master `b8726053` retains both corrected hash implementations. |
| LZ4 | Both production fixes from #1890 incorporated through maintainer #1905, merged October 20 at 03:33:12 UTC. | [Explicit acknowledgement](https://github.com/lz4/lz4/pull/1890#issuecomment-6281751967), [merge `4eba0114`](https://github.com/lz4/lz4/commit/4eba01144bb54014d6adde134b6da2cf44c28885). Original #1890 closed unmerged; the larger test was simplified. Current inspected dev `0abbf9f` retains both fixes. |
| Commons CSV | Useful automatic-header coverage from #640 adapted on October 22. | [Maintainer explanation](https://github.com/apache/commons-csv/pull/640#issuecomment-6339536042), [incorporation `e9ed42a`](https://github.com/apache/commons-csv/commit/e9ed42afa814b07ccf3be74ece6b25e16d59be54). Original #640 closed unmerged. Current inspected master `7918b27` retains the test and contributor credit. |

The [machine-readable observation](2026-11-01-selected-observation.json) records
full SHAs and exact historical acceptance times. One project is counted once,
regardless of additional PRs or source revisions. Rejected JavaParser #5175 and
BCEL #540 receive no acceptance credit. Historical libzip #576 remains outside
this campaign cohort.

### CSV evidence is characterization, not a parser fix

CSV-312's reported exception was not reproduced. The submitted four tests
characterized LF/CRLF inside quoted headers with bare parsing or automatic
header extraction. The maintainer retained three adapted automatic-header cases
for CR, LF and CRLF in the existing `CSVParserTest`, omitting redundant no-header
coverage. The accepted changelog credits agamal026 and #640.

The [immutable historical proof packet](https://github.com/agamal026/commons-csv/blob/5b7686ca63bcbeb1177d7e4d2bcb6726063fb83d/contribution-review/csv-312/README.md)
records 4/4 focused cases and a complete default build of 989 tests: 978 passed,
zero failures/errors, 11 existing skips. Required default gates completed.
The final build finished October 22 at 05:14:16 UTC on baseline `b217f58` plus
the reviewed test bytes. Equivalent source `f609cb0` was created at 06:26:18 UTC;
the earlier build did not check out that later commit. The public packet retains
source hashes, complete final logs and earlier failure qualifications.

The campaign's command field uses the retained, sanitized full-build invocation,
including environment-specific settings, cache and JDK-module Javadoc launcher.
The original focused invocation's complete flags were not retained; ordinary
reviewer commands are not relabeled as historical execution. Three automated
policy/source/artifact reviews are recorded in the recovered original handoff;
no human review is inferred from those reviews.

## Existing open PRs

| PR | Current source | Actual upstream state |
| --- | --- | --- |
| [BeanUtils #444](https://github.com/apache/commons-beanutils/pull/444) | `51a346ab` | Open/unmerged; Java CI and CodeQL require admission, zero actual jobs. The description still identifies older source. Its prior update operation was denied; it was not repeated. |
| [JavaParser #5188](https://github.com/javaparser/javaparser/pull/5188) | `07afbca4` | Open/unmerged; Maven and code-generation workflows require admission, zero jobs. AppVeyor reports success. |
| [Compress #825](https://github.com/apache/commons-compress/pull/825) | `7e647788` | Open/unmerged; three workflows require admission, zero jobs. |
| [Jackson #6302](https://github.com/FasterXML/jackson-databind/pull/6302) | `38261628` | Open/unmerged; four historical upstream build jobs passed, two trigger jobs skipped. Helper discussion is resolved; personal CLA remains unresolved. |

No new maintainer source revision request was found. Checks requiring admission
with zero jobs are unexecuted, not passed or failed source tests. No unchanged
upstream test matrix was rerun and no admission comments were posted.

The completed COMPRESS-729 contribution remains in
[owned validation draft #2](https://github.com/agamal026/commons-compress/pull/2),
source `f0ad0a1`, with its
[complete validation packet](https://github.com/agamal026/commons-compress/blob/46b6e4fe3ff023d54595c110bdf0aaecd4b06da7/contribution-review/COMPRESS-729/close-deflater-20261031/README.md).
The actual upstream PR-create operation returned HTTP 403. This owned draft is
neither an upstream submission nor acceptance, and the denied action was not
retried. The separate newer Jackson owned validation draft also remains distinct
from #6302's submitted source and personal requirements.

## Libzip: reconcile two different acceptance dates

The September crypto contribution was already reviewed separately on October 22.
A later continuation summary retained only the November 22 checkpoint for the
October CI change. That omission must not reset the older crypto acceptance
clock or trigger a false claim of first-time eligibility discovery.

| Scope | Acceptance and retained evidence | Remaining limits |
| --- | --- | --- |
| Crypto clearing | [`c3ba909`](https://github.com/nih-at/libzip/commit/c3ba909e296e824f794e26d36379174524af74b8), September 22 at 10:49:41 UTC; [maintainer acknowledgement](https://github.com/nih-at/libzip/pull/576#issuecomment-5777143699) at 13:12:13 UTC. Its conservative one-month checkpoint was already supported October 22. | Source retention and a security rationale do not establish panel qualification, participant eligibility, application status or payment. |
| Later CI work | [`2ff3269`](https://github.com/nih-at/libzip/commit/2ff326957e9633d051cf398bba88d41564eaf0f8), October 22 at 08:39:22 UTC; actual diff is five CI files. | November 22 at 08:39:23 UTC is this change's conditional retention checkpoint only. CI portability does not itself establish qualifying security impact. |

Current main [`729d89f`](https://github.com/nih-at/libzip/commit/729d89f1a6cbeaebe9d4accad23fc65f5a93bcde)
contains the crypto incorporation. A non-shallow public clone and connector
agreed on that head; `git merge-base --is-ancestor` returned zero. Inspection of
82 reachable revision snapshots, including acceptance and 81 later commits,
found the crypto implementation, tests, configuration and build integration
retained. `lib/zip_crypto.c` and both added regression files keep their original
blobs. A later header change adds missing string declarations without removing
the hardening. These are history/source checks, not 82 runtime tests.

The retained fallback uses volatile byte stores when explicit clearing routines
are unavailable. Current callers clear default and per-entry passwords and
WinZip AES wrapper state before release. This supports a concrete hardening
rationale; it does not prove exploitation, clearing of every secret copy,
optimizer behavior on every platform, or the panel's assessment of impact.

Current [program rules](https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md)
and [scope](https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md)
retain libzip as Tier 1, the one-month unreverted requirement, twelve-month age
limit and three-submissions-per-person-per-month limit. Their exact blob hashes
are in the companion observation. Full reward eligibility and application
status remain unverified. No form, personal declaration, application, reminder,
award or payment resulted from this continuation.

## Validation of this accounting correction

Three preliminary targeted regressions on the unchanged renderer produced two
assertion failures and one validation error: submission inflated the goal, the
filtered report inherited that mistake, and honest characterization was rejected.
The final tests add historical-acceptance and stage-validation controls.

The complete required local validation ran at **23:18:28–23:18:29 UTC on October
31**: **82 tests passed**, zero failures/errors/skips; registry validation,
unchanged historical STATUS consistency, campaign validation, generated campaign
report consistency and `git diff --check` all passed. The campaign validator
reports 100 targets, **3 / 100 accepted**, and six recorded qualified submission
histories.

[Validation receipt](evidence/2026-11-01-accepted-accounting/validation.json)
and [complete successful unittest log](evidence/2026-11-01-accepted-accounting/unittest.log)
identify commands, times, runtime, exact tested source hashes and limits. The
preliminary failing output is summarized but not archived as a complete log.
Tests ran before publication; a later commit must match these source bytes.
Hosted validation of the new revision was not yet executed at receipt authoring.

## Continuation

No new candidate issue IDs were allocated. The coordinator was the only source
writer; native specialists independently checked acceptance, history, access
scope and design. The new accounting change is distinct from older denied
checkpoint payloads and does not repair external GitHub permissions, replay
those actions or remove their restrictions.

The existing hourly task was observed paused, with its last recorded result
requiring user action but exposing no explanatory content. No schedule, enabled
state, duplicate task or immediate-run action was changed. This manual work does
not demonstrate restored recurring execution.

Continue from [the current record](../data/continuation.json), recover applicable
private restrictions before affected work, and act on a concrete maintainer
request or an eligible task with a usable publication and complete validation
route. Retain all accepted, historical, prepared and declined work separately.
