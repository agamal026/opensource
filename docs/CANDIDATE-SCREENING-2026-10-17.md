# Candidate screening — October 17, 2026

**Screen window:** October 17, 2026, **22:16:57–22:24:32 UTC**.
**Result:** **zero candidates selected** for a new implementation. No new
contribution, acceptance, cash payment, credit or subscription was confirmed.

This bounded, read-only screen followed the [goal](../GOAL.md),
[opportunity priorities](OPPORTUNITIES.md) and [campaign queue](../data/campaign.json).
It prioritized available paid work, then Java/backend problems suitable for
cloud validation. Previously parked Expensify, json-c, libyaml and Gson findings
were not investigated again. The existing H2 contribution remained the active
implementation; this screen did not create a second one.

## Paid leads that did not qualify

### pgstrap: a suitable workflow with many competing fixes

[seveibar/pgstrap issue #2](https://github.com/seveibar/pgstrap/issues/2) requests
type generation through embedded PGlite without a running PostgreSQL server.
The [tscircuit sponsor listing](https://algora.io/tscircuit/bounties) advertised
**$30**. Live GitHub records showed the issue open and unassigned, with 65 comments,
but its open pull requests included many implementations of the same request.
[PR #98](https://github.com/seveibar/pgstrap/pull/98) had opened that morning at
09:17:07 UTC; [#97](https://github.com/seveibar/pgstrap/pull/97),
[#96](https://github.com/seveibar/pgstrap/pull/96) and numerous earlier solutions
were also open.

**Decision:** do not add another competing implementation. The task appears
compatible with cloud testing, but an empty assignee field does not establish
that a bounty is available for a new contributor. No selection or payout
eligibility was established.

### Archestra: reserved and closed

[archestra-ai/archestra issue #3378](https://github.com/archestra-ai/archestra/issues/3378)
advertised **$500** for agent schedule triggers. The live issue was closed,
assigned to `kennethaasan`, and explicitly reserved for a specific contributor.
Its posted Algora process requires core-team assignment. The stated payment
timing follows a reward decision, rather than simply submitting a pull request.

**Decision:** unavailable; no implementation or application was justified.

### microG: sponsor restriction and physical validation

[microg/GmsCore issue #2843](https://github.com/microg/GmsCore/issues/2843)
advertised **$2,340** in its title and remained open. The bounty sponsor's
October 4 update requires maintainer-accepted WearOS support on recent real
devices, covering notifications, media controls and apps. The same sponsor
expressly rejects AI coding-agent involvement in this bounty. This is a
restriction stated by the **bounty sponsor**, not a verified project-wide microG
contribution policy. Existing implementation attempts were also linked.

**Decision:** unsuitable for this contribution workflow and its available
physical validation. No reward eligibility or earnings were established for this session.

The current [ZIO bounty page](https://algora.io/zio/bounties) also reported
**zero open bounties**. Older search results about completed Scala/JVM rewards
therefore supplied no currently listed task to select.

## Java queue exclusions

- [Jackson #1761](https://github.com/FasterXML/jackson-core/issues/1761), concerning
  premature DataInput EOF exceptions, was open and unassigned, but
  [PR #1763](https://github.com/FasterXML/jackson-core/pull/1763) already supplied
  an open implementation, last updated October 14.
- Other Jackson parser leads also had open solutions:
  [#1735](https://github.com/FasterXML/jackson-core/issues/1735) had
  [PR #1736](https://github.com/FasterXML/jackson-core/pull/1736), and
  [#1640](https://github.com/FasterXML/jackson-core/issues/1640) had
  [PR #1648](https://github.com/FasterXML/jackson-core/pull/1648).
- [jsoup #2552](https://github.com/jhy/jsoup/issues/2552), cyclic DOM creation,
  was closed as completed on August 10 and labelled fixed. A search-indexed
  issue list still presented it as open; the live API resolved that stale result.
- [jsoup #2541](https://github.com/jhy/jsoup/issues/2541), configurable input limits
  and truncation reporting, remained open but was assigned to maintainer `jhy`.
  No invitation to take over that work was established.

Jackson and jsoup's conditional project scope in the campaign does not establish
that these particular changes qualify for [Patch Rewards](https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md).
Patch-specific security value, contributor eligibility, acceptance, award and
payment remain separate questions. No lead passed the selection gates, so this
screen did not progress to reproduction, builds or a complete contribution-policy
review for a new implementation.

## Next selection action

Advance H2 through any remaining unblocked gates. If a personal contributor
statement or access dependency blocks submission, park H2 with its concrete
review package queued for personal review, and select the next useful unblocked
task. Keep at most one main upstream implementation active, as described in
[cloud operation](CLOUD-OPERATION.md). Retain the exclusions above for future
screens. Start the next bounded search with a different Java/backend repository
or a newly posted sponsor task; fetch both its live issue and open pull requests
before coding. Require available assignment or an otherwise uncontested scope,
then verify current contributor/AI policy, acceptance and benefit terms, and
practical cloud validation. A listed reward or unassigned issue alone is insufficient.

This screen created no comments, applications, source edits, forks or pull
requests. Its outcome is research evidence, not a submitted-project milestone.
