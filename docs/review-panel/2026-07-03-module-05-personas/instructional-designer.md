# Persona: Instructional Designer — Module 05 — 2026-07-03

## Top finding: the "compose all four" claim doesn't survive contact with what's actually built

The README frames the capstone as diagnosing "prompt, context, harness, and loop engineering... as one system rather than four separate topics," and the implementation plan says 05 "composes the prior four rather than introducing a fifth topic." But in both shipped variants, prompt and background.md are **byte-identical** across variants and are permanent red herrings ("both shipping an identical informally-worded prompt and an identical moderately-noisy `background.md`, so neither of those is ever the differentiator"). A learner never experiences a case where the bottleneck *is* the prompt or context, only harness or loop. That's 2 of 4 layers actually exercised as live hypotheses; the other two are always eliminated by inspection, not diagnosis.

This directly answers the assigned question: **yes, a learner who skipped Modules 01/02 could complete either shipped variant fine.** Ruling out prompt/context (rubric criterion 3) requires only reading the fixed prompt and background doc and noting nothing's wrong, no prompt-crafting skill from 01, no context-curation/budgeting skill from 02, is ever applied. Compare `sabotaged-loop-defense.md`'s "Not the prompt" / "Not the context" paragraphs, which are near-boilerplate, against "Not the harness," which required an actual isolating test. Only Module 03 (harness scope) and Module 04 (bounded-loop verification discipline) are load-bearing here.

## Second finding: the Takeaway overclaims its own grounding

"Built by generalizing two real diagnoses, not written from theory" is true for the harness/loop branches of the promised diagnostic playbook, but the prompt/context branches of that same playbook are necessarily theoretical, no real diagnosis backs them yet. The "not written from theory" claim should be scoped to the two layers actually verified.

## Minor: rubric redundancy

Criteria 3 ("ruled out the other three") and 6 ("layer attribution articulated") substantially restate each other in practice, `sabotaged-loop-defense.md`'s "Layer attribution" section repeats what "Ruling out the other three › The loop, confirmed" already established.

The module's own status note discloses the 2-of-4 gap honestly, but the Learning Objectives and framing prose don't hedge to match it.
