# Workshop Review Panel — Module 02 Content Review

**Date:** 2026-07-03
**Scope:** `modules/02-context-engineering/README.md`, `fixtures/receipts/variants/bloated/`, `scripts/generate-bloated-variant.py`, `scripts/context-budget.sh`, `.claude/skills/context-budgeting/SKILL.md`, `runs/2026-07-03-module-02-dry-run/`.
**Run:** the panel's third real-content run (after the initial design-doc pass and Module 01). Seven personas reviewed independently and in parallel.

Full per-persona critiques: `docs/review-panel/2026-07-03-module-02-personas/`.

## Agreements (2+ personas, independently)

### 1. The exercise is buried again, the exact defect Module 01 had before its restructure (Developer Evangelist + Technical Writer)

Both personas independently noted that Module 02 reads like the pre-fix version of Module 01: the exercise sits behind four to five headers of framing, and an internal citation to the prior review-panel report ("This module had no exercise anchor at all before the Workshop Review Panel's Instructional Designer flagged the gap...") leaks into learner-facing prose. This is the identical failure mode Module 01's restructure removed; it simply wasn't carried over to Module 02 when that fix happened.

**Status: fixed in this pass.**

### 2. The noise self-announces itself, which defeats the exercise's actual premise (AI/ML Practitioner + End-User/Learner)

The most serious finding of this run. Both personas, independently, discovered that every noise file in `fixtures/receipts/variants/bloated/` literally confessed to being noise: `config/tax_rates.yaml` opened with a comment reading "Red herring... group_expenses_by_month never reads this file"; `legacy_export.py`'s docstring said "A red herring by inclusion... it looks like it might matter to a nervous reader and does not"; every stale doc opened with "Stale, predates the current CLI. Not maintained"; the README said outright "Kept here as historical bloat for Module 02." The End-User/Learner persona's verdict: "I'd curate this in under two minutes by grepping for the word 'unrelated,' which isn't the skill the module claims to be teaching." This wasn't a a digestibility problem, it was a validity problem: the exercise was solvable by pattern-matching a label, not by the curation judgment it claims to test.

**Status: fixed in this pass, with real engineering, not a word change** (see Actions Taken).

## Single-persona findings

### 3. Line-count budget is a weaker proxy for context pressure than the module treats it as (AI/ML Practitioner)

Measured directly: `config/tax_rates.yaml` runs at 24 chars/line, `README.md` at 51, `CHANGELOG.md` at 53, over 2x variance in token density per line within the same fixture. The rubric's gate is lines-only; a curator could stay "under budget" on lines while carrying more actual token weight than a curator who didn't.

**Status: not fixed.** A real fix means changing the gate to a token-based budget (or a combined line-and-token gate), which is a bigger rubric change than this pass's scope; logged in Deferred.

### 4. "Necessary inclusion" and "the red herring is genuine" were both asserted, not demonstrated with a negative control (Skeptical Practitioner / Critic)

The dry run shows one successful 182-line curation; nothing shows what happens if a load-bearing file is cut (does the task actually fail?) or if the red herring is included (does it actually mislead a model, or is it just extra bytes?). Also: the budget was never pressure-tested near its boundary (182/2000 lines, 9% utilization).

**Status: not fixed this pass** — a full negative-control run (deliberately cut something load-bearing, confirm failure; deliberately include the red herring in a naive curation, confirm it actually misleads) is real, valuable additional verification, but a larger scope of new experimentation than this pass's budget. Logged in Deferred.

### 5. The cumulative hook (reusing Module 01's actual prompt) was narrative, not mechanically enforced (Instructional Designer)

The README claimed "you already hold a proven prompt from Module 01," but the exercise text never told the learner to use that specific prompt, and nothing in the rubric checked prompt provenance. A learner writing a fresh prompt from scratch satisfied the exercise identically.

**Status: fixed in this pass** — the exercise now explicitly instructs bringing the saved Module 01 prompt/takeaway forward.

### 6. Rubric criteria 3 and 4 substantially overlapped (Instructional Designer)

"Necessary inclusion" and "justified exclusion" were checking largely the same thing from two directions; a grader checking one had mostly already checked the other.

**Status: fixed in this pass** — merged into one criterion with the verbatim requirement and the write-up folded together; the noise-exclusion check kept separate since it's testing something distinct (that noise wasn't partially smuggled in).

### 7. Objective 2 (summarize-vs-cut judgment) isn't actually exercised by the validated solution (End-User / Target Learner)

The minimum viable curation (182 lines) is pure inclusion/exclusion; no summarization was needed to hit the budget.

**Status: acknowledged honestly, not fixed** — added a note to the Learning Objectives section saying so directly, rather than silently claim the objective is fully tested. A tighter-budget or messier-content variant would be needed to force real summarization judgment; logged in Deferred.

### 8. Curation/reset mechanics and `context-budget.sh` usage weren't explained on the page (End-User / Target Learner)

Unlike Module 01 (which explicitly says to recopy into a scratch directory for each fresh attempt), Module 02 didn't repeat the instruction, and never showed a sample invocation of the measurement script.

**Status: fixed in this pass.**

### 9. The context-budgeting Skill's "cut anything not in the verification path" heuristic has no security carve-out (Security-Conscious Reviewer)

Portable advice that doesn't generalize safely: auth/validation/permission code is often untouched by the specific test in scope but shouldn't be cut on that basis alone.

**Status: fixed in this pass.**

### 10. Minor: "9,289 lines of noise" mislabeled the fixture's total size as pure noise (End-User / Target Learner)

Off by roughly the 230 real lines of spec and code included in the total.

**Status: fixed in this pass** — corrected to the precise real/noise split, recalculated after the noise regeneration (9,286 total, 231 real, 9,055 noise).

### Positive findings worth keeping

- **Curation necessity checked out on inspection** (AI/ML Practitioner): the 182-line curated set really is the load-bearing minimum; cutting `cli.py` was a correct call, independently verified against what the test suite actually imports.
- **The hands-on gate is real and unambiguous** (Instructional Designer): concrete artifacts required, no read-and-move-on escape hatch.
- **Voice and brand compliance clean at the sentence level** (Technical Writer): the digestibility problem was structural, not tonal, same pattern as Module 01.

## Actions Taken (this pass)

- **Rewrote `scripts/generate-bloated-variant.py`** to remove every self-announcing tell from the generated noise (the README, CHANGELOG, `legacy_export.py`, stale docs, and tax-rate config no longer say "red herring," "stale," "historical bloat," "unrelated to the receipts CLI's current scope," or similar). Regenerated `fixtures/receipts/variants/bloated/` (9,286 lines) and reverified the whole exercise pipeline end to end: still fails cleanly unimplemented, still measures over budget, the existing 182-line curated set (untouched, since it never included any noise files) still passes under budget. Confirmed directly with `grep` that none of the removed tells remain in the noise files.
- **Restructured `modules/02-context-engineering/README.md`**: exercise moved to the second section; internal review-panel citation removed; curation/reset mechanics and a sample `context-budget.sh` invocation added; the cumulative hook made mechanically real (the exercise now says to bring your saved Module 01 prompt forward, not just asserts you have one); Required-to-advance and Stop-condition merged; Takeaway moved to the end.
- **Merged rubric criteria 3 and 4** into one, removing the overlap the Instructional Designer flagged; kept the noise-exclusion criterion separate since it tests something distinct.
- **Added an honest note to Learning Objectives** acknowledging that this fixture's minimum curation doesn't force summarization judgment, rather than let the objective claim more than the exercise delivers.
- **Fixed the noise/real line-count mislabeling** with the precise post-regeneration split.
- **Added a security carve-out** to `.claude/skills/context-budgeting/SKILL.md`'s cut heuristic, and softened its "which is most of the time" overclaim.

## Deferred (real, but not fixed this pass)

- Line-count-only budget gate (finding #3): a token-aware gate would be more accurate; bigger rubric change than this pass's scope.
- Negative-control verification (finding #4): proving the red herring actually misleads, and that cutting a load-bearing file actually breaks the task, is real additional evidence worth generating, but a larger new experiment than restructuring content; a candidate for a future dry-run addendum.
- A tighter-budget or messier-content variant that would force genuine summarize-vs-cut judgment (finding #7's honest gap) is a content-design change, not a quick fix.

## Panel Verdict

The most valuable finding this run wasn't a wording problem, it was a validity problem: two personas independently discovered the fixture's noise gave away the answer to the exercise it was supposed to test. That's exactly the kind of thing a single-lens review or a self-check is likely to miss (the noise files read as "obviously fake" to whoever built them, which is precisely why a fresh, independent read catches what a builder's read doesn't). Fixed with real engineering, not a rewrite of claims: the generator script itself was corrected and the fixture regenerated and reverified end to end. Two findings (line-count-only budget, negative-control verification) are logged as real and deferred rather than quietly ignored.
