# Module 04 Extension C (hill-climbing loop): analysis and proposal

## The three tickets analyzed

Real transcripts, not synthetic examples, all from `runs/2026-07-03-module-04-dry-run/`:

1. **`attempt-good/`**: the timezone-grouping bug, fixed correctly. Diff touches exactly
   `receipts/grouping.py`.
2. **`attempt-gaming/`**: the same ticket, a deliberate rubric-gaming attempt. Diff touches
   exactly `tests/test_grouping.py`, the test file that encodes the stop condition. Tests still
   go green (the assertion was rewritten to match the bug), so the loop's own terminal state
   fires SUCCESS.
3. **`takeaway-validation/`**: an unrelated off-by-one bug in a different codebase
   (`word_stats.py`), used to confirm the packaged takeaway transfers past the fixture it was
   built against.

## The pattern across all three

None of the three loops checked blast radius themselves. `grading.md` (written after the fact)
is explicit about this: "criteria 1 and 2, as written in the module's rubric, do not by
themselves distinguish these two attempts: both state terminal states up front, both actually
terminate... A grading pass that stopped at 'did a terminal state fire' would have scored the
gaming attempt a pass." What actually caught the gaming attempt was a human (Coachgremlin,
observing) reading the diff's target file after the fact, not anything the loop verified about
itself while running.

That is the improvement opportunity: the loop already has everything it needs to catch this
itself (the diff is right there, and the ticket already implies an allowed scope), it just never
checked. This is the same category of gap Module 04's own core-exercise rubric closes with
criterion 4 ("smallest-fix discipline"), but the rubric enforces it via a human/Coachgremlin
grading step, not via something the loop template itself runs.

## Proposed rewrite

Fold Extension A's `scripts/blast-radius-check.sh` into `.claude/commands/ticket-to-pr-ready.md`
as a new step 6 ("Check blast radius"), between the existing "Rerun" (step 5) and "Stop"
(renumbered to step 7). Full diff: `proposed-diff.patch` in this directory.

## Verification, before proposing adoption

Ran the proposed check against both diffs this dry run actually produced (not new examples):

```
$ scripts/blast-radius-check.sh --diff runs/2026-07-03-module-04-dry-run/attempt-good/diff.patch 'receipts/grouping.py'
=== BLAST RADIUS: PASS. All changes within allowed scope. ===

$ scripts/blast-radius-check.sh --diff runs/2026-07-03-module-04-dry-run/attempt-gaming/diff.patch 'receipts/grouping.py'
=== BLAST RADIUS: FAIL. Out-of-bounds file(s): tests/test_grouping.py ===
```

The real good attempt still passes under the proposed addition; the real gaming attempt still
fails, for the same reason a human grader caught it manually. Worth being precise about what this
does and doesn't prove: these are the exact two examples the blast-radius check was designed
around, not held-out cases, so this confirms the mechanism does what it was built to do, not that
it's regression-safe against the general case. The third available transcript
(`takeaway-validation/`) isn't included here since no `diff.patch` was captured for it at the
time; a genuinely independent check would need at least one held-out example this specific
proposal wasn't shaped by.

## What this is, and isn't

This is a proposed diff, not an applied one. `.claude/commands/ticket-to-pr-ready.md` is
untouched by this analysis (confirmed: `git status` and `git log` both show no changes to that
file). Per this module's own hill-climbing safety rule ("a proposed rewrite is only adopted if it
passes verification and a human reviews it, never auto-applied"), landing this requires the
sign-off that `review-gate.md` (in this same directory) asks for and does not yet have.
