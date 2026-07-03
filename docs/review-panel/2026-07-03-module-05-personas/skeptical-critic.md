# Persona: Skeptical Practitioner / Critic — Module 05 — 2026-07-03

## Top finding: the fixture hands learners the answer, undercutting the "genuine ambiguity" claim

The README asserts the prompt and `background.md` are "a constant red herring" and that "you cannot pattern-match the answer from the symptom alone." But the shipped fixture files a learner actually opens contradict this. `variants/sabotaged-harness/background.md` (identical in `sabotaged-loop`) ends with: **"None of the above is required to diagnose the current bug."** `prompt.md` ends with its own meta-commentary: **"It isn't, on its own, enough to fully explain why this setup fails to reach done."** These aren't internal notes, they are in the exact files the learner reads during the exercise. A red herring that announces itself as a red herring isn't ambiguity; it's a spoiler. This directly weakens the "genuine-ambiguity requirement" the module leans on to justify why this isn't a Module 04 repeat.

## Second finding: the "tempting prompt fix" claim is asserted, not demonstrated

The module README calls the prompt "sloppy" and "tempting," but `sabotaged-loop-defense.md`'s own hypothesis section undercuts this: "The prompt is informal but names the right area (date handling in monthly totals)." The prompt correctly points at the exact seeded bug location per `SPEC.md`. Nothing about it would lead a competent learner to suspect prompt-engineering is the fix, it's casual phrasing, not misdirection. Calling that "tempting" overstates the trap; the module never shows a case where someone plausibly chased the prompt and got burned.

## Third finding: "ruled out the prompt" for sabotaged-loop is itself an assertion

The rubric demands evidence "not assertion" for ruling out layers, but the defense's "Not the prompt" bullet rests on applying the fix "directly," bypassing the prompt entirely, no agent was ever run against `sabotaged-loop`'s actual informal prompt (confirmed by `README.md`: "directly for the loop variant... since that bug is purely mechanical"). So the claim that "the informal wording never blocked a correct fix" was never actually tested against an agent following that prompt, it's inferred, not observed. This is the same evidentiary gap Module 04's panel flagged for a different claim.

**What's needed:** strip the self-spoiling disclaimers from the shipped fixture text, and either run an agent against the actual `sabotaged-loop` prompt to genuinely test it, or drop the "ruled out the prompt" claim to "not tested."
