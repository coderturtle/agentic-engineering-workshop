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
- Rubric criterion 3 (persistent state survives reset, gate): phase 2 had no memory of phase 1 and completed the task correctly using only the on-disk notes file. This is the hardest criterion to fake and the one this exercise is actually testing.
- Rubric criterion 4 (actually ran, gate): every step above is a real subagent run with a real, independently re-verified result, not a described one.
- Rubric criterion 6 (reusable generality): the sub-agent definition doesn't hardcode a fixture-specific absolute path; it's already close to drop-in for a real project with `receipts/`-shaped scope.

Not exercised in this pass: rubric criterion 5 (worktree isolation) is conditional and wasn't used here, a plain isolated directory was sufficient to demonstrate the required mechanism. Noted as optional in the module content, with a pointer to how a learner could add it.
