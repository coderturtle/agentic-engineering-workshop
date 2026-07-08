# This is not one of Module 05's two required variants

If you're doing the capstone exercise, use `sabotaged-harness/` or `sabotaged-loop/` instead;
this directory isn't part of it.

This variant was built to make the **prompt** the bottleneck (unlike its siblings, its
`harness-config.md` and `loop.sh` are both genuinely correct). Across 5 independent fresh-agent
runs, two structurally different sabotage designs (a confident wrong diagnosis, and an instruction
to distrust the failing test), every run caught the misdirection and fixed the real bug anyway.
That's a real, rigorously tested negative finding, not an unfinished exercise: see
`../../../../modules/05-synthesis-capstone/README.md`'s "Why prompt and context aren't live
variants here" section, and the full evidence at
`../../../../runs/2026-07-04-module-05-sabotaged-prompt-dry-run/README.md`.

The "correct" diagnosis for this variant is genuinely "no single layer is the bottleneck," which
Module 05's rubric isn't built to grade, so it isn't offered as a pick.
