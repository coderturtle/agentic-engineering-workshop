# Diagnosis and defense: sabotaged-loop variant

Full treatment of the rubric's heaviest-weighted criterion (evidence, not guess), for one of the two variants. The other variant (sabotaged-harness) got the isolation test but not this full written defense; see `README.md` in this directory for both.

## Symptom

Given `fixtures/receipts/variants/sabotaged-loop/` (prompt, context, harness config, and a bounded loop, all provided), running `./loop.sh` ends in `TERMINAL STATE: FAILURE` after two attempts. Surface symptom: "the loop never reaches done."

## Hypothesis

The prompt is informal but names the right area (date handling in monthly totals). The context includes the full spec and test file, plus a background doc that's noisy but not misleading. The harness config's scope (`receipts/` editable, tests runnable) is generous enough to fix the bug if the bug is where `SPEC.md` says timezone bugs like this usually live. Initial hypothesis: **the loop is the bottleneck**, specifically its verification step, since nothing else looks obviously broken and the loop is the one component whose job is entirely mechanical (check a result), which is a common place for a silent bug to hide.

## Evidence, not guess

**Isolating test:** fixed the bug directly in `receipts/grouping.py` (the same tz-conversion fix used elsewhere in this fixture), touching nothing else, then reran `./loop.sh` unchanged.

- Confirmed independently, outside the loop, that the fix is genuinely correct: `PYTHONPATH=. python3 -m unittest discover -s tests -v` reports `OK`, all 5 tests green.
- Ran the unmodified `./loop.sh` against the now-correctly-fixed code. Result: `Still failing after attempt 2.` / `TERMINAL STATE: FAILURE.`, despite the tests actually passing.

This is the observable that confirms the hypothesis: the failure did not move when the underlying bug was fixed, which means the loop's report of failure is disconnected from the actual test result. Reading `loop.sh` confirms the mechanism: its verification step is

```bash
if grep -q "ALL TESTS PASSING" /tmp/sabotaged-loop-run.log; then
```

`unittest`'s actual success output is the string `OK`, never `ALL TESTS PASSING`. The check greps for a marker that never appears, so it reports failure unconditionally, regardless of the real test result.

## Ruling out the other three

- **Not the prompt:** the informal wording never blocked a correct fix. The isolating test used no prompt engineering at all, just applied the known-correct fix directly, and the loop still failed. If the prompt were the bottleneck, a better prompt would have been necessary to get a correct fix in place; it wasn't.
- **Not the context:** the `background.md` noise never prevented locating or understanding the bug. `SPEC.md` and `tests/test_grouping.py`, both included as provided, contain everything needed to fix it correctly, and the isolating fix used only that information.
- **Not the harness:** the harness config's scope (`receipts/` editable) already permits exactly the edit needed; the isolating test's fix lived entirely inside that scope and worked. (Contrast with the sabotaged-harness variant, where narrowing the scope to `docs/` produces a real, unfixable failure with an identical loop, prompt, and context; see `README.md`.)
- **The loop, confirmed:** the same loop script, unchanged, reports failure on objectively passing code. That is not something a better prompt, more context, or wider harness scope could ever fix, since none of those layers touch the loop's own verification logic.

## Minimal fix

One line, in `loop.sh` only:

```diff
-  if grep -q "ALL TESTS PASSING" /tmp/sabotaged-loop-run.log; then
+  if [ "$status" -eq 0 ]; then
```

(along with capturing `status=$?` right after the test command, the same pattern already used correctly in the sabotaged-harness variant's `loop.sh` and in the Module 04 dry run's fixed loop harness, `runs/2026-07-03-module-04-dry-run/attempt-good/loop.sh`, after that dry run's own pipefail bug was caught and fixed.) Nothing in `receipts/`, the prompt, or the context needs to change.

## Layer attribution

A loop problem, not a prompt, context, or harness problem: the loop's own success check was checking for a signal the tool under test never produces, so it would report failure on any outcome, correct or not. The fix belongs entirely to the verification step, the layer whose only job is to tell the truth about what happened.
