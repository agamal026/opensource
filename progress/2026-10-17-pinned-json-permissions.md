# 2026-10-17 — pinned-json directory-permission fix

Published [pinned-json v0.1.1](https://github.com/agamal026/pinned-json/releases/tag/v0.1.1)
as an **alpha prerelease**, fixing a reproduced Linux directory-permission bug.
All 36 tests passed on the PC and in the
[three Python CI jobs](https://github.com/agamal026/pinned-json/actions/runs/39065995086).
The release includes a verified wheel, source distribution and checksums.
The [verification receipt](2026-10-17-pinned-json-permissions-verification.json)
records the exact sources, validation scope and asset hashes.

## The defect and change

A known, readable fixture could fail with `FILE_ACCESS_ERROR` when a directory
allowed search (execute) but denied listing. The
[previous implementation](https://github.com/agamal026/pinned-json/blob/ac03f31bfb157051d7b0bab366169a69eacd8779/src/pinned_json/core.py)
opened each directory for reading, unnecessarily requiring directory-listing
permission. Direct reads of the manifest and fixture still succeeded.

The [fix](https://github.com/agamal026/pinned-json/commit/93b9c46a324097a0cc43f16cbf31e16269e8139d)
uses `O_PATH` at both directory-opening sites while retaining
`O_DIRECTORY | O_NOFOLLOW | O_CLOEXEC`. Linux
[documents path descriptors](https://man7.org/linux/man-pages/man2/open.2.html)
for directory-relative operations without requiring read access to the directory.
The retained directory and no-follow flags continue rejecting symlink components.
Final files retain their read-only, no-follow, nonblocking open and regular-file
checks. Byte limits, digest verification and strict JSON validation are unchanged.

The six changed files cover the implementation, regressions, README, changelog,
provenance and version metadata. The project remains Linux-only and Alpha.
Material Codex assistance is disclosed in
[PROVENANCE.md](https://github.com/agamal026/pinned-json/blob/93b9c46a324097a0cc43f16cbf31e16269e8139d/PROVENANCE.md).

## Reproduction and validation

Three new cases cover an execute-only selected root, a root ancestor and a nested
fixture directory. With mode `0111`, ordinary reads of the known files succeeded
while listing the restricted directory raised `PermissionError`. Both cloud and
PC reproductions exposed the old implementation's rejection.

Two additional cases require rejection when directory search or fixture-read
permission is absent. The tests check library behavior, CLI exit codes, exact
successful output and sanitized errors with empty stdout on failure. Actual
filesystem operations establish whether permissions are enforced; tests explicitly
skip if privileges bypass them. Cleanup restores the original modes.

| Validation | Observed result |
| --- | --- |
| Five new regressions against baseline `ac03f31`, Linux/Python 3.12.14, UID 65534 | Three expected traversal errors; both access-denial guards passed; zero skips. |
| Complete fixed source suite, Linux/Python 3.12.14, UID 65534 | **36 passed; zero failures, errors or skips.** |
| Complete fixed source suite on the PC, Linux/Python 3.14.4, UID 1000 | **36 passed; zero failures, errors or skips.** |
| [Hosted CI](https://github.com/agamal026/pinned-json/actions/runs/39065995086), Python 3.10/3.12/3.14 | **36 passed in each job**, including all five permission cases; installed CLI example passed in each job. |
| Separate privileged invocation with permission bypass demonstrated | All five permission tests explicitly skipped. These are not counted as permission-validation passes. |
| Installed release wheel, Python 3.14.4 | `verify` exited 0 silently; `emit demo` exited 0 with exactly 273 original bytes and no stderr. |
| Downloaded release assets | Wheel, source distribution and checksum file exactly matched the local build outputs and GitHub asset digests. |

A separate agent reviewed all six edited files and found no concrete remaining
issue. This was static review; the reviewer did not rerun tests. The source
publication used the exact reviewed Git tree and an expected-parent update.

The first PC test runner omitted `PYTHONPATH` from CLI subprocesses; its import
failures were a runner setup error. The corrected runner passed with unchanged
package and test source. The first build-environment setup also stopped because
`ensurepip` was unavailable. Existing pip then managed isolated environments
through its documented `--python` option. Initial logs remain preserved locally;
the receipt distinguishes these attempts from the successful runs.

## Source and release identity

| Record | Exact value |
| --- | --- |
| Baseline | [`ac03f31bfb157051d7b0bab366169a69eacd8779`](https://github.com/agamal026/pinned-json/commit/ac03f31bfb157051d7b0bab366169a69eacd8779) |
| Published source and release tag target | [`93b9c46a324097a0cc43f16cbf31e16269e8139d`](https://github.com/agamal026/pinned-json/commit/93b9c46a324097a0cc43f16cbf31e16269e8139d) |
| Published tree | `342f5271800441d47296fcd0aa0ec78c7d2f2a46` |
| Complete prepublication patch SHA-256 | `aee2890b2b84be785ab1c9b7118b8c85a1005e49a4b69a97cd760cd2a7839dd7` |
| Core source SHA-256 | `aed8713f7f953f089e7208e1f8f4e38fb9ef32c4fcafc26a429029459500bde8` |
| Test source SHA-256 | `e878d6dbbb387c15e19b2f76a736f3aeeecae325f80f3526f5b55e2c06eaa880` |

The PC build used Python 3.14.4 and `build` 1.6.1. It created the source
distribution, built the wheel from that distribution, and installed the wheel
in a fresh isolated environment. Archive contents were inspected; package core
bytes matched the reviewed source, as did the source distribution's tests.
The cloud and PC suites exercised source checkouts. Hosted CI installed the
package before its full suite. The separately attached release wheel was checked
with the documented CLI example.

| Release asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `pinned_json-0.1.1-py3-none-any.whl` | 8,643 | `a8c88b9d982e6e70ac4f621eed954e9833c06d5ba0e7373fc5f16e8a0c9bee36` |
| `pinned_json-0.1.1.tar.gz` | 11,148 | `9bdfd5c87bd9b8b26b5a02ac73c9bd3f96abf1c73970deeaa92e6c323f7485d0` |
| `SHA256SUMS` | 192 | `c1fc291e15bcb3e4220fd6f60b5bb47da2776825a4f50c18b9a64b4db55f5739` |

The release was published at **20:19:57 UTC**. Download verification completed
at **20:21:33 UTC**. The canonical PC checkout advanced cleanly to the same
published source at **20:20:30 UTC**.

## Upstream status and opportunity selection

A fresh live CLI snapshot at **2026-10-17T20:01:04Z** returned the same six complete
PR observations and 70 check contexts as the earlier 18:22:53Z snapshot. Only the
observation timestamp changed. The exact promoted bytes and collection scope are
recorded in [snapshot provenance](../data/snapshot-source.json); the
[generated status](STATUS.md) retains failed, pending and unavailable results.
The accompanying upstream discussion review found no new substantive feedback
requiring a source change in this session.

The hub passed all **51 offline tests**, catalog validation, generated-report
consistency and whitespace checks before publication. No hub tool or skill code
changed in this update.

The bounded paid-assignment screen did not identify a suitable selectable task.
The [existing opportunity review](../docs/OPPORTUNITIES.md) remains a separate
dated assessment. This permission fix was the selected owned-project improvement.
No new cash payment, subscription, compute-credit allocation, external adoption
or external merge is confirmed by this work.

## Continuation

The release demonstrates directory-relative file access and regressions that
detect privilege bypass. Personal learning has not been assessed; a useful
practice exercise is to reproduce the three permission cases and explain why
`O_PATH` still needs the retained directory and no-follow flags.

Continue with a currently selectable paid issue or new concrete project feedback.
The earliest existing libzip retention checkpoint remains
**2026-10-22T13:12:13Z**; eligibility and payment remain unverified.
Prepared libavif #2428 retains its
[personal contributor-review requirement](../docs/LIBAVIF-2428-REVIEW.md).
This session added no background worker or scheduled automation.
