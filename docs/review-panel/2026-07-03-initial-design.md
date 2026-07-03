# Workshop Review Panel — Initial Design Review

**Date:** 2026-07-03
**Scope:** `README.md`, `docs/workshop-design.md`, `docs/workshop-gremlin-design.md`, `docs/implementation-plan.md` — design docs only; no module content exists yet.
**Run:** first-ever test run of the Workshop Review Panel (`~/hekton/gremlins/workshop/workshop-review-panel.md`), run before the Gremlin was added to the Workshop Gremlin's roster. Seven personas reviewed independently and in parallel (no persona saw another's critique before writing its own).

This report is the synthesis. Full per-persona critiques are preserved in `docs/review-panel/2026-07-03-personas/` for anyone who wants the original phrasing rather than the paraphrase.

## Agreements (2+ personas, independently)

### 1. Current-state docs still say the name is "pending" — but it isn't (Developer Evangelist + Technical Writer)

The naming pass completed and the rename was executed, but the prose in `README.md`, `docs/workshop-design.md`, `docs/workshop-gremlin-design.md`, and `docs/implementation-plan.md` still contained sentences describing the name as a pending working title. The bulk find-replace during the rename correctly caught every literal occurrence of the old project-name *string*, but not the surrounding *prose* asserting the naming process was still open — since that prose never contained the old name as a string, sed had nothing to match. A reader hits "Terminal Velocity" in the title and then, two lines later, reads that the name hasn't been chosen yet.

**Status: fixed in this pass** (see Actions Taken, below).

### 2. The harness-is-static / hill-climbing-rewrites-harness contradiction, and the missing review caveat (AI/ML Practitioner + Security-Conscious Reviewer)

`docs/workshop-design.md` defines harness engineering as structural and "largely static... you can describe a harness completely without ever running it," then describes the hill-climbing loop as an outer loop that rewrites the harness's own config or prompts at runtime. Two personas converged on the same underlying gap from different angles: the AI/ML Practitioner flagged it as an unreconciled technical contradiction that undercuts the module 3/4 boundary the whole arc depends on; the Security-Conscious Reviewer flagged the missing caveat that hill-climbing edits should be reviewed proposals, not auto-applied changes, since nothing in the text stops a learner from copying "let the loop auto-apply the rewrite" as the default shape of the pattern.

**Status: fixed in this pass** (see Actions Taken, below).

## Single-persona findings (real signal, not gaps between other lenses)

### 3. Overclaiming / unsupported causal claims (Skeptical Practitioner / Critic)

Five distinct instances of asserted-not-argued claims: "the harness *is* the classroom" stated as a pedagogical finding rather than a working hypothesis; "different *kinds* of question... not cosmetic" oversold as settled when one of the three cited sources treats it as a continuous historical arc, not two discontinuous kinds; a flat historical/causal claim about *when and why* loop engineering became its own discipline, with no dates or named examples; the build-log's "real demonstration of the practices being taught" claimed before a single entry exists to demonstrate anything; and three vendor blog posts labeled "Sources reviewed" in a way that lends more authority than they've earned next to confident causal claims.

**Status: fixed in this pass** — softened the "our view" section's confidence level and reframed Sources as industry blog posts, not research (see Actions Taken).

### 4. Module 2 (context engineering) has no exercise-pattern anchor (Instructional Designer)

`docs/implementation-plan.md` §1 gives concrete exercise-pattern pointers for modules 01, 03, 04, and 05, but skips module 02 entirely — not even a placeholder note like module 01 got. Related: module ordering is justified by chronology ("the evolution of practice, in order") rather than demonstrated prerequisite dependency, and module 4 is asked to carry four sub-concepts (agent/verification/event-driven/hill-climbing loops) plus three named patterns on the same "at least one exercise" budget as every other module.

**Status: partially fixed** — added a module 02 anchor note to `docs/implementation-plan.md` §1 in this pass. The sequencing-as-chronology and module-4-overload points are real but only resolvable once actual exercises are designed — logged as guidance for the Coachgremlin content-building phase, not fixed here.

### 5. No exercise exists yet to evaluate the "harness is the classroom" promise against (End-User / Target Learner)

As the advertised learner, there's nothing to *do* in these docs yet, so the honest reaction is "come back later" rather than a verdict on engagement. The capstone description ("diagnose which of the four is the bottleneck... then fix it") is the one moment concrete enough to picture actually doing — the reviewer wants more of that concreteness pulled earlier rather than four modules of pure definition before any task appears.

**Status: not fixed** — this is the expected state of a design-only pass; content-building is explicitly the next phase, not this one. Logged as a priority for that phase: pull concreteness earlier if possible, don't leave the capstone as the only tangible moment.

### 6. Harness vocabulary may lean Claude-Code-specific despite "bring your own harness" framing (End-User / Target Learner)

Module 3 name-drops sub-agents/specialists, reusable skills, plugins/connectors (MCP), and isolated worktrees — concepts that may not map cleanly onto every harness a learner uses (e.g. Cursor). Not fixed; flagged as a content-building-phase decision: design exercises harness-agnostically, or be explicit that some content assumes Claude Code with a "translate to your tool" note.

### 7. Grader trust is asserted, not shown (End-User / Target Learner)

Coachgremlin promises feedback "against the learner's actual attempt," but nothing in the docs demonstrates it can distinguish "solved it a valid but different way" from "missed the point." Not fixable at the design-doc stage — logged as a real risk to revisit once Coachgremlin has actual runs behind it (matches its own Review Triggers: "run 3+ times... contracts stable enough to bump to v0").

### Positive findings worth keeping

- **Attribution accuracy checked out.** The AI/ML Practitioner fact-checked the workshop's taxonomy against the live source URLs directly and confirmed the four-layer loop taxonomy, Osmani's "five-plus-one," and the "ralph loop" attribution are all faithfully represented. One correction: CodeRabbit's own term is "context management," not "context engineering" — the Sources bullet already quotes this correctly even though the workshop's module 2 uses the more standard term; no fix needed, just confirmed as intentional and non-contradictory.
- **Audience calibration is correctly pitched**, per the End-User persona — not condescending, not over-assuming, the two coined terms (context/loop engineering) are the only vocabulary not assumed.
- **The one concrete piece of automation (the Pages deploy workflow) is a good model to teach by example** — `workflow_dispatch`-only trigger, minimal permissions, human-gated first deploy — per the Security-Conscious Reviewer, nothing to fix there.

## Actions Taken (this pass)

- Removed stale "naming pending" / working-title language from `README.md`, `docs/workshop-design.md`, `docs/workshop-gremlin-design.md`, and `docs/implementation-plan.md`; replaced with plain statements that the name is Terminal Velocity.
- Rewrote `docs/workshop-design.md`'s harness/loop split to explicitly reconcile "harness is largely static" with "hill-climbing rewrites the harness," and added the missing caveat that hill-climbing edits are reviewed proposals, not auto-applied changes.
- Softened the "our view" section's confidence framing and relabeled the Sources section to be explicit these are industry blog posts informing a synthesis, not independently validated research.
- Added a module 02 exercise-pattern anchor note to `docs/implementation-plan.md` §1.

## Deferred to the content-building phase (not design-doc fixable)

- Pull more concrete, doable moments earlier than the capstone.
- Decide harness-agnostic vs. Claude-Code-leaning exercise design explicitly.
- Design exercises as cumulative across modules, not independent silos, if the "the sequence really builds" claim is to hold.
- Give module 4 an exercise budget proportional to its four sub-concepts, or split it.
- Revisit Coachgremlin's grading trustworthiness once it has real runs (per its own Review Triggers).

## Panel Verdict

Ran successfully as designed: seven independent lenses, two genuine cross-persona agreements (both fixed), five single-persona findings none of the others would have caught (overclaiming, module-2 gap, learner engagement, harness-agnosticism, grader trust). No finding was averaged away — the two agreements were agreements because two personas independently reached the same conclusion from different reasoning, not because they were merged into a compromise. This run is the evidence base for moving the Workshop Review Panel from "designed, untested" to "wired into the Workshop Gremlin's roster."
