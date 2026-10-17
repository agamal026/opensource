# Working in this repository

Use this hub to maintain original tools and accurate open-source contribution
records. Start every resumed session with [GOAL.md](GOAL.md),
[docs/OPPORTUNITIES.md](docs/OPPORTUNITIES.md), and the latest dated progress
entry. Then read `README.md`, `progress/STATUS.md`, and `docs/ROADMAP.md` before
continuing work. For the continuous 100-project campaign, also read
`docs/CLOUD-OPERATION.md`, `data/campaign.json`, and `progress/CAMPAIGN.md`.
The default executor is a fresh GPT cloud session; the connected PC is optional.

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
