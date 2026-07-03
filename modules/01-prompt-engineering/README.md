# Module 01: Prompt Engineering

## The question this module answers

What's the single best instruction for this one turn?

## Exercise: implement the spec, one prompt

Runs against the shared `receipts` fixture's unimplemented variant (`fixtures/receipts/variants/unimplemented/`, spec in its `SPEC.md`), not the buggy variant Module 04 uses: this exercise is about writing a correct implementation from a spec, not fixing an existing one.

> Write one prompt that produces a correct `group_expenses_by_month(rows, tz)` from the signature and spec in `fixtures/receipts/variants/unimplemented/SPEC.md`, passing the provided test file, on the first try with no follow-up correction turn. The spec names four edge cases: empty input, a receipt whose UTC timestamp crosses a month boundary in the target timezone, duplicate timestamps, and a malformed row. Run your prompt three times from a clean session, each against a fresh copy of the fixture (recopy `fixtures/receipts/variants/unimplemented/` into a new scratch directory before each run, or `git checkout` it if it's tracked, so each attempt genuinely starts from the unimplemented stub, not a prior attempt's result). All three outputs must pass, and none may touch the test file.

## Rubric

1. **First-try pass (gate).** Output passes all provided tests with zero correction turns.
2. **Reproducibility (gate).** Three consecutive fresh runs of the same prompt all pass. Any flaky run fails this gate.
3. **Edge-case coverage in the instruction (scored).** The prompt names the four edge cases rather than hoping the model infers them. Score is the fraction named.
4. **Constraint economy (scored).** No contradictory or dead constraints; each constraint is traceable to a specific failure it prevents.
5. **Output-shape control (scored).** Exact signature, return type, and file scope specified so the output is drop-in, not hand-reshaped, and doesn't touch the test file that's checking it.

Before counting any run as a pass, skim the actual diff, not just the test result. A green test suite is not the same claim as "this is a correct, minimal implementation" (Module 04's dry run has a worked example of a green suite that wasn't: `runs/2026-07-03-module-04-dry-run/grading.md`).

## Required to advance / stop condition

Produce one prompt that gets `group_expenses_by_month` right on the first try, no follow-up correction turn, three times in a row from a clean session, with no run touching the test file. Submit the prompt plus all three runs' actual output, checked against the rubric above. Reading this module does not count: you advance on a working, reproducible prompt, not on having read this page.

**Valid alternate terminal:** if, after several prompt revisions, the task genuinely cannot be made first-try single-turn, name why and classify it as "outgrown one prompt" instead. That's a real, useful outcome, not a failure: it means the task needed more than one prompt can carry, which is exactly the boundary the next module exists to handle.

## Where it sits in the arc

First module. No prior module: this is the atomic unit everything else builds on. Precision, structure, examples, and constraints for a single turn are necessary but insufficient once a task spans more than one turn, which is exactly why module 02 (context engineering) exists. See [modules/README.md](../README.md) for the full arc and why this order.

## Learning objectives

- Write a single-turn instruction precise enough that the model's output is predictable, not just plausible.
- Recognize the point where a task has outgrown "one better prompt" and needs multi-turn structure instead.
- Distinguish a prompting problem from a context problem (module 02) or a harness problem (module 03) when a turn goes wrong.

## Why this is hard, and what actually turned out to matter

An advanced practitioner already writes decent prompts daily, so this exercise has to establish a genuinely new capability, not review what daily use already teaches. The intended new capability is the shift from "get a plausible answer once" to "specify tightly enough that the output is determined, reproducibly, first try."

That claim was tested directly, not just asserted: a fully-specified prompt and a deliberately naive one (no edge cases named, no scope constraint stated) were each run three times against this fixture, independently reverified. Both got all four edge cases right, every time. The reason: this fixture's own docstring, sitting directly above the function being implemented, already lists all four edge cases, and any reasonably capable agent reads the file it's about to edit as a matter of ordinary diligence. Naming the edge cases in the prompt didn't turn out to be what separated the two attempts here.

What did differ, consistently: the specified prompt states its scope boundary outright ("do not modify the test file"); the naive one never says this and only avoided the file because the agent happened to make that call unprompted. That's the actual, demonstrated stake in specifying tightly: not whether a vague prompt drops information that happens to be sitting in plain sight, but whether your instruction leaves anything to the agent's discretion that you didn't mean to leave there. Full method and result: `runs/2026-07-03-module-01-dry-run/README.md`.

## Harness

Agnostic. Nothing in this exercise is specific to one coding-agent tool. Only the takeaway's storage form names per-harness options: a Claude Code slash command (as built here), a Cursor/Codex snippet, or a plain snippet-library entry.

## Takeaway

Don't open this section before your first attempt: it names the winning structure directly, and the exercise is partly about finding that structure yourself.

A reusable prompt template: the winning prompt's structure, generalized past this one task (what's fixed, what's a fill-in-the-blank, why each constraint is there), saved somewhere you'll actually use it again: a personal snippet library, a slash command, whatever your harness supports. Not the raw one-off prompt as submitted; the pattern behind it. Reference implementation: `.claude/commands/spec-impl.md`.

> Content status: core exercise authored 2026-07-03, validated with a real 3-for-3 reproducibility check plus a naive-prompt counterfactual (also 3-for-3, which changed what this module claims: see "Why this is hard," above). Reviewed by the Workshop Review Panel the same day (`docs/review-panel/2026-07-03-module-01-content.md`); this restructure and the counterfactual are its direct output.
