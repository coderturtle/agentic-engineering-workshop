# Workshop Review Panel — Module 01 Content Review

**Date:** 2026-07-03
**Scope:** `modules/01-prompt-engineering/README.md`, `fixtures/receipts/variants/unimplemented/SPEC.md`, `.claude/commands/spec-impl.md`, `runs/2026-07-03-module-01-dry-run/` — real, authored module content, not a design doc.
**Run:** the Workshop Review Panel's (`~/hekton/gremlins/workshop/workshop-review-panel.md`) first run against real module content. The prior run (`2026-07-03-initial-design.md`) only had design docs to work with, before any exercise existed; this run was explicitly logged as a follow-up action, triggered here by the project owner reading Module 01 and describing it as "probably good but not very digestible." Seven personas reviewed independently and in parallel (no persona saw another's critique before writing its own).

This report is the synthesis. Full per-persona critiques are preserved in `docs/review-panel/2026-07-03-module-01-personas/` for anyone who wants the original phrasing rather than the paraphrase.

## Agreements (2+ personas, independently)

### 1. The exercise is buried under front-matter, and internal process leaks into learner-facing prose (Developer Evangelist + Technical Writer)

Both personas, independently, hit the same wall at the same place: a first-time reader crosses five headers (title, "question this module answers," "where it sits in the arc," "learning objectives," "exercise material this module draws from") before reaching the actual task at line 21. The fifth header is the sharpest problem: it promises "material this module draws from" and instead opens with "No external named pattern," then explains why, citing `docs/review-panel/2026-07-03-initial-design.md` by name mid-paragraph. The Developer Evangelist called this "someone's internal review notes by mistake, not an invitation to write a prompt"; the Technical Writer called it "a design rationale for why there's no exercise material... it belongs in `docs/`, not as the last thing a learner reads before the task." This is the direct, confirmed cause of "not very digestible": the content itself isn't the problem, its position on the page is.

**Status: fixed in this pass** (see Actions Taken).

### 2. The module's central pedagogical claim was validated with no negative control (AI/ML Practitioner + Instructional Designer)

The README states: "The discriminator against osmosis is reproducibility: one lucky pass is a plausible output; three-for-three is a specified one." Both personas independently caught the same gap in the evidence behind that claim, from different angles: the AI/ML Practitioner flagged it as weak statistical practice (n=3 has real power to still pass a genuinely unreliable prompt by chance); the Instructional Designer flagged it as a validity gap (the exercise's whole discriminating mechanism was never run against the thing it's supposed to discriminate from — a typical, undisciplined "osmosis-level" prompt). The dry run only ever tested the fully-specified candidate prompt, three times, and it passed all three. Nothing on record shows a naive prompt failing the bar the module claims exists.

**Status: fixed in this pass, and the result was not what the original claim predicted.** The counterfactual was run for real: a deliberately naive prompt, three fresh sessions, same fixture. It also passed 3-for-3. The reason is now understood (the fixture's own docstring already documents the edge cases, so any reasonably diligent agent finds them regardless of the prompt), and the module's claim was corrected to say what was actually shown rather than keep the unsupported original version. See Actions Taken and `runs/2026-07-03-module-01-dry-run/README.md`'s "Counterfactual" section for the full result.

## Single-persona findings (real signal, not gaps between other lenses)

### 3. SPEC.md's own run instructions point at the wrong directory (End-User / Target Learner)

A real, confirmed bug, not a style note: `fixtures/receipts/SPEC.md` and its copy at `fixtures/receipts/variants/unimplemented/SPEC.md` both say `cd fixtures/receipts` under "Running it," but Module 01's exercise runs from inside the `variants/unimplemented/` copy. A learner who follows the module into SPEC.md and then follows SPEC.md's own instructions literally lands in the base fixture (which has a *complete*, if buggy, implementation — a different exercise entirely), not the stub they're supposed to implement against. Verified directly: both files contain the identical hardcoded `cd fixtures/receipts` line.

**Status: fixed in this pass.**

### 4. The takeaway section spoils the exercise on a top-to-bottom read (End-User / Target Learner)

The README's section order (Exercise → Rubric → Required to advance → Takeaway → Stop condition) means a learner reading in order reaches the Takeaway, which links to `.claude/commands/spec-impl.md` and its "why each slot is there" breakdown, before ever attempting the exercise. That breakdown states the winning structural moves outright (name all four edge cases explicitly, run verification before reporting done). For an exercise whose entire point is discovering that structure yourself, reading the page in the obvious order hands you the answer first.

**Status: fixed in this pass**, via the same restructure that fixes finding #1.

### 5. Overclaiming in the takeaway template, four distinct instances (Skeptical Practitioner / Critic)

`.claude/commands/spec-impl.md` states things as measured fact that the evidence doesn't support: "each piece is there because leaving it out was tried and failed during validation" (no ablation was ever run); "the single biggest lever in the validated prompt" (an unranked comparative claim from one undifferentiated 3-run test); "validated 3-for-3" used as blanket endorsement when the dry run's own "What this validates" section only checked 3 of the rubric's 5 criteria; "the agent catches its own near-misses" (no near-miss occurred in any of the three recorded runs).

**Status: mostly fixed in this pass** — the ablation this finding calls for was actually run (see Actions Taken, and finding #2 above, since it's the same missing evidence two personas independently flagged from different angles). Language softened and scoped to what's actually been shown.

### 6. Rubric criterion 2's gate-vs-scored labeling contradicts the rest of the page (Instructional Designer)

Rubric criterion 1 is tagged "(gate)"; criterion 2, reproducibility, is tagged "(scored)" — implying partial credit is possible. But "Required to advance" and "Stop condition" both describe three-for-three in absolute, non-negotiable terms. A grader following the rubric's own labels literally could pass a 2-of-3 attempt on a "scored" item that the rest of the page says isn't a pass at all.

**Status: fixed in this pass.**

### 7. The edge-case rubric criterion is gameable by the exercise's own design (Instructional Designer)

Rubric #3 scores whether the submitted prompt names the four edge cases — but the exercise text itself already lists all four verbatim. A learner can score full marks by copy-pasting the assignment's own enumeration, without practicing edge-case *discovery*, which is arguably the harder and more transferable skill.

**Status: not fixed** — this is a real, structural limitation inherited from the exercise's original design in `docs/coachgremlin-implementation-plan.md` (which also states the four cases explicitly in its own exercise text), not something introduced during authoring. Logged as an honest scope limitation rather than silently redesigning the exercise; see Deferred, below.

### 8. "Green isn't proof" is stated in prose but not carried into the actual workflow (Security-Conscious Reviewer)

The takeaway's own rationale (quoting the Module 04 dry run) acknowledges that a fix can make tests pass while missing the point. But the exercise's success criteria are purely automated (tests pass, three-for-three, no touched test file) — nothing asks the learner to actually look at the generated diff before counting a run as a pass. Not a severe finding (this persona is intentionally lighter-weight), but a real inconsistency between what the module teaches in prose and what its own rubric rewards.

**Status: fixed in this pass** — one line added.

### 9. Statistically thin reproducibility claim, plus a minor portability note (AI/ML Practitioner)

Covered above as part of finding #2 (the reproducibility claim). Separately, minor: `SPEC.md`'s "no external dependencies: stdlib only" elides that `zoneinfo` needs the system IANA tz database, absent on some minimal platforms without the `tzdata` package.

**Status: reproducibility claim fixed per #2. Portability note not fixed** — real but low-severity; logged in Deferred.

### 10. Redundant structure and terminology drift (Technical Writer)

"Required to advance" and "Stop condition" restate the same requirement almost verbatim; "one shot," "single-turn instruction," and "one prompt" are used interchangeably without ever being anchored as synonyms.

**Status: fixed in this pass.**

### Positive findings worth keeping

- **The gate itself is real and unambiguous** (Instructional Designer, End-User/Learner both independently noted this): "Reading this module does not count" leaves no read-and-move-on escape hatch, and the exercise doesn't talk down to the advertised audience.
- **The takeaway template's actual scoping discipline is a good model** (Security-Conscious Reviewer): narrow file access, verification required before reporting done. The finding was that the *lesson* about verification isn't fully carried into the rubric, not that the template itself is unsafe.
- **Voice and brand compliance are clean at the sentence level** (Technical Writer): no banned phrases, no em dashes. The digestibility problem is entirely architectural (what's said where), not tonal (how it's said).
- **The core technical fix (timezone conversion via `zoneinfo`) is correct and well-chosen** (AI/ML Practitioner): a real, common practitioner bug, not a contrived one.

## Actions Taken (this pass)

- **Ran the missing counterfactual for real**, closing findings #2 and #5's shared evidence gap: a deliberately naive prompt (no named edge cases, no file-scope constraint, no verification-before-done instruction) was run against three fresh, independent sessions on the same fixture. **Result: it also passed 3-for-3**, contradicting the module's original claim that a naive prompt drops the edge cases. Root cause: the fixture's target function docstring already documents the edge cases, so a reasonably diligent agent finds them regardless of prompt wording. The module's claim was rewritten to state what was actually demonstrated (reproducibility and explicit scope control) rather than keep the unsupported original. Full method and result: `runs/2026-07-03-module-01-dry-run/README.md`'s new "Counterfactual" section.
- **Restructured `modules/01-prompt-engineering/README.md`**: exercise moved to appear immediately after the framing intro, ahead of the osmosis-problem discussion; the internal review-panel citation removed from learner-facing prose (the underlying reasoning kept, the audit-trail citation cut); Takeaway section moved to the end of the page, after Stop Condition, with an explicit note not to read it before a first attempt; "Required to advance" and "Stop condition" merged into one section; terminology standardized on "one prompt."
- **Fixed the wrong-directory bug** in `fixtures/receipts/SPEC.md` and its copy in `variants/unimplemented/`: "Running it" no longer hardcodes `cd fixtures/receipts`; it now says to run from whichever directory contains that copy of `SPEC.md`.
- **Softened `.claude/commands/spec-impl.md`'s overclaiming language**: "tried and failed during validation" and "the single biggest lever" reworded to what the (now expanded) evidence actually supports; "validated 3-for-3" scoped explicitly to which rubric criteria were checked; "catches its own near-misses" reworded to state the mechanism without claiming an unobserved event.
- **Fixed rubric criterion 2's gate-labeling**: now tagged as a gate, matching the absolute language used elsewhere on the page.
- **Added a line** to the rubric addressing finding #8: skim the diff, not just the test result, before counting a run as a pass.
- **Added fixture-reset instructions**: a short note on how to get a genuinely fresh copy for each of the three runs.

## Deferred (real, but not fixed this pass)

- Finding #7 (edge-case criterion gameability) is a structural property of the exercise's original design, not this authoring pass; redesigning it is a bigger change than a content fix and would need to happen alongside a review of whether Module 02 (which reuses this exact task) inherits the same limitation.
- The `zoneinfo`/`tzdata` portability note (finding #9) is real but low-severity; worth a one-line addition to `SPEC.md` in a future pass, not urgent enough to hold this one.
- The same "internal citation leaks into learner content" pattern (finding #1) exists in Module 04's README too (the Technical Writer noted this explicitly as a house habit, not a one-off). Not fixed here to keep this pass scoped to Module 01; logged as a candidate for a small cross-module style pass, or a `docs/brand.md` rule making it explicit.

## Panel Verdict

The panel's first run against real content did exactly what it's for: found the actual cause of "not very digestible" (two personas independently converged on the same structural diagnosis, not seven versions of the same complaint), caught a real functional bug (the wrong-directory instruction) that a prose-only review would likely have missed, and surfaced a genuine evidence gap in the module's central claim that got closed with a real experiment rather than a word change. No finding was averaged away. One finding (#7) is logged as a real, acknowledged limitation rather than silently patched, which is itself the kind of honesty this workshop's brand voice asks for.
