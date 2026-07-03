# Module 01 verification: reproducibility check

Not a full Coachgremlin dry run (that treatment was reserved for Module 04, the actual first real run). This is narrower: does the candidate prompt in `candidate-prompt.md` actually work, reproducibly, from a clean session, against `fixtures/receipts/variants/unimplemented/`?

## Method

Three independent, isolated working copies (`run-1/`, `run-2/`, `run-3/`), each a fresh copy of the unimplemented variant. Three independent subagents, each given only `candidate-prompt.md`'s text verbatim and explicit instructions not to read anything outside its own directory (no reference implementation, no access to the rest of this repo). Each subagent's self-report was then independently re-verified from this session, not trusted at face value: the test file diffed against the original (confirming no tampering) and the test suite rerun directly.

## Result

3 for 3. All three produced a correct implementation on the first try, no follow-up correction turn, none touched the test file, all passed the full suite when rerun independently.

The three implementations are not identical (one used `defaultdict`, two used `dict.get`/manual insertion; one instantiates `ZoneInfo` once, others inline it), but all correctly convert to `tz` before computing the month key, all handle the four edge cases, and none touched anything outside `receipts/grouping.py`. This is the rubric's actual bar: correct and reproducible, not byte-identical.

## What this validates

- Rubric criterion 1 (first-try pass): met, 3/3.
- Rubric criterion 2 (reproducibility): met, 3/3 fresh clean-session runs.
- Rubric criterion 5 (output-shape control): met; the prompt's explicit scope constraint ("do not modify any other file, including the test file") held in all three attempts, with no attempt reaching for the shortcut Module 04's dry run showed is otherwise tempting.

## Counterfactual: does a naive prompt actually fail?

Added after the Workshop Review Panel's Module 01 content review (`docs/review-panel/2026-07-03-module-01-content.md`): the AI/ML Practitioner and Instructional Designer personas independently flagged that the module's central claim, "the hardness is the edge cases a naive prompt drops," had never actually been tested against a naive prompt. Only the fully-specified candidate prompt had ever been run. That's a real gap: validating the positive case says nothing about what fails without it.

**Method:** three more fresh, isolated working copies (`naive-1/`, `naive-2/`, `naive-3/`), same isolation rules as above. Each given a single deliberately undisciplined prompt, the kind an "osmosis-level" daily practitioner might write without this module's specific discipline: *"Implement group_expenses_by_month in receipts/grouping.py so it correctly groups expenses by month according to the docstring, and passes the tests in tests/test_grouping.py."* No edge cases named, no file-scope constraint stated, no explicit instruction to verify before reporting done.

**Result, independently reverified the same way as the main check: 3 for 3.** The naive prompt also produced a correct implementation on every run, and none touched the test file.

**This is not the result the claim predicted, and the honest thing to do is report that, not bury it.** The reason becomes clear on inspection: `receipts/grouping.py`'s own docstring, sitting directly above the function being implemented, already lists all four required edge cases verbatim (see the module docstring, "Required edge cases" section). A prompt doesn't need to name the edge cases itself if it points a reasonably capable agent at a file whose own docstring already does. Every naive attempt read that docstring as a matter of ordinary diligence, not because the prompt told it to.

**What this does and doesn't show:**

- It does **not** show that "name your edge cases explicitly" is load-bearing for *this specific fixture*. For a self-documenting target function, a naive-but-correctly-pointed prompt gets the same edge-case coverage a disciplined one does, because the coverage was never actually withheld from the agent, only from the prompt text.
- It **does** show the actual, verifiable difference between the two prompts: the disciplined prompt states the scope boundary ("do not modify the test file") explicitly; the naive one doesn't say this at all and only avoided the file by the agent's own unprompted judgment. A less careful agent, or a differently-behaved one, is not guaranteed to make that same call unprompted. Reproducibility and explicit scope control are real, demonstrated advantages of the specified prompt. "Prevents edge cases from being silently dropped," for this fixture, is not.
- It surfaces a genuinely useful insight for the arc, not a weakness in it: prompt precision and context availability are easy to conflate, and this counterfactual shows *why* they're separate concerns. The naive prompt succeeded here because the needed information was co-located and discoverable, not because the prompt was well-written. Module 02 buries that same information under noise specifically to test what happens once it *isn't* trivially discoverable, which is the more honest place to locate "does an under-specified prompt actually fail."

`modules/01-prompt-engineering/README.md` was corrected to reflect this rather than keep the unsupported original claim.
