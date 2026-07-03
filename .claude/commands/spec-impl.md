---
description: Implement one specified function from a signature and spec, correctly, on the first try
---

# Spec-to-implementation, one shot

The Module 01 takeaway: a template for turning "here's a function signature and a spec" into a single instruction precise enough that the output is determined, not just plausible, first try, no correction turn. Validated 3-for-3 on a real exercise before being generalized here (`runs/2026-07-03-module-01-dry-run/`).

## Template

Fill in every `{slot}`. Everything else is fixed scaffolding, not decoration; each piece is there because leaving it out was tried and failed during validation.

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

- **`{file_path}` + "do not modify any other file"**: without an explicit scope boundary, a plausible fix can land in the wrong file, or worse, in the check itself. See `runs/2026-07-03-module-04-dry-run/grading.md` for what happens when a fix touches the wrong file: it doesn't just miss the point, it can still make everything green.
- **`{function_signature}` + supporting context**: names the exact contract instead of leaving return shape, types, or existing helpers to be inferred or reinvented.
- **Numbered edge cases, not "handle errors gracefully"**: vague robustness language gets vague robustness. A model that isn't told the specific inputs it will be judged against will guess which ones matter, and guess wrong at least once. This is the single biggest lever in the validated prompt: all four edge cases named explicitly, not implied.
- **`{verification command}` + `{pass condition}`, run before reporting done**: moves the check inside the same turn instead of leaving it to a human's next message. This is what makes "no follow-up correction turn" survive contact with a real attempt: the agent catches its own near-misses before they ever reach you.

## When to reach for this

A single, well-specified function or unit with a fixed contract and a way to check it (tests, a schema, a golden output). Not for open-ended or exploratory work: if you can't write the numbered edge cases without guessing, the task hasn't been scoped enough for one shot yet, and this template will just produce a confident wrong answer instead of a plausible one.
