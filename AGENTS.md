# Working in this repository

Use this hub to maintain original tools and accurate open-source contribution
records. Resolve the current handoff from [data/continuation.json](data/continuation.json)
instead of guessing from progress filenames. Start every resumed session with [GOAL.md](GOAL.md),
[docs/OPPORTUNITIES.md](docs/OPPORTUNITIES.md), and the latest dated progress
entry. Then read `README.md`, `progress/STATUS.md`, and `docs/ROADMAP.md` before
continuing work. For the continuous 100-project campaign, also read
`docs/CLOUD-OPERATION.md`, `data/campaign.json`, and `progress/CAMPAIGN.md`.
The default executor is a fresh GPT cloud session; the connected PC is optional.

## Recovery and connection checks

Recover the current private handoff from its latest Library metadata when that
handoff is supplied. Read the exact returned backing file and version; a bare
alias or an older conversation copy is not proof of the latest saved state.
Keep private identifiers and recovery records out of this public repository.

Discover the required connector action in the current session. If filtered
lookup finds nothing, inspect the full connector action catalog once before
reporting an action as unavailable. Do not carry an earlier session's tool list
forward as current, or hard-code an expected action count.

Treat these as separate observations: authenticated account, readable resource,
available write action, successful owned-repository write, authorized upstream
publication, browser context, and scheduled execution. None proves all the others.
A browser-context failure does not require abandoning working connector actions
or asking the user to sign in again. A discovered write action is not evidence
that its provider will authorize the operation.

Use the next substantive authorized operation, not a disposable permission probe.
On a real access, approval, or safety gate, stop that operation and preserve its
exact target, action, result, and resumption condition. Do not retry it through
another provider, browser, machine, credential, head, or wrapper to bypass the
gate. Continue independently permitted work; do not reset connections, broaden
permissions, repeat successful tests, or create more handoff packets by default.

For a scheduled task, match the result to its run ID and timestamps before
reporting its outcome. An empty result requiring user action is not success.
Do not repeatedly enable a paused task or claim that a prompt or connection
change repairs recurrence without actual execution evidence.

## Work selection

Use the goal and opportunity evidence to choose the next useful task. Keep at
most one main upstream implementation and one owned-tool improvement active.
Verify that paid work is selectable before implementation, and timebox crowded
unpaid proposal investigations as described in `GOAL.md`.

## Source and validation

- Keep reusable code in `tools/` and its meaningful offline regressions in `tests/`.
- Treat `data/catalog.json` as curated context and `data/github.json` as a dated
  observation. Refreshing observations must not erase contributor notes.
- Generate `progress/STATUS.md` with `tools/oss_status.py`; do not hand-edit it.
- Run the commands in `CONTRIBUTING.md` before publishing a change.
- Record the exact source revision, validation scope, and remaining dependency
  when handing work to another session. Preserve historical evidence.
- Make a durable checkpoint after a reproduction and after a reviewable fix,
  before starting long validation. Keep incomplete checks explicit and respect
  the publication scope below; an end-of-session note is not the only checkpoint.

## Publication scope

Track only deliberately selected public records. Local workspace mappings and
working snapshots belong in `.local/`. Inspect the staged diff before a commit;
an ignore file is not a substitute for reviewing the actual files.

Do not import surrounding checkouts, private reports, grant forms, credentials,
browser state, research data, or unpublished third-party patch content into this
hub. Link canonical upstream repositories and existing public evidence.

## Contribution accounting

Keep owned-project releases, external upstream contributions, and prepared local
patches distinct. A successful check does not establish maintainer acceptance.
Report check failures, pending admission, and unavailable results explicitly.
Count an external merge from its actual upstream merge evidence; claims of
independent validation need their own evidence.

Keep advertised benefits, verified eligibility, applications, grants, activated
access, and payments distinct. Record human learning only when the contributor
personally reviews or practices the work; agent output alone cannot establish it.

Respect each upstream's current contribution policy, including personal human
review and legal signatures when required. Additional automated review cannot
establish that a person reviewed a submission. Make any needed review concrete
without inventing permission gates for already authorized routine work.

This repository's tools read Git and GitHub state. They must not merge, push,
submit comments, purchase services, or install scheduled jobs as a side effect.
