---
name: resume-open-source
description: Resume an open-source workspace from its actual Git state and dated evidence, advance an unblocked tool or upstream contribution, and record a verified handoff. Use when continuing interrupted work, reconciling local changes with published PRs, refreshing this workbench, or preparing a contribution for review.
---

# Resume open-source work

## Recover the checkpoint

1. Locate the repository and read its applicable `AGENTS.md`, README, latest
   progress entry, and active plan. In this workbench, read
   `progress/STATUS.md`, `docs/ROADMAP.md`, and `docs/CONTINUING.md`.
2. Confirm the actual execution host and workspace. A connected PC and a cloud
   shell are different environments. Use the user's requested connection when
   available; never infer that local files are mounted in a remote runtime.
3. Inspect branches, HEADs, and dirty state before editing. Run the workbench's
   checkpoint tool from its repository root when available:

   ```sh
   python3 tools/workspace_snapshot.py --config .local/workspaces.json --output .local/workspace-state.json
   ```

   Read relevant diffs in their actual checkouts before changing code. Check for
   another active worker before modifying a shared plan or worktree. Preserve
   unrelated edits and historical receipts; use an isolated worktree when useful.
4. Reconcile published state using a current read-only GitHub observation:

   ```sh
   python3 tools/oss_status.py refresh
   python3 tools/oss_status.py validate --snapshot .local/github.json
   python3 tools/oss_status.py render --snapshot .local/github.json
   ```

   Inspect material changes against the tracked snapshot. Failed queries and
   unavailable checks remain unknown. A PR being mergeable, an owned release,
   and an accepted external contribution are separate facts.

## Advance one useful task

Choose the highest-priority unblocked item from the recovered plan. Prefer actual
maintainer feedback, a reproduced defect, or an agreed deliverable. Keep the
workspace's existing limit on simultaneous new patches. Do useful preparation
while an external dependency is pending; avoid repeated status polling.

Read the upstream contribution rules before submitting there. Complete the exact
change, focused regression, relevant existing suite, and reviewable PR draft
within the user's authorization. Record validation scope and source revision.
Do not treat agent review as a contributor's required personal review or legal
signature. If that step is missing, prepare the concrete review package, name
the applicable requirement, and continue other authorized work.

## Publish and hand off

Keep machine paths, credentials, private reports, application forms, research
data, and unpublished patch content outside this public hub. Review the actual
staged files. Link canonical repositories instead of copying their worktrees.

Use current authorization for publication; do not ask again for routine
reversible work. Do not let a read-only refresh send messages, submit PRs, or
install schedules as a side effect.

Validate the catalog and regenerated report using `CONTRIBUTING.md`. Commit and
push only the intended work. Confirm the remote revision and actual CI result;
retain an explicit pending state if a required job has not run.

Add a dated progress entry with the result, why it matters, exact source links,
and verification performed this session. Identify reused historical evidence by
its original date and scope. Leave the next executable action and any dependency.

Do not claim an upstream merge, activated funding, adoption, or comprehensive
platform coverage from a local test or an owned-project release.
