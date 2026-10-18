# Open-source progress

Observed at: 2026-10-18T10:19:27Z. Baseline date: 2026-10-13 (UTC).

This report is generated from the public catalog and a dated GitHub snapshot. It is not a live status page.

## Upstream contributions

Registered pull requests: 7; open: 6; merged: 1; closed without merge: 0.

Registered PRs with a recorded merge on or after 2026-10-13: 0.

This date comparison does not establish an additional independently tested contribution or completion of a project goal. Partial integrations in otherwise open PRs require separate evidence. Own-project releases are listed separately and do not enter these counts.

Check results describe only the rollup returned by GitHub for each recorded head. Missing checks and unrecognized states remain unknown. Success does not establish review approval, complete test coverage, or readiness to merge.

| Pull request | State | Returned checks | Review decision | Updated (UTC) |
| --- | --- | --- | --- | --- |
| [AOMediaCodec/libavif \#3350](<https://github.com/AOMediaCodec/libavif/pull/3350>) | merged | 42 passed | approved | 2026-09-09T23:21:10Z |
| [AOMediaCodec/libavif \#3413](<https://github.com/AOMediaCodec/libavif/pull/3413>) | open | 1 failed; 25 passed | not reported | 2026-10-13T19:43:27Z |
| [javaparser/javaparser \#5175](<https://github.com/javaparser/javaparser/pull/5175>) | open | 1 passed | not reported | 2026-10-18T10:13:18Z |
| [libevent/libevent \#1916](<https://github.com/libevent/libevent/pull/1916>) | open | unknown (no checks returned) | review required | 2026-10-15T13:13:47Z |
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

### javaparser/javaparser #5175: Preserve spacing before the type when removing the last import

Preserve the existing separator before a type when the lexical\-preserving printer removes the last of multiple imports\.

- Source: [pull request](<https://github.com/javaparser/javaparser/pull/5175>)
- Head commit: `2a437e500bf54024772dd9f3d6d4149506defed2`
- Base commit: `dc6bc07155cb0d0d7a8a427b76411848eb862136`
- Catalog note: Published source: https://github\.com/agamal026/javaparser/commit/2a437e500bf54024772dd9f3d6d4149506defed2 \. The exact tested tree and automated review are retained at https://github\.com/agamal026/javaparser/blob/be86f30a136fddc1e741fdcb36094bbbbfaaa454/contribution\-review/4074/README\.md \.
- Catalog note: Previously completed Linux/Java 17 AlsoSlowTests validation passed 5,831 tests with 35 skips and all nine reactor modules successful\. This is reused local evidence, not execution of the upstream hosted matrix\.
- Catalog note: At 2026\-10\-18T10:19:27Z, AppVeyor reported success without underlying log inspection\. Both GitHub Actions runs still required authorization and their job lists returned zero jobs\. Submission does not establish acceptance or benefit eligibility\.

| Check | Kind | Raw status | Conclusion | Interpretation |
| --- | --- | --- | --- | --- |
| [continuous\-integration/appveyor/pr](<https://ci.appveyor.com/project/ftomassetti/javaparser/builds/54919188>) | status context | SUCCESS | not reported | passed |

### libevent/libevent #1916: Replace the bundled ARC4 RNG with operating\-system randomness

Replace the bundled ARC4 random\-number generator with operating\-system randomness\.

- Source: [pull request](<https://github.com/libevent/libevent/pull/1916>)
- Head commit: `14e56a95e1d524d8500da73bb49f9b0c80397057`
- Base commit: `d82464a277d0f42703702c4dfd9af6af38595a83`
- Catalog note: The published PR records remaining platform, real\-chroot, and concurrency coverage limits\.

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
