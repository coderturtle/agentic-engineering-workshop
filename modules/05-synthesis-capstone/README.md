# Module 05: Synthesis Capstone

## The question this module answers

Given a broken agent task, which of the four layers is actually the bottleneck?

## Exercise: diagnose a sabotaged setup

Two variants are provided, each a complete agent setup (prompt, context, harness config, bounded loop, all in one directory): `fixtures/receipts/variants/sabotaged-harness/` and `fixtures/receipts/variants/sabotaged-loop/`. Pick one yourself (flip a coin, or have someone else hand you a directory listing without the name), and don't peek at the other until you're done: the point is diagnosing without knowing the answer in advance, and you can only get that from yourself once.

**If you browse `fixtures/receipts/variants/` yourself** (the exercise below tells you to "read every file," so you likely will): you'll see two more directories there, `sabotaged-prompt/` and `sabotaged-context/`. Those are not part of this exercise, don't pick them. Each has its own `NOT-A-REQUIRED-EXERCISE.md` explaining why; short version further down this page, in "Why prompt and context aren't live variants here."

What each file in the variant is: `prompt.md` is what the task was requested with; `background.md` is the context that shipped alongside it; `harness-config.md` is the sub-agent's stated scope (the harness layer); `loop.sh` is the bounded reproduce-fix-verify loop (the loop layer). Both variants share an identical `prompt.md` and `background.md`, so neither is ever the differentiator, only `harness-config.md` and `loop.sh` vary.

> Here is a broken agent task: harness, prompt, context, and loop all provided, that fails its goal. Instrument it: read every file, run `./loop.sh` once as shipped to see it fail, then form a hypothesis about which single layer is the bottleneck. Confirm with evidence: isolate by fixing one layer in a throwaway copy, changing nothing else, and see whether the failure moves. Apply the minimal fix to that layer only, in your real working copy. Write a defense: why this layer, not the other three, citing the evidence that ruled each out.

Running `./loop.sh` unmodified doesn't diagnose anything by itself, it just shows you the symptom (`TERMINAL STATE: FAILURE`), the same way running a failing test shows you a red X without telling you why. The diagnosis happens in the isolating step: copy the variant, change exactly one file (say, `harness-config.md`'s stated scope, or `loop.sh`'s verification check), rerun, and see whether the terminal state flips to `SUCCESS`. If it does, that layer was the bottleneck. If it doesn't, put it back and try a different layer.

The prompt looks a little sloppy (tempting prompt fix); `background.md` looks bloated (tempting context fix). In both shipped variants, neither is the real bottleneck, confirmed by actually running each variant's real prompt through a fresh agent: one variant's harness config wrongly scopes edits away from the file with the bug, the other's loop checks for a success signal the test runner never actually produces. You cannot pattern-match the answer from the symptom alone; the isolating test is the only way to know.

## Rubric

1. **Correct layer identified (gate).** The diagnosed bottleneck is the actual one.
2. **Evidence, not guess (scored, heavily weighted).** Diagnosis is backed by an isolating test, change one variable, observe whether the failure moves or stays, not the most obvious symptom.
3. **Ruled out the other three (scored).** The defense explicitly says why each other layer was not the bottleneck, with evidence, not assertion. For the two shipped variants, ruling out prompt and context is legitimately faster than ruling out harness or loop, since both are identical and neutral across variants; don't pad the write-up pretending otherwise, but do state what you checked (that the prompt and background are the same regardless of variant, and that neither references anything that would misdirect a fix) rather than skip the step because it feels obvious.
4. **Minimal fix (scored).** Fixed the diagnosed layer without shotgun-correcting the other three.
5. **Fix works (gate).** After the fix, the task succeeds: `TERMINAL STATE: SUCCESS`, independently reproducible.
6. **Layer attribution articulated (scored).** The defense attributes the fix to the layer's actual job ("a loop problem, not a prompt problem, because the verification step itself was checking the wrong thing"), not just which file changed.

## Required to advance / stop condition

Diagnose which layer is the actual bottleneck in your chosen variant, fix it with a minimal, isolated change, and defend the diagnosis in writing: why this layer, not the other three, citing the isolating test's evidence. The defense must survive the "why not the other three" test: could a reader independently confirm each ruled-out layer really wasn't the cause from what's written down? Submitted diagnosis, fix, and written defense, checked against the rubric above. Reading this module does not count: you advance on a correct diagnosis and fix, not on having read this page.

## Where it sits in the arc

Final module, after all four core modules. This is not a fifth new skill; it's the point where prompt, context, harness, and loop engineering are diagnosed as one system rather than four separate topics: a prompt is one turn's instruction; context engineering shapes what that turn can see; harness engineering decides what the agent can reach and how its work is organized; loop engineering decides when it stops, how it verifies, and how it rewrites itself. See [modules/README.md](../README.md) and `docs/workshop-design.md`.

**Honest scope note:** the two shipped variants make harness and loop the two live hypotheses; prompt and context are permanent, identical red herrings across both, not variants where they're ever actually the answer. This is not for lack of trying: prompt-bottleneck and context-bottleneck variants were built and rigorously tested (see "Why prompt and context aren't live variants here," below), and the finding was structural, not a construction shortfall. This capstone's required exercise genuinely composes two of the four layers as live diagnoses, and rules the other two out by inspection every time, not four as originally framed.

## Learning objectives

- Diagnose, given a deliberately broken agent task, which of the four layers is the actual bottleneck rather than guessing or fixing the most obvious symptom. **Directly gated by the required exercise**, for the harness/loop axis specifically; see the honest scope note above.
- Fix the diagnosed layer without over-correcting the other three.
- Articulate why the fix belongs to that layer specifically (e.g. "this was a harness problem, not a prompt problem, because...").

## Why prompt and context aren't live variants here (optional reading, not required)

This is the most conceptually load-bearing paragraph in the capstone, not a footnote: it's the one place in the whole workshop where "structural" and "behavioral" get pressure-tested against each other directly. Worth reading even though nothing here is gated.

Two more full agent setups were built: `fixtures/receipts/variants/sabotaged-prompt/` and `fixtures/receipts/variants/sabotaged-context/`, each with a genuinely correct harness and loop (copied from the proven-correct halves of the two shipped variants) and the identical seeded bug, differing only in a misleading `prompt.md` or `background.md`. Across **10** independent fresh-agent runs, **every single run caught the misdirection and fixed the real bug anyway**:

| Variant | Sabotage tried | Runs | Outcome |
|---|---|---|---|
| `sabotaged-prompt` | v1: confident wrong diagnosis (blame deduplication), then a stronger v1 iteration | 2 | Both reached the correct fix |
| `sabotaged-prompt` | control: honest prompt, same harness/loop | 1 | Reached the correct fix, as expected |
| `sabotaged-prompt` | v2: instruct the agent to distrust/skip the failing test | 2 | Both reached the correct fix anyway |
| `sabotaged-context` | v1, then a strengthened v2: false background claim ("no timezone conversion needed") | 2 | Both reached the correct fix |
| `sabotaged-context` | control: honest background, same harness/loop | 1 | Reached the correct fix, as expected |
| `sabotaged-context` | v3: same false claim, plus `SPEC.md`'s own answer-key section redacted, and its control | 2 | Both reached the correct fix |

Full evidence, including every transcript and diff: `runs/2026-07-04-module-05-sabotaged-prompt-dry-run/` and `runs/2026-07-04-module-05-sabotaged-context-dry-run/`.

The reason is consistent across both, not a coincidence of wording: this fixture family is deliberately self-documenting for Modules 01-04's sake (`SPEC.md`, the target function's own docstring, and the failing test's inline comment all independently state the real bug, by design, so a learner or agent can find it from the code alone). That is a strength for the first four modules and a structural liability for prompt/context sabotage specifically. This connects directly to "Where it sits in the arc," above: harness and loop bottlenecks are **structural**, mechanical, knowing the right answer doesn't help if you literally cannot reach the file or your verification script is broken. Prompt and context are **behavioral**, single-turn: they only work if the agent trusts them over everything else it could read, and a thorough agent that reads the code and tests it already has access to routes around bad instructions or false context the same turn it encounters them. Two attempts of two different shapes against this fixture both lost that contest; that's real evidence the pattern holds here, not proof it holds everywhere, so treat "hard to fool a diligent agent" as demonstrated for this fixture family, not as a universal law about prompt/context bottlenecks.

These two variants are shipped anyway, as real, evidenced negative-control artifacts, not as working exercises: don't pick them for the required exercise above, since the "correct" diagnosis for either is genuinely "no single layer is the bottleneck here," which the rubric above isn't built to grade. **If you want to see it yourself rather than take this on faith:** point your own fresh agent at `fixtures/receipts/variants/sabotaged-prompt/`, give it `prompt.md` as the task and `harness-config.md`'s scope as a hard boundary, and watch whether it catches the misdirection the same way these ten runs did. It's a five-minute check, not a re-litigation of the finding.

## Why the sabotage design works, and where it doesn't yet

The genuine-ambiguity requirement is the design constraint that keeps this from collapsing into Module 04's shape: diagnosis of a provided system is a different task than construction of one. Two techniques enforce it: a layer-neutral surface symptom ("the loop never reaches done," true regardless of which layer actually caused it), and variants where the obvious-looking culprit is present as a constant, ruled-out control, while the real bottleneck varies between the two layers currently built.

## Harness

Diagnostic method agnostic; shipped scenario Claude-Code-shaped with translation notes. Diagnosis is a mental method and fully portable to any harness. The broken scenario provided here is Claude-Code-shaped because Module 03 established that vocabulary (sub-agent config, bounded loop script); translate per Module 03's translation table. The playbook takeaway is fully agnostic: the checklist itself names no tool.

## Takeaway

A personal diagnostic playbook, packaged as a Skill: the "which layer is actually broken" method you just practiced, written down as a repeatable checklist (symptom → suspect layer → how to confirm → how to fix) you can run against a real broken agent task later. This is the capstone's own synthesis turned into the workshop's single most reusable artifact: everything from modules 01-04, compressed into one diagnostic tool. Reference implementation: `.claude/skills/diagnose-agent-failure/SKILL.md`, built by generalizing two real diagnoses (harness, loop). The prompt- and context-layer rows in the Skill's quick-reference table are written from the same principles, not from an equivalent diagnosis of those two layers specifically; treat those two rows as reasoned, and now investigated with a real negative result (see "Why prompt and context aren't live variants here," above), rather than confirmed the same way harness and loop are.

> Content status: core exercise authored 2026-07-03, verified with two fully real, independently diagnosed variants (one harness-bottleneck, one loop-bottleneck), each confirmed via an actual isolating test, not asserted (`runs/2026-07-03-module-05-dry-run/`). Restructured 2026-07-03 after the Workshop Review Panel's Module 05 run (`docs/review-panel/2026-07-03-module-05-content.md`), which found and fixed two real fixture bugs (a harness-config scope pointing at a directory that didn't exist; the fixture's own context files spoiling the diagnosis by confessing to being red herrings) and closed an evidence gap (the loop variant's "ruled out the prompt" claim was reverified with a real agent following the actual prompt, not just a hand-applied fix). Prompt-bottleneck and context-bottleneck variants were built and rigorously tested 2026-07-04 (10 independent fresh-agent runs across both); neither reproduced its intended failure mode against this fixture family, a real structural finding for this fixture, not a construction gap, documented in "Why prompt and context aren't live variants here," above. Shipped as evidenced negative-control artifacts, not as required-exercise options.