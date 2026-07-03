# Workshop Review Panel — Module 05 Content Review

**Date:** 2026-07-03
**Scope:** `modules/05-synthesis-capstone/README.md`, `fixtures/receipts/variants/sabotaged-harness/` and `sabotaged-loop/`, `.claude/skills/diagnose-agent-failure/SKILL.md`, `runs/2026-07-03-module-05-dry-run/`.
**Run:** the panel's sixth and final real-content run for this authoring pass (after design docs, Modules 01-04). Seven personas reviewed independently and in parallel.

Full per-persona critiques: `docs/review-panel/2026-07-03-module-05-personas/`.

## Agreements (2+ personas, independently)

### 1. The exact digestibility pattern from Modules 01-04, unfixed here too (Developer Evangelist + Technical Writer)

Both independently confirmed: exercise buried under four orientation headers; an internal review-panel citation naming a specific persona in learner prose; three-way redundant restatement of the terminal-state requirement; Takeaway before Stop condition with a redundant audit-trail citation appearing twice. Module 05 was authored in the same session as Module 04, before any of these fixes existed as a template, so it inherited none of them.

**Status: fixed in this pass**, matching the restructure applied to Modules 01-04.

### 2. Two independent personas found the same real fixture bug: a scope reference to a directory that doesn't exist (AI/ML Practitioner + End-User/Learner)

`sabotaged-harness/harness-config.md` scopes edits to `docs/`, but no `docs/` directory shipped in the fixture at all. A learner (or an agent) listing the repo discovers this instantly, no isolating test required, which undercuts the "genuine ambiguity" the module leans on to justify this variant's design. Caught by two personas from different angles: technical rigor (AI/ML Practitioner) and a learner's actual first move (End-User/Learner, who called it "a real, findable red herring once you know to look at scope" while also flagging it broke the intended challenge).

**Status: fixed in this pass** — a real, plausible-but-irrelevant `docs/contributing.md` added so the wrong scope constrains something real.

## Single-persona findings

### 3. The fixture's own context files spoiled the diagnosis by confessing to being red herrings (Skeptical Practitioner / Critic)

`background.md` ended with "None of the above is required to diagnose the current bug"; `prompt.md` ended with "It isn't, on its own, enough to fully explain why this setup fails to reach done." Both are read by the learner during the exercise, not internal notes. This is the identical self-announcing-noise failure Module 02's panel run found and fixed in that module's bloated variant, recurring here independently.

**Status: fixed in this pass** — both confessions stripped from both files (they're shared, byte-identical, across both variants).

### 4. "Ruled out the prompt" for the loop variant was inferred, not observed (Skeptical Practitioner / Critic)

The defense's fix was hand-applied directly to the code, never produced by an agent actually working from `sabotaged-loop`'s real, informal prompt. The claim that "the informal wording never blocked a correct fix" hadn't actually been tested against an agent following that wording.

**Status: fixed in this pass, with a real experiment, not a word change.** Ran a fresh subagent against the actual prompt and correctly-scoped harness config, independently reverified. It fixed the bug correctly, and explicitly reported the informal phrasing caused no real difficulty, since the module docstring and the one failing test made the fix unambiguous. This is now genuine evidence for the "not the prompt" claim, not an inference.

### 5. Asymmetric verification depth between the two variants, not disclosed (AI/ML Practitioner)

Sabotaged-harness got a full agent attempt; sabotaged-loop's original verification was a hand-patch. The module's "Content status" line described both as equally "confirmed via an actual isolating test" without distinguishing.

**Status: fixed by finding #4's fix** — both variants now have genuine agent-driven verification; the asymmetry no longer exists to disclose.

### 6. The "compose all four layers" claim doesn't survive contact with what's built (Instructional Designer)

Prompt and context are byte-identical, permanent, ruled-out-by-inspection controls in both shipped variants; only harness and loop are ever live hypotheses. A learner who skipped Modules 01/02 could complete either variant unaffected, since ruling out prompt/context takes no skill from those modules, just reading two unchanged files.

**Status: acknowledged honestly, not silently fixed.** Added an explicit "Where it sits in the arc" scope note stating the capstone currently composes two of four layers as live diagnoses, not four, until the deferred prompt- and context-bottleneck variants exist. Also softened the Takeaway's "not written from theory" claim to scope it to the two layers actually diagnosed.

### 7. Mechanics were left abstract: no worked example, no assignment mechanism, no explicit layer-to-file mapping, and running `loop.sh` unmodified doesn't demonstrate anything by itself (End-User / Target Learner)

Four separate but related usability gaps, all confirmed on inspection: nothing said how a learner gets assigned a variant; "instrument it" and "isolate in a throwaway" had no concrete first step; the file-to-layer correspondence (`harness-config.md` = harness, `loop.sh` = loop) was implicit; and the exercise's own "runs `./loop.sh` to `TERMINAL STATE: FAILURE`" line reads like the script demonstrates the bug, when it only shows the symptom.

**Status: fixed in this pass** — added a concrete assignment suggestion, an explicit file-to-layer mapping, and a clarifying paragraph on what running the unmodified loop does and doesn't show.

### 8. The diagnostic method has no check for a fix introducing a new problem, and no posture for ambiguous evidence (Security-Conscious Reviewer)

Both real, general training-shape gaps in the takeaway Skill: "the symptom cleared" isn't the same claim as "nothing new broke," and the method assumes a clean single-cause world with no guidance for genuinely inconclusive evidence.

**Status: fixed in this pass** — two new steps added to `.claude/skills/diagnose-agent-failure/SKILL.md`: checking the fix didn't trade one failure for another, and reporting honestly when evidence doesn't cleanly clear a layer instead of forcing a confident-sounding verdict.

### 9. Rubric criteria 3 and 6 substantially overlap in practice (Instructional Designer)

Both effectively re-test "did the defense properly attribute the cause," from slightly different angles.

**Status: acknowledged, not merged** — kept distinct since they test different things in general (evidence for exclusion vs. correct framing of the cause), even though this run's own defense document restates similar ground for both; logged rather than force a merge that would lose the general-case distinction, consistent with how Module 04 handled its own criteria 3/4 overlap.

### Positive findings worth keeping

- **The core diagnostic logic is sound and the two root causes are cleanly separable** (AI/ML Practitioner): no coincidental-fix risk in either shipped variant, confirmed on inspection.
- **The Extensions/deferred-variant framing was already honest about being incomplete** (multiple personas implicitly): the gap was in the surrounding claims overselling completeness, not in hiding that two variants are still unbuilt.
- **Voice and brand compliance clean at the sentence level** (Technical Writer): the sixth and final confirmation that this workshop's recurring content problem across the whole panel run has been structural placement and evidence scope, not writing quality.

## Actions Taken (this pass)

- **Restructured `modules/05-synthesis-capstone/README.md`**: exercise moved to the second section; internal citation removed; three-way redundancy merged; Takeaway moved to the end; added a concrete assignment mechanism, file-to-layer mapping, and a clarification of what the unmodified loop script does and doesn't show.
- **Fixed a real fixture bug**: added a genuine `docs/` directory to `sabotaged-harness/` so its wrong scope constrains something real instead of pointing at a phantom path.
- **Fixed a second real fixture bug**: stripped self-spoiling confessions from `background.md` and `prompt.md` (shared by both variants), the same failure mode Module 02's panel run found independently in a different module.
- **Closed a real evidence gap with a new experiment**: ran a fresh agent against `sabotaged-loop`'s actual prompt and correctly-scoped harness, confirming "not the prompt" with observation rather than inference, and closing the asymmetric-verification gap between the two variants in the same step.
- **Corrected the "compose all four layers" overclaim** with an honest scope note, and scoped the Takeaway's "not written from theory" claim to the two layers actually diagnosed.
- **Added two new steps to `.claude/skills/diagnose-agent-failure/SKILL.md`**: check the fix didn't create a new problem; report honestly when evidence is genuinely ambiguous instead of forcing a verdict.

## Deferred (real, but not fixed this pass)

- The prompt-bottleneck and context-bottleneck variants remain unbuilt; until they exist, the capstone's "compose all four" framing stays honestly scoped to two, not silently upgraded back to four.
- Rubric criteria 3/6 overlap (finding #9) is logged, not merged, consistent with how the same class of overlap was handled in Module 04.

## Panel Verdict

The two most serious findings this run, a fixture referencing a nonexistent directory and fixture text that literally confessed to being a red herring, are exactly the kind of thing that's invisible to whoever built the fixture (both read as "obviously fine" from the builder's seat) and immediately visible to an independent read. Both got fixed with real changes to the actual fixture files, and one finding (the loop variant's untested "ruled out the prompt" claim) got closed with a genuine new agent run rather than a rewritten sentence, the same evidentiary standard this whole panel series has held every prior module to. With this run, all five modules have now been through the panel against real content, not just design docs.
