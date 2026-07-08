# Next Actions: Terminal Velocity

## Status: Module 03 pilot completion plan's Phase A run (second harness + fresh attempt) (2026-07-08)

Ran `docs/module-03-pilot-completion-plan.md`'s Phase A from a cleared-context session, as the
plan itself required. Three separate `codex exec` (Codex CLI, `gpt-5.5`) invocations against a
scratch copy of `fixtures/receipts/`: a cold design+build, a genuinely separate resume-from-notes
process, and a required negative control with the notes file withheld. **Go, with a real finding**:
write isolation held throughout (independently verified via diff/find, not self-report; live
fixture and rest of repo stayed clean), but the negative-control invocation's read access was not
scoped to its intended directory — it read a forbidden solved checkpoint from the prior
2026-07-04 dry run (`runs/2026-07-04-module-03-manifest-dry-run/checkpoints/negative-control-
without-notes/.receipts-category-progress.md`), because Codex's `workspace-write` sandbox
restricts writes but not reads, and the resume prompt (unlike phase 1's) didn't explicitly confine
it. Full record, self-assessment against `module.yaml`'s six-criterion rubric (via
`coachgremlin/grader.md`, no certification), and honest reporting on both the harness-boundary
claim and how "fresh" this attempt really was: `runs/2026-07-08-module-03-second-harness-spike/
retro.md`, ledger entry `runs/run-20260708-AEW-012.yaml` (`human_confirmed: false`).

**Phase A's own setup deviated from the plan in one way**: git-based checkpointing (`git init` +
commit inside the scratch copy) was blocked by this repo's `git-guardrail.sh` hook, which checks
the harness's tracked working directory rather than the command's actual target, so it fired even
for an unrelated scratch repo. Substituted plain filesystem diffs/snapshots for the same
evidentiary purpose throughout; noted in the retro's Deviation section.

**What's still open**: Phase B (the actual human-confirmation exercise — coderturtle reviews the
harness config and reset-and-resume evidence, writes `human_notes` personally) and Phase C
(the `tv` CLI / MCP server decision, gated on what Phase A/B reveal) remain, per the plan's own
sequencing. Phase A's read-boundary finding is real evidence Phase C should weigh.

## Status: Module 03 pilot completion plan written; both feature branches merged (2026-07-08)

`agent/claude/module-03-agent-native-pilot` merged into `main` (this session's full arc: manifest
pilot, dry run, review-panel fixes, local-model spikes, Codex cross-check, num_ctx resolution).
`local-agentic-coding-lab`'s `fix/patch-generation-json-format` merged into its own `main` (both
commits: `fmt="json"` + `context_by_profile`); the branch and its worktree were deleted after
merge (`git branch -d`, only succeeds on a fully-merged branch). Neither repo's `main` was pushed.

**New: `docs/module-03-pilot-completion-plan.md`** — the concrete next step for Module 03's still-
open items (human-confirmation exercise; a second harness *and* a genuinely fresh, uninvolved
attempt, per the review panel's Instructional Designer finding that the existing dry run
validated the pilot's own authors more than a cold learner). Designed to be run by a session with
**cleared context** — deliberately, since the exact gap being closed is "does this hold up for
someone who wasn't in the room," and an orchestrating session that remembers this build's history
would bias that test. Recommends Codex CLI (proven cold-capable this session against Module 04)
for Phase A, satisfying "second harness" and "fresh attempt" in one motion; Phase B (the actual
human-confirmation exercise) stays explicitly human-only, not delegated forward; Phase C (`tv`
CLI / MCP server decision) stays gated on what A/B reveal, per the original plan's own sequencing.

## Status: num_ctx question resolved, student-gremlin spike now converges (2026-07-08)

Follow-up to 2026-07-07's patch investigation below. The "requested 32768, observed 384000, cause
unconfirmed" framing was wrong — checked `local-agentic-coding-lab`'s actual Ollama server log
instead of continuing to guess. Real cause: devstral-small-2:24b's own genuine max context
(384000, not a placeholder) needs ~32GB of KV cache, too large for this 24GB machine even though
correct for a 64GB profile. Fixed properly (a `context_by_profile` registry field, not a guessed
magic number) on the same `fix/patch-generation-json-format` branch (still local-commit-only, not
pushed). **The student-gremlin spike now converges**: live-verified, carefully monitored, no
resource issue — the local `devstral-small-2:24b` pipeline joins Codex CLI as a second positive
fresh-agent result for Module 04. A real, separate concurrency observation (another active
session hitting the same shared Ollama instance mid-run) was confirmed but wasn't the cause here;
logged as its own backlog item in `local-agentic-coding-lab/docs/next-actions.md`, not built now.
Full record: `runs/2026-07-08-module-04-student-gremlin-spike/retro.md`.

**Still true**: Module 03's own still-open items (human-confirmation exercise, second harness,
fresh/uninvolved learner-or-agent test) are unaffected — none of this work reached Module 03.

## Status: Codex CLI spike (go) + patch investigation, same-day follow-up (2026-07-07)

Follow-up to the two spikes below. **Codex CLI, run cold as an independent full harness against
Module 04: go, cleanly** — stated terminal states up front, correctly reproduced/root-caused/
fixed/reran, minimal diff, one shot. This is real, positive fresh-agent evidence for Module 04
(complementing, not replacing, the student-gremlin spike's negative result for the specific
local-pipeline approach). Full record: `runs/2026-07-07-module-04-codex-spike/retro.md`.

**Patch investigation** on `local-agentic-coding-lab` (per the user's request to turn the
truncation finding into a real patch, checked for cascading effects): the original root-cause
guess was wrong (checked and ruled out: timeout, `num_predict`). Real cause found and fixed
(`fmt="json"` missing on the patch-generation call, cascading to an identical call in
`workflows/refactor.py`) on a local branch (`fix/patch-generation-json-format`, not
pushed/merged). A second real factor (Ollama's small default context) was found, confirmed to fix
the issue in isolation, but caused a genuine resource-safety incident when wired into the full
workflow (~49GB memory, stuck 30+ minutes) — **deliberately not shipped**, left open. Full record:
`runs/2026-07-07-module-04-student-gremlin-spike/retro.md` (all three attempts, consolidated) and
`local-agentic-coding-lab/docs/decisions.md`'s ADR-044.

**Still true below**: Module 03's own still-open items are unaffected by any of this — none of
today's work (student-gremlin, judging panel, or Codex) reached Module 03.

## Status: two bounded local-model spikes run — student gremlin no-go (root cause found), judging panel go (2026-07-07)

Ran two spikes on adjacent Hekton labs targeting this project's two open evidence gaps. **Student
gremlin** (`local-agentic-coding-lab`, driving its existing `coding.bugfix` loop against Module
04, not Module 03): no-go, but with a precise, well-evidenced root cause (the coder model's
structured-edit patch JSON got truncated before parsing, on every attempt across two runs, despite
correctly diagnosing the actual bug every time) — read as a plumbing limitation in that lab's
shared workflow, not a verdict that a local model can't do this. **Judging panel** (`local-llm-lab`,
a 3-persona blind panel scoring Module 04's already-graded transcripts): go — independently
reproduced the original good/gaming split with zero access to the original verdict. Full detail
in `docs/decisions.md`'s 2026-07-07 row and `docs/session-log.md`'s matching entry.

**What this changes below:** RISK-0004 (`docs/risks.md`) is updated with the judging-panel result
— narrowed, not closed. Module 03's own still-open items (human-confirmation exercise, second
harness, fresh/uninvolved learner-or-agent test) are **unchanged** — the student-gremlin spike
deliberately targeted the easier Module 04 first and did not reach Module 03 at all.

## Status: content backlog closed, all five modules human-confirmed (2026-07-04)

Module 04's three optional extensions (verification-deepened, event-driven, hill-climbing) and
Module 05's two remaining variants (prompt-bottleneck, context-bottleneck) are now built, verified,
and Review-Panel-reviewed. Module 05's two new variants are a real, well-evidenced negative
finding (10 independent fresh-agent runs, neither sabotage reproduced), shipped as documented
negative-control artifacts, not required-exercise options; the capstone's required exercise stays
at 2 of 4 layers live, honestly. coderturtle confirmed (go) all five modules' existing dry-run
evidence in `runs/` ledger entries. See `docs/decisions.md`'s 2026-07-04 rows for full detail.

**Still open, not done this session:**
- [ ] Whether Module 04's dry run counts as run 1 of Coachgremlin's 3-run Review Trigger (a
      Coachgremlin-maturity question, separate from module-content confirmation).
- [x] ~~Module 03's agent-native manifest pilot needs its own human-confirmation exercise, then the
      plan's scoped 3-persona review-panel re-run~~ **Review-panel re-run done 2026-07-04**
      (`docs/review-panel/2026-07-04-module-03-manifest-pilot-content.md`): found the Human Gate is
      enforced by instruction only (no hook/CI reads `human_confirmed`), an overclaim in how the
      dry run's "two disconnected phases" was summarized (fixed), and that this pilot's harness-
      agnostic claim is still untested against a second harness.
- [x] ~~A second harness *and* a genuinely fresh, uninvolved attempt~~ **Done 2026-07-08**
      (`docs/module-03-pilot-completion-plan.md` Phase A, `runs/2026-07-08-module-03-second-
      harness-spike/`): Codex CLI, three separate cold `codex exec` invocations. Go, plus a real
      finding — the negative control read a forbidden solved checkpoint because Codex's sandbox
      doesn't restrict reads, only writes. See the status section at the top of this file.
- [ ] **Phase B (human-confirmation exercise, human-only)**: coderturtle reviews the harness
      config and both/all transcripts, independently confirms the reset-and-resume evidence, and
      writes `human_notes` personally — not "an artifact exists." Cannot be delegated forward.
- [ ] **Phase C (`tv` CLI / MCP server decision)**: gated on Phase A/B; Phase A's read-boundary
      finding is real evidence to weigh here.
- [ ] Consider whether the Module 04/05 review-panel findings (e.g. the blast-radius script's
      rename/deletion handling, now fixed) suggest a similar audit of the two original Module 05
      variants (`sabotaged-harness`/`sabotaged-loop`), which haven't been re-reviewed since 2026-07-03.

## Status: LIVE at terminal-velocity.coderturtle.io (2026-07-04)

The site is deployed and reachable over both HTTP and HTTPS (cert already issued). Route53 records
applied via `agentic-infra-lab`'s `github-pages-dns` pattern; Pages enabled and the custom domain
set; `deploy-pages.yml` runs clean end to end (`workflow_dispatch`).

**Real discovery, corrected in `deploy-pages.yml`**: the workflow's own design assumed its default
`GITHUB_TOKEN` could enable Pages and set the custom domain via `gh api` — it cannot, under any
`permissions:` grant (`administration` isn't even a valid `GITHUB_TOKEN` permission scope; a
workflow declaring it fails to parse entirely). Both are one-time, human-run steps now (already
done for this repo, via a human's own authenticated `gh` session). CI's job is build + deploy only.
See `docs/session-log.md`'s "2026-07-04 - First live deploy" entry for the full story (three failed
runs, each catching a different real bug) and `docs/decisions.md` for the corrected design record.

**Not yet done:**
- [ ] Uncomment the `push` trigger in `deploy-pages.yml` so future `site/**`/`docs/build-log/**`
      changes auto-publish — deliberately not done yet without separate confirmation, since it's a
      standing behavior change (every future push to `main` touching those paths auto-deploys).
- [ ] Visually confirm the live site in a browser (verified via `curl`/API only so far).
- [ ] Run `npm audit` on `site/`'s dependencies before this matters more (site is now public).
- [x] **Minimal styling pass done** (this branch): accent color actually used (links, nav, wordmark), dark mode via `prefers-color-scheme` (RGB-channel CSS custom properties, no toggle/JS/new dependency), card treatment for build-log/homepage entry lists, subtle header divider. Verified against the real `astro build` output (not just `astro dev`, which had a stale-HMR artifact) via `astro preview` + Playwright screenshots in both light and dark, plus a clean `astro check`.

This supersedes the "GitHub Pages custom-domain design pass" and cross-repo-infra-blocked sections
that previously lived here — the domain is live, so those are resolved, not just planned.

## Next session: priorities (as of 2026-07-04, agent-native manifest pilot for Module 03)

Built the static-manifest pilot from `docs/agent-native-interaction-plan.md`, scoped to Module 03 only, sequencing steps 1-4: `modules/.manifest.schema.yaml`, `runs/.schema.yaml` extended with exercise-attempt fields, `coachgremlin/grader.md` (the loadable grader persona), `modules/03-harness-engineering/module.yaml`, `modules/03-harness-engineering/AGENT.md`. Checked for drift against the README: `question` and `gate` text match verbatim.

**Dry run complete (this branch, see `docs/decisions.md` and `runs/2026-07-04-module-03-manifest-dry-run/`)**: a fresh agent, driven only by `AGENT.md`/`module.yaml`, completed the exercise across two genuinely disconnected phases, self-graded via `coachgremlin/grader.md`, and wrote a `runs/` entry without self-certifying. Two real ambiguities in `AGENT.md` were found and fixed. Remaining from the plan's §5 sequencing: one real human-confirmation exercise, then the scoped 3-persona review-panel re-run (Instructional Designer, Security-Conscious Reviewer, Skeptical Critic) before deciding whether phase 2 (`tv` CLI) or phase 3 (MCP server) are worth building at all.

## Next session: priorities (as of 2026-07-03, end of the content-authoring + panel-review pass)

**Does this need deep analysis first? No.** The substantive design questions for everything remaining are already answered in existing docs (`docs/coachgremlin-implementation-plan.md` for the module extensions/variants, `docs/agent-native-interaction-plan.md` for the manifest). What's left is execution against those specs, plus a set of items that are blocked on coderturtle, not on more research. A fresh Opus-style planning pass would be re-deriving decisions already made, not making new ones.

### Blocked on you, not on more agent work

1. ~~Human-confirm the first GitHub Pages deploy~~ — **done 2026-07-04**, see the top status section.
2. **Review all five modules' content and evidence** (`runs/2026-07-03-module-0{1,2,3,4,5}-dry-run/`, plus the six `docs/review-panel/2026-07-03-*-content.md` reports). Confirm or contest each "go," and decide whether the Module 04 dry run counts as run 1 of Coachgremlin's 3-run Review Trigger. This is the biggest lever: every other open item either follows from this review or doesn't depend on it.
3. **Visually confirm the guide page and build-log entries** in a real browser (dev server was left running for this once; would need restarting).
4. **Authorize registering the three Gremlins in the mind-palace Gremlin Registry** (vault mutation, currently deferred beyond this project's own card).

### Ready to execute next session, no new design needed, specs already exist

In the order the original plan sequences them (`docs/coachgremlin-implementation-plan.md` §6, plus `docs/agent-native-interaction-plan.md`):

1. ~~**Module 03's agent-native manifest**: schema first...~~ **Done 2026-07-04** — see the priorities section at the top of this file. Steps 1-4 of the plan's sequencing built (schema, grader persona, manifest, agent entry point); step 5 (the real dry run) is the next actual work here, not a new design task.
2. **Module 04's three optional extensions** (verification-deepened, event-driven, hill-climbing): specs already written in `docs/coachgremlin-implementation-plan.md` §2. Module 03's harness now exists for the event-driven/hill-climbing extensions to build on, so the dependency that gated deferring these is resolved.
3. **Module 05's remaining two sabotaged variants** (prompt-bottleneck, context-bottleneck), following the exact pattern already proven for the harness/loop variants: build the variant, verify it's genuinely single-cause with a real isolating test, no self-spoiling noise (learned the hard way twice this session).

Recommend #2 in "Blocked on you" (the module review) happens before piling more unreviewed content on top of five modules that haven't had human eyes on them yet, but that's a judgment call, not a hard dependency.

### Optional / lower priority, pick up if there's time or specific interest

- Independent/blind grading pass on any module's evidence, before treating "the rubric discriminates" as fully proven rather than well-evidenced (`docs/risks.md` RISK-0004).
- A Review Panel run against a second, differently-shaped workshop, to test the "different workshops" half of the panel's own maturation trigger (seven runs so far are all within this one workshop).
- Whether README.md and the site guide page should be more substantially differentiated, not just cross-linked and internally consistent (this session's fix).
- Transcript-based "See it in action" previews for Modules 01/02/03/05, matching Module 04's.
- `npm audit` on `site/`'s dependencies before the first real deploy (4 vulnerabilities reported at install time, inherited from the blog-factory-lab starter, not yet triaged).

## Immediate

- [x] Resolve GitHub push credential (was `IdentitiesOnly` missing on the `github.com-coderturtle` SSH alias) — fixed 2026-07-03, `main` pushed.
- [x] Produce an implementation plan for the next phase (deliverables/branding + build-log/Pages publisher) — `docs/implementation-plan.md`, produced via an Opus-run planning pass, reflecting the revised four-module arc.
- [x] Run the Workshop Gremlin's naming agent — chose **Terminal Velocity**. Repo, local dir, mind-palace mirror (repo-local and live vault) all renamed 2026-07-03.
- [x] Design + test-run the Workshop Review Panel (7 personas) against this project's current design docs — `~/hekton/gremlins/workshop/workshop-review-panel.md`; report at `docs/review-panel/2026-07-03-initial-design.md`. Fixes from that run applied directly to README.md, docs/workshop-design.md, docs/workshop-gremlin-design.md, docs/implementation-plan.md.
- [x] Ran the site locally (`npm run dev` + headless Chromium) before deploying anywhere: homepage and build-log entry both render correctly under the `/terminal-velocity/` base path, no console errors.
- [x] Deep Opus research pass on agent-native workshop interaction — `docs/agent-native-interaction-plan.md`. Recommends module 03 as the pilot, a static manifest (not a live server) as the correct default, and a concrete Human Gate extension for agent-submitted attempts.

## This Week

- [x] Execute `docs/implementation-plan.md` §1: module directory skeleton (`modules/01-prompt-engineering/` … `05-synthesis-capstone/`, each a structure-only README stub, plus `modules/README.md` index with the loop taxonomy). Module 02's exercise-anchor gap closed.
- [x] Execute §3: `docs/brand.md` brand layer. Real name throughout; hard rules (no em dash, no unqualified efficacy claims) written directly in response to the review panel's Skeptical Critic findings.
- [x] Execute §2: reworked top-level `README.md` for a learner audience with a literal copy-pasteable clone command; relocated internal Hekton framing to `docs/maintainers.md`.
- [x] Execute §4: adapted `blog-factory-lab/site-starters/astro-blog` into `site/` (dropped React/narrative components per the plan, kept MDX), wired `docs/build-log/` via an Astro 5 Content Layer `glob` loader (entries stay in `docs/build-log/`, not duplicated into `src/`), wrote the first build-log entry, added `.github/workflows/deploy-pages.yml` (`workflow_dispatch`-only trigger, `push` commented out — no live deploy without explicit human confirmation per the Human Gate).
- [x] Verified per `docs/implementation-plan.md` §6: `npm run build` and `npx astro check` both clean; seed entry renders on the homepage and its own route with the correct `/terminal-velocity/` base path; workflow YAML validated; no em dashes or banned phrases in published content; all README/modules links resolve; mirror-drift and `verify-project.sh` clean.

## Later

- [x] **Hands-on-by-design retrofit**: added a "Required to advance" gate to all 5 module READMEs plus `modules/README.md`'s arc table, per coderturtle's direction that every workshop must require the learner to produce/demonstrate something, never just read. Now a standing principle in `~/hekton/gremlins/workshop/workshop-gremlin.md`'s Design Principles, not just this workshop's choice.
- [x] Fixed a pre-existing em-dash violation across `modules/` and `README.md` (written before `docs/brand.md`'s hard rules existed) — published content is now clean.
- [x] **Workshop Lifecycle documented** (`~/hekton/gremlins/workshop/workshop-lifecycle.md`): Workshop Gremlin (Build) and Coachgremlin (Learn) stay separate, formalized as two phases of one lifecycle rather than merged. Both Gremlins gained a `Lifecycle Phase` header field; `agents/index.md` gained a Phase column.
- [x] **Takeaways added**: every module gained a "Takeaway" section (`modules/*/README.md`, `modules/README.md`'s "What you keep") — a keepable Skill/prompt-template/sub-agent-definition/loop-template per module, not just proof of completion. New Design Principle 4 in `workshop-gremlin.md`; Coachgremlin's Workflow gained a "package the takeaway" step.
- [x] **Dogfooded loop engineering on the build process**: named and wired the "Docs Consistency Loop" (a verification loop, per `modules/README.md`'s own taxonomy) — new `scripts/check-brand-lint.sh` alongside the existing `scripts/check-mirror-drift.sh`, both wired warn-only into the pre-push hook (`scripts/setup-hooks.sh`). Documented in `~/hekton/gremlins/workshop/workshop-lifecycle.md`'s "Dogfooding" section, which also explains why the more tempting hill-climbing candidate (Gremlin-contract revision) stays manual for now (moving target, not stable, per this factory's own rule).
- [x] **Detailed Coachgremlin content-building plan produced** — `docs/coachgremlin-implementation-plan.md` (Opus-run). Full exercise specs, rubrics, stop conditions, and takeaway-packaging instructions for all 5 modules; a shared cumulative fixture (`receipts` CLI); recommends **module 04 (Ticket-to-PR-Ready core)** as Coachgremlin's actual first real run, with a concrete go/no-go dry-run design; harness-agnostic vs. Claude-Code-leaning decided per module; full sequencing and verification plan. Not yet executed.
- [x] **Human-confirm the first GitHub Pages deploy**: done 2026-07-04 — see the "Status: LIVE" section at the top of this file. The site is live at `terminal-velocity.coderturtle.io`. The `push` trigger in `.github/workflows/deploy-pages.yml` is still deliberately commented out, pending separate confirmation.
- [x] **Built the shared `receipts` fixture** (`fixtures/receipts/`, plan §6 step 0): stdlib-only Python, `group_expenses_by_month(rows, tz)` with the four required edge cases, one seeded bug isolated to exactly one failing test.
- [x] **Authored Module 04's core exercise content**, replacing the rubric/stop-condition placeholders (`modules/04-loop-engineering/README.md`). Extensions A/B/C intentionally deferred to after Module 03.
- [x] **Ran Coachgremlin's first real dry run** (Module 04 core, plan §5): a genuine good attempt and a genuine rubric-gaming attempt, both graded against the rubric, feedback given without handing over the fix, takeaway packaged (`.claude/commands/ticket-to-pr-ready.md`) and validated on a second, unrelated bug. **Go**, with one real finding (a rubric-gaming loophole) found and closed in both the module rubric and `~/hekton/gremlins/coaching/coachgremlin.md`. Full record: `runs/2026-07-03-module-04-dry-run/` (`grading.md`, `retro.md`), `runs/run-20260703-AEW-001.yaml` (`human_confirmed: false`, Human Gate).
- [x] Committed the fixture/Module-04/dry-run work (`e22fb88`, local, not pushed).
- [x] **Added a filtered real-transcript preview for prospective learners**: `scripts/render-transcript-preview.py` condenses `runs/2026-07-03-module-04-dry-run/attempt-good/transcript.txt` into `docs/sample-attempt-preview.md`, linked from README's new "See it in action" section. Direct answer to the Workshop Review Panel's End-User/Learner finding (no sample to look at before committing) without adding a parallel hand-maintained tutorial track. Rerun the script if the source transcript ever changes.
- [x] **Authored and verified all four remaining modules** (01, 02, 03, 05), each against a real fixture variant, each actually attempted at least once (Module 01 three times) and independently reverified, not just written. Full detail in `docs/session-log.md`'s 2026-07-03 "Authored and verified Modules 01, 02, 03, 05" entry. All five modules now have real exercises, rubrics, stop conditions, and packaged, evidence-backed takeaways.
- [ ] **coderturtle: review all five modules' content and evidence** (`runs/2026-07-03-module-0{1,2,3,4,5}-dry-run/`), per the Human Gate. Confirm or contest each "go," and decide whether the Module 04 dry run counts as run 1 of Coachgremlin's 3-run Review Trigger.
- [x] **Restructured the site**: `site/src/pages/index.astro` is now a guide page (repo link, harness-as-classroom framing, runbook, human-vs-agent takeaway split), `build-log/` stays a separate section, `BaseLayout.astro` gained nav between the two. Four new `docs/build-log/` entries catch the journal up to the project's real state. Verified via `astro check`, `npm run build`, and direct checks against the running dev server.
- [ ] **coderturtle: visually confirm the guide page and new build-log entries** in the browser (dev server was left running for this).
- [ ] Push the local commits once reviewed, so the guide page's GitHub links (repo clone URL, sample-preview blob link) resolve instead of 404ing.
- [ ] Consider a screenshot-based visual review of the guide page before the first live Pages deploy (this session verified via HTTP/build output only, no rendered screenshot; Playwright isn't set up as a project dependency yet).
- [ ] Consider running an independent/blind grading pass on any of the five modules' evidence before treating "the rubric discriminates" / "the diagnosis is correct" as proven rather than plausible; every rubric so far was validated by the same session that authored it (`docs/risks.md` RISK-0004, now generalized past Module 04 to all five).
- [x] **Ran the Workshop Review Panel against Module 01**, its first run against real content (previously design docs only): `docs/review-panel/2026-07-03-module-01-content.md`. Two cross-persona agreements (the digestibility complaint's real structural cause; the module's central claim untested against a negative control), fixed for real: restructured the module, fixed a real wrong-directory bug in `SPEC.md`, ran the missing counterfactual (which contradicted the original claim and led to rewriting it honestly rather than keeping it). Full detail in `docs/session-log.md`'s matching entry.
- [x] **Ran the same scoped panel treatment for Modules 02, 03, 04, and 05.** All five modules have now been through the panel against real content. Two real fixture bugs found and fixed (Module 02's self-announcing noise; Module 05's nonexistent `docs/` directory plus self-spoiling context files), one real rubric-vs-grading-evidence inconsistency caught and fixed (Module 04), one central claim contradicted by its own negative control and rewritten honestly (Module 03's reset-and-resume), one evidence gap closed with a fresh agent run (Module 05's loop-variant prompt). Full detail in `docs/session-log.md`'s matching entry and `docs/review-panel/2026-07-03-module-0{2,3,4,5}-content.md`. `~/hekton`'s panel definition updated with a summary across all six runs.
- [x] **Ran the panel against the user-facing entry-point docs** (README.md, modules/README.md, the site guide page, sample-attempt-preview.md): `docs/review-panel/2026-07-03-user-docs-content.md`. Real value was cross-document consistency, invisible from any single file: README/site guide duplicated with no cross-link and disagreed on sequencing; a stale "diagnose all four layers" claim survived in three docs after Module 05 had already corrected it in a fourth; "what you keep" wording genuinely diverged across documents (Skill vs. checklist); a `~/hekton` local-machine path had leaked into the public arc index. All fixed. With this run, every piece of user-facing content in the repo has been through an independent review pass.
- [ ] **A run against a second, differently-shaped workshop** (not `terminal-velocity`) is what would test the "different workshops" half of the panel's own maturation trigger; seven runs so far are all within this one workshop.
- [ ] **Consider whether README.md and the site guide page should be more substantially differentiated**, not just cross-linked and made internally consistent (this pass's fix), since they still cover largely the same ground for two different landing contexts.
- [ ] **Deliberately deferred, not forgotten:** Module 04's three optional extensions (verification-deepened, event-driven, hill-climbing), Module 05's prompt- and context-bottleneck sabotaged variants (of the plan's two-to-four; two are built). Module 03's agent-native manifest co-production is now done, dry-run included — see the priorities section near the top of this file. Order depends on what the Review Panel re-run surfaces as highest-value.
- [ ] Consider a transcript-based "See it in action" preview (like Module 04's) for one or more of Modules 01/02/03/05 now that each has real dry-run evidence of its own.
- [ ] Register all three Gremlins in the mind-palace Gremlin Registry (vault mutation currently deferred beyond this project's own card — needs explicit authorisation for the registry file itself).
- [ ] Consider running `npm audit` on `site/`'s dependencies before the first real deploy (4 vulnerabilities reported at install time, inherited from the blog-factory-lab starter, not yet triaged).
