# Workshop Review Panel — Module 05 Prompt/Context Variants Content Review

**Date:** 2026-07-04
**Scope:** `modules/05-synthesis-capstone/README.md`'s updated sections (the new "Why prompt and context aren't live variants here," the required-exercise disambiguation note, the honest scope note), `modules/README.md`'s Module 05 references, and the two new fixture variants (`fixtures/receipts/variants/sabotaged-prompt/`, `sabotaged-context/`) plus their run evidence.
**Run:** a scoped, three-persona run (Skeptical Practitioner/Critic, Instructional Designer, End-User/Learner), matching the "scoped re-run for a judgment-call pass" pattern rather than the full seven, since this content documents a finding rather than introducing a new exercise arc.

## Agreements / consistent findings

None of the three findings below were flagged by more than one persona independently, but all three converged on the same underlying gap: the honest finding was well-argued in prose but under-supported by the surrounding structure (positioning, filesystem, evidence visibility).

## Findings

### 1. Run count was wrong: "9" stated, actual count is 10 (Skeptical Practitioner/Critic)

Counted directly against the run directories (5 in each of `runs/2026-07-04-module-05-sabotaged-prompt-dry-run/` and `runs/2026-07-04-module-05-sabotaged-context-dry-run/`). An unverified number undermining the exact claim ("we were rigorous, here's the count") it exists to support.

**Status: fixed.** Corrected to 10 throughout, with an inline table breaking down which runs went where.

### 2. "Regardless of how the misdirection is worded" overreached past the tested evidence (Skeptical Practitioner/Critic)

The underlying run READMEs explicitly hedge this ("does not validate that no prompt-level attack can defeat this fixture/agent combination, only that two attempts, of two different shapes, both failed"); the module's synthesis had smoothed that hedge away into a universal claim.

**Status: fixed.** Reworded to "real evidence the pattern holds here, not proof it holds everywhere... demonstrated for this fixture family, not... a universal law."

### 3. No in-directory marker distinguishing required vs. negative-control variants (Instructional Designer)

`ls fixtures/receipts/variants/` shows all four sabotage directories as visual peers; the disambiguating prose lives only in the module README, 30+ lines after the point a learner following "read every file" would browse the directory.

**Status: fixed.** Added `NOT-A-REQUIRED-EXERCISE.md` inside both `sabotaged-prompt/` and `sabotaged-context/`, plus an early flag in the module README's required-exercise section itself, before a skimmer would reach the fixture folder.

### 4. No hands-on action for the optional content (Instructional Designer)

The section recited the finding rather than inviting the learner to reproduce any part of it, in tension with the module's own "if a module ever reduces to read this, then move on, that's a defect" standard, even though this section is explicitly non-required.

**Status: fixed.** Added a concrete five-minute "try it yourself" action: point your own fresh agent at `sabotaged-prompt/` and watch whether it catches the misdirection.

### 5. Section buried between required exercise and Learning Objectives, at the same visual weight as instructions (End-User/Learner)

A skimming learner hits four fixture directory names before the module unambiguously says only two are "pick one."

**Status: fixed.** Added the early disambiguation note in the required-exercise section; moved the full section to after Learning Objectives and relabeled it "(optional reading, not required)"; added a one-line framing ("the most conceptually load-bearing paragraph in the capstone, not a footnote") since the End-User/Learner persona found the content itself was strong, just positioned like trivia.

### 6. Claim asserted without inline evidence a skimming learner would actually see (End-User/Learner)

"9 [now 10] independent runs" and "every single run" were citations to two other files, not evidence shown on the page itself.

**Status: fixed.** Added the inline breakdown table (variant, sabotage design, run count, outcome) directly in the module README, so the claim doesn't require leaving the page to spot-check.

### 7. Arc-level structural/behavioral framing sat adjacent to the finding, not integrated with it (Instructional Designer)

The module's official structural/behavioral theory (from `docs/workshop-design.md`) and the new finding's actual mechanism (a trust contest an agent's diligence wins) were stated near each other without being explicitly connected.

**Status: fixed.** The rewritten section now explicitly maps the finding onto that framing: harness/loop are structural (mechanical, unaffected by what the agent knows), prompt/context are behavioral (single-turn, only work if trusted over everything else readable), which is why one resists sabotage differently than the other.

## Not acted on

- The Skeptical Practitioner/Critic's confirmation that positive evidence (harness/loop correctness) and the "don't pick these" disambiguation were both already clean required no further action.
