# Open-source progress

Observed at: 2026-10-18T15:25:01Z. Baseline date: 2026-10-13 (UTC).

This report is generated from the public catalog and a dated GitHub snapshot. It is not a live status page.

## Upstream contributions

Registered pull requests: 9; open: 8; merged: 1; closed without merge: 0.

Registered PRs with a recorded merge on or after 2026-10-13: 0.

This date comparison does not establish an additional independently tested contribution or completion of a project goal. Partial integrations in otherwise open PRs require separate evidence. Own-project releases are listed separately and do not enter these counts.

Check results describe only the rollup returned by GitHub for each recorded head. Missing checks and unrecognized states remain unknown. Success does not establish review approval, complete test coverage, or readiness to merge.

| Pull request | State | Returned checks | Review decision | Updated (UTC) |
| --- | --- | --- | --- | --- |
| [AOMediaCodec/libavif \#3350](<https://github.com/AOMediaCodec/libavif/pull/3350>) | merged | 42 passed | approved | 2026-09-09T23:21:10Z |
| [AOMediaCodec/libavif \#3413](<https://github.com/AOMediaCodec/libavif/pull/3413>) | open | 1 failed; 25 passed | not reported | 2026-10-13T19:43:27Z |
| [FasterXML/jackson\-databind \#6302](<https://github.com/FasterXML/jackson-databind/pull/6302>) | open | 5 passed; 2 skipped | not reported | 2026-10-18T15:24:42Z |
| [javaparser/javaparser \#5175](<https://github.com/javaparser/javaparser/pull/5175>) | open | 1 passed | not reported | 2026-10-18T10:13:18Z |
| [libevent/libevent \#1916](<https://github.com/libevent/libevent/pull/1916>) | open | unknown (no checks returned) | review required | 2026-10-15T13:13:47Z |
| [lz4/lz4 \#1890](<https://github.com/lz4/lz4/pull/1890>) | open | 55 passed | not reported | 2026-10-18T14:41:45Z |
| [nginx/nginx \#1734](<https://github.com/nginx/nginx/pull/1734>) | open | 1 passed | review required | 2026-10-15T12:33:23Z |
| [nih\-at/libzip \#576](<https://github.com/nih-at/libzip/pull/576>) | open | 1 passed | not reported | 2026-10-13T18:42:17Z |
| [npm/cli \#9954](<https://github.com/npm/cli/pull/9954>) | open | unknown (no checks returned) | review required | 2026-10-15T14:24:47Z |

### AOMediaCodec/libavif #3350: Keep codec option updates atomic on allocation failure

Make codec\-option updates atomic when allocation fails\.

- Source: [pull request](<https://github.com/AOMediaCodec/libavif/pull/3350>)
- Head commit: `04a56971f8994627dd5685b58c9ebfe299d01f97`
- Base commit: `66663952a677bb8a13ea1530d5694775d7d143d4`
- Recorded merge: 2026-09-09T23:21:10Z
- Catalog note: Merged on 2026\-09\-09, before the 2026\-10\-13 continuation baseline\. Retained as prior contribution history\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [build\-android\-jni](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430320/job/102673244045>) | check run | COMPLETED | SUCCESS | passed |
| [build\-disable\-gtest \(ubuntu\-latest\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430219/job/102673242008>) | check run | COMPLETED | SUCCESS | passed |
| [build\-linux\-oldest\-cmake](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430355/job/102673246466>) | check run | COMPLETED | SUCCESS | passed |
| [build\-mingw \(clang64\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430544/job/102673249389>) | check run | COMPLETED | SUCCESS | passed |
| [build\-mingw \(ucrt64\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430544/job/102673249098>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(macos\-latest, false\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430333/job/102673245457>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, 0\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430205/job/102673241591>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, 1\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430205/job/102673241557>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, 2\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430205/job/102673241565>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, false\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430333/job/102673245638>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, true\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430333/job/102673245619>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(windows\-latest, 0\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430205/job/102673241575>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(windows\-latest, 1\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430205/job/102673241438>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(windows\-latest, 2\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430205/job/102673241372>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(macos\-latest, libyuv LOCAL\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430422/job/102673247977>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(macos\-latest, libyuv OFF\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430422/job/102673248111>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(ubuntu\-latest, libyuv LOCAL\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430422/job/102673248006>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(ubuntu\-latest, libyuv OFF\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430422/job/102673247659>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local\-fuzztest \(ubuntu\-latest, LOCAL\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430349/job/102673245735>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local\-fuzztest \(ubuntu\-latest, OFF\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430349/job/102673245892>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-run\-golden\-tests \(ubuntu\-latest\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430261/job/102673243072>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-run\-golden\-tests \(ubuntu\-latest\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430533/job/102673249482>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static \(macos\-latest, Debug\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430345/job/102673246052>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static \(macos\-latest, Release\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430345/job/102673246309>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static \(ubuntu\-latest, Debug\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430345/job/102673246227>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static \(ubuntu\-latest, Release\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430345/job/102673246182>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-av2 \(LOCAL\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430358/job/102673253221>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-av2 \(OFF\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430358/job/102673253070>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-sanitized \(macos\-latest, address\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430362/job/102673247642>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-sanitized \(macos\-latest, thread\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430362/job/102673247939>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-sanitized \(macos\-latest, undefined\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430362/job/102673247857>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-sanitized \(ubuntu\-latest, address\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430362/job/102673247771>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-sanitized \(ubuntu\-latest, thread\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430362/job/102673247815>) | check run | COMPLETED | SUCCESS | passed |
| [build\-static\-sanitized \(ubuntu\-latest, undefined\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430362/job/102673248127>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows \(windows\-latest\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430471/job/102673276625>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows \(windows\-latest, \-G Ninja\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430471/job/102673276872>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows\-installed \(clang\-cl\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430262/job/102673243364>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows\-installed \(msvc\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430262/job/102673243561>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows\-shared\-local \(clang\-cl\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430340/job/102673245642>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows\-shared\-local \(msvc\)](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430340/job/102673245798>) | check run | COMPLETED | SUCCESS | passed |
| [clang\-format\-check](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430321/job/102673244058>) | check run | COMPLETED | SUCCESS | passed |
| [cmake\-format\-check](<https://github.com/AOMediaCodec/libavif/actions/runs/34413430321/job/102673243806>) | check run | COMPLETED | SUCCESS | passed |

### AOMediaCodec/libavif #3413: Fix automatic format selection for grayscale JPEGs with ICC profiles

Correct automatic output\-format selection for grayscale JPEGs with ICC profiles\.

- Source: [pull request](<https://github.com/AOMediaCodec/libavif/pull/3413>)
- Head commit: `93ef0a32c07741c34bb515295f5be3d270cca02d`
- Base commit: `c9cb32dbbaa3394d9f57afd2b4965ab0e56aaa62`
- Catalog note: The recorded individual CLA and the GitHub CLA check are separate evidence; retain the actual check result until its association is resolved\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [CLA bot check](<https://aomedia.org/license/individual-contributor-license-agreement/>) | status context | FAILURE | not reported | failed |
| [build\-android\-jni](<https://github.com/AOMediaCodec/libavif/actions/runs/38453428896/job/115489896289>) | check run | COMPLETED | SUCCESS | passed |
| [build\-linux\-oldest\-cmake](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429041/job/115490112196>) | check run | COMPLETED | SUCCESS | passed |
| [build\-mingw \(clang64\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429024/job/115489897433>) | check run | COMPLETED | SUCCESS | passed |
| [build\-mingw \(ucrt64\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429024/job/115489896821>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(macos\-latest, false\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453428982/job/115489896595>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, 0\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429145/job/115489904673>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, 1\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429145/job/115489905174>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, 2\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429145/job/115489905099>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, false\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453428982/job/115489896931>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(ubuntu\-latest, true\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453428982/job/115489897886>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(windows\-latest, 0\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429145/job/115489905121>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(windows\-latest, 1\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429145/job/115489905116>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-installed \(windows\-latest, 2\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429145/job/115489905265>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(macos\-latest, libyuv LOCAL\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429037/job/115490508965>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(macos\-latest, libyuv OFF\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429037/job/115490508850>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(ubuntu\-latest, libyuv LOCAL\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429037/job/115490508493>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local \(ubuntu\-latest, libyuv OFF\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429037/job/115490508986>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local\-fuzztest \(ubuntu\-latest, LOCAL\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429118/job/115489897884>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-local\-fuzztest \(ubuntu\-latest, OFF\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429118/job/115489896883>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-run\-golden\-tests \(ubuntu\-latest\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429006/job/115489897142>) | check run | COMPLETED | SUCCESS | passed |
| [build\-shared\-run\-golden\-tests \(ubuntu\-latest\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429538/job/115489898267>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows\-installed \(clang\-cl\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429359/job/115489899649>) | check run | COMPLETED | SUCCESS | passed |
| [build\-windows\-installed \(msvc\)](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429359/job/115489899229>) | check run | COMPLETED | SUCCESS | passed |
| [clang\-format\-check](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429058/job/115489896133>) | check run | COMPLETED | SUCCESS | passed |
| [cmake\-format\-check](<https://github.com/AOMediaCodec/libavif/actions/runs/38453429058/job/115489896433>) | check run | COMPLETED | SUCCESS | passed |

### FasterXML/jackson\-databind #6302: Write an empty array when singleton container content is filtered out

Write an empty array when content filtering suppresses an unwrapped singleton, while preserving configured exception wrapping\.

- Source: [pull request](<https://github.com/FasterXML/jackson-databind/pull/6302>)
- Head commit: `38261628a27c109e6e49c916cdb0f7e8bf7bbf45`
- Base commit: `5d64697ef018099e3d5f951668752ec9d4ffabf9`
- Catalog note: Original 3\.x submission, before the October 18 retarget to 3\.1: https://github\.com/agamal026/jackson\-databind/commit/de533c218b30a86ac9e74a6627b7224c2a0d2987 \. The exact source, before/after hosted validation and independent automated review are retained at https://github\.com/agamal026/jackson\-databind/blob/942fb1328e72dd76cf58a32b194d9d3783baad16/contribution\-review/6299/README\.md \.
- Catalog note: Original 3\.x fork validation, before the October 18 retarget to 3\.1: the final fork CI passed all 53 new regression invocations on Linux JDK 17/21/25 and Windows JDK 17\. Full\-suite totals were 7,574 on JDK 17 and 7,576 on JDK 21/25, with zero failures or errors and one skip per build\. Linux JDK 17 also passed static Android API compatibility; no device execution is claimed\.
- Catalog note: At 2026\-10\-18T12:11:13Z, the upstream Gitar CheckRun reported success, but its bot comment states functional validation was not enabled\. Build and Deploy Snapshot required maintainer authorization and returned zero jobs\. One admission follow\-up is already posted at https://github\.com/FasterXML/jackson\-databind/pull/6302\#issuecomment\-6249752236 \. Do not duplicate it without new evidence\. CLA acceptance, upstream acceptance, issue bounty, patch\-specific reward eligibility and realized benefits remain unverified\.
- Catalog note: New maintainer feedback was observed on October 18: https://github\.com/FasterXML/jackson\-databind/pull/6302\#issuecomment\-6250227789 requests the oldest maintained affected branch, and https://github\.com/FasterXML/jackson\-databind/pull/6302\#discussion\_r4307148911 requests a helper for the repeated singleton guards\. The submitted review is COMMENTED, not approval\. A real 3\.1 backport and helper change are being prepared; the 13:37 observation still has the unchanged 3\.x head de533c218b30a86ac9e74a6627b7224c2a0d2987\.
- Catalog note: At 13:40 UTC, Build and Deploy Snapshot still required action and its actual job list returned zero jobs\. The maintainer CLA reminder is https://github\.com/FasterXML/jackson\-databind/pull/6302\#issuecomment\-6250307295 \. CLA acceptance remains unverified; no duplicate admission request, approval, acceptance or benefit is established\.
- Catalog note: The actual 3\.1 backport/helper source 38261628a27c109e6e49c916cdb0f7e8bf7bbf45 is published upstream at base 5d64697ef018099e3d5f951668752ec9d4ffabf9 \(12 files, 776 additions, no deletions; all blobs verified\)\. The baseline produced one failure and 32 errors among 53 cases per build; c2366f stopped at test compilation with zero executed tests; 60218d executed 74 with 72 passes/two compatibility assertion failures\. A separately reviewed fixture\-only correction retains all original 53 cases and compares unwrapped behavior with the established wrapped path\. Final owned workflow 39137464915 passed all 74 cases in all four builds\. Before/after evidence: https://github\.com/agamal026/jackson\-databind/blob/3e832d88429ddd257b144fb1a811eebb3a3a91e2/contribution\-review/6299/3\.1\-followup/README\.md
- Catalog note: Upstream workflow 39138054220 attempt 2 completed successfully at 2026\-10\-18T15:10:36Z; metadata/log audit at 15:13:35\-15:13:49 established four successful builds, two skipped downstream triggers and seven CheckRuns including successful Gitar\. All 74 cases passed per build, with full totals 5,883 on JDK 17 and 5,885 on JDK 21/25, zero failures/errors and one skip\. Linux JDK 17 passed Android API compatibility\. Evidence: https://github\.com/agamal026/jackson\-databind/blob/d4b18b11fea2be9088b7ad19c768ae31998e2aed/contribution\-review/6299/3\.1\-upstream/README\.md \. The earlier action\_required/zero\-job observation is historical\. Empty legacy statuses do not represent a pending workflow\.
- Catalog note: Final PR body updated at 15:24:42 UTC and canonically verified at 15:25:01; open/non\-draft, five issue comments and two inline comments\. One substantive helper reply was posted at 15:16:02 and verified at 15:16:13: https://github\.com/FasterXML/jackson\-databind/pull/6302\#discussion\_r4307557870 \. Old owned 3\.x draft is closed/archived; owned validation draft \#2 stays open/draft and receives no campaign credit\. Existing maintainer review is COMMENTED; CLA acceptance, human approval, upstream acceptance and benefits remain unverified\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [Gitar](<https://github.com/FasterXML/jackson-databind/runs/117706532128>) | check run | COMPLETED | SUCCESS | passed |
| [Trigger v2 dep builds](<https://github.com/FasterXML/jackson-databind/actions/runs/39138054220/job/117710178535>) | check run | COMPLETED | SKIPPED | skipped |
| [Trigger v3 dep builds](<https://github.com/FasterXML/jackson-databind/actions/runs/39138054220/job/117710178712>) | check run | COMPLETED | SKIPPED | skipped |
| [build \(17, ubuntu\-24\.04\)](<https://github.com/FasterXML/jackson-databind/actions/runs/39138054220/job/117709602754>) | check run | COMPLETED | SUCCESS | passed |
| [build \(17, windows\-latest, W\)](<https://github.com/FasterXML/jackson-databind/actions/runs/39138054220/job/117709603036>) | check run | COMPLETED | SUCCESS | passed |
| [build \(21, ubuntu\-24\.04\)](<https://github.com/FasterXML/jackson-databind/actions/runs/39138054220/job/117709602933>) | check run | COMPLETED | SUCCESS | passed |
| [build \(25, ubuntu\-24\.04\)](<https://github.com/FasterXML/jackson-databind/actions/runs/39138054220/job/117709603004>) | check run | COMPLETED | SUCCESS | passed |

### javaparser/javaparser #5175: Preserve spacing before the type when removing the last import

Preserve the existing separator before a type when the lexical\-preserving printer removes the last of multiple imports\.

- Source: [pull request](<https://github.com/javaparser/javaparser/pull/5175>)
- Head commit: `2a437e500bf54024772dd9f3d6d4149506defed2`
- Base commit: `dc6bc07155cb0d0d7a8a427b76411848eb862136`
- Catalog note: Published source: https://github\.com/agamal026/javaparser/commit/2a437e500bf54024772dd9f3d6d4149506defed2 \. The exact tested tree and automated review are retained at https://github\.com/agamal026/javaparser/blob/be86f30a136fddc1e741fdcb36094bbbbfaaa454/contribution\-review/4074/README\.md \.
- Catalog note: Previously completed Linux/Java 17 AlsoSlowTests validation passed 5,831 tests with 35 skips and all nine reactor modules successful\. This is reused local evidence, not execution of the upstream hosted matrix\.
- Catalog note: At 2026\-10\-18T10:19:27Z, AppVeyor reported success without underlying log inspection\. Both GitHub Actions runs still required authorization and their job lists returned zero jobs\. Submission does not establish acceptance or benefit eligibility\.
- Catalog note: At the October 18 13:37\-13:40 UTC follow\-through, the submitted head remained 2a437e500bf54024772dd9f3d6d4149506defed2\. The only comment was the existing admission request; no inline comments or submitted reviews were returned\. Both Actions runs remained action\_required and their actual job lists each returned zero jobs\. AppVeyor still reported success without underlying log inspection\. Do not duplicate the existing request\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [continuous\-integration/appveyor/pr](<https://ci.appveyor.com/project/ftomassetti/javaparser/builds/54919188>) | status context | SUCCESS | not reported | passed |

### libevent/libevent #1916: Replace the bundled ARC4 RNG with operating\-system randomness

Replace the bundled ARC4 random\-number generator with operating\-system randomness\.

- Source: [pull request](<https://github.com/libevent/libevent/pull/1916>)
- Head commit: `14e56a95e1d524d8500da73bb49f9b0c80397057`
- Base commit: `d82464a277d0f42703702c4dfd9af6af38595a83`
- Catalog note: The published PR records remaining platform, real\-chroot, and concurrency coverage limits\.

### lz4/lz4 #1890: Accept zero end markers in legacy LZ4 streams

Fix \#1889: accept the Linux kernel four\-zero\-byte end marker in legacy LZ4 decoding and listing, preserving following\-frame handling and queued output cleanup\.

- Source: [pull request](<https://github.com/lz4/lz4/pull/1890>)
- Head commit: `0917e70420429ea2acab6aaac48cffdf4e827440`
- Base commit: `e7c36223415219c0a18ea75e3fe2eb5d267ee667`
- Catalog note: Published source: https://github\.com/agamal026/lz4/commit/f83be8241c6042a0f9b500da927f68caa905fc92 \. Exact source, failed baseline, local validation and independent automated review: https://github\.com/agamal026/lz4/blob/9016232b3f5ef31764c6b4ae30f201da1ecaa445/contribution\-review/1889/README\.md \.
- Catalog note: Linux x86\-64 GCC 13\.3\.0 builds and the extended legacy regression passed in threaded and nonthreaded modes; the existing listing suite passed 10 tests with no failures, errors or skips\. The broader CLI command failed at test\-lz4\-blocksize, reproduced with the unchanged upstream binary\. No complete upstream suite pass is claimed\.
- Catalog note: At 2026\-10\-18T13:13:26Z, all 54 upstream CheckRuns and all 54 actual workflow jobs showed 48 successes and six in progress, with no failures\. Six of nine workflows were successful; three and AppVeyor remained pending\. The dated CI supplement is https://github\.com/agamal026/lz4/blob/77b69464c6c9afb253eb8c186ac404afbc43e87b/contribution\-review/1889/UPSTREAM\_CI\.md \. No complete matrix pass is established; no admission follow\-up is needed\. Upstream acceptance and Tier 1 project scope remain separate from patch\-specific reward eligibility or payment\.
- Catalog note: The October 18 13:37\-13:38 UTC follow\-through resolved all pending jobs on f83be8241c6042a0f9b500da927f68caa905fc92: 53 of 54 CheckRuns and actual jobs succeeded; ThreadSanitizer failed at https://github\.com/lz4/lz4/actions/runs/39130134533/job/117683433807 \. Eight workflows succeeded and Sanitizers failed\. AppVeyor reported success\. The actual failed log identifies a race between legacy progress\-counter update and writer display; the extended legacy script exits 66\. No complete matrix pass is claimed\.
- Catalog note: A separate GCC 13 ThreadSanitizer control reproduced the race on unchanged upstream e7c36223415219c0a18ea75e3fe2eb5d267ee667 using an ordinary 26 MiB legacy stream, exit 66: https://github\.com/agamal026/lz4/blob/a7f764a75f381654296c2d6e55d9c89478c21400/contribution\-review/1889/tsan\-baseline/README\.md \. Correction 0917e70420429ea2acab6aaac48cffdf4e827440 is now verified in upstream PR \#1890\. Eight actual local commands passed, including the same TSan control, the complete TSan legacy regression and normal threaded/nonthreaded regressions: https://github\.com/agamal026/lz4/blob/a96c638dc9160f43544c8cd8414624cb2c166730/contribution\-review/1889/tsan\-followup/README\.md \. At 14:11:25\-14:11:26 UTC, all 54 actual jobs, 54 CheckRuns and nine workflows succeeded on corrected source; AppVeyor also reports success\. The full successful TSan log confirms all end\-marker cases and assertions without a TSan diagnostic: https://github\.com/lz4/lz4/actions/runs/39133845170/job/117694255444 \. The earlier failed source and broader local CLI limitation remain recorded; this does not establish acceptance or reward eligibility\.
- Catalog note: The completed corrected hosted matrix and full successful TSan log are preserved at https://github\.com/agamal026/lz4/blob/7751a987a7199b696902630b16d8e831880e9451/contribution\-review/1889/tsan\-hosted/README\.md \. Evidence commit 7751a987a7199b696902630b16d8e831880e9451 has five verified direct blobs\. Its 258,638\-byte ZIP has SHA\-256 9375604c1dcf8f545a12c5b24ac4130fe2be3d1f6ec5b1d1b3ac594f7b86d265 and contains the complete monitoring receipt and decoded job log\. The observed CI time remains October 18 14:11:25\-14:11:26 UTC; evidence publication does not refresh that observation\.
- Catalog note: Final PR body update at 2026\-10\-18T14:41:45Z links completed hosted packet 7751a987 and reports 54 successful jobs/CheckRuns, nine workflows and AppVeyor success\. Canonical matching body/head/base/open\-state readback was verified; its exact clock was not captured\. No comment was posted\. Full CI observation remains 14:11:25\-14:11:26 UTC\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [ABI Compatibility Tests](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255215>) | check run | COMPLETED | SUCCESS | passed |
| [ARM \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255202>) | check run | COMPLETED | SUCCESS | passed |
| [ARM64 \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255441>) | check run | COMPLETED | SUCCESS | passed |
| [AddressSanitizer \(x64\)](<https://github.com/lz4/lz4/actions/runs/39133845170/job/117694255347>) | check run | COMPLETED | SUCCESS | passed |
| [Benchmark Tests](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255231>) | check run | COMPLETED | SUCCESS | passed |
| [Block Device Compression Test](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255222>) | check run | COMPLETED | SUCCESS | passed |
| [Build Examples](<https://github.com/lz4/lz4/actions/runs/39133845148/job/117694255255>) | check run | COMPLETED | SUCCESS | passed |
| [Clang Static Analyzer](<https://github.com/lz4/lz4/actions/runs/39133845148/job/117694255177>) | check run | COMPLETED | SUCCESS | passed |
| [Core Tests \(macos\-latest, Release\)](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255374>) | check run | COMPLETED | SUCCESS | passed |
| [Core Tests \(ubuntu\-latest, Debug\)](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255407>) | check run | COMPLETED | SUCCESS | passed |
| [Core Tests \(ubuntu\-latest, Release\)](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255395>) | check run | COMPLETED | SUCCESS | passed |
| [Core Tests \(windows\-latest, Release\)](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255480>) | check run | COMPLETED | SUCCESS | passed |
| [Cppcheck Static Analysis](<https://github.com/lz4/lz4/actions/runs/39133845148/job/117694254997>) | check run | COMPLETED | SUCCESS | passed |
| [Custom Configuration Tests](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255210>) | check run | COMPLETED | SUCCESS | passed |
| [Environment Info \(ubuntu\-22\.04\)](<https://github.com/lz4/lz4/actions/runs/39133845154/job/117694255303>) | check run | COMPLETED | SUCCESS | passed |
| [Environment Info \(ubuntu\-24\.04\)](<https://github.com/lz4/lz4/actions/runs/39133845154/job/117694255308>) | check run | COMPLETED | SUCCESS | passed |
| [Environment Info \(ubuntu\-latest\)](<https://github.com/lz4/lz4/actions/runs/39133845154/job/117694255239>) | check run | COMPLETED | SUCCESS | passed |
| [Extended Tests \(cmake\_versions\)](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255464>) | check run | COMPLETED | SUCCESS | passed |
| [Extended Tests \(integration\)](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255351>) | check run | COMPLETED | SUCCESS | passed |
| [Extended Tests \(static\_lib\)](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255420>) | check run | COMPLETED | SUCCESS | passed |
| [Fuzzer Tests](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255265>) | check run | COMPLETED | SUCCESS | passed |
| [Git Version Tag Check](<https://github.com/lz4/lz4/actions/runs/39133845154/job/117694255092>) | check run | COMPLETED | SUCCESS | passed |
| [LZ4 Frame Tests](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255195>) | check run | COMPLETED | SUCCESS | passed |
| [M68K \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255263>) | check run | COMPLETED | SUCCESS | passed |
| [MIPS \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255295>) | check run | COMPLETED | SUCCESS | passed |
| [Make CMake](<https://github.com/lz4/lz4/actions/runs/39133845224/job/117694255278>) | check run | COMPLETED | SUCCESS | passed |
| [Makefile Standard Variables Test](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255198>) | check run | COMPLETED | SUCCESS | passed |
| [Memory Usage Tests](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694254996>) | check run | COMPLETED | SUCCESS | passed |
| [MemorySanitizer \(x64\)](<https://github.com/lz4/lz4/actions/runs/39133845170/job/117694255431>) | check run | COMPLETED | SUCCESS | passed |
| [Meson \+ Ninja](<https://github.com/lz4/lz4/actions/runs/39133845143/job/117694254952>) | check run | COMPLETED | SUCCESS | passed |
| [Meson \+ Ninja \(MSVC, shared library\)](<https://github.com/lz4/lz4/actions/runs/39133845143/job/117694255176>) | check run | COMPLETED | SUCCESS | passed |
| [OSS\-Fuzz \(address\)](<https://github.com/lz4/lz4/actions/runs/39133845150/job/117694255196>) | check run | COMPLETED | SUCCESS | passed |
| [OSS\-Fuzz \(memory\)](<https://github.com/lz4/lz4/actions/runs/39133845150/job/117694255318>) | check run | COMPLETED | SUCCESS | passed |
| [OSS\-Fuzz \(undefined\)](<https://github.com/lz4/lz4/actions/runs/39133845150/job/117694255418>) | check run | COMPLETED | SUCCESS | passed |
| [PPC \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255247>) | check run | COMPLETED | SUCCESS | passed |
| [PPC64LE \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255757>) | check run | COMPLETED | SUCCESS | passed |
| [RISC\-V \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255275>) | check run | COMPLETED | SUCCESS | passed |
| [S390X \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255258>) | check run | COMPLETED | SUCCESS | passed |
| [SPARC \(QEMU\)](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255286>) | check run | COMPLETED | SUCCESS | passed |
| [ThreadSanitizer \(x64\)](<https://github.com/lz4/lz4/actions/runs/39133845170/job/117694255444>) | check run | COMPLETED | SUCCESS | passed |
| [UndefinedBehaviorSanitizer \(x64\)](<https://github.com/lz4/lz4/actions/runs/39133845170/job/117694255449>) | check run | COMPLETED | SUCCESS | passed |
| [UndefinedBehaviorSanitizer \(x86\)](<https://github.com/lz4/lz4/actions/runs/39133845170/job/117694255399>) | check run | COMPLETED | SUCCESS | passed |
| [Unicode Linting](<https://github.com/lz4/lz4/actions/runs/39133845148/job/117694255143>) | check run | COMPLETED | SUCCESS | passed |
| [Valgrind Memory Analysis](<https://github.com/lz4/lz4/actions/runs/39133845148/job/117694255207>) | check run | COMPLETED | SUCCESS | passed |
| [Version Compatibility Tests](<https://github.com/lz4/lz4/actions/runs/39133845188/job/117694255219>) | check run | COMPLETED | SUCCESS | passed |
| [cc on ubuntu\-latest](<https://github.com/lz4/lz4/actions/runs/39133845159/job/117694255644>) | check run | COMPLETED | SUCCESS | passed |
| [clang on ubuntu\-latest](<https://github.com/lz4/lz4/actions/runs/39133845159/job/117694255662>) | check run | COMPLETED | SUCCESS | passed |
| [clang\-14 on ubuntu\-22\.04](<https://github.com/lz4/lz4/actions/runs/39133845159/job/117694255639>) | check run | COMPLETED | SUCCESS | passed |
| [clang\-18 on ubuntu\-24\.04](<https://github.com/lz4/lz4/actions/runs/39133845159/job/117694255742>) | check run | COMPLETED | SUCCESS | passed |
| [continuous\-integration/appveyor/pr](<https://ci.appveyor.com/project/YannCollet/lz4-1lndh/builds/54919870>) | status context | SUCCESS | not reported | passed |
| [gcc on ubuntu\-latest](<https://github.com/lz4/lz4/actions/runs/39133845159/job/117694255678>) | check run | COMPLETED | SUCCESS | passed |
| [gcc\-11 on ubuntu\-22\.04](<https://github.com/lz4/lz4/actions/runs/39133845159/job/117694255485>) | check run | COMPLETED | SUCCESS | passed |
| [gcc\-14 on ubuntu\-24\.04](<https://github.com/lz4/lz4/actions/runs/39133845159/job/117694255689>) | check run | COMPLETED | SUCCESS | passed |
| [macOS](<https://github.com/lz4/lz4/actions/runs/39133845146/job/117694255030>) | check run | COMPLETED | SUCCESS | passed |
| [windows\-2022 Visual Studio](<https://github.com/lz4/lz4/actions/runs/39133845143/job/117694255224>) | check run | COMPLETED | SUCCESS | passed |

### nginx/nginx #1734: Core: add a total client request body timeout\.

Add a total timeout for receiving a client request body\.

- Source: [pull request](<https://github.com/nginx/nginx/pull/1734>)
- Head commit: `cba808773e79f4e329d25e5c70c4262f8f590ad1`
- Base commit: `231a60ee3e90a43b829b9ca0a3013a8359b98d7e`
- Catalog note: Companion tests: https://github\.com/agamal026/nginx\-tests/commit/b3a6c55 \. Companion documentation: https://github\.com/agamal026/nginx\.org/commit/308a9143e2bada4f479d806ca6116ce25f8c8b19 \.
- Catalog note: Bounded local proof and an approved CLA do not establish that every upstream configuration has passed\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [F5 Contributor License Agreement \(CLA\)](<https://github.com/nginx/nginx/actions/runs/35681728612/job/106599923641>) | check run | COMPLETED | SUCCESS | passed |

### nih\-at/libzip #576: CI: restore AppVeyor x86 and ARM builds

Restore AppVeyor x86/ARM builds after the related portable crypto\-clearing fix was integrated\.

- Source: [pull request](<https://github.com/nih-at/libzip/pull/576>)
- Head commit: `5aeb57b6e922934125008756998b3ce2a93ba498`
- Base commit: `564f17974a45aba8b3d852f40a279e0b6ff82a80`
- Catalog note: The maintainer confirmed the crypto\-clearing integration separately: https://github\.com/nih\-at/libzip/pull/576\#issuecomment\-5777143699 \. The open CI remainder must not be reported as a fully merged PR\.
- Catalog note: Windows/CI support was invited at https://github\.com/nih\-at/libzip/pull/576\#issuecomment\-5698019796 \. This is a contribution invitation, not appointment as an upstream maintainer\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [continuous\-integration/appveyor/pr](<https://ci.appveyor.com/project/nih-at/libzip/builds/54772589>) | status context | SUCCESS | not reported | passed |

### npm/cli #9954: feat\(arborist\): warn on incomplete lockfile provenance

Warn about incomplete lockfile provenance in Arborist\.

- Source: [pull request](<https://github.com/npm/cli/pull/9954>)
- Head commit: `2e9c31473c5e7557f4a506a586f4a1b1f1f7c770`
- Base commit: `c9876d7ea7150b0702e4151210b9fa1a8dbc7fbf`
- Catalog note: Record upstream workflow admission and maintainer feedback before claiming readiness\.

## Maintained projects

Cataloged release and CI links are references. This command refreshes pull requests only; it does not verify a release or run project tests.

| Project | Description | Declared license | Release | CI |
| --- | --- | --- | --- | --- |
| [agamal026/pinned\-json](<https://github.com/agamal026/pinned-json>) | Offline Python library and CLI that verifies a separately trusted manifest digest and emits JSON fixtures as their original bytes\. Python 3\.10\+ on Linux; v0\.1\.1 is an alpha prerelease fixing traversal through directories without listing permission\. | MIT | [v0\.1\.1](<https://github.com/agamal026/pinned-json/releases/tag/v0.1.1>) | [CI](<https://github.com/agamal026/pinned-json/actions/runs/39065995086>) |
| [agamal026/raydium\-cpmm\-arb\-monitor](<https://github.com/agamal026/raydium-cpmm-arb-monitor>) | Read\-only Node\.js/TypeScript CLI for Raydium CPMM pool discovery and estimated cross\-pool spreads\. Node 22\+; v0\.1\.1 fixes response\-body timeouts\. It does not execute trades\. | MIT | [v0\.1\.1](<https://github.com/agamal026/raydium-cpmm-arb-monitor/releases/tag/v0.1.1>) | [CI](<https://github.com/agamal026/raydium-cpmm-arb-monitor/actions/runs/38885587743>) |

## Candidate work

Stages and next actions below are curated catalog notes, not GitHub readiness decisions.

| Candidate | Stage | Next action |
| --- | --- | --- |
| [AOMediaCodec/libavif \#2428: Tolerate unsupported non\-essential pixi versions while preserving item\-property indexes\.](<https://github.com/AOMediaCodec/libavif/issues/2428>) | human\_review\_pending | The contributor must personally review the prepared parser change, fixture, tests, and PR text under AOMedia's contribution policy\. Then refresh the exact source and upstream state before authorized submission\. |
| [AOMediaCodec/libavif \#2780: Investigate Xcode object\-library targets and duplicate source basenames\.](<https://github.com/AOMediaCodec/libavif/issues/2780>) | parked | Resume after macOS/Xcode workflow admission permits actual static/shared and libyuv\-off validation\. Linux or Ninja results do not establish Xcode correctness\. |
