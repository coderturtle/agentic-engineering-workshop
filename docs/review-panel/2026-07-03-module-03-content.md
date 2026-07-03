# Workshop Review Panel — Module 03 Content Review

**Date:** 2026-07-03
**Scope:** `modules/03-harness-engineering/README.md`, `.claude/agents/receipts-category-summary.md`, `runs/2026-07-03-module-03-dry-run/`.
**Run:** the panel's fourth real-content run (after design docs, Module 01, Module 02). Seven personas reviewed independently and in parallel.

Full per-persona critiques: `docs/review-panel/2026-07-03-module-03-personas/`.

This is the richest run so far: four independent structural agreements confirming Module 03 didn't inherit Modules 01/02's fixes, and three independent personas converging on the same unproven central claim, which led to a real negative-control experiment whose result contradicted the original text.

## Agreements (2+ personas, independently)

### 1. Module 03 reproduces the exact pre-fix structure Modules 01 and 02 already had fixed (Developer Evangelist + Technical Writer)

Both personas independently confirmed the same four sub-findings: the exercise buried under five headers of front-matter; an internal review-panel citation leaking into learner prose ("flagged by the Workshop Review Panel's End-User/Learner persona"); Takeaway appearing before Stop Condition with no spoiler guard (unlike Module 01's fixed version); and Required-to-advance/Stop-condition left unmerged and redundant. The Developer Evangelist's framing: "Module 03 confirms it's spreading, not shrinking." This happened because each module's authoring pass fixed what its own dry run surfaced, and the digestibility fixes from Module 01's panel run weren't retroactively applied to modules authored after it, only referenced as a pattern to watch for.

**Status: fixed in this pass**, matching the same restructure applied to Modules 01 and 02.

### 2. The reset-and-resume's central claim was never tested against its own stated negative control (AI/ML Practitioner + Skeptical Critic + End-User/Learner)

Three personas independently converged on the same gap: the module claims "the second session can only complete the task by reading the state the first one left behind," and even names the exact verification the stop condition should have required ("check what the second session could plausibly have known without the notes file"), but the reference dry run never ran that check. The AI/ML Practitioner reasoned it out technically (the remaining task is fully inferable from the code plus the one failing test); the Skeptical Critic demanded the ablation directly; the End-User/Learner discovered, separately, that the reference run doesn't even ship a transcript to check.

**Status: fixed in this pass, and the result was not what the original claim predicted.** The negative control was run for real: phase 2, rerun from the identical starting point, with the notes file deliberately withheld. It also succeeded, using code and test investigation alone. The module's claim was rewritten to say what was actually shown (the mechanism is real and correctly built; its necessity for this specific, small task wasn't demonstrated) rather than keep the stronger, untested original. See Actions Taken and `runs/2026-07-03-module-03-dry-run/README.md`'s new "Negative control" section.

## Single-persona findings

### 3. No transcript exists in the reference run at all (End-User/Learner, Skeptical Critic, Security-Conscious Reviewer all separately noted this)

Confirmed by direct inspection: `runs/2026-07-03-module-03-dry-run/` contained only a narrative README, a diff, and the progress-notes file, no raw tool-call or conversation log, despite the exercise's own requirement (d) demanding "show it actually running, with a transcript." Three personas caught this independently from different entry points (trust, evidence-standard, security-verification), which is itself a strong signal it's real.

**Status: acknowledged honestly, partially addressed.** This session's tooling (subagents invoked via an internal agent-dispatch tool) doesn't expose a raw tool-call transcript the way an interactive Claude Code session's own log would. Rather than fabricate one, the module's own exercise text (requirement d) was rewritten to define what counts as a transcript honestly: your own session log or terminal history in the normal case, or a real-time action record the agent writes as it works if your harness doesn't expose one, explicitly not a summary written after the fact. This is a limitation of this reference build's environment, disclosed rather than hidden, not a claim that real learners will hit the same constraint.

### 4. The sub-agent's file-scope boundary was prose only, with no enforcement mechanism (Security-Conscious Reviewer)

`.claude/agents/receipts-category-summary.md`'s frontmatter had only `name` and `description`, no `tools:` restriction. The rubric already half-acknowledged the risk ("not just followed by luck") without requiring anything address it.

**Status: fixed in this pass** — added a `tools: Read, Edit, Write, Bash` restriction, with an honest note that this narrows tool access but doesn't by itself enforce path scope, so the path boundary still needs explicit verification.

### 5. Persistent state was trusted blindly, with no guidance to verify it (Security-Conscious Reviewer)

The sub-agent instructions said to read the progress file and resume from what it says, with no instruction to treat its contents as a claim to verify rather than ground truth.

**Status: fixed in this pass** — added explicit guidance to rerun the verification command before trusting what the notes claim, and to treat the test suite, not the notes file, as the source of truth about actual state.

### 6. The reset-and-resume gate had a copy-paste loophole (Instructional Designer)

Nothing in the original rubric forbade phase 1 from writing the complete finished solution into the notes file, letting phase 2 merely transcribe it, which would satisfy the letter of "resumes and completes correctly" without demonstrating genuine incremental resumption.

**Status: fixed in this pass** — rubric criterion 3 and the sub-agent's own instructions now explicitly require notes to describe state and reasoning, not contain a finished, copy-pasteable answer.

### 7. Verification was asymmetric: reset-and-resume got an independent-check instruction, bounded reach didn't (Security-Conscious Reviewer)

The stop condition told learners to independently verify the reset; nothing parallel told them to verify the scope boundary held (e.g., diffing outside the granted path).

**Status: fixed in this pass** — added the equivalent instruction to rubric criterion 1.

### 8. The worktree learning objective doesn't survive the exercise (Instructional Designer)

Listed as a core objective, but the exercise makes it explicitly optional and the reference run didn't use one at all.

**Status: fixed in this pass** — objective reworded to state plainly that it's demonstrated as optional, not exercised as a requirement, rather than imply it's tested when it isn't.

### 9. The cumulative-hook claim overstated a mechanical pipeline that doesn't exist (Instructional Designer)

The plan's original language ("runs the specified task repeatedly with the curated context") implied Module 02's curated output literally feeds Module 03's harness; the shipped exercise re-stubs the target from the clean canonical fixture instead.

**Status: fixed in this pass** — reworded to state the real, honest continuity (fixture-family and CLI-shape) without implying a pipeline that isn't there, the same honesty pattern already applied to Module 02's claim about Module 01.

### 10. The translation table overstated enforcement parity across harnesses (AI/ML Practitioner)

Implied Cursor/Codex equivalents to Claude Code sub-agents enforce the same file-scope boundary; they don't.

**Status: fixed in this pass** — added an explicit note that enforcement isn't equivalent across the row, plus a missing "context reset" row the End-User/Learner persona separately flagged as absent.

### Positive findings worth keeping

- **The mechanism itself (bounded sub-agent, persistent state, two genuinely separate sessions) is real and correctly built**, confirmed by the negative control: it wasn't necessary for this task, but nothing about how it was built was wrong.
- **`receipts/cli.py`'s default behavior stayed unbroken and scope held** in both the original run and the negative control, independently reverified each time.
- **Voice and brand compliance clean at the sentence level** (Technical Writer), consistent with the other three modules: the recurring problem across this whole panel is structural placement, not prose quality.

## Actions Taken (this pass)

- **Ran the missing negative control for real**: reconstructed the phase-1-complete checkpoint, withheld the notes file, reran phase 2. It succeeded anyway. Rewrote the module's central claim to match what was shown, not what was hoped for.
- **Restructured `modules/03-harness-engineering/README.md`**: exercise moved to the second section; internal citation removed; Required-to-advance and Stop-condition merged; Takeaway moved to the end with a spoiler guard; worktree objective and cumulative-hook language corrected to be honest about what's actually exercised.
- **Added real enforcement to the sub-agent definition**: a `tools:` restriction, guidance to verify (not blindly trust) the persistent-state file, and an explicit prohibition on notes containing a finished copy-pasteable answer.
- **Closed the asymmetric-verification gap**: bounded reach now gets the same independent-check instruction reset-and-resume already had.
- **Added a "context reset" row and an enforcement-parity caveat** to the Claude Code / Cursor / Codex translation table.
- **Addressed the missing-transcript finding honestly**: defined what counts as a transcript to account for harnesses (and this reference build's own tooling) that don't expose a raw tool-call log, rather than either ignore the gap or fabricate an artifact.

## Deferred (real, but not fixed this pass)

- A literal raw tool-call transcript for the reference run itself still doesn't exist; the exercise text now defines an honest substitute, but a future pass could capture a genuine terminal/session log if the tooling allows it.
- Whether other modules authored after Module 01's panel run (Module 05, not yet reviewed at the time this run happened) inherited the same un-carried-forward fixes is an open question for that module's own panel pass.

## Panel Verdict

This run found the same class of gap twice, at two different scales: a systemic one (four structural fixes that existed in Modules 01/02 simply weren't propagated to Module 03) and a substantive one (the module's single most important claim was never tested against the exact negative control its own text names). Both got fixed with real work, not word changes: a genuine rerun of the exercise under the missing condition, not an edit to soften the claim. The result changed what the module honestly teaches, in the same direction Module 01's and Module 02's real findings did: agents are good at reconstructing context from artifacts that are already self-documenting, and the exercises that isolate a mechanism's real necessity need to be designed harder than "a task a diligent agent could solve without it."
