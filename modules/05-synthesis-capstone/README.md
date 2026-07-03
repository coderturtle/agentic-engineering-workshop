# Module 05: Synthesis Capstone

## The question this module answers

Given a broken agent task, which of the four layers is actually the bottleneck?

## Where it sits in the arc

Final module, after all four core modules. This is not a fifth new skill; it's the point where prompt, context, harness, and loop engineering are diagnosed as one system rather than four separate topics: a prompt is one turn's instruction; context engineering shapes what that turn can see; harness engineering decides what the agent can reach and how its work is organized; loop engineering decides when it stops, how it verifies, and how it rewrites itself. See [modules/README.md](../README.md) and `docs/workshop-design.md`.

## Learning objectives

- Diagnose, given a deliberately broken agent task, which of the four layers is the actual bottleneck rather than guessing or fixing the most obvious symptom.
- Fix the diagnosed layer without over-correcting the other three.
- Articulate why the fix belongs to that layer specifically (e.g. "this was a harness problem, not a prompt problem, because...").

## Exercise material this module draws from

The capstone exercise: diagnose which of the four is the bottleneck in a deliberately broken agent task, then fix it. **The genuine-ambiguity requirement**, per the Workshop Review Panel (Instructional Designer): this cannot reuse Module 04's "build a loop that terminates" shape, since diagnosis of a provided system is a different task than construction of one. Two design techniques enforce it here: a layer-neutral surface symptom ("the loop never reaches done," true regardless of which layer actually caused it), and variants where the obvious-looking culprit (a sloppy prompt, a noisy context bundle) is present in every variant as a constant red herring, while the real bottleneck varies.

## Exercise: diagnose a sabotaged setup

Two variants are provided, both against the shared `receipts` fixture's seeded month-boundary bug, both shipping an identical informally-worded prompt and an identical moderately-noisy `background.md`, so neither of those is ever the differentiator: `fixtures/receipts/variants/sabotaged-harness/` and `fixtures/receipts/variants/sabotaged-loop/`. You get one; you don't know which.

> Here is a broken agent task: harness, prompt, context, and loop all provided, that fails its goal. Instrument it. Form a hypothesis about which single layer is the bottleneck. Confirm with evidence: isolate by fixing one layer in a throwaway and seeing whether the failure moves. Apply the minimal fix to that layer only. Write a defense: why this layer, not the other three, citing the evidence that ruled each out.

Each variant runs `./loop.sh` to `TERMINAL STATE: FAILURE`. The prompt looks a little sloppy (tempting prompt fix); `background.md` looks bloated (tempting context fix). In both shipped variants, neither is the real bottleneck: one variant's harness config wrongly scopes edits away from the file with the bug, the other's loop checks for a success signal the test runner never actually produces. You cannot pattern-match the answer from the symptom alone; the isolating test is the only way to know.

## Rubric

1. **Correct layer identified (gate).** The diagnosed bottleneck is the actual one.
2. **Evidence, not guess (scored, heavily weighted).** Diagnosis is backed by an isolating test, change one variable, observe whether the failure moves or stays, not the most obvious symptom.
3. **Ruled out the other three (scored).** The defense explicitly says why each other layer was not the bottleneck, with evidence, not assertion.
4. **Minimal fix (scored).** Fixed the diagnosed layer without shotgun-correcting the other three.
5. **Fix works (gate).** After the fix, the task succeeds: `TERMINAL STATE: SUCCESS`, independently reproducible.
6. **Layer attribution articulated (scored).** The defense attributes the fix to the layer's actual job ("a loop problem, not a prompt problem, because the verification step itself was checking the wrong thing"), not just which file changed.

## Required to advance

Diagnose which layer is the actual bottleneck in your assigned variant, fix it with a minimal, isolated change, and defend the diagnosis in writing: why this layer, not the other three, citing the isolating test's evidence. Submitted diagnosis, fix, and written defense, checked against the rubric above. Reading this module does not count: you advance on a correct diagnosis and fix, not on having read this page.

## Takeaway

A personal diagnostic playbook, packaged as a Skill: the "which layer is actually broken" method you just practiced, written down as a repeatable checklist (symptom → suspect layer → how to confirm → how to fix) you can run against a real broken agent task later. This is the capstone's own synthesis turned into the workshop's single most reusable artifact: everything from modules 01-04, compressed into one diagnostic tool. Reference implementation: `.claude/skills/diagnose-agent-failure/SKILL.md`, built by generalizing two real diagnoses, not written from theory (`runs/2026-07-03-module-05-dry-run/`).

## Stop condition

Correct diagnosis, plus a working minimal fix localized to one layer, plus a written defense that rules out the other three with the isolating test's evidence, not assertion. The defense must survive the "why not the other three" test: could a reader independently confirm each ruled-out layer really wasn't the cause from what's written down?

## Harness

Diagnostic method agnostic; shipped scenario Claude-Code-shaped with translation notes. Diagnosis is a mental method and fully portable to any harness. The broken scenario provided here is Claude-Code-shaped because Module 03 established that vocabulary (sub-agent config, bounded loop script); translate per Module 03's translation table. The playbook takeaway is fully agnostic: the checklist itself names no tool.

> Content status: core exercise authored 2026-07-03, verified with two fully real, independently diagnosed variants (one harness-bottleneck, one loop-bottleneck), each confirmed via an actual isolating test, not asserted (`runs/2026-07-03-module-05-dry-run/`). Two further variants (prompt-bottleneck, context-bottleneck) are a defined, not-yet-built extension.
