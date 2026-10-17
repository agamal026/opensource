# Operate the contribution campaign from the cloud

## Goal and durable state

Complete useful, validated submissions to 100 distinct external projects, then
continue their review, maintenance, and benefit follow-through. Start with
[GOAL.md](../GOAL.md), [campaign progress](../progress/CAMPAIGN.md),
[the queue](../data/campaign.json), [existing PR status](../progress/STATUS.md),
and the most recent dated progress entry. The repository is the checkpoint;
temporary cloud files are working copies.

The initial [research snapshot](../data/campaign-sources.json) identifies 100
canonical upstream repositories in a current conditional reward scope. It does
not identify 100 available assignments. Task-specific policies, technical fit,
reward eligibility, and competing implementations still need checking.

## Execution model

| Responsibility | Default location | Evidence of completion |
| --- | --- | --- |
| Source review, implementation, tests and patch review | GPT cloud execution environment | Exact source revision, commands, results, limits and review record |
| Durable source, branch, queue and progress | Connected GitHub repositories | Read-back of published commit, PR or comment URL |
| Repeatable platform checks | Existing hosted CI permitted by the project | Actual jobs on the submitted revision; admission is separate |
| Resume the goal | Hosted Scheduled task, `Advance open-source contributions` | Enabled native task and actual run history |
| Private application evidence | Existing private workspace when needed | Private receipt; only a deliberately redacted public summary |
| Prepared public patch and review evidence | Deliberately selected branches in the contributor's fork | Immutable source and evidence commits, including remaining submission gates |
| Hardware-specific or local-only test | Suitable authorized machine or hosted runner | Test output from the actual required platform |

The PC is not a daily prerequisite for development or continuation. A fresh cloud
session checks out public source and restores the next action from GitHub.
Publishing into an external upstream still needs a connection that permits that
operation. Local paths, credentials, unsubmitted private patches, and application
forms stay out of this repository.
[Official scheduled-task guidance](https://learn.chatgpt.com/docs/automations)
explains that web tasks can use connected tools and saved context, but do not
retain a local folder or worktree between runs. A hosted task resumes bounded
sessions; it is not a continuously running private server.

## One useful run

1. Read the checkpoint and queue. Check the current default branch, preserve
   unfinished changes in an isolated branch, and resume an active task with a
   sound checkpoint before beginning another implementation.
2. Read new feedback and check results for existing submissions. Address a
   requested change or concrete failing test first. Follow up when there is a
   specific unresolved action, new evidence, or a maintainer question. Read the
   whole relevant thread immediately before posting and record the returned URL.
3. Advance one selected upstream change through reproduction, a focused fix,
   meaningful tests, policy review, and submission when required access and
   reviews are available. Claim only the platforms and checks actually run.
   Automated review never substitutes for required personal review.
4. If nothing is selected, screen the next few suitable targets: current problem,
   competing patches, license and contribution rules, expected outcome, feasible
   validation, accepted submission channel, and benefit conditions. Confirm
   selection for paid assignments. The current tracker counts GitHub upstream
   PRs. Keep targets using another process parked until that process can be
   handled and counted truthfully; do not submit to the wrong channel to satisfy
   a tracker. For example, [Linux's guide](https://docs.kernel.org/process/submitting-patches.html)
   directs patches to maintainers and mailing lists by email. The initial
   100-target pool can therefore need replacements as screening progresses.
   Limit a crowded unpaid investigation to 30 minutes, then park it if no distinct
   useful contribution emerges.
5. Publish the checkpoint and campaign record. Verify the remote result, run
   repository validation, and retain exact source and evidence references. An
   attempted tool call is not a confirmed submission.

Keep at most one main upstream implementation and one useful owned-tool change
active. Research and independent review can run in parallel. Test the actual
risks and required gates; do not rerun unchanged successful matrices or rebuild
the workbench instead of advancing upstream work.

Publish small permitted checkpoints after establishing a reproduction and after
obtaining a reviewable fix, before long validation. Record the exact base or
proposed revision, commands and outcomes already observed, remaining work, and a
verified recovery location. Preserve restricted material in an available durable
private destination. This reduces the work lost if a session is interrupted.

## Sustainable selection and effort

Prefer clear user impact, reproducible defects, small reviewable changes,
attainable validation, responsive maintainers, and credible benefit terms.
Existing feedback and accepted work approaching a reward checkpoint take
priority over speculative searches. Keep only a few fully screened tasks ahead
of the active implementation; the remaining targets are a backlog.

At each seven-day review checkpoint, compare actual submissions, acceptance,
review requests, measured effort, and realized benefits. Shift effort toward
projects with demonstrated useful outcomes. Unknown cost or effort is unknown,
not zero. Use the existing environment and permitted CI first; additional paid
infrastructure needs its own decision. Avoid a PR-per-day quota and preserve the
reasons unsuitable targets were parked.

## Follow-through and earnings

Keep submitted, accepted, granted, activated and paid states separate. Historical
submissions do not become new campaign work. Count each external project once
after its evidence-backed submitted milestone; later changes to that project
are follow-through. After 100 submissions, maintain the portfolio instead of
silently expanding the target.

The [Google Patch Rewards rules](https://github.com/google/bughunters/blob/main/bughunters/articles/about/rules/open-source/patch-rewards-program-rules.md)
require substantive qualifying work, upstream acceptance and a full unreverted
month before applying; awards are discretionary. Generic fixes and tests do not
automatically qualify. Reporting limits also prevent treating 100 projects as
100 immediate applications. Keep specific patch and participant eligibility
unverified until supported.

Recheck the existing libzip integration at or after
**2026-10-22T13:12:13Z**. Verify retention and terms before preparing the reward
submission. Assess CodeSupply before its recorded deadline only if project and
applicant fit can be supported. Preserve private application ownership and the
October 13/November 12 planning anchors. Pursue subscriptions or compute for an
actual workflow need; activated access is separate from cash. Record personal
learning only when the person reviews or practices the work.

## Access checks and blocked actions

On 2026-10-17 the GitHub connector read the hub and external PRs, and published
owned source and branches. It rejected the two external follow-up comments with
HTTP 403, `Resource not accessible by integration`. The earlier failure remains
documented in [the campaign-start checkpoint](../progress/2026-10-17-campaign-start.md).

Later in the same session, the already authorized PC GitHub CLI served as an
explicit publishing bridge. The
[npm CI-admission question](https://github.com/npm/cli/pull/9954#issuecomment-6241492647)
was posted at 21:35:40 UTC, and the
[libavif CLA-association question](https://github.com/AOMediaCodec/libavif/pull/3413#issuecomment-6241498834)
at 21:36:01 UTC. Both were read back through the cloud connector. Do not post
these drafts again. The underlying admission and CLA checks still need their
respective maintainers or administrators to act.

The bridge also created the public H2 fork because no fork-creation operation
was exposed by the cloud connector. The cloud connector then published the
reviewed four-file patch at
[`9d7a0ad`](https://github.com/agamal026/h2database/commit/9d7a0ad26f8a53654e0ce106a80f702ae5840a28)
on `fix/4456-any-parameter-types`. Creating a branch uses `create_branch`;
`update_ref` only moved an existing branch in this session. No credential was
copied from the PC. Future fully cloud-based upstream publication still needs
the relevant supported write capability; a successful owned-repository push
does not establish it.

The [H2 review draft](https://github.com/agamal026/h2database/pull/1) is in the
contributor's fork and receives no external-submission credit. Its complete
[evidence checkpoint](https://github.com/agamal026/h2database/blob/0feb07c57de0641cda13ad69de24ecf88fc4c917/contribution-review/4456/README.md)
is on `review/4456-evidence`. Recover the source commit and these text artifacts
from GitHub. Focused checks and automated review are complete; the final full
upstream suite, remaining build/documentation gates, and truthful contributor
statement remain unresolved. Keep this prepared work parked if a personal or
access dependency blocks it, and advance the next useful unblocked task.

Read access does not establish write access. When an action is forbidden,
preserve the tested patch or draft, record the blocked operation, and continue
unblocked work. Do not loop on the same failed mutation, extract a PC token,
change account permissions, or invent a successful submission. Entirely
cloud-based publication needs a supported, authorized connection with the
required write access. After an uncertain write, inspect canonical state before
retrying. Reconcile concurrent changes and use non-forced publication against
the expected previous commit.

## Schedule and notifications

The hosted task **Advance open-source contributions** was created and read back
as **enabled** at **2026-10-17T21:12:24Z**. It starts on **2026-10-18** and runs
daily in **Europe/Vienna**, with flexible scheduling around **08:00**. Its saved
prompt matches [the published continuation prompt](CONTINUATION-PROMPT.md).
The two existing project-tracker tasks were preserved. No scheduled execution
of this new task has occurred yet; check native run history for actual outcomes.
After editing a task, read back both its prompt and cadence and verify the
intended daily schedule. Updating instructions alone is not evidence that the
schedule remained unchanged.

The prompt reads current repository instructions, advances the strongest
unblocked contribution, and publishes evidence and the next action. Notify for
a submission, acceptance, confirmed benefit, material failure, or concrete
required user action. Keep unchanged routine checks quiet. Review the first few
runs against actual tool access, then adjust the queue or procedure using the
results. Do not create duplicate workers or modify the separate project tracker.

Pause or edit `Advance open-source contributions` in Scheduled to change future
runs. Cloud work and evidence recovery do not require an always-on PC or local
service. Unavailable publishing permissions remain explicit blockers, not a
reason to lose the patch or repeat the same forbidden call. The retired
dedicated bug-bounty project remains outside this campaign.
