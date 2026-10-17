# Data conventions

## Curated registry: `data/catalog.json`

Schema version 1 has an owner, a baseline date, and three lists:

| List | Meaning |
| --- | --- |
| `projects` | Owned projects with descriptions, licenses, release and CI links. Identify prereleases in the description. |
| `contributions` | Upstream repository/PR coordinates, purpose, and notes preserved by automated refreshes. |
| `candidates` | Prepared or parked work with issue links, stage, and next action. These are not submitted PRs. |

IDs and coordinates must be unique. PR and issue URLs must match the repository
and number. Validation rejects unknown fields, duplicate JSON keys, invalid
dates/URLs, and malformed records instead of silently dropping data.

The `2026-10-13` baseline comes from the recovered project. It distinguishes
earlier history from subsequent observations; it is not a completion deadline.

## Observations: `data/github.json`

Schema version 1 records a UTC `observed_at` and one observation per registered
PR, including source URL, state, draft flag, update/merge dates, head/base
revisions, review decision, and the check rollup. It contains no PR body, comment
content, author identity, or token.

`CheckRun` and legacy `StatusContext` records are normalized separately. Failed,
pending, action-required, and unknown results remain visible. The check summary
is an observation, not an approval decision or a complete platform matrix.

Refreshes are transactional across registered PRs. A failure preserves the prior
output, so a partial refresh is never published as complete. A committed snapshot
can become stale; its timestamp remains visible in the generated report.

## Reports and checkpoints

Generate `progress/STATUS.md` with `tools/oss_status.py render`. Validate it with
`render --check` and an explicit output path. Rendering makes no network calls
and uses no changing clock value.

Observed merge dates may be grouped around the baseline. They do not establish
independent testing, funding, appointment as a maintainer, or external adoption.
Those claims need separate direct evidence.

Local mappings use `config/workspaces.example.json` as a model. Checkpoint
snapshots include only allowlisted Git-state fields and stay in `.local/` unless
deliberately reviewed for publication.
