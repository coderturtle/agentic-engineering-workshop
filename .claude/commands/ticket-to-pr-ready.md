---
description: Run a bounded Ticket-to-PR-Ready loop against a reproducible bug
---

# Ticket-to-PR-Ready loop

A bounded, verification-first loop for turning a bug report into a reviewable fix. This is the takeaway from Terminal Velocity's Module 04 (loop engineering) core exercise, generalized past the `receipts` fixture it was built against.

It exists because "the tests pass now" and "the bug is fixed" are different claims, and it is astonishingly easy to produce the first one without the second.

State both terminal states before starting, out loud, in the conversation:

- **Success:** the check(s) named in the ticket pass, and no test file was modified to get there.
- **Failure:** after two genuine reproduce/root-cause attempts, the bug still cannot be reproduced or localized. Stop here; do not keep guessing.

## Steps

1. **Classify the ticket.** One sentence: is this a stable goal (one function, one described bug, a fixed spec to check against) or a moving target (an open-ended "make it better" ask with no fixed done-state)? Only loop-ify stable goals. If it is a moving target, say so and stop; this loop is the wrong tool for it.
2. **Reproduce.** Run the failing check named in the ticket. Confirm the same failure it describes, not a different one.
3. **Root-cause.** Read the code path the failing check exercises. State the mechanism in a sentence or two: not "the check fails" but why.
4. **Smallest fix.** Change only what the root cause requires. Two things are always out of bounds: (a) any test file that encodes the stop condition, (b) code unrelated to the diagnosed mechanism. If the diff touches either, it is not a fix, it is moving the goalposts.
5. **Rerun.** Run the full check suite, not just the one that was failing. Trust its result over a read of the diff.
6. **Stop.** Green: state success, stop. Red after two smallest-fix attempts: state the failure terminal explicitly, stop. Do not keep iterating past the bound.

## Why the test-file rule (step 4) exists

A loop that edits the check instead of the code under test will always terminate "successfully." Of course it will; you told it what answer to get. That is not verification, it is the loop grading its own homework and giving itself an A. External verification means the check sits outside the loop's own reach to modify, structurally, not just by convention, not just because the instructions asked nicely. See `runs/2026-07-03-module-04-dry-run/grading.md` for the concrete gaming attempt this rule was written to close: someone, or something, actually tried it, and it very nearly worked.

## Provenance

Built and validated against two unrelated bugs during Coachgremlin's first real dry run (`docs/coachgremlin-implementation-plan.md` §5): the `receipts` fixture's timezone-grouping bug, and a second, unrelated off-by-one bug used only to confirm the template transfers. See `runs/2026-07-03-module-04-dry-run/` for both. The loop harness that ran the first attempt also shipped its own bug on the first try, a `pipefail` interaction that quietly reported a real, reproduced failure as "could not reproduce." A loop-engineering exercise breaking its own loop before teaching anyone else to build one is either deeply embarrassing or exactly on brand; this workshop has decided to call it the latter.
