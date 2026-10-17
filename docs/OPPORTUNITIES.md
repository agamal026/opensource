# Opportunities and next decisions

**Checked: 2026-10-17.** Use this review with [the goal](../GOAL.md) and
[current contribution status](../progress/STATUS.md). The curated
[opportunities registry](../data/opportunities.json) records advertised benefits,
scoped eligibility, applications and outcomes separately. Recheck current terms
and assignment availability before acting.

The [late October 17 screening](CANDIDATE-SCREENING-2026-10-17.md) selected no
new paid or Java/backend task. It records claimed, crowded, closed and
incompatible leads so future runs can start with a different suitable issue.
The [H2 final CI checkpoint](../progress/2026-10-17-h2-final-ci-checkpoint.md)
preserves the prepared contribution and its remaining personal/technical gates.

## Cash opportunities

| Opportunity | Advertised benefit | Current assessment and next action |
| --- | --- | --- |
| [Google Patch Rewards: libzip](https://github.com/google/bughunters/blob/main/patch-rewards-program/scope.md) | Tier 1 base awards of **$500 / $2,000 / $7,500 / $15,000**, at panel discretion. | **Project scope verified; full reward eligibility unverified.** Prioritize the existing accepted hardening. Recheck at **2026-10-22T13:12:13Z**; this checkpoint does not establish qualification or an award. |
| [NLnet CodeSupply](https://nlnet.nl/codesupply/) | **€5,000–€50,000** for a first project grant. | **Project/applicant fit unverified.** The call closes **2026-11-03 at 12:00 CET (11:00 UTC)**. Assess one original supply-chain metadata project before preparing an application. |
| [Expensify/App #104027](https://github.com/Expensify/App/issues/104027) | **$175** advertised. | **Investigated; no distinct proposal justified.** There were **26 proposal comments** and no contractor selection observed. Park implementation; revisit only if selection or new evidence changes the opportunity. |

Google requires acceptance followed by **one full month without reverts**;
the [current rules](https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md)
also limit eligible patch age and submission frequency. Keep the
[accepted crypto-clearing commit](https://github.com/nih-at/libzip/commit/c3ba909e296e824f794e26d36379174524af74b8)
and [maintainer acknowledgment](https://github.com/nih-at/libzip/pull/576#issuecomment-5777143699)
separate from the open CI remainder of PR #576. The published award categories
are program terms; no amount has been established for this contribution.

CodeSupply requires relevant open deliverables and a
[European dimension](https://nlnet.nl/codesupply/eligibility/); the usual route
allocates at least 60% of funds to participants from Horizon Europe-eligible
countries, with an exceptional-project route described in the policy. No
residence or team qualification is assumed. Its
[FAQ](https://nlnet.nl/codesupply/faq/) says payment follows completed milestones,
with **no upfront payment**, and review normally takes **three to five months**
after the deadline. Read the [applicant guide](https://nlnet.nl/codesupply/guideforapplicants/)
and [AI policy](https://nlnet.nl/foundation/policies/generativeAI/): applicants
must own and understand the work, disclose application AI use with interaction
logs, and disclose material development assistance with provenance. Purely
AI-generated outcomes are not eligible for payment. Fixture/provenance tooling
is a possible starting point; a qualifying project has not been established.

The Expensify investigation inspected source at
[`ef784ba78226f211bbaa5d6698a5a162c20221e9`](https://github.com/Expensify/App/blob/ef784ba78226f211bbaa5d6698a5a162c20221e9/src/libs/navigateAfterOnboarding.ts).
Existing proposals, including [this same-revision proposal](https://github.com/Expensify/App/issues/104027#issuecomment-6228351983),
covered the traced cases. No runtime reproduction, patch, tests or submission
resulted. [Contribution rules](https://github.com/Expensify/App/blob/main/contributingGuides/CONTRIBUTING.md)
require a meaningfully different proposal, a verified Upwork profile, selection
and hiring before a PR; unpaid investigation does not guarantee compensation.
[AI etiquette](https://github.com/Expensify/App/blob/main/contributingGuides/AI_ETIQUETTE.md)
requires human understanding and evidence of manual testing.

**Excluded from current work:** [Expensify #103620](https://github.com/Expensify/App/issues/103620)
advertised **$250**, but a [reviewer recommended another contributor's proposal](https://github.com/Expensify/App/issues/103620#issuecomment-6194789017).
An open issue is insufficient evidence of an available paid assignment. Keep
crowded investigations within the timebox in `GOAL.md`.

## Services, subscriptions and compute

These benefits provide tools or service access. Their advertised value is not
cash income. Only the existing GitHub Actions execution has confirmed use in
this review; no other grant or activation is established here.

| Priority | Program and official terms | Benefit, fit and next action |
| --- | --- | --- |
| Use existing | [GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions) | Standard hosted runners are free for public repositories. [The hub's four-job run](https://github.com/agamal026/opensource/actions/runs/39058303362) succeeded. Continue useful CI; larger runners and storage follow separate billing terms. |
| Evaluate if useful | [Codecov OSS](https://about.codecov.io/for/open-source/) · [pricing](https://about.codecov.io/pricing/) | Free public-repository coverage reporting. Public MIT repository fit is verified; authorization and activation are not. Measure locally first and integrate only for a concrete testing benefit. |
| Check once | [Copilot for maintainers](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers) | Free Copilot Pro for eligible maintainers of popular OSS, reevaluated monthly. Check the actual account eligibility screen; popularity has not been established. |
| Assess project fit | [Codex for OSS](https://developers.openai.com/community/codex-for-oss) · [application](https://openai.com/form/codex-for-oss/) · [terms](https://learn.chatgpt.com/docs/codex-for-oss-terms) | Six months of ChatGPT Pro including Codex; possible API credits with no fixed amount promised. Rolling, discretionary review. Document genuine maintenance, adoption and a concrete workflow need; compare incremental value with existing subscriptions. |
| Use for a specific gap | [CircleCI OSS](https://circleci.com/open-source/) · [credit terms](https://circleci.com/docs/guides/plans-pricing/credits/) | Up to **400,000 Linux credits/month** for public repositories in qualifying Free Plan organizations. Actual plan/allocation is unverified. Official macOS figures conflict (**25,000 vs 30,000**); confirm platform allocation before relying on it. |
| Check intended use | [JetBrains OSS](https://www.jetbrains.com/community/opensource/) · [license](https://www.jetbrains.com/legal/docs/toolbox/license_opensource/) | Approved established projects may receive a one-year All Products Pack. Broad ecosystem impact is unverified; the OSS license has noncommercial restrictions. The [separate individual route](https://sales.jetbrains.com/hc/en-gb/articles/18950890312210-The-free-non-commercial-licensing-FAQ) may fit learning/unpaid work. Do not assume it covers paid bounty work. |
| Defer | [Claude OSS](https://claude.com/contact-sales/claude-for-oss) · [terms](https://www.anthropic.com/claude-for-oss-terms) | Six months of Max 20x, without automatic renewal. **Not eligible under the current two-year GitHub-account rule.** The [public account API](https://api.github.com/users/agamal026) records creation at **2025-01-26T19:46:19Z**. Recheck all criteria and program availability on **2027-01-26T19:46:19Z**. |

The owned [pinned-json release](https://github.com/agamal026/pinned-json/releases/tag/v0.1.0)
and [monitor release](https://github.com/agamal026/raydium-cpmm-arb-monitor/releases/tag/v0.1.1)
establish published work. They do not establish broad adoption. Authored upstream
PRs do not establish appointment as an upstream maintainer. Preserve that
distinction in every program assessment.

## Registry conventions: version 1

This is a manually reviewed JSON file; `oss_status.py` does not validate or
refresh it. Top-level fields are `schema_version`, `checked_on`, `scope` and
`opportunities`. Each entry has a unique `id`, positive integer `priority`
(lower means earlier consideration), `program`, curated `stage`, `benefit`,
`eligibility`, `application`, `outcome`, `next_action` and direct HTTPS `sources`.
Optional `deadline_at` and `recheck_at` are UTC timestamps. Recheck dates are
planning checkpoints, not scheduled tasks or promises of eligibility.

`benefit` contains `kinds`, `advertised` and `term`; kinds are `cash`,
`subscription`, `compute` or `developer_service`. It records program terms,
never inferred earnings. State fields have these meanings:

| Field | Allowed states and interpretation |
| --- | --- |
| `eligibility` | `unverified`, `verified`, `not_eligible`, with explicit `scope` and `evidence`. A verified repository criterion does not verify every applicant condition or grant approval. |
| `application` | `unknown`, `not_applied`, `submitted`, `withdrawn`, `declined`, with explicit `scope`. Use `unknown` when public evidence is absent; do not import private application history. |
| `outcome` | `none`, `granted`, `activated`, `paid`, with explicit `scope`. `none` means no benefit verified within that recorded scope. Grant approval, usable access and received payment require separate evidence. |

Before changing a state, add appropriate public evidence to `sources` and explain
the transition in dated progress. Preserve earlier states in Git history. Keep
private forms, application identifiers, account receipts and payment details out
of this registry. No application, service configuration or background monitoring
is performed by these files.
