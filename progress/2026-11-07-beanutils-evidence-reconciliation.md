# BeanUtils submission evidence reconciled

Reviewed November 7, 2026. This reconciles an existing contribution record;
it does not describe a new upstream submission, source change or acceptance.

**Accepted campaign progress remains 4 / 100.** The qualified-submission history
now includes seven distinct projects instead of six because BeanUtils #444's
existing evidence chain is recorded. The other 99 project records, historical
submissions and benefit records remain unchanged.

## Why the record needed correction

The BeanUtils entry still said that no contribution had been selected and
contained only a `target` milestone. Its next-action text already acknowledged
the open [upstream PR #444](https://github.com/apache/commons-beanutils/pull/444).
The earlier acceptance-count reconciliation deliberately left this full audit
for later. That stale summary and incomplete history are now corrected.

The PR was created on **October 22**, targeting the maintained `1.X` branch.
Its final submitted revision was published on **October 30**:
[`51a346ab12e0fd683df794ab40c9f18e58f92068`](https://github.com/agamal026/commons-beanutils/commit/51a346ab12e0fd683df794ab40c9f18e58f92068).
The validated and submitted milestones use October 30 to identify that revision;
they do not move the original PR creation date.

## Problem, selection and original reproduction

[BEANUTILS-417](https://issues.apache.org/jira/browse/BEANUTILS-417) concerns
`DynaProperty` writing custom metadata before default fields, which the actual
JBoss Marshalling serializing cloner rejects. The
[maintainer's earlier requirement](https://github.com/apache/commons-beanutils/pull/430#issuecomment-5105326637)
permits a new writer format if the new reader accepts both historical and new
data. The contribution writes default fields first and uses an empty serializable
superclass to distinguish legacy input without replacing callers' ordinary
`ObjectInputStream`.

The prior author had [abandoned PR #430](https://github.com/apache/commons-beanutils/pull/430#issuecomment-5499734362)
before this contribution. Screening retained the
[pinned contributor guide](https://github.com/apache/commons-beanutils/blob/22354f22fb150f82ae8cb7d4e444d2bf0d2bb1ff/CONTRIBUTING.md)
and [ASF generative-tooling guidance](https://www.apache.org/legal/generative-tooling.html);
the submitted PR discloses AI generation and automated reviews.

The [original immutable proof](https://github.com/agamal026/commons-beanutils/blob/cf4a3bcc5b8646fe71638b1d8f7112774b44aed4/contribution-review/BEANUTILS-417/README.md)
records the October 22 baseline at upstream
[`22354f22fb150f82ae8cb7d4e444d2bf0d2bb1ff`](https://github.com/apache/commons-beanutils/commit/22354f22fb150f82ae8cb7d4e444d2bf0d2bb1ff),
with only the documented test/dependency patch applied. The focused run reported
104 cases: 91 passed, three assertion failures, nine errors and one skip.
The regression cases exercise the real serializing cloner; this was not a full
application-server deployment. The recorded command and environment retain
their original October 22 date.

## Validation of the final submitted source

The [October 30 correction packet](https://github.com/agamal026/commons-beanutils/blob/8686e6f615c3eee822ef5325ddf56e3aaf8b27eb/contribution-review/BEANUTILS-417/static-accessor-validation-20261030/README.md)
binds the tested files to source `51a346ab`, complete tree
`285a9ca59ab976121d2935722875f310d80756b6`, and parent
`1d95c95c3045da8939db4c93ba2d13cf27ae241f`. The source was tested before commit
creation; its complete tree and file identities were subsequently verified.

The follow-up replaces a final instance helper with a static accessor, avoiding
a method collision with an existing same-package subclass. Its regression
checks actual constructor-supplied subclass state. The control using the prior
submitted production fails during test compilation: **zero JUnit cases ran**
in that control. This is separate from the original October 22 runtime failures.

| October 30 execution | Reported | Passed | Failed | Errors | Skipped |
| --- | ---: | ---: | ---: | ---: | ---: |
| Corrected focused suite | 105 | 104 | 0 | 0 | 1 |
| Corrected full default lifecycle | 1,294 | 1,286 | 0 | 0 | 8 |

The full log and all 105 suite totals were independently audited for this record.
The baseline-control, focused and final full-log hashes match the immutable
packet. The full lifecycle completed `clean apache-rat:check verify japicmp:cmp
javadoc:javadoc checkstyle:check`: RAT approved 293 files with no unknown or
unapproved files, Checkstyle checked 269 files with no violations, and Javadoc
was generated. No BeanUtils tests or builds were rerun for this reconciliation.

Environment: Linux amd64, Temurin 17.0.21+9, Maven 3.9.16, compiler release 8.
The eight existing skips and memory-test exclusions remain. No Java 8 runtime,
other operating system, complete application-server or coverage result is
established. The original binary-client and wire checks remain historical;
they were not relabeled as executions against the later source.

Japicmp reports source/binary compatibility and the explicit
`SERIALIZABLE_INCOMPATIBLE_SUPERCLASS_MODIFIED` finding. That finding is not
suppressed. Compatibility is directional: new readers accept old and new data;
old releases reading newly written data are outside the guarantee. The hierarchy
change is observable through reflection and commits the marker's serialized form.
All 22 historical fixtures remain unchanged and are read by one active test case,
not counted as 22 separate tests.

The [public review record](https://github.com/agamal026/commons-beanutils/blob/8686e6f615c3eee822ef5325ddf56e3aaf8b27eb/contribution-review/BEANUTILS-417/static-accessor-validation-20261030/review.md)
records separate automated design and integration/evidence reviews. This is AI
review, not a claim of personal human review or maintainer acceptance.

## Remaining dependencies

PR #444 remains open and unmerged at `51a346ab`. Its upstream Java CI and CodeQL
workflows require admission and have zero jobs. There is no owned-fork hosted
run for that source; the passing evidence above is local execution. Missing or
unadmitted CI is not a passing check or an observed code failure.

The upstream description still cites initial source `1d95c95c` and its original
1,293-case build. The attempted description update has an unresolved integration
permission denial. The
[prepared revised description](https://github.com/agamal026/commons-beanutils/blob/3786470d8004e1cc811ecfabc63dbb127e29e45e/contribution-review/BEANUTILS-417/static-accessor-validation-20261030/prepared-pr-description.md)
remains a draft in the owned fork, not an applied upstream change. This audit
did not retry that operation or send another admission request.

The four accepted projects, all benefit records and the original campaign start
remain unchanged. No new eligibility, payment, activated benefit or personal
learning is asserted. Follow substantive maintainer feedback or admitted checks;
reuse the existing source proof with its original dates.
