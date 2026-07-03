# Module 04: Loop Engineering

## The question this module answers

When does it stop, how do we know it's right, and how does it get better without me watching every turn?

## Where it sits in the arc

Fourth module, built on top of a harness that already exists (module 03). This is the **behavioral** counterpart to harness engineering's structural concern: dynamic, runtime, and (at the frontier) self-modifying under human review. Last core module before the synthesis capstone. See [modules/README.md](../README.md) and `docs/workshop-design.md`'s loop taxonomy.

## Learning objectives

_(finalized in the Coachgremlin content pass, placeholders below)_

- Define a stop condition/terminal state for a bounded agent loop before running it, not after.
- Add a verification pass that checks output against a rubric rather than trusting the agent's own "done."
- Explain, with a concrete example, why a hill-climbing loop's proposed harness/prompt rewrites must be human-reviewed and verification-gated before adoption, never auto-applied.
- Apply the stable-goal-vs-moving-target rule to decide whether a task is worth building a loop for at all.

## Loop taxonomy used here

See [modules/README.md](../README.md#loop-taxonomy-module-04-uses-this-vocabulary-throughout) for the four-layer table (agent / verification / event-driven / hill-climbing loop).

**On hill-climbing specifically:** a proposed rewrite is only adopted if it passes verification (regression-free) and a human reviews it, never auto-applied. This must be explicit in the exercise content, not implicit; flagged by the Workshop Review Panel (AI/ML Practitioner and Security-Conscious Reviewer both caught the same gap independently; see `docs/review-panel/2026-07-03-initial-design.md`). A learner copying this pattern without the review gate is copying an unsafe default.

## Exercise material this module draws from

- **Ticket-to-PR-Ready Loop**: reproduce → root-cause → smallest fix → rerun tests, with an explicit "can't reproduce after two attempts" terminal state (a concrete example of what a stop condition looks like in practice).
- **Restartable Handoff Loop**: a session-continuity exercise: state a goal, changes, verification evidence, untouched scope, and open risks well enough that a fresh session can resume cold.
- **The "ralph loop"** (Geoffrey Huntley): a long-running loop that preserves progress via git history and external memory instead of context-window state; material for the hill-climbing/self-improving concept.
- The stable-goal-vs-moving-target decision rule, for deciding whether a task deserves a loop at all.

## Required to advance

Build and run a bounded loop (modeled on Ticket-to-PR-Ready or an equivalent) with a real, stated stop condition, and show it actually terminating correctly, not just describe one. Submitted loop definition plus a real run transcript showing the terminal state firing correctly, checked against a rubric (rubric TBD by Coachgremlin). Reading this module does not count: you advance on a loop that actually stopped correctly, not on having read this page.

## Takeaway

A reusable loop template: the bounded loop you built, generalized past this one task into something you can point at a different problem later, a slash command, a script, or a documented pattern (in the same style as Ticket-to-PR-Ready) with its stop condition and verification step named explicitly. If it used hill-climbing, the template must carry the review-gate requirement with it, not just the mechanism.

## Stop condition

_(rubric + terminal state defined per exercise by Coachgremlin)_

> Content status: skeleton only. Teaching content is built one concept at a time in a later Coachgremlin run (see `docs/next-actions.md`).
