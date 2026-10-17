# Open-source workbench

Tools, reusable skills, progress, and contributions maintained by
[@agamal026](https://github.com/agamal026).

The [goal](GOAL.md) is to pursue useful open-source work with a documented route
to financial benefits, subscriptions, or compute credits while improving skills,
workflows, and tools. Advertised benefits, eligibility, and realized outcomes are
tracked separately.

The current campaign aims for **100 distinct external projects with validated
work submitted**, followed by review, maintenance, and benefit follow-through.
See the [campaign progress](progress/CAMPAIGN.md), [source-backed queue](data/campaign.json),
and [cloud operating procedure](docs/CLOUD-OPERATION.md). GPT cloud sessions are
the default executor; GitHub provides durable state between sessions.

This repository makes it practical to resume work from a verifiable checkpoint:
inspect the current local checkouts, refresh public pull-request observations,
and carry the next useful change through validation. It also indexes the original
projects and upstream work already in progress.

**Start every resumed session with [the goal](GOAL.md),
[opportunity notes](docs/OPPORTUNITIES.md), and the latest dated entry in
[progress](progress/).** Then read [current status](progress/STATUS.md), the
[roadmap](docs/ROADMAP.md), and the [continuation guide](docs/CONTINUING.md).

## Tools in this repository

| Tool | Purpose |
| --- | --- |
| [oss_status.py](tools/oss_status.py) | Validate the public registry, read current PR/check results through GitHub CLI, and generate a reproducible Markdown status report. |
| [workspace_snapshot.py](tools/workspace_snapshot.py) | Record local Git branches, revisions, and change counts without copying paths, filenames, diffs, remote URLs, or credentials into the output. |
| [contribution_campaign.py](tools/contribution_campaign.py) | Validate evidence for the 100-project campaign and report researched targets, qualified submissions, acceptance, historical work, and realized benefits separately. |
| [resume-open-source](skills/resume-open-source/SKILL.md) | Reusable agent workflow for recovering a checkpoint, choosing an unblocked task, verifying it, and writing a useful handoff. |

Python **3.10 or newer** is required. The tools have no Python package
dependencies. Local snapshots also require Git; live PR refreshes require an
authenticated [GitHub CLI](https://cli.github.com/).

```sh
git clone https://github.com/agamal026/opensource.git
cd opensource
python3 -m unittest discover -s tests -v
python3 tools/oss_status.py validate
python3 tools/oss_status.py render --output progress/STATUS.md --check
```

On Windows, use `python` or `py -3` if `python3` is not available.

### Refresh public contribution status

```sh
python3 tools/oss_status.py refresh
python3 tools/oss_status.py validate --snapshot .local/github.json
python3 tools/oss_status.py render --snapshot .local/github.json
```

The refresh writes an ignored local candidate snapshot. Review it before replacing
the tracked snapshot. See the [continuation guide](docs/CONTINUING.md) for the
publication commands and failure behavior. Refreshing makes read-only GitHub
queries; it does not submit or change a pull request.

### Inspect local workspaces

Copy [config/workspaces.example.json](config/workspaces.example.json) to
`.local/workspaces.json` and replace its example paths with your checkout paths.
Then run:

```sh
python3 tools/workspace_snapshot.py --config .local/workspaces.json --output .local/workspace-state.json
```

Paths are resolved relative to the configuration file, and `~` expands to your
home directory. The output records counts and revisions, including detached HEADs
and unavailable checkouts. Keep the configuration local.

## Original projects

| Project | Released work | Validation evidence |
| --- | --- | --- |
| [pinned-json](https://github.com/agamal026/pinned-json) | [v0.1.1 alpha prerelease](https://github.com/agamal026/pinned-json/releases/tag/v0.1.1): offline exact-byte JSON fixtures; fixes traversal through directories without listing permission. Python 3.10+ on Linux. | [36 offline tests and the documented example](https://github.com/agamal026/pinned-json/actions/runs/39065995086), Python 3.10/3.12/3.14. |
| [raydium-cpmm-arb-monitor](https://github.com/agamal026/raydium-cpmm-arb-monitor) | [v0.1.1](https://github.com/agamal026/raydium-cpmm-arb-monitor/releases/tag/v0.1.1): read-only CPMM pool monitoring; fixes response-body timeouts. Node 22+. | [11 offline tests](https://github.com/agamal026/raydium-cpmm-arb-monitor/actions/runs/38885587743), Node 22/24 on Linux and Windows. |

These projects retain their own source repositories and MIT licenses. The monitor
does not execute trades; its offline tests make no profitability claim. A release
of an owned project is recorded separately from an external upstream merge.

## Upstream contributions

The registry tracks existing PRs to **libavif, libzip, npm, nginx, and libevent**,
plus the prepared libavif `pixi` contribution and parked Xcode investigation.
[Current status](progress/STATUS.md) links each upstream record and its observed
checks. Dates are snapshots, not a promise of continuous monitoring.

The prepared `pixi` patch remains in its original local worktree. Its contributor
must personally review the exact code, fixture, tests, and PR text before
submission under [AOMedia's contribution policy](https://aomedia.org/about/legal/).
The [review guide](docs/LIBAVIF-2428-REVIEW.md) records the scope and retained
evidence without republishing the patch.

## Repository map

| Directory | Contents |
| --- | --- |
| `tools/`, `tests/` | Executable tools and offline regression tests. |
| `skills/` | Versioned workflow skills; read the skill file directly or install it in your agent's skill directory. |
| `data/` | Curated public project/PR registry and reviewed GitHub observation snapshot. |
| `progress/` | Generated status and dated work logs. |
| `docs/` | Opportunity screening, continuation, improvement roadmap, and contribution review guidance. |
| `config/` | Portable examples without machine-specific configuration. |
| `.local/` | Ignored working configuration and candidate observations. |

See [CONTRIBUTING.md](CONTRIBUTING.md) for validation and change conventions.
The original tools and documentation in this hub are [MIT licensed](LICENSE).
