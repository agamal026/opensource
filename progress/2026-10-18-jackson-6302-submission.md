# Jackson databind #6302 — upstream submission checkpoint

**The second qualified campaign submission is published:** [Jackson databind #6302](https://github.com/FasterXML/jackson-databind/pull/6302), created on **2026-10-18 at 12:07:28 UTC**. Canonical read-back collected through **12:11:13 UTC** confirmed the exact reviewed source and PR body. It is open, not a draft, and unmerged. The campaign now has **2 / 100** qualified submitted projects and no accepted campaign project or realized benefit.

## Problem and scoped change

[Issue #6299](https://github.com/FasterXML/jackson-databind/issues/6299) combines content inclusion with single-element array unwrapping. When filtering suppresses a container's only element, the serializers previously emitted no JSON value. A root container produced an empty string; inside a bean, writing the following property encountered an invalid generator state.

The fix checks content-aware emptiness only inside the existing effective singleton-unwrapping branch. A suppressed singleton emits `[]` and returns. A retained singleton follows its existing writer; a physically larger container that filters down to one element remains an array. The change covers fourteen implementations across nine production files: six reference-container paths, Iterable, EnumSet, and boolean, short, int, long, float and double arrays. Five reference serializers preserve their established exception-wrapping behavior around the new check. See the [independent automated source review](https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/AUTOMATED_REVIEW.md) for dispatch, configuration and error-path analysis.

The 53 regression invocations cover suppressed and retained singletons, physically larger mixed containers, property format overrides, null inclusion, disabled filtering, root output, custom content serializers, and exception wrapping. A following bean property checks generator state; parsed JSON and `valueToTree()` exercise distinct output paths. Iterator serialization remains outside this change. Retained values can have their inclusion predicate evaluated by both the emptiness precheck and content writer; no exact predicate-call-count contract or support for state-changing keep-then-suppress predicates is claimed.

## Exact source and durable evidence

| Record | Verified identity |
| --- | --- |
| [Submitted source](https://github.com/agamal026/jackson-databind/commit/de533c218b30a86ac9e74a6627b7224c2a0d2987) | `de533c218b30a86ac9e74a6627b7224c2a0d2987` |
| Upstream `3.x` base | `d2d5526ee317cbc0300c29e3257a6e9690774d96` |
| Source tree | `d9550ccd43d7acf13d6e5405728c3f155a53a1df` |
| Actual final fork CI merge checkout | `ffdc7267fb85cc13bdf946840a2623ab898e0d35`; its tree equals the source tree |
| PR scope | Ten files, 394 additions, zero deletions: nine production files and one test file |
| [Immutable evidence index](https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/README.md) | Evidence commit `942fb1328e72dd76cf58a32b194d9d3783baad16` |
| Final test SHA-256 | `173bca7131ff03859d7d7d55dc80a10824d740467ee45d3ded4c14d33829e185` |
| Final patch SHA-256 | `4e92003969feedb3df738bb4544a0cbf6e41a1f7d3e74c49f7fbc1a59e34efd8` |

The fork publishes four artifacts directly: the [README](https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/README.md), [validation record](https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/VALIDATION.json), [automated review](https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/AUTOMATED_REVIEW.md), and [evidence ZIP](https://github.com/agamal026/jackson-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution-review/6299/jackson-databind-6299-evidence.zip). The canonical directory was checked against the prepared file sizes and Git blob IDs. The ZIP is 416,739 bytes with SHA-256 `df69e69cbf2d097ae2511175c8cc578e9d0516dd04705bcf18dbfacbc0a2bc9b`.

Its twenty entries contain the source patch and file hashes, complete decoded baseline/final logs, job metadata, audits and `SHA256SUMS`. Paths such as `final-hosted/audit.json` and `source/SOURCE_FILES.json` are **inside the ZIP**, not separately published GitHub blob URLs. The [submission verification record](2026-10-18-jackson-6302-submission-verification.json) lists exact artifact hashes and archive members.

The contributor-side [draft PR #1](https://github.com/agamal026/jackson-databind/pull/1) was updated and read back to point to the external PR and completed evidence. It remains an owned draft and adds no campaign credit.

## Two failing baselines and the final four-build result

The recorded hosted command was `./mvnw -B -ff -ntp verify`. Counts are **tests / failures / errors / skipped**; full-suite totals include the skipped test.

| Stage | Hosted job | New regression class | Full suite |
| --- | --- | --- | --- |
| Corrected baseline | [Linux JDK 17](https://github.com/agamal026/jackson-databind/actions/runs/39124036186/job/117665313783) | 48 / 1 / 32 / 0 | 7569 / 1 / 32 / 1 |
| Corrected baseline | [Windows JDK 17](https://github.com/agamal026/jackson-databind/actions/runs/39124036186/job/117665313857) | 48 / 1 / 32 / 0 | 7569 / 1 / 32 / 1 |
| Corrected baseline | [Linux JDK 21](https://github.com/agamal026/jackson-databind/actions/runs/39124036186/job/117665313618) | 48 / 1 / 32 / 0 | 7571 / 1 / 32 / 1 |
| Corrected baseline | [Linux JDK 25](https://github.com/agamal026/jackson-databind/actions/runs/39124036186/job/117665313774) | 48 / 1 / 32 / 0 | 7571 / 1 / 32 / 1 |
| Exception baseline | [Linux JDK 21](https://github.com/agamal026/jackson-databind/actions/runs/39124541594/job/117666801298) | 53 / 5 / 0 / 0 | 7576 / 5 / 0 / 1 |
| Final | [Linux JDK 17](https://github.com/agamal026/jackson-databind/actions/runs/39124679661/job/117667201285) | 53 / 0 / 0 / 0 | 7574 / 0 / 0 / 1 |
| Final | [Windows JDK 17](https://github.com/agamal026/jackson-databind/actions/runs/39124679661/job/117667201282) | 53 / 0 / 0 / 0 | 7574 / 0 / 0 / 1 |
| Final | [Linux JDK 21](https://github.com/agamal026/jackson-databind/actions/runs/39124679661/job/117667201332) | 53 / 0 / 0 / 0 | 7576 / 0 / 0 / 1 |
| Final | [Linux JDK 25](https://github.com/agamal026/jackson-databind/actions/runs/39124679661/job/117667201103) | 53 / 0 / 0 / 0 | 7576 / 0 / 0 / 1 |

The corrected baseline at [`342f5dbae53a7b44ec7327fd6def30808f8a1047`](https://github.com/agamal026/jackson-databind/commit/342f5dbae53a7b44ec7327fd6def30808f8a1047) contains the first 48 regression invocations without the fix. Each of four builds proves the same one root-output failure and 32 `StreamWrite` errors. Two numeric-node equality false positives in the earlier test draft were corrected before freezing this baseline; they are not counted as product defects.

The initial implementation fixed all 48 output cases, but independent automated review found an exception-path regression: a throwing content filter in five serializers escaped the existing `WRAP_EXCEPTIONS` behavior. The test-only exception baseline at [`3da7256ce0a33801c7cc9166304c1fb9ec47f66e`](https://github.com/agamal026/jackson-databind/commit/3da7256ce0a33801c7cc9166304c1fb9ec47f66e) proves precisely five failures, expecting `DatabindException` but receiving `IllegalStateException`; the preceding 48 cases pass. The final correction wraps the new checks using each affected serializer's existing index-zero convention. Tests verify the original cause and path with wrapping enabled and the raw unchecked exception with wrapping disabled.

All 53 final invocations pass on all four builds. Independent log audits reconcile every per-class total with the aggregate: 1,080 classes on JDK 17 and 1,081 on JDK 21/25, whose additional class contains two tests. The single suite skip is in `JDKTypeSerializationTest`. Linux JDK 17 also passes `./mvnw -B -q -ff -ntp -DskipTests animal-sniffer:check`; this is static Android API compatibility, not device or emulator execution.

The evidence retains its limits. A local build encountered dependency-host DNS failure; only the recorded hosted runs establish execution. Logs are decoded tool-returned text, not original HTTP transport bytes. The Maven runtime version was not printed, and Maven snapshot dependency hashes were not pinned or captured. Exact source hashes do not guarantee identical later dependency resolution. The hub update reuses these completed results and does not rerun Jackson tests.

## Upstream checks, review and admission

At **12:11:13 UTC**, the upstream [Gitar CheckRun](https://github.com/FasterXML/jackson-databind/runs/117671129240) was `COMPLETED / SUCCESS`. Its [12:08:53 UTC bot comment](https://github.com/FasterXML/jackson-databind/pull/6302#issuecomment-6249735858) reports no issues and medium risk, and explicitly says functional validation was not enabled. No submitted reviews were returned. This check and comment do not establish human approval or an executed build.

The separate upstream [Build and Deploy Snapshot run 39125996146](https://github.com/FasterXML/jackson-databind/actions/runs/39125996146) remained `completed / action_required`. Its actual job-list GET returned **zero jobs**. One [admission follow-up](https://github.com/FasterXML/jackson-databind/pull/6302#issuecomment-6249752236) was posted and read back at **12:10:40 UTC**, requesting maintainer authorization and pointing to the existing four-build proof. **Do not duplicate that request without a reply or material change.** The PR had two comments and no review comments, with its last update at 12:10:40 UTC. Maintainer modification of the contributor branch was disabled.

The [central contribution guide](https://github.com/FasterXML/jackson/blob/main/CONTRIBUTING.md) and [exact-base repository guidance](https://github.com/FasterXML/jackson-databind/blob/d2d5526ee317cbc0300c29e3257a6e9690774d96/CLAUDE.md) were read during screening. The central guide was observed at its current URL; no immutable policy permalink was recorded. **CLA acceptance remains unverified** and is required before upstream acceptance. Implementation and review were AI-assisted; no human review or legal signature is claimed.

## Accounting, screening and continued work

Jackson is now the second distinct campaign repository at `submitted`, alongside JavaParser. H2 remains `validated` and parked behind its existing personal contributor statement and documented gates. Ninety-seven other repositories remain `target`. The six historical submissions across five projects remain unchanged and excluded from the campaign numerator. The status registry now contains eight PRs across seven projects: seven open and one historical merge.

The [Tier 2 project route](https://github.com/google/oss-fuzz/blob/master/projects/jackson-databind/project.yaml) and [Patch Rewards rules](https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md) support only a conditional project-level reason to investigate; Jackson's route date is now October 18. This correctness fix has no verified issue bounty, patch-specific security-reward qualification, contributor eligibility, award or payment. No new cash receipt, subscription or credits are recorded.

The bounded **11:18:27–11:18:28 UTC** follow-through made five metadata-only GETs for npm #9954, libavif #3413, libevent #1916, nginx #1734 and libzip #576. Heads, bases and comment counts were unchanged, and no PR update followed the 11:07:19 UTC cutoff. It did not reread discussion bodies or refresh check rollups. The seven earlier snapshot rows and their original observation dates are retained: six historical records and 70 contexts from **October 17 at 20:01:04 UTC**, plus JavaParser's **October 18 at 10:19:27 UTC** row. Jackson's new observation is appended; the [snapshot provenance](../data/snapshot-source.json) identifies its separate collection time.

[jsoup #2638](https://github.com/jhy/jsoup/issues/2638) was screened out because an [existing claim](https://github.com/jhy/jsoup/issues/2638#issuecomment-6017720355) already occupied the implementation. No duplicate patch or campaign milestone was added. Preserve the candidate exclusions from the [11:00 checkpoint](2026-10-18-1100-continuation.md) before screening again.

Next, read actual admission/results and substantive feedback on Jackson and JavaParser, address concrete requests, and reuse unchanged passing source evidence. Keep H2 and the prepared libavif work parked where their personal gates apply. Preserve the existing hourly native cadence, completion-only notification rule, October 13 baseline, November 12 review and earliest libzip recheck at **2026-10-22T13:12:13Z**. Preserve every other existing task and schedule. The libzip date is a recheck threshold, not reward entitlement.

## Additional screening for the next session

A bounded parallel screen inspected two other targets from **12:16:28 to 12:18:18 UTC**. The coordinator independently read the four competing PRs at **12:20:11 UTC** and confirmed that each was open and explicitly fixed its corresponding issue. These scopes are occupied:

| Candidate issue | Existing implementation |
| --- | --- |
| [jackson-core #1761](https://github.com/FasterXML/jackson-core/issues/1761), premature DataInput EOF | [PR #1763](https://github.com/FasterXML/jackson-core/pull/1763) |
| [jackson-core #1640](https://github.com/FasterXML/jackson-core/issues/1640), asynchronous numeric separators | [PR #1648](https://github.com/FasterXML/jackson-core/pull/1648) |
| [Gson #3122](https://github.com/google/gson/issues/3122), eager runtime adapter lookup | [PR #3123](https://github.com/google/gson/pull/3123) |
| [Gson #3128](https://github.com/google/gson/issues/3128), numeric-only address filtering | [PR #3129](https://github.com/google/gson/pull/3129) |

No new defect, selection milestone or implementation resulted. The screen's ten public GET attempts returned seven useful responses; Gson's contribution-policy discovery remained unresolved after three unavailable file paths. A different Gson selection still needs current contribution and AI-use rules. The prior conditional benefit-route observations were not refreshed, and other authors' test claims were not treated as execution evidence. Carry these four exclusions forward with the earlier jsoup and tscircuit exclusions.

## Automated workflow lesson and hub verification

Separating implementation from source review found a real compatibility regression that output-only success missed. The reviewer identified the existing exception boundary, the coordinator added five focused failing controls to the already passing implementation, and only the necessary five source guards changed. The final test file is byte-identical to the exception baseline. This is evidence of an improved automated review workflow; it does not establish the contributor's personal learning or human review. No new tool or skill implementation was needed for this checkpoint.

The [verification record](2026-10-18-jackson-6302-submission-verification.json) preserves exact source and artifact identities, both baselines, four final jobs, upstream check/admission observations, campaign accounting, historical observation limits, and the actual hub command receipts. All six prescribed `CONTRIBUTING.md` gates returned exit zero on Python 3.12.14, completing at **2026-10-18T12:18:20.303716Z**. The offline hub suite passed **81 tests**, with zero failures, errors or skips; the registry and campaign validated, both generated reports matched their inputs, and the whitespace check passed. These hub checks do not rerun Jackson source validation. Subsequent hub publication and hosted CI remain for the coordinator to verify against the actual published commit; this checkpoint does not invent a self-referential publication receipt.
