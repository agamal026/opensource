# Continue a work session

## Recover current state

Read `AGENTS.md`, [the goal](../GOAL.md), [the opportunity review](OPPORTUNITIES.md),
the latest entry in `progress/`, and the roadmap. Locate the
actual worktree instead of assuming that a cloud terminal contains the PC's
files. If reconnecting over Tailscale, confirm the intended host and existing
authenticated access. Keep connection details in local configuration.

Initialize local configuration only if it is absent; existing checkout mappings
are preserved:

```sh
python3 -c "from pathlib import Path
destination = Path('.local/workspaces.json')
destination.parent.mkdir(exist_ok=True)
try:
    with destination.open('xb') as output:
        output.write(Path('config/workspaces.example.json').read_bytes())
except FileExistsError:
    pass"
```

For a new configuration, edit the example checkout paths. Then record the
relevant checkout states with the local checkpoint tool:

```sh
python3 tools/workspace_snapshot.py --config .local/workspaces.json --output .local/workspace-state.json
```

The output contains labels, branches, revisions, and change counts. It excludes
paths, remote URLs, filenames, diffs, and Git identity. It is a checkpoint, not a
backup: inspect relevant local diffs before changing them. Review labels before
sharing a snapshot. Partial results have `complete: false` and a nonzero exit code.

Duplicate keys, malformed JSON, and other configuration errors return 2 before
Git inspection. When writing to a file, these errors leave the previous
checkpoint intact and print a sanitized category to stderr. Check the command's
exit status and the snapshot timestamp before using an existing output: a
preserved file describes the earlier successful attempt.

## Refresh upstream observations

Use an existing authenticated GitHub CLI session. The refresh queries the
explicit PR coordinates in the public catalog.

```sh
python3 tools/oss_status.py refresh
python3 tools/oss_status.py validate --snapshot .local/github.json
python3 tools/oss_status.py render --snapshot .local/github.json
git diff --no-index data/github.json .local/github.json
```

`git diff --no-index` returns 1 when it finds differences. Review substantive
state and check changes, including workflow admission and CLA results. Read the
upstream discussion if new feedback needs action; the snapshot contains no
comment bodies.

The refresh writes only after every registered PR is retrieved and validated.
A failed query leaves the previous output file intact. It traverses check-context
pages and rejects changed PR metadata, inconsistent counts, repeated checks or
cursors, and incomplete pagination. It aborts above 10,000 contexts instead of
truncating them. Empty or unknown checks must not be described as passed. The
returned rollup does not prove that every possible workflow or platform ran.

After reviewing the candidate, promote those exact bytes:

```sh
python3 -c 'from pathlib import Path; Path("data/github.json").write_bytes(Path(".local/github.json").read_bytes())'
```

Update `data/snapshot-source.json` in the same change. Record the promoted
snapshot's `observed_at` and SHA-256, the actual collection method, tool source
revision and runtime versions, and any collection limits or unavailable fields.
Keep those facts tied to the run that produced the promoted bytes. A refresh
changes the snapshot only; it does not update its companion provenance. Do not
leave REST collection claims attached to a snapshot produced by GraphQL.

Preserve earlier observations and provenance through commit-specific links in
the dated progress log. See [the data conventions](DATA.md) for the distinction
between the current snapshot and historical evidence. Then regenerate and check:

```sh
python3 tools/oss_status.py validate
python3 tools/oss_status.py render --output progress/STATUS.md
python3 tools/oss_status.py render --output progress/STATUS.md --check
```

The refresh uses [`gh api graphql`](https://cli.github.com/manual/gh_api) with
read-only queries. GitHub's GraphQL references document the
[pull request fields](https://docs.github.com/en/graphql/reference/pulls#pullrequest),
[commit check rollup and status contexts](https://docs.github.com/en/graphql/reference/commits#statuscheckrollup),
and [check run fields](https://docs.github.com/en/graphql/reference/checks#checkrun)
used by the command.

## Advance and publish

Follow [the roadmap](ROADMAP.md). Prioritize actual feedback and reproduced
defects. Preserve the active libavif patch until the personal review described in
[its review guide](LIBAVIF-2428-REVIEW.md) is complete.

For code changes, retain a reproduction, implement a focused fix, and test its
real risks. Historical receipts stay bound to their original sources and dates.
Distinguish verifying receipt hashes from rerunning the tests.

Run `CONTRIBUTING.md` validation, add a dated log, and inspect the staged diff.
Push within current authorization, verify the remote commit, and inspect hosted
CI before describing it as successful. Record owned releases and upstream merges
separately. Keep private application records in their original workspace.

Leave a handoff identifying what changed, what was actually tested, what remains
blocked, and the next concrete action. Preserve older evidence.
