# Workshop Review Panel — User-Facing Entry-Point Docs Review

**Date:** 2026-07-03
**Scope:** `README.md` (top-level), `modules/README.md` (arc index), `site/src/pages/index.astro` (deployed site guide page), `docs/sample-attempt-preview.md`. Deliberately excludes internal/maintainer docs (`docs/workshop-design.md`, `docs/brand.md`, `docs/decisions.md`, etc.) and the build-log journal, which serve a different purpose.
**Run:** the panel's seventh real-content run (after design docs and five module-content runs). Seven personas reviewed independently and in parallel. This run's distinguishing feature: cross-document consistency mattered more than any single module review, since these four documents describe the same workshop from different angles and need to agree with each other.

Full per-persona critiques: `docs/review-panel/2026-07-03-user-docs-personas/`.

## Agreements (2+ personas, independently)

### 1. README.md and the site guide page duplicate almost entirely, with no cross-linking or sequencing agreement (Developer Evangelist + End-User/Learner + Instructional Designer)

Three personas converged on overlapping facets of the same problem. The Developer Evangelist found the two documents reproduce the same thesis, runbook, and "see it in action" pitch nearly verbatim, with no differentiation of purpose. The End-User/Learner found neither document links to the other, so a visitor landing on one has no signal the other exists. The Instructional Designer found the two documents actually *disagreed* on internal sequencing: README puts "See it in action" before "How to start"; the site put its equivalent section *after* the clone-and-start runbook, undermining its own "before you clone anything" heading.

**Status: fixed in this pass.** Reordered the site to match README's sequencing; added a one-line differentiation note to each pointing at the other's actual role (site = entry point for deployed-site visitors; README = the detailed version once cloned).

### 2. `modules/README.md`'s Content status blockquote repeats the exact internal-citation-leak pattern found in all five module reviews (AI/ML Practitioner + Technical Writer)

A 250+ word run-on sentence citing `docs/coachgremlin-implementation-plan.md`, five separate `docs/review-panel/2026-07-03-module-NN-content.md` reports, and `docs/next-actions.md`, narrating the panel's own review history directly above the arc table a first-time visitor needs. The exact defect five separate module-level fixes already addressed, recurring at the arc-index level, which had never been directly reviewed before this run.

**Status: fixed in this pass** — condensed from 250+ words to two sentences; the detail moved to where it belongs (each module's own README, `docs/decisions.md`, and the review-panel reports themselves).

## Single-persona findings

### 3. The "compose/diagnose all four layers" claim is stale in three of four in-scope docs (AI/ML Practitioner)

`README.md`, `modules/README.md`'s arc table, and `site/index.astro` all state the capstone diagnoses "which of the four" layers, contradicting Module 05's own honest scope note (added in the prior panel run) that only two of four layers currently have a built, live-hypothesis scenario.

**Status: fixed in this pass** in all three documents, with a consistent, honest scope note.

### 4. A real factual inconsistency in "what you keep," not just wording (Professional Technical Writer)

Module 02's takeaway was a "Skill" in two documents and a "checklist" in the third; Module 03's takeaway was "sub-agent or harness-config definition" in two documents and narrowed to just "sub-agent definition" on the site.

**Status: fixed in this pass** — site's wording aligned to match `modules/README.md`, the source of truth.

### 5. modules/README.md referenced a path on the maintainer's local machine, unresolvable for anyone who cloned the repo (End-User/Learner)

`~/hekton/gremlins/workshop/workshop-lifecycle.md` is outside this repository entirely. A learner following that reference from a fresh clone gets nothing.

**Status: fixed in this pass** — removed; the substantive point (why takeaways are a standing principle) didn't need the external citation to stand on its own.

### 6. An unhedged outcome claim on the site directly violates `docs/brand.md`'s own rule, one section after the page correctly hedges a different claim (Skeptical Practitioner / Critic)

"You get practiced judgment..." stated as settled fact, immediately after "This is a bet, not a settled finding" for a related claim on the same page.

**Status: fixed in this pass** — reworded to state what the exercises are designed to produce, with a pointer to each module's own evidence, rather than assert the outcome as guaranteed.

### 7. "Not cherry-picked" overclaims what's actually true (Skeptical Practitioner / Critic)

The featured transcript (the successful attempt) was a choice; the text itself wasn't edited. "Not cherry-picked" claims more than "not edited."

**Status: fixed in this pass** — reworded to the accurate, available claim, and pointed directly at the gaming attempt that exists alongside it, so the choice is disclosed rather than implied away.

### 8. Dead-end "Build in public" mention with no link (Developer Evangelist, independently confirmed by End-User/Learner)

Named the GitHub Pages journal but gave no URL.

**Status: fixed in this pass** — added the real URL. Will 404 until the first live deploy is human-confirmed (already a tracked, pending action; not a new problem introduced here).

### 9. Hands-on-by-design not stated in the top-level README (Instructional Designer)

The principle appeared in `modules/README.md` and the site, not in the document most learners hit first.

**Status: fixed in this pass** — added directly to README's opening framing.

### 10. Module 01's arc-table gate description undersold its actual reproducibility requirement (Instructional Designer)

Said "first try" without mentioning the three-clean-run requirement that's an actual named gate in the module itself.

**Status: fixed in this pass.**

### 11. "Report it" had no destination (Instructional Designer)

No issues link, no CONTRIBUTING reference anywhere in scope.

**Status: fixed in this pass** — both README and the site now point to the real GitHub issues URL.

### 12. Minor wording/precision fixes, all applied (Technical Writer, Instructional Designer)

Hypothesis-vs-bet wording aligned; the site now names Module 04 explicitly instead of "one of the modules"; README's "linked from the same page" corrected to an actual link.

### 13. A dead link that will resolve once this branch merges, not a content bug (Security-Conscious Reviewer)

The site's `sample-attempt-preview.md` blob link targets `main`; the file only exists on the current working branch. Flagged as a pre-deploy checklist item, not fixed here since it resolves automatically at merge.

**Status: logged, not fixed** (nothing to fix; it's a sequencing dependency, not an error).

### Positive findings worth keeping

- **The actual clone-to-Module-01 critical path was intact throughout**: every link on the direct "clone → modules/README.md → 01-prompt-engineering/README.md" path resolved correctly even before this pass (End-User/Learner).
- **No unsafe setup instructions anywhere in scope** (Security-Conscious Reviewer): clean git clone commands, no curl-pipe-to-shell, no elevated permissions.
- **`modules/README.md`'s per-module evidence claims, once trimmed, are a model of "prove it" writing** (Skeptical Practitioner / Critic): concrete, falsifiable, evidence-linked, exactly the standard the site's outcome claim needed to be held to.
- **`docs/sample-attempt-preview.md` is the strongest single asset in scope** (Developer Evangelist): real, credible, and under-promoted relative to its value, addressed in this pass by giving it a more prominent, correctly-sequenced placement on both entry points.

## Actions Taken (this pass)

- Reordered the site guide page to match README's sequencing (sample preview before the runbook, not after).
- Condensed `modules/README.md`'s Content status blockquote from a 250+ word internal-review narration to two sentences.
- Corrected the "diagnose/compose all four layers" claim to an honest two-of-four scope note in `README.md`, `modules/README.md`, and `site/index.astro`.
- Aligned the "what you keep" wording for Modules 02 and 03 across all three documents.
- Removed the unresolvable `~/hekton` path reference from `modules/README.md`.
- Hedged the site's unhedged outcome claim per `docs/brand.md`'s own rule.
- Corrected "not cherry-picked" to the accurate, available claim, and disclosed the gaming attempt that exists alongside the featured transcript.
- Added the real GitHub Pages URL to README's "Build in public" section.
- Added a hands-on-by-design statement to README's opening framing.
- Corrected Module 01's arc-table gate description to name its reproducibility requirement.
- Added real GitHub issues links to both README and the site for "report it."
- Minor: aligned hypothesis/bet wording, named Module 04 explicitly on the site, fixed README's false "linked" claim into an actual link.

## Deferred (real, but not fixed this pass)

- The site's sample-preview blob link will 404 until this branch merges to `main`; already tracked in `docs/next-actions.md` as a standing "push once reviewed" item, not a new one.
- Whether README.md and the site guide page should be more substantially differentiated (not just cross-linked) rather than remain two similar entry points is a bigger editorial decision than this pass; the fix here makes the overlap honest and navigable, not smaller.

## Panel Verdict

This run's real value was catching problems that only exist *across* documents, a factual inconsistency invisible from reading any one file alone (the takeaway-type mismatch), a stale claim that one document's own honest update (Module 05's scope note) had already outdated in three others, and a sequencing disagreement between two pages that individually looked fine. Single-document review, even careful single-document review, wouldn't have caught most of this; it took checking the same claim across four places at once. Combined with the five module runs, every piece of user-facing content in this repository has now been through an independent review pass.
