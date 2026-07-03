# Module 05 verification: two sabotaged variants, diagnosed for real

## What was built

`fixtures/receipts/variants/sabotaged-harness/` and `fixtures/receipts/variants/sabotaged-loop/`: two full setups (prompt, context, harness config, bounded loop, all provided) attempting the same task, fixing the seeded month-boundary bug. Both share an identical, slightly informal prompt and an identical, moderately noisy `background.md`, so neither is the differentiator. In `sabotaged-harness`, the harness config wrongly scopes edits to `docs/` instead of `receipts/`, so the bug is structurally unreachable. In `sabotaged-loop`, the harness config is correctly scoped, but the loop's own verification step checks for a log string (`"ALL TESTS PASSING"`) that `unittest` never prints, so it reports failure regardless of the actual result.

The plan calls for two to four variants; two are built and fully verified here (one harness-bottleneck, one loop-bottleneck). A prompt-bottleneck and a context-bottleneck variant are a defined, not-yet-built extension, noted in the module content rather than built this pass.

## Method

For each variant: ran it as provided (via a scope-obedient subagent for the harness variant, directly for the loop variant, since that bug is purely mechanical), confirmed the stated symptom actually occurs, then performed the isolating test the exercise requires: fix one layer only, in a throwaway copy, and check whether the failure moves.

## Results

**sabotaged-harness:** a subagent instructed to follow `harness-config.md`'s stated scope literally could not fix the bug, correctly identified why (the file with the bug is out of scope), and the loop terminated in `FAILURE` genuinely, not by choice. Isolating test: in a fresh copy, changed only the harness config's scope from `docs/` to `receipts/`, touched nothing else, reran with a fresh subagent. Result: `TERMINAL STATE: SUCCESS`, independently reverified (only `harness-config.md` differs from the shipped variant; `receipts/grouping.py` was the only file the agent touched; tests genuinely pass). The failure moved when, and only when, the harness layer was fixed.

**sabotaged-loop:** full defense in `sabotaged-loop-defense.md`. Applied the correct fix directly, confirmed independently that the tests pass, then reran the unmodified loop and confirmed it still reports `FAILURE`. The failure did not move when the underlying bug was fixed, which is exactly what isolates the loop as the true bottleneck: nothing about the code changed the loop's own broken verification.

## What this validates

- Rubric criterion 1 (correct layer identified, gate): both variants' true bottlenecks were correctly identified before any fix was applied to the "real" layer.
- Rubric criterion 2 (evidence, not guess): both diagnoses rest on an isolating test (change one variable, observe whether the failure moves), not the most obvious symptom (the sloppy prompt, the noisy background doc).
- Rubric criterion 3 (ruled out the other three): done explicitly, with evidence, in `sabotaged-loop-defense.md`; done implicitly but concretely for sabotaged-harness (the identical prompt, context, and loop succeed once only the harness scope changes).
- Rubric criterion 4 (minimal fix): sabotaged-loop's fix is one line, in the loop only. Sabotaged-harness's fix is one line, in the harness config only.
- Rubric criterion 5 (fix works, gate): both isolating tests end in a genuine, independently reverified `TERMINAL STATE: SUCCESS`.
- Rubric criterion 6 (layer attribution): both defenses state which layer's *definition* the fix belongs to (verification's job is to tell the truth about the result; the harness's job is to grant reach to what needs fixing), not just which file changed.
