---
description: Implement one specified function from a signature and spec, correctly, on the first try
---

# Spec-to-implementation, one shot

The Module 01 takeaway: a template for turning "here's a function signature and a spec" into a single instruction precise enough that the output is determined, not just plausible, first try, no correction turn. The fully-specified version of this template passed 3-for-3 on a real exercise (`runs/2026-07-03-module-01-dry-run/`) for first-try pass and reproducibility (rubric criteria 1 and 2). A deliberately naive version was also run 3-for-3 against the same fixture, which is why this template is scoped the way it is below, not the way an earlier draft claimed.

## Template

Fill in every `{slot}`. Everything else is fixed scaffolding, not decoration.

```
In {file_path}, implement {function_signature} to satisfy {spec_reference}. Do not modify any other file{, including the test file if one exists}.

{Supporting context already in the file: existing helpers, types, or partial
scaffolding the implementation should use rather than duplicate.}

Handle exactly these {N} cases:

{Numbered, concrete edge cases. Not "handle errors gracefully": name the
actual inputs that need to behave a specific way, and what that behavior is.}

When you are done, run {verification command} and confirm {pass condition} before reporting done.
```

## Why each slot is there

- **`{file_path}` + "do not modify any other file"**: this is the slot with real, demonstrated evidence behind it. A naive prompt lacking this constraint still avoided the test file in testing, but only because the agent happened to make that call unprompted, not because anything told it not to. A less careful agent, or a differently-behaved one, isn't guaranteed to make the same call. See `runs/2026-07-03-module-04-dry-run/grading.md` for what happens when a fix touches the wrong file under a different exercise: it doesn't just miss the point, it can still make everything green.
- **`{function_signature}` + supporting context**: names the exact contract instead of leaving return shape, types, or existing helpers to be inferred or reinvented.
- **Numbered edge cases, not "handle errors gracefully"**: still good practice, and vague robustness language does get vague robustness in general, but be honest about what this specific exercise showed: against a fixture whose own docstring already documented the edge cases, a naive prompt got them right anyway, just by reading the file it was editing. This slot matters most when the target isn't already self-documenting, or when you can't be sure the agent will go looking. Don't oversell it as the thing that mattered here; the scope-boundary slot above is the one with the real evidence.
- **`{verification command}` + `{pass condition}`, run before reporting done**: moves the check inside the same turn instead of leaving it to a human's next message, so a near-miss gets caught before it reaches you rather than after. No near-miss actually occurred in the runs this template is built from; the mechanism is sound but untested against a genuine near-miss so far.

## When to reach for this

A single, well-specified function or unit with a fixed contract and a way to check it (tests, a schema, a golden output). Not for open-ended or exploratory work: if you can't write the numbered edge cases without guessing, the task hasn't been scoped enough for one shot yet, and this template will just produce a confident wrong answer instead of a plausible one.
