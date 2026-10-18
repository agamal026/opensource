# Contribution campaign

Started: 2026-10-17. Records reviewed through: 2026-10-18.

**Goal progress: 3 / 100 distinct external repositories with qualified campaign submissions.**

Full research queue: 100 repositories. Historical submissions: 6; excluded from this goal.

A qualified submission has the policy, selection, reproduction, exact source, passing validation, review and upstream PR evidence required by the schema. It does not establish acceptance or benefit eligibility.

This offline report checks record structure and consistency. Verify what the linked evidence establishes, current policies, ownership and benefit eligibility. This offline tool does not start background work.

## Contribution stages

| Stage | Currently at stage | Reached in displayed queue |
| --- | ---: | ---: |
| target | 96 | 100 |
| screened | 0 | 4 |
| selected | 0 | 4 |
| reproduced | 0 | 4 |
| validated | 1 | 4 |
| submitted | 3 | 3 |
| accepted | 0 | 0 |

## Batches

| Batch | Targets | Screened | Selected | Qualified submitted | Accepted |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 10 | 1 | 1 | 0 | 0 |
| 2 | 10 | 1 | 1 | 1 | 0 |
| 3 | 10 | 0 | 0 | 0 | 0 |
| 4 | 10 | 0 | 0 | 0 | 0 |
| 5 | 10 | 0 | 0 | 0 | 0 |
| 6 | 10 | 1 | 1 | 1 | 0 |
| 7 | 10 | 1 | 1 | 1 | 0 |
| 8 | 10 | 0 | 0 | 0 | 0 |
| 9 | 10 | 0 | 0 | 0 | 0 |
| 10 | 10 | 0 | 0 | 0 | 0 |

## Benefits

Only dated benefit records within this campaign appear in these totals. Advertised amounts, unpaid grants, subscriptions and credits are never converted into paid cash.

| Kind | Advertised | Granted | Activated | Paid |
| --- | ---: | ---: | ---: | ---: |
| cash | 0 | 0 | 0 | 0 |
| subscription | 0 | 0 | 0 | 0 |
| credits | 0 | 0 | 0 | 0 |

Recorded paid cash: none.

## Queue and evidence

### [abseil/abseil\-py](<https://github.com/abseil/abseil-py>)

Batch 1 · current stage: **target**.

abseil\-py: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Park \#428 until the intended allow\_overwrite semantics are clarified; a scalar\-style guard would break repeated multi\-value flags\. Look for a distinct unblocked defect\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/abseil-py/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/abseil/abseil-py>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/abseil-py/project.yaml>).

### [AOMediaCodec/libavif](<https://github.com/AOMediaCodec/libavif>)

Batch 1 · current stage: **target**.

libavif: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Follow the existing submission and its precise blockers first; preserve historical evidence\. Select a new distinct contribution only after checking current review feedback and policy\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/AOMediaCodec/libavif>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [h2database/h2database](<https://github.com/h2database/h2database>)

Batch 1 · current stage: **validated**.

Investigate \#4456: adding a VARCHAR index changes the result of a numeric comparison with a parameter array\.

Next action: Recover source 9d7a0ad and the immutable initial and supplemental evidence from agamal026/h2database\. The complete upstream CI\-selected suite passed on Java 11 and 17\. Preserve the unresolved Java 11 background memory diagnostic, failed documentation gate on an unchanged baseline file, and incomplete non\-CI validation\. Resolve the truthful contributor statement and remaining required validation before an upstream PR\. The contributor\-fork draft is not an upstream submission\. Park for a personal/access dependency and advance useful unblocked work; no issue\-specific cash offer is verified\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/h2database/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/h2database/h2database>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/h2database/project.yaml>).
- 2026-10-17 **screened**: [evidence 1](<https://github.com/h2database/h2database/issues/4456>); [evidence 2](<https://github.com/h2database/h2database/pulls>); [policy\_ref](<https://h2database.com/html/build.html#providing_patches>).
- 2026-10-17 **selected**: [evidence 1](<https://github.com/h2database/h2database/issues/4456>); [selection\_ref](<https://github.com/h2database/h2database/issues/4456>).
- 2026-10-17 **reproduced**: [evidence 1](<https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/logs/baseline-original-reproducer.log>); [evidence 2](<https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/logs/baseline-final-regression.log>); [source f2922a7766ec2472bc65d5e5ab4086390a76a42c](<https://github.com/h2database/h2database/commit/f2922a7766ec2472bc65d5e5ab4086390a76a42c>).
  Validation command: java \-ea \-cp &quot;$H2\_PROOF/baseline\-classes:$H2\_PROOF/classes:$H2\_SOURCE/h2/temp:$H2\_SOURCE/h2/ext/\*&quot; RunRegression4456; result: **reproduced**; [validation record](<https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/COMMANDS.md#original-production-negative-control>).
- 2026-10-17 **validated**: [evidence 1](<https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/README.md#what-actually-passed>); [evidence 2](<https://github.com/agamal026/h2database/pull/1>); [evidence 3](<https://github.com/agamal026/h2database/actions/runs/39073428774>); [evidence 4](<https://github.com/agamal026/h2database/blob/f190120801a23792717d6a2f0690b61398a5bafc/contribution-review/4456-follow-up/README.md>); [evidence 5](<https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/receipts/final-verification-commands.json>); [review\_ref](<https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/README.md#status-and-exact-source>); [source 9d7a0ad26f8a53654e0ce106a80f702ae5840a28](<https://github.com/agamal026/h2database/commit/9d7a0ad26f8a53654e0ce106a80f702ae5840a28>).
  Validation command: \./build\.sh jar testCI; result: **passed**; [validation record](<https://github.com/agamal026/h2database/blob/f190120801a23792717d6a2f0690b61398a5bafc/contribution-review/4456-follow-up/hosted-ci/receipt.json>).

### [json\-c/json\-c](<https://github.com/json-c/json-c>)

Batch 1 · current stage: **target**.

json\-c: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Do not duplicate \#984: PR \#986 already addresses it\. Select a different uncovered problem or respond to a maintainer request for independent validation\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/json-c/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/json-c/json-c>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/json-c/project.yaml>).

### [libevent/libevent](<https://github.com/libevent/libevent>)

Batch 1 · current stage: **target**.

libevent: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Follow the existing submission and its precise blockers first; preserve historical evidence\. Select a new distinct contribution only after checking current review feedback and policy\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/libevent/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/libevent/libevent>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/libevent/project.yaml>).

### [nginx/nginx](<https://github.com/nginx/nginx>)

Batch 1 · current stage: **target**.

nginx: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Follow the existing submission and its precise blockers first; preserve historical evidence\. Select a new distinct contribution only after checking current review feedback and policy\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/nginx/nginx>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [nih\-at/libzip](<https://github.com/nih-at/libzip>)

Batch 1 · current stage: **target**.

libzip: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Follow the existing submission and its precise blockers first; preserve historical evidence\. Select a new distinct contribution only after checking current review feedback and policy\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/nih-at/libzip>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [npm/cli](<https://github.com/npm/cli>)

Batch 1 · current stage: **target**.

npm: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Follow the existing submission and its precise blockers first; preserve historical evidence\. Select a new distinct contribution only after checking current review feedback and policy\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/npm/cli>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [pytest\-dev/iniconfig](<https://github.com/pytest-dev/iniconfig>)

Batch 1 · current stage: **target**.

iniconfig: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/iniconfig/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pytest-dev/iniconfig>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/iniconfig/project.yaml>).

### [rthalley/dnspython](<https://github.com/rthalley/dnspython>)

Batch 1 · current stage: **target**.

dnspython: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/dnspython/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/rthalley/dnspython>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/dnspython/project.yaml>).

### [c\-ares/c\-ares](<https://github.com/c-ares/c-ares>)

Batch 2 · current stage: **target**.

ares: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/c-ares/c-ares>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [facebook/zstd](<https://github.com/facebook/zstd>)

Batch 2 · current stage: **target**.

zstdlib: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/facebook/zstd>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [libarchive/libarchive](<https://github.com/libarchive/libarchive>)

Batch 2 · current stage: **target**.

libarchive: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/libarchive/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/libarchive/libarchive>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/libarchive/project.yaml>).

### [libexpat/libexpat](<https://github.com/libexpat/libexpat>)

Batch 2 · current stage: **target**.

expat: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/expat/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/libexpat/libexpat>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/expat/project.yaml>).

### [libssh2/libssh2](<https://github.com/libssh2/libssh2>)

Batch 2 · current stage: **target**.

libssh2: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/libssh2/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/libssh2/libssh2>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/libssh2/project.yaml>).

### [lz4/lz4](<https://github.com/lz4/lz4>)

Batch 2 · current stage: **submitted**.

Fix \#1889: accept the Linux kernel four\-zero\-byte end marker in legacy LZ4 decoding and listing, preserving following\-frame handling and queued output cleanup\.

Next action: Follow upstream PR \#1890 at exact head f83be8241c6042a0f9b500da927f68caa905fc92\. At 2026\-10\-18T13:13:26Z, all 54 upstream CheckRuns and all 54 actual workflow jobs showed 48 successes and six in progress, with no failures\. Six of nine workflows were successful; three and AppVeyor remained pending\. No admission request is needed\. Read actual remaining CI results and substantive feedback, then address concrete changes\. Reuse published Linux threaded/nonthreaded regression and 10\-test listing results for unchanged source\. The broader CLI command failed at test\-lz4\-blocksize, reproduced with the unchanged upstream binary; do not label it passing\. No patch\-specific security\-reward eligibility, bounty, upstream acceptance or realized benefit is established\.

Benefit route: **cash / conditional**, checked 2026-10-18. Tier 1 project scope rechecked on October 18: LZ4 is explicitly listed among Other essential libraries\. This compatibility fix has no demonstrated patch\-specific security benefit or reward eligibility; issue bounty, participant eligibility, upstream acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/lz4/lz4>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).
- 2026-10-18 **screened**: [evidence 1](<https://github.com/lz4/lz4/issues/1889>); [evidence 2](<https://github.com/lz4/lz4/blob/e7c36223415219c0a18ea75e3fe2eb5d267ee667/README.md>); [evidence 3](<https://github.com/lz4/lz4/blob/e7c36223415219c0a18ea75e3fe2eb5d267ee667/doc/lz4_Frame_format.md>); [policy\_ref](<https://github.com/lz4/lz4/blob/e7c36223415219c0a18ea75e3fe2eb5d267ee667/SECURITY.md>).
- 2026-10-18 **selected**: [evidence 1](<https://github.com/lz4/lz4/issues/1889>); [evidence 2](<https://github.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution-review/1889/README.md>); [selection\_ref](<https://github.com/lz4/lz4/issues/1889>).
- 2026-10-18 **reproduced**: [evidence 1](<https://github.com/agamal026/lz4/blob/f9f961ec521cb16ef602e0178f0f19a9f899f058/contribution-review/1889/baseline/BASELINE.md>); [source 28ca6d54d6e14c8546ebd24eb671b968b568a099](<https://github.com/agamal026/lz4/commit/28ca6d54d6e14c8546ebd24eb671b968b568a099>).
  Validation command: sh test\-lz4\-multiple\-legacy\.sh; result: **reproduced**; [validation record](<https://github.com/agamal026/lz4/blob/f9f961ec521cb16ef602e0178f0f19a9f899f058/contribution-review/1889/baseline/BASELINE.md>).
- 2026-10-18 **validated**: [evidence 1](<https://github.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution-review/1889/README.md>); [evidence 2](<https://github.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution-review/1889/VALIDATION.json>); [evidence 3](<https://github.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution-review/1889/baseline-blocksize-control.json>); [review\_ref](<https://github.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution-review/1889/AUTOMATED_REVIEW.md>); [source f83be8241c6042a0f9b500da927f68caa905fc92](<https://github.com/agamal026/lz4/commit/f83be8241c6042a0f9b500da927f68caa905fc92>).
  Validation command: sh test\-lz4\-multiple\-legacy\.sh; result: **passed**; [validation record](<https://github.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution-review/1889/VALIDATION.json>).
- 2026-10-18 **submitted**: [evidence 1](<https://github.com/lz4/lz4/pull/1890>); [evidence 2](<https://github.com/agamal026/lz4/commit/f83be8241c6042a0f9b500da927f68caa905fc92>); [evidence 3](<https://github.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution-review/1889/README.md>); [pr\_url](<https://github.com/lz4/lz4/pull/1890>); validated source f83be8241c6042a0f9b500da927f68caa905fc92.

### [pallets/jinja](<https://github.com/pallets/jinja>)

Batch 2 · current stage: **target**.

Jinja: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pallets/jinja>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [pypa/pip](<https://github.com/pypa/pip>)

Batch 2 · current stage: **target**.

pip: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pypa/pip>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [tukaani\-project/xz](<https://github.com/tukaani-project/xz>)

Batch 2 · current stage: **target**.

xz: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/tukaani-project/xz>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [yaml/libyaml](<https://github.com/yaml/libyaml>)

Batch 2 · current stage: **target**.

libyaml: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/libyaml/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/yaml/libyaml>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/libyaml/project.yaml>).

### [angular/angular](<https://github.com/angular/angular>)

Batch 3 · current stage: **target**.

Angular: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/angular/angular>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [apache/avro](<https://github.com/apache/avro>)

Batch 3 · current stage: **target**.

avro: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/avro/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/avro>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/avro/project.yaml>).

### [apache/commons\-bcel](<https://github.com/apache/commons-bcel>)

Batch 3 · current stage: **target**.

apache\-commons\-bcel: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-bcel/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-bcel>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-bcel/project.yaml>).

### [apache/commons\-beanutils](<https://github.com/apache/commons-beanutils>)

Batch 3 · current stage: **target**.

apache\-commons\-beanutils: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-beanutils/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-beanutils>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-beanutils/project.yaml>).

### [apache/commons\-cli](<https://github.com/apache/commons-cli>)

Batch 3 · current stage: **target**.

apache\-commons\-cli: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-cli/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-cli>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-cli/project.yaml>).

### [apache/commons\-collections](<https://github.com/apache/commons-collections>)

Batch 3 · current stage: **target**.

apache\-commons\-collections: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-collections/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-collections>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-collections/project.yaml>).

### [apache/commons\-compress](<https://github.com/apache/commons-compress>)

Batch 3 · current stage: **target**.

apache\-commons\-compress: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-compress/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-compress>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-compress/project.yaml>).

### [apache/commons\-csv](<https://github.com/apache/commons-csv>)

Batch 3 · current stage: **target**.

apache\-commons\-csv: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-csv/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-csv>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-csv/project.yaml>).

### [apache/commons\-fileupload](<https://github.com/apache/commons-fileupload>)

Batch 3 · current stage: **target**.

apache\-commons\-fileupload: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-fileupload/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-fileupload>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-fileupload/project.yaml>).

### [apache/commons\-imaging](<https://github.com/apache/commons-imaging>)

Batch 3 · current stage: **target**.

apache\-commons\-imaging: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-imaging/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-imaging>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-imaging/project.yaml>).

### [apache/commons\-jxpath](<https://github.com/apache/commons-jxpath>)

Batch 4 · current stage: **target**.

apache\-commons\-jxpath: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-jxpath/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-jxpath>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-jxpath/project.yaml>).

### [apache/commons\-lang](<https://github.com/apache/commons-lang>)

Batch 4 · current stage: **target**.

apache\-commons\-lang: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-lang/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-lang>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-lang/project.yaml>).

### [apache/commons\-net](<https://github.com/apache/commons-net>)

Batch 4 · current stage: **target**.

apache\-commons\-net: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-net/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-net>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-net/project.yaml>).

### [apache/commons\-text](<https://github.com/apache/commons-text>)

Batch 4 · current stage: **target**.

apache\-commons\-text: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-text/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-text>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-text/project.yaml>).

### [apache/commons\-validator](<https://github.com/apache/commons-validator>)

Batch 4 · current stage: **target**.

apache\-commons\-validator: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-validator/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/commons-validator>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-commons-validator/project.yaml>).

### [apache/cxf](<https://github.com/apache/cxf>)

Batch 4 · current stage: **target**.

apache\-cxf: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-cxf/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/cxf>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-cxf/project.yaml>).

### [apache/httpd](<https://github.com/apache/httpd>)

Batch 4 · current stage: **target**.

Apache httpd: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/httpd>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [apache/poi](<https://github.com/apache/poi>)

Batch 4 · current stage: **target**.

apache\-poi: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-poi/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/poi>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-poi/project.yaml>).

### [apache/shiro](<https://github.com/apache/shiro>)

Batch 4 · current stage: **target**.

apache\-shiro: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-shiro/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/shiro>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-shiro/project.yaml>).

### [apache/tika](<https://github.com/apache/tika>)

Batch 4 · current stage: **target**.

apache\-tika: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/apache-tika/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/tika>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/apache-tika/project.yaml>).

### [apache/wicket](<https://github.com/apache/wicket>)

Batch 5 · current stage: **target**.

Wicket: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/apache/wicket>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [auth0/java\-jwt](<https://github.com/auth0/java-jwt>)

Batch 5 · current stage: **target**.

java\-jwt: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/java-jwt/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/auth0/java-jwt>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/java-jwt/project.yaml>).

### [axboe/liburing](<https://github.com/axboe/liburing>)

Batch 5 · current stage: **target**.

liburing: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/axboe/liburing>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [civiform/civiform](<https://github.com/civiform/civiform>)

Batch 5 · current stage: **target**.

CiviForm: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/civiform/civiform>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [cncf/xds](<https://github.com/cncf/xds>)

Batch 5 · current stage: **target**.

xds: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/cncf/xds>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [curl/curl](<https://github.com/curl/curl>)

Batch 5 · current stage: **target**.

curl: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/curl/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/curl/curl>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/curl/project.yaml>).

### [dart\-lang/sdk](<https://github.com/dart-lang/sdk>)

Batch 5 · current stage: **target**.

Dart: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/dart-lang/sdk>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [django/django](<https://github.com/django/django>)

Batch 5 · current stage: **target**.

Django: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/django/django>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [dovecot/core](<https://github.com/dovecot/core>)

Batch 5 · current stage: **target**.

Dovecot: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/dovecot/core>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [drupal/drupal](<https://github.com/drupal/drupal>)

Batch 5 · current stage: **target**.

Drupal: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/drupal/drupal>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [eggert/tz](<https://github.com/eggert/tz>)

Batch 6 · current stage: **target**.

tz: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/eggert/tz>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [emberjs/ember\.js](<https://github.com/emberjs/ember.js>)

Batch 6 · current stage: **target**.

Ember: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/emberjs/ember.js>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [FasterXML/jackson\-core](<https://github.com/FasterXML/jackson-core>)

Batch 6 · current stage: **target**.

jackson\-core: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/jackson-core/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/FasterXML/jackson-core>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/jackson-core/project.yaml>).

### [FasterXML/jackson\-databind](<https://github.com/FasterXML/jackson-databind>)

Batch 6 · current stage: **submitted**.

Fix \#6299: write a valid empty array when content inclusion suppresses the sole element of an unwrapped container, preserving configured content\-filter exception wrapping\.

Next action: Follow upstream PR \#6302 at exact head de533c218b30a86ac9e74a6627b7224c2a0d2987\. At 2026\-10\-18T12:11:13Z, Gitar reported success with no issues and medium risk; functional validation was not enabled\. Upstream Build and Deploy Snapshot run 39125996146 required maintainer authorization and its actual job list returned zero jobs\. The admission follow\-up is already posted at https://github\.com/FasterXML/jackson\-databind/pull/6302\#issuecomment\-6249752236; do not repeat it without a reply or material change\. Read admission/results and substantive feedback, then address concrete changes\. Reuse the published four\-job fork validation and independent automated review for unchanged source: all 53 new cases pass, with zero full\-suite failures or errors and one skip per build\. CLA acceptance remains unverified and is required before upstream acceptance\. No issue bounty, patch\-specific reward qualification, upstream acceptance or realized benefit is verified\.

Benefit route: **cash / conditional**, checked 2026-10-18. Tier 2 project scope checked on October 18\. This serialization correctness fix has no verified issue bounty or patch\-specific security\-reward qualification; participant eligibility, upstream acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/jackson-databind/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/FasterXML/jackson-databind>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/jackson-databind/project.yaml>).
- 2026-10-18 **screened**: [evidence 1](<https://github.com/FasterXML/jackson-databind/issues/6299>); [evidence 2](<https://github.com/FasterXML/jackson-databind/blob/d2d5526ee317cbc0300c29e3257a6e9690774d96/CLAUDE.md>); [policy\_ref](<https://github.com/FasterXML/jackson/blob/main/CONTRIBUTING.md>).
- 2026-10-18 **selected**: [evidence 1](<https://github.com/FasterXML/jackson-databind/issues/6299>); [evidence 2](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/README.md>); [selection\_ref](<https://github.com/FasterXML/jackson-databind/issues/6299>).
- 2026-10-18 **reproduced**: [evidence 1](<https://github.com/agamal026/jackson-databind/actions/runs/39124036186>); [evidence 2](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/VALIDATION.json>); [source 342f5dbae53a7b44ec7327fd6def30808f8a1047](<https://github.com/agamal026/jackson-databind/commit/342f5dbae53a7b44ec7327fd6def30808f8a1047>).
  Validation command: \./mvnw \-B \-ff \-ntp verify; result: **reproduced**; [validation record](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/README.md#before-and-after>).
- 2026-10-18 **validated**: [evidence 1](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/README.md>); [evidence 2](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/VALIDATION.json>); [evidence 3](<https://github.com/agamal026/jackson-databind/actions/runs/39124679661>); [review\_ref](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/AUTOMATED_REVIEW.md>); [source de533c218b30a86ac9e74a6627b7224c2a0d2987](<https://github.com/agamal026/jackson-databind/commit/de533c218b30a86ac9e74a6627b7224c2a0d2987>).
  Validation command: \./mvnw \-B \-ff \-ntp verify; result: **passed**; [validation record](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/README.md#before-and-after>).
- 2026-10-18 **submitted**: [evidence 1](<https://github.com/FasterXML/jackson-databind/pull/6302>); [evidence 2](<https://github.com/agamal026/jackson-databind/commit/de533c218b30a86ac9e74a6627b7224c2a0d2987>); [evidence 3](<https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/README.md>); [pr\_url](<https://github.com/FasterXML/jackson-databind/pull/6302>); validated source de533c218b30a86ac9e74a6627b7224c2a0d2987.

### [git/git](<https://github.com/git/git>)

Batch 6 · current stage: **target**.

git: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/git/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/git/git>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/git/project.yaml>).

### [golang/go](<https://github.com/golang/go>)

Batch 6 · current stage: **target**.

Go: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/golang/go>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [google/brotli](<https://github.com/google/brotli>)

Batch 6 · current stage: **target**.

brotli: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/brotli/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/google/brotli>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/brotli/project.yaml>).

### [google/flatbuffers](<https://github.com/google/flatbuffers>)

Batch 6 · current stage: **target**.

flatbuffers: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/google/flatbuffers>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [google/gson](<https://github.com/google/gson>)

Batch 6 · current stage: **target**.

gson: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/gson/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/google/gson>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/gson/project.yaml>).

### [google/guava](<https://github.com/google/guava>)

Batch 6 · current stage: **target**.

guava: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/guava/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/google/guava>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/guava/project.yaml>).

### [google/nsjail](<https://github.com/google/nsjail>)

Batch 7 · current stage: **target**.

nsjail: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/google/nsjail>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [google/re2](<https://github.com/google/re2>)

Batch 7 · current stage: **target**.

re2: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/google/re2>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [grpc/grpc](<https://github.com/grpc/grpc>)

Batch 7 · current stage: **target**.

grpc: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/grpc/grpc>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [grpc/grpc\-proto](<https://github.com/grpc/grpc-proto>)

Batch 7 · current stage: **target**.

grpc\_proto: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/grpc/grpc-proto>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [gwtproject/gwt](<https://github.com/gwtproject/gwt>)

Batch 7 · current stage: **target**.

GWT: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/gwtproject/gwt>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [harfbuzz/harfbuzz](<https://github.com/harfbuzz/harfbuzz>)

Batch 7 · current stage: **target**.

harfbuzz: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/harfbuzz/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/harfbuzz/harfbuzz>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/harfbuzz/project.yaml>).

### [html5lib/html5lib\-python](<https://github.com/html5lib/html5lib-python>)

Batch 7 · current stage: **target**.

html5lib\-python: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/html5lib-python/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/html5lib/html5lib-python>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/html5lib-python/project.yaml>).

### [isc\-projects/bind9](<https://github.com/isc-projects/bind9>)

Batch 7 · current stage: **target**.

BIND: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/isc-projects/bind9>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [isc\-projects/dhcp](<https://github.com/isc-projects/dhcp>)

Batch 7 · current stage: **target**.

ISC DHCP: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/isc-projects/dhcp>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [javaparser/javaparser](<https://github.com/javaparser/javaparser>)

Batch 7 · current stage: **submitted**.

Fix \#4074: preserve the existing separator before a class when removing the last of multiple imports with the lexical\-preserving printer\.

Next action: Follow upstream PR \#5175 at exact head 2a437e500bf54024772dd9f3d6d4149506defed2\. The issue announcement and PR were published and read back on October 18\. At 10:19:27 UTC, AppVeyor build 54919188 reported success; its underlying logs were not inspected\. The formatting and Maven GitHub Actions runs still required maintainer authorization, and both job lists returned zero jobs\. Await admission and substantive review, then address concrete feedback\. Reuse the published Linux/Java 17 validation and automated review for unchanged source\. Connector PR creation returned HTTP 403; an authorized authenticated browser completed this submission, which does not establish future connector or fork\-creation permission\. No issue bounty, acceptance, reward qualification or realized benefit is verified\. The admission follow\-up is already posted at https://github\.com/javaparser/javaparser/pull/5175\#issuecomment\-6248629643; do not repeat it without a reply or material change\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope was previously verified\. This formatting fix has no verified security\-reward eligibility, advertised issue bounty, award or payment; participant eligibility and upstream acceptance remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/javaparser/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/javaparser/javaparser>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/javaparser/project.yaml>).
- 2026-10-17 **screened**: [evidence 1](<https://github.com/javaparser/javaparser/issues/4074>); [evidence 2](<https://github.com/javaparser/javaparser/pull/2704>); [evidence 3](<https://github.com/agamal026/opensource/blob/aec8a5eb1983230f1bb7470a51b2e7bc53ef0f70/progress/2026-10-18-javaparser-4074.md>); [policy\_ref](<https://github.com/javaparser/javaparser/blob/dc6bc07155cb0d0d7a8a427b76411848eb862136/CONTRIBUTING.md>).
- 2026-10-17 **selected**: [evidence 1](<https://github.com/javaparser/javaparser/issues/4074>); [evidence 2](<https://github.com/agamal026/opensource/blob/aec8a5eb1983230f1bb7470a51b2e7bc53ef0f70/progress/2026-10-18-javaparser-4074.md>); [selection\_ref](<https://github.com/javaparser/javaparser/issues/4074>).
- 2026-10-17 **reproduced**: [evidence 1](<https://github.com/agamal026/opensource/blob/aec8a5eb1983230f1bb7470a51b2e7bc53ef0f70/progress/2026-10-18-javaparser-4074.md>); [evidence 2](<https://github.com/agamal026/opensource/blob/aec8a5eb1983230f1bb7470a51b2e7bc53ef0f70/progress/2026-10-18-javaparser-4074-validation.json>); [source dc6bc07155cb0d0d7a8a427b76411848eb862136](<https://github.com/javaparser/javaparser/commit/dc6bc07155cb0d0d7a8a427b76411848eb862136>).
  Validation command: \./mvnw \-B \-ntp \-pl javaparser\-core\-testing \-am test \-Dtest=Issue4074Test,LexicalPreservingPrinterTest,DifferenceApplyRemovedRulesCompleteTest,DifferenceApplyLeftoverRulesTest,MethodDeclarationTransformationsTest,CompilationUnitTransformationsTest \-Dsurefire\.failIfNoSpecifiedTests=false; result: **reproduced**; [validation record](<https://github.com/agamal026/opensource/blob/aec8a5eb1983230f1bb7470a51b2e7bc53ef0f70/progress/2026-10-18-javaparser-4074-validation.json>).
- 2026-10-18 **validated**: [evidence 1](<https://github.com/agamal026/javaparser/blob/be86f30a136fddc1e741fdcb36094bbbbfaaa454/contribution-review/4074/README.md>); [evidence 2](<https://github.com/agamal026/javaparser/blob/be86f30a136fddc1e741fdcb36094bbbbfaaa454/contribution-review/4074/FINAL-REACTOR.json>); [evidence 3](<https://github.com/agamal026/javaparser/blob/be86f30a136fddc1e741fdcb36094bbbbfaaa454/contribution-review/4074/javaparser-4074-review-package.zip>); [review\_ref](<https://github.com/agamal026/javaparser/blob/be86f30a136fddc1e741fdcb36094bbbbfaaa454/contribution-review/4074/AUTOMATED_REVIEW.md>); [source 2a437e500bf54024772dd9f3d6d4149506defed2](<https://github.com/agamal026/javaparser/commit/2a437e500bf54024772dd9f3d6d4149506defed2>).
  Validation command: \./mvnw \-\-errors \-\-show\-version \-B \-ntp \-\-log\-file &quot;$REVIEW\_PACKET/final\-reactor\-slow/maven\.log&quot; clean test \-\-activate\-profiles AlsoSlowTests; result: **passed**; [validation record](<https://github.com/agamal026/javaparser/blob/be86f30a136fddc1e741fdcb36094bbbbfaaa454/contribution-review/4074/FINAL-REACTOR.json>).
- 2026-10-18 **submitted**: [evidence 1](<https://github.com/javaparser/javaparser/pull/5175>); [evidence 2](<https://github.com/javaparser/javaparser/issues/4074#issuecomment-6248510250>); [evidence 3](<https://github.com/agamal026/javaparser/commit/2a437e500bf54024772dd9f3d6d4149506defed2>); [pr\_url](<https://github.com/javaparser/javaparser/pull/5175>); validated source 2a437e500bf54024772dd9f3d6d4149506defed2.

### [jhy/jsoup](<https://github.com/jhy/jsoup>)

Batch 8 · current stage: **target**.

jsoup: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/jsoup/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/jhy/jsoup>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/jsoup/project.yaml>).

### [joomla/joomla\-cms](<https://github.com/joomla/joomla-cms>)

Batch 8 · current stage: **target**.

Joomla: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/joomla/joomla-cms>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [jquery/jquery](<https://github.com/jquery/jquery>)

Batch 8 · current stage: **target**.

jQuery: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/jquery/jquery>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [keycloak/keycloak](<https://github.com/keycloak/keycloak>)

Batch 8 · current stage: **target**.

keycloak: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/keycloak/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/keycloak/keycloak>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/keycloak/project.yaml>).

### [knockout/knockout](<https://github.com/knockout/knockout>)

Batch 8 · current stage: **target**.

Knockout: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/knockout/knockout>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [libgit2/libgit2](<https://github.com/libgit2/libgit2>)

Batch 8 · current stage: **target**.

libgit2: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/libgit2/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/libgit2/libgit2>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/libgit2/project.yaml>).

### [libjpeg\-turbo/libjpeg\-turbo](<https://github.com/libjpeg-turbo/libjpeg-turbo>)

Batch 8 · current stage: **target**.

libjpeg\-turbo: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/libjpeg-turbo/libjpeg-turbo>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [libjxl/libjxl](<https://github.com/libjxl/libjxl>)

Batch 8 · current stage: **target**.

jpegxl: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/libjxl/libjxl>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [lxml/lxml](<https://github.com/lxml/lxml>)

Batch 8 · current stage: **target**.

lxml: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/lxml/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/lxml/lxml>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/lxml/project.yaml>).

### [magento/magento2](<https://github.com/magento/magento2>)

Batch 8 · current stage: **target**.

Magento: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/magento/magento2>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [netty/netty](<https://github.com/netty/netty>)

Batch 9 · current stage: **target**.

netty: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/netty/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/netty/netty>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/netty/project.yaml>).

### [ntp\-project/ntp](<https://github.com/ntp-project/ntp>)

Batch 9 · current stage: **target**.

University of Delaware NTPD: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/ntp-project/ntp>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [numpy/numpy](<https://github.com/numpy/numpy>)

Batch 9 · current stage: **target**.

numpy: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/numpy/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/numpy/numpy>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/numpy/project.yaml>).

### [opencart/opencart](<https://github.com/opencart/opencart>)

Batch 9 · current stage: **target**.

OpenCart: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/opencart/opencart>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [pallets/flask](<https://github.com/pallets/flask>)

Batch 9 · current stage: **target**.

Flask: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pallets/flask>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [pallets/werkzeug](<https://github.com/pallets/werkzeug>)

Batch 9 · current stage: **target**.

Werkzeug: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pallets/werkzeug>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [pandas\-dev/pandas](<https://github.com/pandas-dev/pandas>)

Batch 9 · current stage: **target**.

pandas: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/pandas/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pandas-dev/pandas>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/pandas/project.yaml>).

### [pnggroup/libpng](<https://github.com/pnggroup/libpng>)

Batch 9 · current stage: **target**.

libpng: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pnggroup/libpng>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [Polymer/polymer](<https://github.com/Polymer/polymer>)

Batch 9 · current stage: **target**.

Polymer: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/Polymer/polymer>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [PrestaShop/PrestaShop](<https://github.com/PrestaShop/PrestaShop>)

Batch 9 · current stage: **target**.

PrestaShop: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/PrestaShop/PrestaShop>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [protobuf\-c/protobuf\-c](<https://github.com/protobuf-c/protobuf-c>)

Batch 10 · current stage: **target**.

protobuf\-c: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/protobuf-c/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/protobuf-c/protobuf-c>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/protobuf-c/project.yaml>).

### [protocolbuffers/protobuf](<https://github.com/protocolbuffers/protobuf>)

Batch 10 · current stage: **target**.

protobuf: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/protocolbuffers/protobuf>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [pyca/cryptography](<https://github.com/pyca/cryptography>)

Batch 10 · current stage: **target**.

cryptography: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/cryptography/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/pyca/cryptography>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/cryptography/project.yaml>).

### [python\-pillow/Pillow](<https://github.com/python-pillow/Pillow>)

Batch 10 · current stage: **target**.

pillow: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/pillow/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/python-pillow/Pillow>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/pillow/project.yaml>).

### [python/cpython](<https://github.com/python/cpython>)

Batch 10 · current stage: **target**.

cpython3: a canonical upstream in the researched Tier 2 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 2 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/oss-fuzz/blob/master/projects/cpython3/project.yaml>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/python/cpython>); [evidence 2](<https://github.com/google/oss-fuzz/blob/master/projects/cpython3/project.yaml>).

### [tensorflow/tensorflow](<https://github.com/tensorflow/tensorflow>)

Batch 10 · current stage: **target**.

tensorflow: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/tensorflow/tensorflow>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [the\-tcpdump\-group/libpcap](<https://github.com/the-tcpdump-group/libpcap>)

Batch 10 · current stage: **target**.

libpcap: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/the-tcpdump-group/libpcap>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [torvalds/linux](<https://github.com/torvalds/linux>)

Batch 10 · current stage: **target**.

Linux kernel: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Parked for the current GitHub\-PR submission workflow: Linux expects patches by email to maintainers and mailing lists\. Follow the canonical process if selected later; do not create a GitHub PR to satisfy this tracker\. Select another compatible source\-backed target for current implementation\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/torvalds/linux>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>); [evidence 3](<https://docs.kernel.org/process/submitting-patches.html>).

### [TYPO3/typo3](<https://github.com/TYPO3/typo3>)

Batch 10 · current stage: **target**.

Typo3: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/TYPO3/typo3>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

### [unicode\-org/icu](<https://github.com/unicode-org/icu>)

Batch 10 · current stage: **target**.

icu: a canonical upstream in the researched Tier 1 project pool; a specific contribution is not yet selected\.

Next action: Read current contribution and AI\-use policies, inspect actual maintenance activity and competing fixes, then select one cloud\-testable problem with a supported benefit route\.

Benefit route: **cash / conditional**, checked 2026-10-17. Tier 1 project scope verified\. Patch\-specific security value, participant eligibility, acceptance, award and payment remain unverified\.

Route evidence: [1](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>), [2](<https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md>).

- 2026-10-17 **target**: [evidence 1](<https://github.com/unicode-org/icu>); [evidence 2](<https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md>).

## Historical submissions (excluded from campaign progress)

- [AOMediaCodec/libavif](<https://github.com/AOMediaCodec/libavif/pull/3350>): submitted 2026-09-06. Accepted 2026-09-09; [upstream acceptance](<https://github.com/AOMediaCodec/libavif/pull/3350>). [evidence 1](<https://github.com/AOMediaCodec/libavif/pull/3350>).
- [nginx/nginx](<https://github.com/nginx/nginx/pull/1734>): submitted 2026-09-06. [evidence 1](<https://github.com/nginx/nginx/pull/1734>).
- [nih\-at/libzip](<https://github.com/nih-at/libzip/pull/576>): submitted 2026-09-06. [evidence 1](<https://github.com/nih-at/libzip/pull/576>).
- [npm/cli](<https://github.com/npm/cli/pull/9954>): submitted 2026-09-06. [evidence 1](<https://github.com/npm/cli/pull/9954>).
- [libevent/libevent](<https://github.com/libevent/libevent/pull/1916>): submitted 2026-09-07. [evidence 1](<https://github.com/libevent/libevent/pull/1916>).
- [AOMediaCodec/libavif](<https://github.com/AOMediaCodec/libavif/pull/3413>): submitted 2026-10-13. [evidence 1](<https://github.com/AOMediaCodec/libavif/pull/3413>).
