# Module 01: Prompt Engineering

## The question this module answers

What's the single best instruction for this one turn?

## Where it sits in the arc

First module. No prior module: this is the atomic unit everything else builds on. Precision, structure, examples, and constraints for a single turn are necessary but insufficient once a task spans more than one turn, which is exactly why module 02 (context engineering) exists. See [modules/README.md](../README.md) for the full arc and why this order.

## Learning objectives

- Write a single-turn instruction precise enough that the model's output is predictable, not just plausible.
- Recognize the point where a task has outgrown "one better prompt" and needs multi-turn structure instead.
- Distinguish a prompting problem from a context problem (module 02) or a harness problem (module 03) when a turn goes wrong.

## Exercise material this module draws from

No external named pattern: this is the one module without a borrowed exercise pattern. **The osmosis problem:** an advanced practitioner already writes decent prompts daily, so this exercise has to establish a genuinely new capability, not review what daily use already teaches (flagged by the Workshop Review Panel's Instructional Designer; see `docs/review-panel/2026-07-03-initial-design.md`). The new capability here is the shift from "get a plausible answer once" to "specify tightly enough that the output is determined, reproducibly, first try."

## Exercise: implement the spec, one shot

Runs against the shared `receipts` fixture's unimplemented variant (`fixtures/receipts/variants/unimplemented/`, spec in its `SPEC.md`), not the buggy variant Module 04 uses: this exercise is about writing a correct implementation from a spec, not fixing an existing one.

> Write one prompt that produces a correct `group_expenses_by_month(rows, tz)` from the signature and spec in `fixtures/receipts/variants/unimplemented/SPEC.md`, passing the provided test file, on the first try with no follow-up correction turn. The spec names four edge cases: empty input, a receipt whose UTC timestamp crosses a month boundary in the target timezone, duplicate timestamps, and a malformed row. Run your prompt three times from a clean session, each against a fresh copy of the fixture. All three outputs must pass, and none may touch the test file.

The hardness is the edge cases a naive prompt drops. The discriminator against osmosis is reproducibility: one lucky pass is a plausible output; three-for-three is a specified one.

## Rubric

1. **First-try pass (gate).** Output passes all provided tests with zero correction turns.
2. **Reproducibility (scored).** Three consecutive fresh runs of the same prompt all pass. Any flaky run costs the criterion.
3. **Edge-case coverage in the instruction (scored).** The prompt names the four edge cases rather than hoping the model infers them. Score is the fraction named.
4. **Constraint economy (scored).** No contradictory or dead constraints; each constraint is traceable to a specific failure it prevents.
5. **Output-shape control (scored).** Exact signature, return type, and file scope specified so the output is drop-in, not hand-reshaped, and doesn't touch the test file that's checking it.

## Required to advance

Produce a single-turn prompt that gets `group_expenses_by_month` right on the first try, no follow-up correction turn, three times in a row from a clean session. Submitted prompt plus all three runs' actual output, checked against the rubric above. Reading this module does not count: you advance on a working, reproducible prompt, not on having read this page.

## Takeaway

A reusable prompt template: the winning prompt's structure, generalized past this one task (what's fixed, what's a fill-in-the-blank, why each constraint is there), saved somewhere you'll actually use it again: a personal snippet library, a slash command, whatever your harness supports. Not the raw one-off prompt as submitted; the pattern behind it. Reference implementation: `.claude/commands/spec-impl.md`, built and validated 3-for-3 against this exact exercise (`runs/2026-07-03-module-01-dry-run/`).

## Stop condition

A single prompt that yields a first-try, test-passing implementation on three consecutive clean runs, no correction turn, and no run touches the test file. **Valid alternate terminal:** if, after several prompt revisions, the task genuinely cannot be made first-try single-turn, name why and classify it as "outgrown one prompt." That is learning objective 2 firing, and it is a pass, not a failure.

## Harness

Agnostic. Nothing in this exercise is specific to one coding-agent tool. Only the takeaway's storage form names per-harness options: a Claude Code slash command (as built here), a Cursor/Codex snippet, or a plain snippet-library entry.

> Content status: core exercise authored 2026-07-03, validated with a real 3-for-3 reproducibility check (`runs/2026-07-03-module-01-dry-run/`).
