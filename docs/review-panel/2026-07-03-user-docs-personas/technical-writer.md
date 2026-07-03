# Persona: Professional Technical Writer / Editor — User Docs — 2026-07-03

**1. `modules/README.md` — internal audit-trail citations leak straight into learner-facing prose, the exact pattern flagged in all five module reviews.** The "Content status" blockquote was a single 250+ word run-on sentence citing `docs/coachgremlin-implementation-plan.md`, `docs/review-panel/2026-07-03-module-NN-content.md`, and `docs/next-actions.md`, narrating internal review history a learner has no use for. This is maintainer/QA voice, not the "competent peer" voice `docs/brand.md` specifies, and it sat directly above the arc table a first-time visitor actually needs.

**2. Real (not just stylistic) inconsistency in "what you keep" across the three docs.** Module 02's takeaway is a "context-budgeting **Skill**" in `README.md` and `modules/README.md`, but a "context-budgeting **checklist**" in `site/index.astro`, different artifact types, not a wording variant. Module 03 is "a real sub-agent **or harness config**" in `README.md` and "sub-agent/harness-config definition" in `modules/README.md`, but narrows to just "a bounded sub-agent definition" on the site, silently dropping the harness-config option. A reader comparing pages would reasonably wonder which is accurate.

**3. Hypothesis framing diverges in wording.** `README.md`: "Our working **hypothesis**, not a settled finding." `index.astro`: "This is a **bet**, not a settled finding." Same brand-mandated disclaimer, different vocabulary for the same claim, minor but avoidable given both quote the identical rule.

**4. Site is vaguer than both its source and README about which module the preview covers.** `README.md` and `docs/sample-attempt-preview.md` both name "Module 04" explicitly; `index.astro` said only "one of the modules."

**5. README's "linked from the same page" overstated what `sample-attempt-preview.md` does**, the raw transcript path was given as inline code, not an actual hyperlink.

No em dashes or banned phrases found in any of the four files; brand hard-rule compliance is otherwise solid.
