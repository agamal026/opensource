# Prepared libavif #2428 contribution

Verified **2026-10-17**: the exact three-file patch remains local, uncommitted,
and unpublished. This page records its checkpoint without republishing the patch.

Issue: [AOMediaCodec/libavif #2428](https://github.com/AOMediaCodec/libavif/issues/2428).

## Scope and source

The prepared change tolerates an unsupported `pixi` item-property version while
retaining its `ipco` slot. Essential associations still make the affected item
unsupported. The ignored property is not exposed for accidental duplication on
re-encoding. The track sample-entry path still rejects the unsupported version.

The local package contains the parser change, GoogleTests, a 321-byte AVIF fixture,
and proposed PR text. Its base is `ab37e2946dfb6d2cc52886f39cb0fbf701db98e1`, a
retained local revision that must be compared with current upstream before submission.

All five current digests matched the retained review package on October 17:

| Artifact | SHA-256 |
| --- | --- |
| Complete review diff | `e1cb392cd170d80f45475c1cfdb6f908909391239fffed9956bb06b1cccd73d3` |
| Proposed PR text | `c5732ad2119254f5be70d459ea68e2ba16bb5107e75c3adbc52c871d94a420a0` |
| `src/read.c` | `17a044045130718868c0b4b5d4215f457dea153afab508defd50b68316ce7fce` |
| `tests/gtest/avifpixitest.cc` | `fbc73e5c81a112c2db1addcf8b09c3c73d0bd6c123b620bee63ce64d09430cc1` |
| `tests/data/unassociated_pixi_v1.avif` | `8842a658956d8aecf7b990c672ab113351d203d8f80affa2b311efd9fd97f8e2` |

## Retained validation

The October 15 package records clang-format 19 success and **51/51 configured
Linux CTest tests** passing against the final source hashes, with independent
source, suite-log, and PR-text review. Earlier receipts cover a 108-observation
parser matrix, 54-observation ASan/UBSan matrix, track controls, targeted tests,
and a codec-backed round trip.

Those earlier matrices preceded a formatting-only update. The package explains
their historical bindings and a byte-identical rebuilt parser archive. These
are bounded local results. The October 17 check verified source bindings; it
did **not** rerun the suite or establish all upstream CI configurations.

## Contributor's next step

Open `continuation/libavif-pixi-2428/review-package.md` in the original workspace.
Review the exact diff, fixture, tests, and PR text; flag or edit anything you
disagree with. Consider essential/non-essential properties, stable indexes,
malformed version-zero behavior, and strict required-`pixi` validation.

[AOMedia's policy](https://aomedia.org/about/legal/#contributions-in-the-context-of-ai-tools)
requires meaningful human review and oversight of AI-assisted contributions.
Agent review and prior review of a different patch do not establish personal
review of this submission. The existing workspace retains its commit, push, and
PR gate for this patch.

After that review, recheck exact source, upstream base, relevant validation, and
CLA state, then submit within authorization. Approval to publish this hub does
not establish personal review of the upstream patch.
