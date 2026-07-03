# Persona: Professional Technical Writer / Editor — Module 01 — 2026-07-03

**1. The exercise is buried under authorial throat-clearing.** A first-time reader hits five headers — title, "question this module answers," "where it sits in the arc," "learning objectives," "exercise material this module draws from" — before reaching the actual task at line 21. Worse, that fifth header promises "material this module draws from" and then immediately says there isn't any: "No external named pattern... **The osmosis problem:**..." (line 19). That's not exercise material, it's a design rationale for why there's no exercise material. It belongs in `docs/`, not as the last thing a learner reads before the task.

**2. Meta-references to internal process leak into learner-facing prose.** Line 19: "(flagged by the Workshop Review Panel's Instructional Designer; see `docs/review-panel/2026-07-03-initial-design.md`)." The takeaway section similarly cites `.claude/commands/spec-impl.md` and `runs/2026-07-03-module-01-dry-run/` as validation evidence (line 43). These are audit-trail citations, useful to the project owner, meaningless and distracting to someone doing the exercise. Module 04 has the identical pattern (line 22, line 57), so this is a house habit, not a one-off — worth a single style rule rather than a per-module fix.

**3. Redundant structure disorients rather than reinforces.** "Required to advance" (lines 37-39) and "Stop condition" (lines 45-47) restate the same three-run, no-correction-turn, no-test-file requirement almost verbatim, with only the "valid alternate terminal" clause differing. A reader has to diff the two paragraphs to confirm they're not subtly different rules.

**4. Sentence density peaks exactly where clarity matters most.** Line 19's key sentence stacks a claim, a consequence, and a citation: "an advanced practitioner already writes decent prompts daily, so this exercise has to establish a genuinely new capability, not review what daily use already teaches (flagged by...)." Three ideas, one sentence, and the parenthetical is the least important one — yet it's structurally central.

**5. Minor terminology drift.** "one shot" (heading), "single-turn instruction" (objectives), and "one prompt" (exercise body) are used interchangeably for the same concept without ever being anchored as synonyms, which risks a learner treating them as distinct requirements.

**Positive note:** no banned phrases, no em dashes, voice matches the "competent peer" register well at the sentence level — the problem is entirely architectural, not tonal.
