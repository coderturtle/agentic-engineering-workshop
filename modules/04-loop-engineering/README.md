# Module 04: Loop Engineering

## The question this module answers

When does it stop, how do we know it's right, and how does it get better without me watching every turn?

## Exercise: Ticket-to-PR-Ready core

Runs against the shared `receipts` fixture (`fixtures/receipts/`, spec in `fixtures/receipts/SPEC.md`). The fixture ships a real ticket:

> `receipts --tz America/New_York` reports totals that look wrong near a month boundary. `tests/test_grouping.py::test_month_boundary_crosses_in_target_timezone` is failing; every other test in the suite passes.

Not a trick question. The bug is real, it lives in one function, and the fix is two lines once you find them. Everything interesting about this exercise is whether you actually verify that, or just talk yourself into it.

**Before building anything**, write one sentence classifying this ticket as a stable goal (worth building a loop for), and name one moving-target counter-example you would not loop-ify. This is the stable-goal-vs-moving-target rule from `docs/workshop-design.md`, applied for real before the loop exists, not after.

**Then build and run a bounded loop:**

> Build and run a bounded loop: reproduce, root-cause, smallest fix, rerun tests. State both terminal states up front, before running: success is tests green; failure is "cannot reproduce after two attempts." Submit the loop definition and a transcript showing the terminal state firing.

"Loop" here means a coding agent, driven by you, actually working through reproduce, root-cause, smallest fix, rerun, with a stop check between attempts, not a script that already knows the answer. A worked reference exists (`runs/2026-07-03-module-04-dry-run/attempt-good/loop.sh`) and is worth reading, but read it as a scaffold for the retry-and-verify structure, not as the mechanism itself: that particular script drives the fix deterministically for grading-reproducibility reasons specific to how it was built, where a real attempt has an agent doing the reproduce/root-cause/fix thinking inside the same bounded loop shape.

The loop must trust the test suite's result, not its own judgment of whether the fix looks right. The fix should touch only what the bug requires. A correct fix here is small: it changes how the grouping key is computed, not the parsing, error handling, or CLI.

There is a faster way to make the suite go green: open the failing test and edit the assertion until it agrees with the bug. Nothing in a shell stops you. The rubric does, once someone actually reads the diff (see criterion 4), and the bug is still sitting there afterward regardless of what your terminal says.

## Rubric

1. **Stop condition stated before running (gate).** Both terminal states (tests green; cannot-reproduce-after-two-attempts) are named before the loop runs, not reconstructed afterward.
2. **Terminated correctly (gate).** The transcript shows a terminal state actually firing: either the tests turn green and the loop stops, or two genuine reproduction attempts fail and the loop stops there. Not an infinite loop, and not a manual kill with no terminal state reached.
3. **Verification is external (scored).** The loop's "done" signal is the test suite's result, not the agent asserting the fix looks right, and the suite itself was not modified by the fix being verified. A loop that edits the check to match the bug and then reruns it has not used external verification, whatever its transcript shows.
4. **Smallest-fix discipline (scored, hard boundary).** The diff is bounded to what the bug requires (the month-key computation). Unrelated code (parsing, error handling, the CLI) is untouched, and **`tests/test_grouping.py` is out of bounds entirely**: a fix that touches the test file that encodes the stop condition is not a smaller fix, it is not a fix at all, whatever else the diff looks like. (Criteria 3 and 4 both trip on the same move here, editing the test file, because for this ticket that's the one gaming shortcut available; treat them as one check in practice for this exercise, two in principle for a ticket where they'd diverge.) Exception, rare: if the test itself is genuinely wrong (a typo, a stale fixture) rather than the code, that's a separate finding to raise on its own, not a reason to fold a test edit into this ticket's fix.
5. **Decision rule applied (scored).** The pre-build sentence correctly classifies the ticket as loop-worthy, and the named moving-target counter-example is a genuine non-example, not a restatement of the same ticket.

Criteria 1, 2, and (once a fix is claimed) "the fix actually works" are gates: fail any one and the attempt does not meet the rubric, whatever the other scores look like. 3-5 are scored on top of a passing gate. Criterion 4's test-file boundary is itself effectively a gate, not just a scored deduction: grade the diff's target files before trusting a green terminal state.

## Required to advance / stop condition

Build and run a bounded loop against the ticket above, with both terminal states stated up front, and show it actually stopping itself, observably, in one of the two states:

- **Success:** the full test suite passes, including `test_month_boundary_crosses_in_target_timezone`.
- **Failure:** after two genuine attempts to reproduce/root-cause the bug, it still cannot be reproduced or localized. This is a valid stop, not a failed exercise: it means the loop correctly recognized it was not converging and quit instead of thrashing.

Either state must be observed firing in the transcript. A human (or Coachgremlin, observing) asserting "this looks done" does not count; the loop's own termination is what's being taught. Submitted loop definition plus a transcript, checked against the rubric above. Reading this module does not count: you advance on a loop that actually stopped correctly, not on having read this page.

## Where it sits in the arc

Fourth module, built on top of a harness that already exists (module 03). This is the **behavioral** counterpart to harness engineering's structural concern: dynamic, runtime, and (at the frontier) self-modifying under human review. Last core module before the synthesis capstone. See [modules/README.md](../README.md) and `docs/workshop-design.md`'s loop taxonomy.

## Learning objectives

- Define a stop condition/terminal state for a bounded agent loop before running it, not after. **Directly gated by the required exercise above.**
- Apply the stable-goal-vs-moving-target rule to decide whether a task is worth building a loop for at all. **Directly gated by the required exercise above.**
- Add a verification pass that checks output against a rubric rather than trusting the agent's own "done." **Partially covered by the core** (the required exercise's stop check is pass/fail against a test suite, not a rubric-graded review); the fuller version, checking blast radius and minimality against a rubric, is Extension A, not yet authored.
- Explain, with a concrete example, why a hill-climbing loop's proposed harness/prompt rewrites must be human-reviewed and verification-gated before adoption, never auto-applied. **Not hands-on in the core.** This objective is stated and reasoned about below, but the required exercise doesn't exercise it; the hands-on version is Extension C, not yet authored. Until then, treat this objective as understood in principle, not practiced.

## Loop taxonomy and hill-climbing safety

See [modules/README.md](../README.md#loop-taxonomy-module-04-uses-this-vocabulary-throughout) for the four-layer table (agent / verification / event-driven / hill-climbing loop).

**On hill-climbing specifically:** a proposed rewrite is only adopted if it passes verification (regression-free) and a human reviews it, never auto-applied. A learner copying this pattern without the review gate is copying an unsafe default, and "the loop rewrote its own instructions overnight and nobody looked" is not a story anyone wants to be in. This rule is currently prose only: no exercise here enforces it the way criterion 4 structurally enforces the test-file boundary, because the exercise that would (Extension C) isn't authored yet. When it is, it needs the same treatment: a structural check, not just an instruction to a well-behaved agent.

## Exercise material this module draws from

- **Ticket-to-PR-Ready Loop**: reproduce → root-cause → smallest fix → rerun tests, with an explicit "can't reproduce after two attempts" terminal state (a concrete example of what a stop condition looks like in practice).
- **Restartable Handoff Loop**: a session-continuity exercise: state a goal, changes, verification evidence, untouched scope, and open risks well enough that a fresh session can resume cold.
- **The "ralph loop"** (Geoffrey Huntley): a long-running loop that preserves progress via git history and external memory instead of context-window state; material for the hill-climbing/self-improving concept.
- The stable-goal-vs-moving-target decision rule, for deciding whether a task deserves a loop at all.

## Extensions (optional, not yet authored)

Three graded extensions target loop engineering's remaining sub-concepts (verification-deepened, event-driven, hill-climbing). Authored once Module 03's harness exists for the event-driven and hill-climbing extensions to build on.

## Harness

Agent-loop mechanics agnostic; concrete build Claude-Code-leaning with translation notes. The loop *concept* is universal. The required build (a slash command, a hook) is shown in Claude Code with a mapping note; extension B's git hooks are agnostic and already modeled in this repo.

## Takeaway

A reusable loop template: the bounded loop you built, generalized past this one ticket into something you can point at a different bug later, a slash command, a script, or a documented pattern (in the same style as Ticket-to-PR-Ready) with its stop condition and verification step named explicitly. Before you consider it done, drop it on a different, unrelated bug and confirm it still helps; a template that only worked once is a fluke with good production values, not a takeaway. If it used hill-climbing (see Extensions above), the template must carry the review-gate requirement with it, not just the mechanism. Reference implementation: `.claude/commands/ticket-to-pr-ready.md`.

> Content status: core exercise authored 2026-07-03, Coachgremlin's first real dry run. Restructured 2026-07-03 after the Workshop Review Panel's Module 04 run, which found the same digestibility pattern already fixed in Modules 01-03 hadn't been carried forward here, plus a real rubric inconsistency (criterion 2 had picked up a claim the grading evidence didn't support) and an honest gap between what the core exercise gates and what all four learning objectives claim. Extensions above not yet authored.