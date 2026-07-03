# Module 05: Synthesis Capstone

## The question this module answers

Given a broken agent task, which of the four layers is actually the bottleneck?

## Where it sits in the arc

Final module, after all four core modules. This is not a fifth new skill; it's the point where prompt, context, harness, and loop engineering are diagnosed as one system rather than four separate topics: a prompt is one turn's instruction; context engineering shapes what that turn can see; harness engineering decides what the agent can reach and how its work is organized; loop engineering decides when it stops, how it verifies, and how it rewrites itself. See [modules/README.md](../README.md) and `docs/workshop-design.md`.

## Learning objectives

_(finalized in the Coachgremlin content pass, placeholders below)_

- Diagnose, given a deliberately broken agent task, which of the four layers is the actual bottleneck rather than guessing or fixing the most obvious symptom.
- Fix the diagnosed layer without over-correcting the other three.
- Articulate why the fix belongs to that layer specifically (e.g. "this was a harness problem, not a prompt problem, because...").

## Exercise material this module draws from

The capstone exercise: diagnose which of the four is the bottleneck in a deliberately broken agent task, then fix it. Open design risk carried from the Workshop Review Panel (Instructional Designer): nothing yet guards against this capstone reusing the same "broken task" shape as module 04's own exercises rather than genuinely requiring cross-layer diagnosis. The content-building pass needs to construct a scenario where the bottleneck could plausibly be any of the four, not one that telegraphs the answer.

## Required to advance

Diagnose which layer is the actual bottleneck in a deliberately broken agent task, fix it, and defend the diagnosis in writing (why this layer, not the other three). Submitted diagnosis, fix, and written defense, checked against a rubric (rubric TBD by Coachgremlin). Reading this module does not count: you advance on a correct diagnosis and fix, not on having read this page.

## Takeaway

A personal diagnostic playbook, ideally packaged as a Skill: the "which layer is actually broken" method you just practiced, written down as a repeatable checklist (symptom → suspect layer → how to confirm → how to fix) you can run against a real broken agent task later. This is the capstone's own synthesis turned into the workshop's single most reusable artifact: everything from modules 01-04, compressed into one diagnostic tool.

## Stop condition

_(rubric + terminal state defined per exercise by Coachgremlin)_

> Content status: skeleton only. Teaching content is built one concept at a time in a later Coachgremlin run (see `docs/next-actions.md`).
