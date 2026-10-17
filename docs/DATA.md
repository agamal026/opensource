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

## Snapshot provenance: `data/snapshot-source.json`

This companion record describes the exact bytes currently in `data/github.json`.
When promoting a reviewed snapshot, update both files in the same change. Record
the observation time, snapshot SHA-256, collection method, tool source revision,
runtime versions, and the relevant collection scope or limits. Link separate
validation evidence when available. The source revision identifies the code that
ran; it need not be the later commit that publishes its output.

`oss_status.py refresh` writes the snapshot only. Its schema validator checks the
catalog and snapshot, not this provenance record, so review the companion for
consistency before publication. Preserve historical source claims in Git and use
commit-specific links when describing an earlier observation. A current-file
link can change as new snapshots are promoted.

Keep unavailable fields distinct from observed values. The first REST observation
could not supply `review_decision`; a later GraphQL observation supplied some of
those values. This additional source coverage does not establish that the review
decisions themselves changed between collection times.

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

Workspace configuration rejects duplicate JSON keys at every object depth.
Configuration errors return exit code 2 before Git inspection. With a file
destination (`--output PATH`, where `PATH` is not `-`), the command preserves an
existing checkpoint file, creates no new output file, and writes a sanitized
error category to stderr. When `--output` is omitted or set to `-`, it emits
the diagnostic JSON on stdout. A valid configuration with an unavailable
checkout still writes its partial snapshot with `complete: false` and returns 1.

## Curated opportunities: `data/opportunities.json`

This separate, manually reviewed registry records current program terms and
opportunity assessments. See [the opportunity review](OPPORTUNITIES.md) for its
schema and source links. `oss_status.py` does not validate or refresh this file.
Keep advertised amounts separate from verified payments and activated services;
eligibility, selection, and outcomes require their own evidence. Public records
must not contain private application forms, payment details, or account receipts.
