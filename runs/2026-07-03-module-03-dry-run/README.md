# Module 03 verification: sub-agent scope + reset-and-resume, run for real

## Method

Added the module's actual target to the canonical fixture: `group_expenses_by_category` (stubbed, `NotImplementedError`) in `receipts/grouping.py`, plus a pre-written failing test file `tests/test_by_category.py` covering both the function directly and the not-yet-existing `--by-category` CLI flag. Confirmed both new tests fail before any work starts, independent of the pre-existing (Module 04) seeded bug elsewhere in the suite.

Defined a bounded sub-agent, `.claude/agents/receipts-category-summary.md`: scope is `receipts/` plus running only `tests/test_by_category.py` (explicitly not the full suite, since it has an unrelated known failure), with a required persistent-state file (`.receipts-category-progress.md`) it must check first and update after each step.

Ran it in two genuinely separate phases, not narrated:

- **Phase 1** (fresh subagent, no memory of anything before it): instructed to implement only `group_expenses_by_category`, stop before touching `receipts/cli.py`, and write progress notes. Verified independently afterward: `receipts/cli.py` byte-identical to the untouched original, the function test passing, the CLI test still failing exactly as expected (the flag doesn't exist yet).
- **Context reset**: phase 1's agent instance ends. No conversation history carries over.
- **Phase 2** (a new fresh subagent, zero memory of phase 1): given no task description beyond "read `.receipts-category-progress.md` and resume." It read the file, wired the CLI flag exactly as the notes described, reran the verification command, and marked the file done.

## Result

Both tests pass. `receipts/cli.py`'s default (no-flag) behavior is unbroken. The full diff (`final-diff.patch`) touches exactly two files, both under `receipts/`: `grouping.py` (the new function) and `cli.py` (the flag and dispatch). Nothing outside `receipts/` was touched by either phase.

## What this validates

- Rubric criterion 1 (bounded reach): both phases stayed inside `receipts/`; verification was scoped to the one relevant test file, not the whole suite.
- Rubric criterion 2 (sub-agent boundary): one named specialist, one stated responsibility, defined once and reused across both phases.
- Rubric criterion 4 (actually ran, gate): every step above is a real subagent run with a real, independently re-verified result, not a described one.
- Rubric criterion 6 (reusable generality): the sub-agent definition doesn't hardcode a fixture-specific absolute path; it's already close to drop-in for a real project with `receipts/`-shaped scope.

Not exercised in this pass: rubric criterion 5 (worktree isolation) is conditional and wasn't used here, a plain isolated directory was sufficient to demonstrate the required mechanism. Noted as optional in the module content, with a pointer to how a learner could add it.

## Negative control: does phase 2 actually need the notes file?

Added after the Workshop Review Panel's Module 03 content review (`docs/review-panel/2026-07-03-module-03-content.md`): the AI/ML Practitioner, Skeptical Critic, and End-User/Learner personas independently flagged the same gap. The original claim above ("phase 2 completed the task correctly using only the on-disk notes file... the hardest criterion to fake") was true as stated, but untested against the actual question: could phase 2 have succeeded *without* the notes file? If yes, the notes file wasn't load-bearing, it was just present.

**Method:** reconstructed the exact phase-1-complete checkpoint (function implemented, `cli.py` untouched, verified byte-identical to the real phase 1's output) in a fresh working copy, `negative-control/without-notes/`, deliberately *without* `.receipts-category-progress.md`. Ran a fresh subagent with the same sub-agent definition and the same "this is a resumed task, a reset happened" framing, with no notes file present to read.

**Result: it also succeeded.** The subagent found no notes file, then read `receipts/grouping.py` (already correct), read `receipts/cli.py` (no `--by-category` flag), read the test file to confirm expected behavior, ran the verification command to see exactly which test failed and why, and wired the flag correctly. Same outcome as the original phase 2, without the notes file it was supposedly relying on.

**This is not the result the original claim predicted, and the honest thing to do is report that, not bury it.** The reason: this task's remaining work happens to be fully reconstructable from the code and the failing test alone. There's no decision, dead end, or non-code-visible context in phase 1's actual notes that phase 2 couldn't re-derive by reading the fixture directly. The mechanism (persistent state, checked first, updated after each step) is real and correctly built. Its *necessity* for this specific, small, two-part task wasn't demonstrated; what was demonstrated is that a capable agent's own diligence can substitute for it here, the same shape of finding Module 01's counterfactual produced for prompt-engineering edge cases.

**What would make persistent state actually necessary:** context that isn't recoverable from the code, a rejected approach and why, a partial external operation in progress, a constraint discovered mid-task that isn't visible in any diff. A task whose only state is "which of two functions is done" doesn't need a notes file to reconstruct that; a task with real accumulated judgment does. `modules/03-harness-engineering/README.md` was corrected to say this rather than keep the stronger, untested original claim.
