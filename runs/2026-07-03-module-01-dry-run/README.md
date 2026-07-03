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
