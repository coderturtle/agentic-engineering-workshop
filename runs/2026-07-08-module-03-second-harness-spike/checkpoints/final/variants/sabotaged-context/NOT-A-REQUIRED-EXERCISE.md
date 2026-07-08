# This is not one of Module 05's two required variants

If you're doing the capstone exercise, use `sabotaged-harness/` or `sabotaged-loop/` instead;
this directory isn't part of it.

This variant was built to make the **context** (`background.md`) the bottleneck (unlike its
siblings, its `harness-config.md` and `loop.sh` are both genuinely correct). Across 5 independent
fresh-agent runs, including one where the fixture's own `SPEC.md` answer-key section was redacted
to remove the free answer, every run caught the false background claim (it directly contradicts
`SPEC.md`, the function's own docstring, and the failing test) and fixed the real bug anyway.
That's a real, rigorously tested negative finding, not an unfinished exercise: see
`../../../../modules/05-synthesis-capstone/README.md`'s "Why prompt and context aren't live
variants here" section, and the full evidence at
`../../../../runs/2026-07-04-module-05-sabotaged-context-dry-run/README.md`.

The "correct" diagnosis for this variant is genuinely "no single layer is the bottleneck," which
Module 05's rubric isn't built to grade, so it isn't offered as a pick.
