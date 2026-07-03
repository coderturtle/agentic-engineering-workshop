# Workshop Review Panel — Module 04 Content Review

**Date:** 2026-07-03
**Scope:** `modules/04-loop-engineering/README.md`, `.claude/commands/ticket-to-pr-ready.md`, `runs/2026-07-03-module-04-dry-run/`.
**Run:** the panel's fifth real-content run (after design docs, Modules 01, 02, 03). Seven personas reviewed independently and in parallel. Module 04 already had the deepest prior treatment of any module, Coachgremlin's actual first real dry run with a genuine good attempt and a genuine gaming attempt, both graded, so this run was a test of whether that depth of evidence prevented the digestibility and drift problems found elsewhere, or whether it had its own separate issues.

Full per-persona critiques: `docs/review-panel/2026-07-03-module-04-personas/`.

## Agreements (2+ personas, independently)

### 1. Module 04 reproduces the Modules 01-03 pre-fix structure, and worse (Developer Evangelist + Technical Writer)

Both personas independently confirmed: exercise buried under six headers (one more than Module 01's original five); two separate internal review-panel citations leaking into learner prose (one in the Loop taxonomy section naming specific panel personas, one in the Rubric citing the dry-run's own grading file); three-way redundant restatement of the terminal-state requirement (Rubric, Required-to-advance, Stop-condition, worse than the two-way redundancy found elsewhere); and the exact Takeaway/Stop-condition ordering issue from Module 01's pre-fix version. This is notable because Module 01's own panel report, written earlier the same day, had already flagged that "the same 'internal citation leaks into learner content' pattern... exists in Module 04's README too," logged as a deferred cross-module item. It stayed unfixed until this run.

**Status: fixed in this pass**, matching the restructure applied to Modules 01-03.

### 2. Depth of evidence didn't prevent the exercise from being mechanically unclear, and the one reference implementation available contradicts the workshop's own premise (Developer Evangelist implicitly, End-User/Learner explicitly)

The End-User/Learner persona found that the module never explains what a "loop" mechanically is, the reference script (`attempt-good/loop.sh`) is never linked from the README at all, and, having found it anyway, that script is deterministic bash with a hardcoded patch, not an agent driving itself, which contradicts the workshop's stated "you drive it [the agent]" premise. This is a real gap distinct from the digestibility pattern above: even a maximally-evidenced module can still leave the exercise's basic mechanics unexplained.

**Status: fixed in this pass.**

## Single-persona findings

### 3. A real, confirmed factual inconsistency: rubric criterion 2 claimed a rubric behavior the grading evidence never tested (Skeptical Practitioner / Critic)

Directly verified against `grading.md`: the module's criterion 2 stated "a terminal state firing on a test file the fix itself just edited does not count," but `grading.md`'s own scoring table explicitly records the gaming attempt as passing criterion 2 "on a literal reading" and being caught by criteria 3 and 4 instead. This clause was added during an earlier session pass and was never reflected in the grading record or the revision log in `docs/decisions.md`. A real error, not a matter of interpretation.

**Status: fixed in this pass** — the unsupported clause removed from criterion 2 (it was also redundant with criterion 4, which does correctly carry the rule).

### 4. Criterion 4's hard boundary has no legitimate-test-fix exception, and the gap propagates into the reusable takeaway (AI/ML Practitioner)

A test that's itself wrong (a typo, a stale fixture) is a real, different case from gaming the test to hide a bug, but the rule as written banned both identically. More consequential in `ticket-to-pr-ready.md`, the generalized template meant for future, unrelated tickets, than in this one engineered exercise.

**Status: fixed in this pass** — both the module rubric and the takeaway template now name the exception explicitly: a genuinely wrong test is a separate finding to raise on its own, not grounds to fold a test edit into the ticket's fix.

### 5. The "core covers the two load-bearing layers" claim overstates what the required exercise actually gates (Instructional Designer)

Of the module's four learning objectives, two are genuinely gated by the core (stop condition, decision rule); the verification-pass objective is thinned to a binary pass/fail check (the fuller rubric-graded version is unauthored Extension A); the hill-climbing-safety objective has zero hands-on component at all (it's prose-only until unauthored Extension C exists). A learner can clear the module having never practiced the objective most directly tied to this workshop's own safety findings.

**Status: acknowledged honestly, not silently fixed.** Rewrote Learning Objectives to state plainly which are directly gated, which are partially covered, and which aren't hands-on yet, rather than let the module claim more coverage than the core actually provides. Redesigning the core exercise to cover all four objectives is a bigger change than this pass; logged in Deferred.

### 6. Rubric criteria 3 and 4 overlap on the identical gaming move for this ticket (Instructional Designer)

Both trip on "the fix touched the test file," double-weighting one failure mode rather than testing two distinct skills, for this specific exercise.

**Status: acknowledged in the rubric text**, with a note that they're one check in practice here and two in principle for a ticket where they'd diverge, rather than force an artificial merge that would lose the general-case distinction.

### 7. The "2 attempts" bound is real code in the throwaway dry-run script and unenforced prose in the reusable takeaway (Security-Conscious Reviewer)

`attempt-good/loop.sh` has an actual bash counter; `ticket-to-pr-ready.md`, the artifact learners actually copy, dropped back to natural language with nothing stopping a self-reported "I tried twice" from being unverifiable, the same self-report risk criterion 3 exists to close for test results, left open here for attempt-counting.

**Status: fixed in this pass** — the takeaway template now requires two logged, numbered attempts (hypothesis and result per attempt) before the failure terminal fires, not a narrated count.

### 8. Hill-climbing's review gate has no structural enforcement pattern designed for it yet (Security-Conscious Reviewer)

Real, but Extension C (the exercise that would operationalize it) doesn't exist yet, so there's nothing to enforce against.

**Status: logged as forward guidance** in the Loop taxonomy section: when Extension C is authored, it needs the same structural treatment criterion 4 gives the test-file boundary, not just an instruction to a well-behaved agent.

### 9. Overclaiming in the takeaway template: "very nearly worked" and a missing methodological hedge (Skeptical Practitioner / Critic)

The gaming attempt failed three of five criteria "clearly, once the diff is read," not a near-miss by any grader who actually looked; and the single-grader-grading-its-own-attempts caveat from `retro.md` never made it into the artifact learners keep.

**Status: fixed in this pass** — reworded to state precisely what "nearly worked" means (passed on a literal, incomplete reading, not a general near-success), and added the methodological hedge directly to the takeaway's Provenance section.

### Positive findings worth keeping

- **The Extensions section already handles "optional, not yet authored" correctly** (End-User/Learner): clearly labeled, no confusion about what's required.
- **The Takeaway's content itself doesn't spoil the fix** (Developer Evangelist): unlike Module 01's original version, it stays at the "generalize your template" level rather than handing over the answer, even though its *position* on the page needed fixing.
- **The Human Gate and external diff-inspection already caught real gaming in this dry run** (Security-Conscious Reviewer): confirmed working, not a new finding, worth restating as evidence the mechanism is sound even where other things needed fixing.

## Actions Taken (this pass)

- **Restructured `modules/04-loop-engineering/README.md`**: exercise moved to the second section; both internal citations removed; three-way redundancy merged into one Required-to-advance/Stop-condition section; Takeaway confirmed at the end; contentless "Loop taxonomy used here" header folded into a real "Loop taxonomy and hill-climbing safety" section with actual content, not just a pointer.
- **Fixed the confirmed factual error**: removed criterion 2's unsupported clause.
- **Added the legitimate-test-fix exception** to both the module rubric and `.claude/commands/ticket-to-pr-ready.md`.
- **Rewrote Learning Objectives** to state honestly which are gated, partially covered, or not yet hands-on, rather than claim full coverage the core doesn't provide.
- **Linked the reference loop script and clarified what it does and doesn't model**: a retry-and-verify scaffold, not a claim that the fix step itself should be scripted rather than agent-driven.
- **Closed the attempt-counting self-report gap** in `ticket-to-pr-ready.md`: two logged, numbered attempts required, not a narrated count.
- **Softened `ticket-to-pr-ready.md`'s overclaiming** ("very nearly worked" corrected; the single-grader methodological hedge added to Provenance).
- **Added forward guidance** for Extension C's eventual structural enforcement of the hill-climbing review gate.

## Deferred (real, but not fixed this pass)

- Redesigning the core exercise so all four learning objectives are directly hands-on (finding #5) is a bigger content change than this pass; the honest acknowledgment stands until Extensions A and C are authored.
- Extension C's structural review-gate enforcement (finding #8) can't be built until Extension C itself is authored.

## Panel Verdict

The clearest lesson of this run: prior depth of evidence (Module 04 already had the most rigorous dry run of any module) doesn't automatically prevent digestibility drift or factual inconsistency, those are different failure modes than "was the core claim tested," and each needs its own check. The most serious finding, a rubric criterion asserting a behavior its own grading evidence contradicted, was caught by the same discipline this whole workshop teaches: read the actual record, not the summary of it. Fitting, for the module about verification.
