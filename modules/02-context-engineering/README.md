# Module 02: Context Engineering

## The question this module answers

What does the model actually need to see, and what should be left out?

## Where it sits in the arc

Second module, after prompt engineering. The shift here is from "write a good instruction" to "curate what the model can see": still a single-turn-adjacent concern, but about the window's contents rather than the instruction itself. Comes before harness engineering (module 03), which is about what the agent can *reach* across tool calls, not just what's in one window. See [modules/README.md](../README.md) for the full arc.

## Learning objectives

_(finalized in the Coachgremlin content pass, placeholders below)_

- Curate a context window to a fixed budget without losing what the task actually needs.
- Decide what to summarize, what to preserve verbatim, and what to exclude on purpose, and justify each decision.
- Recognize when a bad output is a context problem (wrong/missing information) rather than a prompt problem (bad instruction) or a harness problem (wrong tool access).

## Exercise material this module draws from

A context-budget exercise: a deliberately oversized/noisy context that must be curated down to a fixed budget while preserving what the task needs. This forces a real curation tradeoff instead of just discussing one in the abstract. (This module had no exercise anchor at all before the Workshop Review Panel's Instructional Designer flagged the gap; see `docs/review-panel/2026-07-03-initial-design.md`. Exact exercise spec is still a later Coachgremlin task; this is only the pointer.)

## Required to advance

Take a deliberately oversized/noisy context down to a fixed budget and still get the task right, with a short written justification of what you cut and why. Submitted curated context, the task output, and the justification, checked against a rubric (rubric TBD by Coachgremlin). Reading this module does not count: you advance on a working curation, not on having read this page.

## Stop condition

_(rubric + terminal state defined per exercise by Coachgremlin)_

> Content status: skeleton only. Teaching content is built one concept at a time in a later Coachgremlin run (see `docs/next-actions.md`).
