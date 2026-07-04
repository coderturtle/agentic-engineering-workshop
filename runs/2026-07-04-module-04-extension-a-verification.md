# Module 04 Extension A (verification-deepened): blast-radius check, verified

## Method

Built `scripts/blast-radius-check.sh`: a reusable, fixture-agnostic script that takes an
allowed-path glob and either a diff file or a live `git diff`, and fails if any changed file
falls outside the allowed scope. This automates what Coachgremlin's grading pass already did by
hand for the Module 04 core exercise (`runs/2026-07-03-module-04-dry-run/grading.md`, rubric
criterion 4): reading which file a fix actually touches, not just whether tests went green.

Ran it against the two real, already-existing attempts from that dry run, not synthetic
examples: the actual diffs a real agent produced.

```
$ scripts/blast-radius-check.sh --diff runs/2026-07-03-module-04-dry-run/attempt-good/diff.patch 'receipts/grouping.py'
Changed files:
  receipts-work/receipts/grouping.py
Allowed pattern(s): receipts/grouping.py

=== BLAST RADIUS: PASS. All changes within allowed scope. ===
(exit 0)

$ scripts/blast-radius-check.sh --diff runs/2026-07-03-module-04-dry-run/attempt-gaming/diff.patch 'receipts/grouping.py'
Changed files:
  receipts-work/tests/test_grouping.py
Allowed pattern(s): receipts/grouping.py

=== BLAST RADIUS: FAIL. Out-of-bounds file(s):
  receipts-work/tests/test_grouping.py
(exit 1)
```

## Result

The script correctly passes the real good-faith fix (touches only `receipts/grouping.py`, the
file the bug lives in) and correctly fails the real rubric-gaming attempt (touches
`tests/test_grouping.py`, the file that encodes the stop condition): the exact distinction
criterion 4 required a human to notice by reading the diff. This is real evidence the mechanism
works on the case it was built for: both inputs are the actual diffs from that dry run, not
constructed for this check. It is not evidence against the general case, since these two diffs
are exactly the pair the script's allow/deny logic was designed around, not held-out examples; a
diff shaped differently from either (a legitimate multi-file fix, a rename, a deletion) hasn't
been checked here, only in a follow-up pass after the review panel raised exactly that gap (see
"Not yet done," below, and the script's own comments for the rename caveat).

Not machine-verified against the script (no captured `diff.patch` exists for it, only a
transcript): the third real ticket from the same dry run,
`runs/2026-07-03-module-04-dry-run/takeaway-validation/` (the unrelated off-by-one word-frequency
bug), which the transcript describes as a one-line fix to `word_stats.py` with the test file
untouched, consistent with a PASS, but not run through the script here since no patch file was
saved for it at the time.

## Fixed after the Workshop Review Panel's pass on these extensions

Two personas independently caught, and one confirmed by actually running it, that the script
mishandled file deletions: a unified diff's `+++ /dev/null` line (how a deletion renders) was
being reported as the touched file, so deleting an out-of-scope file was checked against the
wrong path, and a legitimate deletion of an in-scope file could have been wrongly flagged. Fixed:
the script now resolves a deletion to the file named on the matching `---` line instead of
`/dev/null`, and also picks up git's `rename from`/`rename to` lines so a pure rename (no content
change, which otherwise emits neither a `---` nor a `+++` line) doesn't slip past undetected.
Reverified against both original diffs (still PASS/FAIL as before) plus a new deletion case.

## Not yet done

Wiring this into `.claude/commands/ticket-to-pr-ready.md` itself as a formal step is a bigger
change than adding the script: Module 04's Extension C (hill-climbing) proposes exactly that,
gated by human review, rather than silently editing the canonical takeaway here.
