# Jackson Databind acceptance and candidate routing — 2026-11-21

## Acceptance recorded

The campaign now has **5 / 100 accepted projects**. Qualified submitted project histories remain **7**; the six historical submissions remain excluded.

- Original [FasterXML/jackson-databind #6302](https://github.com/FasterXML/jackson-databind/pull/6302) closed unmerged on November 16.
- Maintainer [#6454](https://github.com/FasterXML/jackson-databind/pull/6454) merged on November 16 as [`b63b8749041d31159c24d46018559bdcc23dc3a9`](https://github.com/FasterXML/jackson-databind/commit/b63b8749041d31159c24d46018559bdcc23dc3a9).
- Its implementation commit [`e9547600a3e0498f0733ff1be7d06402b62327bc`](https://github.com/FasterXML/jackson-databind/commit/e9547600a3e0498f0733ff1be7d06402b62327bc) explicitly says it is based on #6302 by @agamal026. The merged release notes also credit @agamal026 in [CREDITS](https://github.com/FasterXML/jackson-databind/blob/b63b8749041d31159c24d46018559bdcc23dc3a9/release-notes/CREDITS) and [VERSION](https://github.com/FasterXML/jackson-databind/blob/b63b8749041d31159c24d46018559bdcc23dc3a9/release-notes/VERSION).
- The incorporated implementation is a distinct maintainer approach. This qualifies as explicit source-linked incorporation; it does **not** claim that #6302 itself merged. The submitted head was [`38261628a27c109e6e49c916cdb0f7e8bf7bbf45`](https://github.com/agamal026/jackson-databind/commit/38261628a27c109e6e49c916cdb0f7e8bf7bbf45).
- No personal CLA action was taken in this run. The technical acceptance does not establish separate legal status, reward eligibility, an application, award or payment. No benefit is recorded.

## Existing submitted work

- [BeanUtils #444](https://github.com/apache/commons-beanutils/pull/444) remains open at head `51a346ab12e0fd683df794ab40c9f18e58f92068`, last updated October 30. Its current head has zero check runs and a pending combined status with zero status contexts. No admitted failure or changed maintainer feedback was found.
- [Commons Compress #825](https://github.com/apache/commons-compress/pull/825) remains open at head `7e6477880259d60d4dfa60a5e34e4ea7875176b1`, last updated October 22. Its current head has zero check runs and a pending combined status with zero status contexts. No admitted failure or changed maintainer feedback was found.
- JavaParser #5188 remains accepted once through squash `71544cb30b8857f32282d2edbd23e9d0a581d6a9`. No successful unchanged test matrix was rerun.

## Candidate screening — three sequential waves

All allocations were recorded before querying. No issue was selected for implementation, and no patch was prepared behind a known publication gate.

### Wave 1 — Joomla, jQuery, Keycloak

- **Joomla**: [#48883](https://github.com/joomla/joomla-cms/issues/48883) reports empty-name validation in Media Manager Rename. [#48884](https://github.com/joomla/joomla-cms/pull/48884) is already open and resolves it. The PR documents Vue compile/lint and isolated checks, while its full Cypress system run against a configured Joomla installation remains pending. The [Generative AI policy](https://developer.joomla.org/generative-ai-policy.html) requires the contributor to understand, review and validate the work. No existing contributor fork or supported fork-creation action was available. Parked; do not duplicate.
- **jQuery**: [CONTRIBUTING.md](https://github.com/jquery/jquery/blob/main/CONTRIBUTING.md) explicitly excludes auto-generated issues and pull requests. No genuine user-originated use case or maintainer-requested task was established. The Node test route is documented, but no contributor fork or supported fork-creation action was available. Parked.
- **Keycloak**: [CONTRIBUTING.md](https://github.com/keycloak/keycloak/blob/main/CONTRIBUTING.md) requires a DCO sign-off on every commit; the AI guidance also requires disclosure and contributor understanding/review. No personal sign-off was authorized and no contributor fork or fork-creation action was available. Parked.

### Wave 2 — Netty, lxml, libgit2

- **Netty**: [AGENTS.md](https://github.com/netty/netty/blob/4.2/AGENTS.md) limits agents to trivial text drafting; code changes are treated as security-sensitive, and the project requires a contributor CLA. Issues [#18481](https://github.com/netty/netty/issues/18481) and [#18483](https://github.com/netty/netty/issues/18483) already have competing PRs [#18493](https://github.com/netty/netty/pull/18493), [#18487](https://github.com/netty/netty/pull/18487) and [#18492](https://github.com/netty/netty/pull/18492). The normal Maven verification/leak-check route was not run. No contributor fork or fork-creation action was available. Parked.
- **lxml**: no explicit AI-use policy was located in the repository root. Recent defect work is already represented by active [#564](https://github.com/lxml/lxml/pull/564), [#563](https://github.com/lxml/lxml/pull/563), [#561](https://github.com/lxml/lxml/pull/561) and [#559](https://github.com/lxml/lxml/pull/559). The [tox configuration](https://github.com/lxml/lxml/blob/master/tox.ini) runs extension build plus `make test` across Python 3.9–3.14 and PyPy 3. No distinct unclaimed task or contributor fork was established. Parked.
- **libgit2**: [docs/contributing.md](https://github.com/libgit2/libgit2/blob/main/docs/contributing.md) requires the normal fork-and-PR flow. Issue [#7487](https://github.com/libgit2/libgit2/issues/7487) already has PRs [#7488](https://github.com/libgit2/libgit2/pull/7488) and [#7489](https://github.com/libgit2/libgit2/pull/7489); issue [#7467](https://github.com/libgit2/libgit2/issues/7467) has [#7493](https://github.com/libgit2/libgit2/pull/7493); [#7480](https://github.com/libgit2/libgit2/issues/7480) is security-related and was not selected. The validation route is CMake plus `libgit2_tests`. No contributor fork or fork-creation action was available. Parked.

### Wave 3 — Apache Commons CLI, Commons Net, Commons Validator

- **Commons CLI**: [#452](https://github.com/apache/commons-cli/pull/452) is active; no recent unclaimed issue was selected. [CONTRIBUTING.md](https://github.com/apache/commons-cli/blob/master/CONTRIBUTING.md) says typical small bug fixes may not require an ICLA, but the normal route still uses a JIRA issue, contributor fork and Maven validation. No contributor fork or fork-creation action was available. Parked.
- **Commons Net**: active PRs [#419](https://github.com/apache/commons-net/pull/419), [#420](https://github.com/apache/commons-net/pull/420), [#421](https://github.com/apache/commons-net/pull/421), [#423](https://github.com/apache/commons-net/pull/423) and [#424](https://github.com/apache/commons-net/pull/424) already occupy current work. The normal Apache route requires a JIRA issue and contributor fork; typical small bug fixes may not require an ICLA. No contributor fork or fork-creation action was available. Parked.
- **Commons Validator**: prior screening already recorded the missing contributor-fork route. That result was preserved; no new issue or patch was selected.

## Publishing capability and stop condition

The connected account's current repository inventory contained no contributor fork for these eight newly screened targets. The current GitHub connector exposes branch, file and PR operations but no GitHub fork-creation action. No mirror, alternate wrapper, browser, machine, provider or credential route was used. This is a concrete publication-route limitation for the screened candidates, **not** a claim that all 100 upstream projects are universally prohibited.

No external source code, upstream PR, comment, review, credential, CLA attestation, purchase, benefit application or reward action was created. No external candidate tests were run. A fourth candidate wave was not allocated because the available account inventory and action catalog showed no new-target fork route; another wave would not advance a deliverable contribution.

## Execution receipt

- Origin: manual user-requested continuation. Host start timestamp and scheduled run ID were not exposed.
- Checkpoint timestamp: 2026-11-21T18:18:27.813Z.
- Recovered public checkpoint: `progress/2026-11-12-bcel-378-validation.md`; current public continuation and campaign ledger were read.
- Material work: Jackson acceptance verified; campaign advanced to 5/100; eight candidates screened and recorded; no source implementation prepared.
- Executed checks: campaign report renderer matched the existing Python-generated report byte-for-byte before the update; BeanUtils and Commons Compress check-run/status endpoints were read; no external tests were run.
- Publication: [campaign update PR #8](https://github.com/agamal026/opensource/pull/8) is open. GitHub Actions run [44934806967](https://github.com/agamal026/opensource/actions/runs/44934806967) completed successfully across all four Python/OS matrix jobs; each job ran the offline regression suite, public-record validation, generated status check, campaign validation/report check and whitespace check. No upstream submission was created.
- Accepted delta: +1; qualified submitted histories remain 7.
- Remaining dependency: a new external task needs a project-permitted issue and an existing contributor fork or supported fork-creation action. Existing upstream PRs remain dependent on maintainer feedback/admitted checks.
- Persistence: campaign JSON, generated report and README are committed on the PR branch; this checkpoint and continuation update accompany PR #8. No private Library overwrite was attempted because a canonical current-version-safe write target was not established.
- Scheduling: no task or schedule was created, edited, resumed or forced. The scheduler was not rechecked in this manual run; the last recorded observation remains unchanged.
