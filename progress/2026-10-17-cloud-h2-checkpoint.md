# 2026-10-17 — Cloud continuation, delivered follow-ups and H2 review

## Result and accounting

Cloud development and owned-repository publication are working. The campaign
still has **100 researched targets and zero new upstream submissions**. One
H2 proposal has meaningful focused validation and automated review, and is
preserved in a contributor-side draft. It is not submission-ready: its remaining
technical and contributor-statement gates are explicit. Six historical PRs
across five external projects remain separate. No payment or newly activated
subscription benefit has been verified.

The campaign workbench commit
[`5567ff729e85d3b8b8fad5413cf0e13a75a7fc7b`](https://github.com/agamal026/opensource/commit/5567ff729e85d3b8b8fad5413cf0e13a75a7fc7b)
passed [hosted run 39070443787](https://github.com/agamal026/opensource/actions/runs/39070443787):
Python 3.10, 3.12 and 3.14 on Linux and Python 3.12 on Windows. All four jobs and
their validation steps succeeded. The preceding local verification passed 81
tests with no failures, errors or skips.

The commands, outcomes and file identities for this follow-on hub checkpoint
are recorded in [its verification receipt](2026-10-17-cloud-verification.json).

## Follow-ups actually delivered

After the GitHub connector rejected the two comments with HTTP 403, the already
authorized PC GitHub CLI was used as an explicitly announced publishing bridge.
The correct host and GitHub account were verified, and each discussion was read
immediately before posting. Both public records were then read through the
cloud connector. No credential was transferred to the cloud.

| Existing contribution | Delivered action | Verified public record |
| --- | --- | --- |
| npm/cli #9954 | Ask a maintainer to admit workflows for the unchanged tested PR head; both referenced runs still require action and have no jobs | [Comment at 21:35:40 UTC](https://github.com/npm/cli/pull/9954#issuecomment-6241492647) |
| AOMediaCodec/libavif #3413 | Ask for reconciliation of the CLA bot record; all 25 build/test/format checks passed while the CLA status remained failed | [Comment at 21:36:01 UTC](https://github.com/AOMediaCodec/libavif/pull/3413#issuecomment-6241498834) |

The second browser wait timed out after the CLI had posted the comment. The
canonical GitHub discussion established success before any retry, preventing a
duplicate. These questions now await responses or materially changed evidence.
They do not establish CI admission or CLA clearance themselves. Other unchanged
threads did not receive generic reminders.

## H2 #4456: exact source and review

- [Upstream issue](https://github.com/h2database/h2database/issues/4456).
- [Pinned upstream base](https://github.com/h2database/h2database/commit/f2922a7766ec2472bc65d5e5ab4086390a76a42c):
  `f2922a7766ec2472bc65d5e5ab4086390a76a42c`.
- [Published final source](https://github.com/agamal026/h2database/commit/9d7a0ad26f8a53654e0ce106a80f702ae5840a28):
  `9d7a0ad26f8a53654e0ce106a80f702ae5840a28`, branch
  `fix/4456-any-parameter-types`.
- [Contributor-side review draft](https://github.com/agamal026/h2database/pull/1).
- [Complete immutable evidence](https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/README.md):
  commit `0feb07c57de0641cda13ad69de24ecf88fc4c917`, branch
  `review/4456-evidence`.

The proposal changes four upstream files, with 73 insertions and 3 deletions.
The locally calculated and remote-created source trees both equal
`07172cddd8b11fa8a5325ccb40072de775f3eaa7`. The final patch SHA-256 is
`12214cbedb78209380b7b4d6c7402752de14b96bb464abe9a10ab224abcf3e98`.

The indexed query incorrectly loses a VARCHAR value such as `'01'` when a
numeric `ANY(?)` parameter is converted into an index key. The correction checks
the runtime comparison type and uses the remaining bounds or a scan when that
conversion is unsafe. Safe string lookups retain index use.

Review found a second, stateful failure in the first draft: after a scan stops
early at LIMIT, a reused cursor can feed old rows into the next safe lookup.
The final patch resets that cursor at the start of each execution and includes
an ordered/LIMIT rebinding regression. The discarded draft is retained only as
a labeled negative control in the evidence branch.

### Passing focused evidence

| Validation | Actual outcome |
| --- | --- |
| Build and Javadoc | Final `./build.sh jar` exits 0; JDK 17 with Java source target release 11 |
| Original JDBC reproduction | Unchanged source returns 1 before indexing and 0 after; final source returns 1 and 1 |
| Exact integrated regression | Original production exits 1 on missing rows; first draft exits 1 on ordering; final production exits 0 |
| Selected complete upstream classes | TestPreparedStatement, TestIndex, TestCompoundIndexSearch, TestCompoundIndexParamSearch and TestOptimizations all pass with memory mode, assertions and a 128 MiB maximum heap |
| Binding/configuration coverage | 96 cases within the integrated method, plus four safe lookup scan-count controls |
| Ordering/rebinding differential probe | 432 cases per version; 160 original indexed/scan mismatches, zero final mismatches |
| Changed production coverage | 8/8 executable lines and 4/4 new branch outcomes covered by JaCoCo |

These are scoped results. Root performed automated code review of the exact
final diff; personal human review has not been asserted.

### Remaining technical and contributor gates

Both broad-suite attempts ran before the final cursor reset, reported failures,
and were stopped with exit 130. There is **no complete final-patch full-suite
pass**. Original-production controls reproduce the memory-exhaustion and lazy
query timing failures. File-lock, SSL trust, MVStore format and MVStore benchmark
failures remain unclassified. Final and pristine-baseline spelling/format checks
have identical diagnostics after only working-directory normalization, but both
remain failed. Full documentation/release validation is also incomplete; the
release installer was not executed because it contains Maven publication.

The fork's unchanged CI workflow specifies Java 11 and 17 and
`./build.sh jar testCI` with a read-only contents token. The initial workflow
list was empty, and enabling it by filename returned 404. The Actions page then
identified the actual cause: inherited workflows were disabled on the new fork.
After reviewing the workflow, fork Actions were enabled through the authorized
GitHub browser session. Creating `ci/4456-java11-17` at the exact final source
triggered [hosted run 39073428774](https://github.com/agamal026/h2database/actions/runs/39073428774)
at **22:02:30 UTC**. Its head is
`9d7a0ad26f8a53654e0ce106a80f702ae5840a28`; it was **in progress** when read back
at 22:06 UTC. This is an actual CI execution, with its final outcome still
pending. Read the run and complete job results before treating it as a pass.
The earlier `ci/4456-any-parameter-types` branch also points to the same source
but established no validation result.

[H2's contribution guide](https://h2database.com/html/build.html#providing_patches)
requires a truthful authorship/licensing statement for significant contributions.
That statement has not been supplied or signed on the user's behalf. AI
assistance is disclosed in the source commit and review draft. Before an
upstream PR, resolve that statement and the remaining validation gates. The
draft is in the user's fork, with maintainer modification permission disabled;
it is not an upstream submission and earns no campaign goal credit.

### Portable recovery

The review directory contains 47 payload files and two checksum inventories,
including the exact patch, four Java reproduction/test launchers, command
receipts, actual logs, coverage XML and license/dependency provenance. No full
checkout or dependency jars are included. The text artifacts are preserved in
the immutable evidence commit above, so recovery does not depend on this cloud
checkout or the PC.

The matching downloadable package is `h2-4456-review-package.zip`, 74,663 bytes,
SHA-256 `e8e9a74e445694504aa3602b2723bc8077b28276fd6ed60657fced5cce19d3d9`.
Checksum and ZIP integrity checks passed. Only deliberately selected public
material was published; the hub links to the fork's evidence rather than
importing third-party patch contents.

## Sustainable continuation

The hosted task **Advance open-source contributions** remains enabled, daily
around **08:00 Europe/Vienna**, starting **October 18, 2026**. Its updated prompt
and daily cadence were independently read back at 21:56 UTC and match the
[published continuation prompt](../docs/CONTINUATION-PROMPT.md). No scheduled
execution has occurred yet. The prompt now recovers the exact H2 branches,
recognizes the delivered comments, parks personal/access dependencies, and
prioritizes useful unblocked work.

A workflow review added two concrete improvements. First, preserve a durable
checkpoint after reproduction and after a reviewable fix, before long tests.
Second, verify the upstream's accepted submission channel during screening.
For example, [Linux requires email patches](https://docs.kernel.org/process/submitting-patches.html),
while the current campaign schema counts GitHub upstream PRs. Linux remains a
parked research target; the pool may need additional compatible targets as work
progresses. No tracker expansion was added to avoid this selection decision.
The roadmap's outdated statement that no schedule existed was also corrected
to point to the enabled hosted task and its actual run history.

The next financial follow-through remains the libzip accepted-change retention
check at or after **2026-10-22T13:12:13Z**. Its date alone does not establish
eligibility or an award. Current program terms and retained upstream evidence
must support any later application. The original October 13 baseline, November
12 review anchor, private application records and separate project ownership
remain preserved.
