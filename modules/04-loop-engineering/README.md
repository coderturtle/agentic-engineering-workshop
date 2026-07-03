# Module 04: Loop Engineering

## The question this module answers

When does it stop, how do we know it's right, and how does it get better without me watching every turn?

## Where it sits in the arc

Fourth module, built on top of a harness that already exists (module 03). This is the **behavioral** counterpart to harness engineering's structural concern: dynamic, runtime, and (at the frontier) self-modifying under human review. Last core module before the synthesis capstone. See [modules/README.md](../README.md) and `docs/workshop-design.md`'s loop taxonomy.

## Learning objectives

- Define a stop condition/terminal state for a bounded agent loop before running it, not after.
- Add a verification pass that checks output against a rubric rather than trusting the agent's own "done."
- Explain, with a concrete example, why a hill-climbing loop's proposed harness/prompt rewrites must be human-reviewed and verification-gated before adoption, never auto-applied.
- Apply the stable-goal-vs-moving-target rule to decide whether a task is worth building a loop for at all.

## Loop taxonomy used here

See [modules/README.md](../README.md#loop-taxonomy-module-04-uses-this-vocabulary-throughout) for the four-layer table (agent / verification / event-driven / hill-climbing loop).

**On hill-climbing specifically:** a proposed rewrite is only adopted if it passes verification (regression-free) and a human reviews it, never auto-applied. This must be explicit in the exercise content, not implicit; flagged by the Workshop Review Panel (AI/ML Practitioner and Security-Conscious Reviewer both caught the same gap independently; see `docs/review-panel/2026-07-03-initial-design.md`). A learner copying this pattern without the review gate is copying an unsafe default, and "the loop rewrote its own instructions overnight and nobody looked" is not a story anyone wants to be in.

## Exercise material this module draws from

- **Ticket-to-PR-Ready Loop**: reproduce → root-cause → smallest fix → rerun tests, with an explicit "can't reproduce after two attempts" terminal state (a concrete example of what a stop condition looks like in practice).
- **Restartable Handoff Loop**: a session-continuity exercise: state a goal, changes, verification evidence, untouched scope, and open risks well enough that a fresh session can resume cold.
- **The "ralph loop"** (Geoffrey Huntley): a long-running loop that preserves progress via git history and external memory instead of context-window state; material for the hill-climbing/self-improving concept.
- The stable-goal-vs-moving-target decision rule, for deciding whether a task deserves a loop at all.

## Exercise: Ticket-to-PR-Ready core

Runs against the shared `receipts` fixture (`fixtures/receipts/`, spec in `fixtures/receipts/SPEC.md`). The fixture ships a real ticket:

> `receipts --tz America/New_York` reports totals that look wrong near a month boundary. `tests/test_grouping.py::test_month_boundary_crosses_in_target_timezone` is failing; every other test in the suite passes.

Not a trick question. The bug is real, it lives in one function, and the fix is two lines once you find them. Everything interesting about this exercise is whether you actually verify that, or just talk yourself into it.

**Before building anything**, write one sentence classifying this ticket as a stable goal (worth building a loop for), and name one moving-target counter-example you would not loop-ify. This is the stable-goal-vs-moving-target rule from `docs/workshop-design.md`, applied for real before the loop exists, not after.

**Then build and run a bounded loop:**

> Build and run a bounded loop: reproduce, root-cause, smallest fix, rerun tests. State both terminal states up front, before running: success is tests green; failure is "cannot reproduce after two attempts." Submit the loop definition and a transcript showing the terminal state firing.

The loop must trust the test suite's result, not its own judgment of whether the fix looks right. The fix should touch only what the bug requires. A correct fix here is small: it changes how the grouping key is computed, not the parsing, error handling, or CLI.

There is a faster way to make the suite go green: open the failing test and edit the assertion until it agrees with the bug. Nothing in a shell stops you. The rubric does, once someone actually reads the diff (see criterion 4), and the bug is still sitting there afterward regardless of what your terminal says.

## Rubric

1. **Stop condition stated before running (gate).** Both terminal states (tests green; cannot-reproduce-after-two-attempts) are named before the loop runs, not reconstructed afterward.
2. **Terminated correctly (gate).** The transcript shows a terminal state actually firing: either the tests turn green and the loop stops, or two genuine reproduction attempts fail and the loop stops there. Not an infinite loop, and not a manual kill with no terminal state reached. A terminal state firing on a test file the fix itself just edited does not count: see criterion 4.
3. **Verification is external (scored).** The loop's "done" signal is the test suite's result, not the agent asserting the fix looks right, and the suite itself was not modified by the fix being verified. A loop that edits the check to match the bug and then reruns it has not used external verification, whatever its transcript shows.
4. **Smallest-fix discipline (scored, hard boundary).** The diff is bounded to what the bug requires (the month-key computation). Unrelated code (parsing, error handling, the CLI) is untouched, and **`tests/test_grouping.py` is out of bounds entirely**: a fix that touches the test file that encodes the stop condition is not a smaller fix, it is not a fix at all, whatever else the diff looks like.
5. **Decision rule applied (scored).** The pre-build sentence correctly classifies the ticket as loop-worthy, and the named moving-target counter-example is a genuine non-example, not a restatement of the same ticket.

Criteria 1, 2, and (once a fix is claimed) "the fix actually works" are gates: fail any one and the attempt does not meet the rubric, whatever the other scores look like. 3-5 are scored on top of a passing gate. Criterion 4's test-file boundary is itself effectively a gate, not just a scored deduction: grade the diff's target files before trusting a green terminal state (see `runs/2026-07-03-module-04-dry-run/grading.md` for the dry-run attempt this rule was written to catch).

## Required to advance

Build and run a bounded loop against the ticket above, with both terminal states stated up front, and show it actually terminating correctly with the tests green, checked against the rubric above. Reading this module does not count: you advance on a loop that actually stopped correctly, not on having read this page.

## Takeaway

A reusable loop template: the bounded loop you built, generalized past this one ticket into something you can point at a different bug later, a slash command, a script, or a documented pattern (in the same style as Ticket-to-PR-Ready) with its stop condition and verification step named explicitly. Before you consider it done, drop it on a different, unrelated bug and confirm it still helps; a template that only worked once is a fluke with good production values, not a takeaway. If it used hill-climbing (see Extensions below), the template must carry the review-gate requirement with it, not just the mechanism.

## Stop condition

The loop stops itself, observably, in one of two states, stated before the loop runs:

- **Success:** the full test suite (`tests/test_grouping.py`) passes, including `test_month_boundary_crosses_in_target_timezone`.
- **Failure:** after two genuine attempts to reproduce/root-cause the bug, it still cannot be reproduced or localized. This is a valid stop, not a failed exercise: it means the loop correctly recognized it was not converging and quit instead of thrashing.

Either state must be observed firing in the transcript. A human (or Coachgremlin, observing) asserting "this looks done" does not count; the loop's own termination is what's being taught.

## Extensions (optional, not yet authored)

Three graded extensions target loop engineering's remaining sub-concepts (verification-deepened, event-driven, hill-climbing). See `docs/coachgremlin-implementation-plan.md` §2 (Module 04) for their design. Authored once the core above has a real run behind it and Module 03's harness exists for the event-driven and hill-climbing extensions to build on, per the plan's sequencing (`docs/coachgremlin-implementation-plan.md` §6).

> Content status: core exercise authored 2026-07-03, Coachgremlin's first real dry run (see `runs/`). Extensions above not yet authored.
