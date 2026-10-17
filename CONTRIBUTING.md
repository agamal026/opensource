# Contributing

Start with an actionable issue, a reproducible defect, or a scoped improvement.
Explain the reason for the change, resulting behavior, and evidence exercising
the important failure path.

## Development

Python 3.10+ and Git are enough for the offline tests. No package installation is
required. Use a branch for ongoing work and retain unrelated edits.

```sh
python3 -m unittest discover -s tests -v
python3 tools/oss_status.py validate
python3 tools/oss_status.py render --output progress/STATUS.md --check
git diff --check
```

After changing curated data or a reviewed snapshot, regenerate the report:

```sh
python3 tools/oss_status.py render --output progress/STATUS.md
```

CI runs the offline suite and report validation on Linux with Python 3.10, 3.12,
and 3.14, and Windows with Python 3.12. Add meaningful regressions for new code
paths; prose-only edits need no implementation-mirroring tests. The workflow uses
pinned official GitHub actions and read-only repository permissions.

## Public records and skills

Use `data/catalog.json` for descriptions and notes; use `data/github.json` for
reviewed GitHub observations. Read [the conventions](docs/DATA.md) before changing
a schema. Keep a PR's merged state separate from partial work incorporated
outside the PR. Link actual maintainer evidence.

Keep skills concise and portable, with `name` and `description` in frontmatter.
Update matching `agents/openai.yaml` metadata when the workflow changes. Version
skills in Git with the tools and evidence they depend on.

## Review and publication

Inspect the staged diff and include only selected public files. Keep private
configuration and evidence local. Do not copy surrounding checkouts, reports,
keys, grant forms, or browser state into this repository.

Follow each external project's license, review, and AI-use rules. This hub's CI
cannot establish a human signature or personal review. Refreshes are deliberate
work-session actions; no timed task is installed here.

The original code and documentation here use MIT. Linked projects retain their
own licenses and contribution processes.
