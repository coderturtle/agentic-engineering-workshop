# Terminal Velocity: Plain-English Project Walkthrough

## What this project is in one paragraph

A public, self-paced workshop for people who already use AI coding agents daily, teaching the next layer up: how to write instructions precise enough to be reproducible, how to curate what the agent sees, how to configure what it's allowed to touch, and how to build supervised loops that know when to stop. You learn each skill by actually doing it inside your own coding-agent tool, not by reading about it.

## The simple analogy

Most AI tutorials teach you to talk to the model better. This workshop assumes you can already do that, and teaches you to run a whole small workshop through your agent: give it a bounded task, watch what it does, check the result against a checklist, and know when to trust it and when not to. It's closer to teaching someone to run experiments than to teaching someone to write better emails.

## What problem we are solving

Practitioners who already use agents daily plateau on "get a plausible answer once." This workshop's bet is that the next skill isn't a better prompt, it's a set of four disciplines (prompt, context, harness, loop) that compound, plus the judgment to know which one is actually broken when something doesn't work.

## What we have built so far

- The five-module arc (prompt, context, harness, loop, synthesis capstone), the brand voice and hard rules, and a published Astro site scaffold (not yet live).
- Two purpose-built teaching agents: Workshop Gremlin (builds a workshop, runs a handful of times) and Coachgremlin (teaches a learner through it, runs continuously per learner). They stay separate by design; see `<hekton-machinery>/gremlins/workshop/workshop-lifecycle.md`.
- A shared, deliberately-broken practice tool (`fixtures/receipts/`, a small command-line expense summarizer with one seeded bug) that every module's exercise runs against, so a learner isn't relearning a new toy problem five times.
- All five modules now have a real exercise, checklist, stop condition, and packaged takeaway, not a placeholder. Loop engineering (04) went first, as Coachgremlin's actual first real run; prompt, context, harness, and the capstone followed the same day.
- Coachgremlin's first real, end-to-end run (2026-07-03): built a real good-faith attempt and a real cheating attempt at Module 04's exercise, graded both, found and fixed a real hole in the grading checklist, and packaged a reusable takeaway (a loop template) validated against an unrelated second bug. See `runs/2026-07-03-module-04-dry-run/`.
- Each of the other four modules got its own real, independently-verified attempt: Module 01's prompt passed three separate clean-session tries; Module 02's curated context was rerun and still worked; Module 03's bounded assistant survived a real memory-wipe-and-resume; Module 05's two broken scenarios were each correctly diagnosed with real supporting evidence, not a guess. See `runs/2026-07-03-module-0{1,2,3,5}-dry-run/`.

## How the pieces fit together

The learner works through modules 01 to 04 in order (each assumes the skill before it), then the capstone diagnoses a broken setup that could be any of the four. Coachgremlin runs every module's exercise: it frames the task, sets the checklist before the learner starts, watches the attempt, gives feedback that points at the actual attempt (never the answer), and packages whatever the learner built into something reusable afterward. The shared `receipts` fixture threads all five modules so the learner's cognitive load stays on the concept, not on re-learning a new domain each time.

## What is deliberately not automated yet

- Module 04's three optional extensions (a deeper verification pass, an event-triggered version, and a "the loop improves its own instructions" version) are built now that Module 03's harness exists, but not yet exercised.
- Module 05's capstone ships two of a planned two-to-four broken scenarios; two more (a bad-prompt case and a bad-context case) are designed but not yet built.
- The agent-native manifest for Module 03 (a machine-readable version of the harness config, so an AI, not just a human, could attempt the module) is researched but not built.
- The site is built and verified locally but not deployed; the deploy workflow requires a human to manually trigger it once before it can auto-publish.
- Whether an AI agent (not a human) could attempt a module on a learner's behalf is researched (`docs/agent-native-interaction-plan.md`) but not built.

## How this could connect to the wider Hekton factory

Both teaching agents (Workshop Gremlin and Coachgremlin) are defined at the factory level, not owned by this one workshop, specifically so a future Hekton workshop can reuse them without rebuilding either from scratch. Today's dry run is also the mechanism by which lessons flow the other direction: a real gap found while grading a Terminal Velocity exercise got written directly into Coachgremlin's own shared contract, so every future workshop that uses it inherits the fix.

## Current confidence level

Medium. All five modules now have a real, attempted, independently re-checked exercise behind them, not a description. What's still missing is anyone other than the session that built each one trying it: every rubric and every diagnosis so far has been judged by its own author, which is a real, named, open risk (`docs/risks.md` RISK-0004), not a hidden one.

## Open questions

- Does the same grading discipline (check what actually changed, not just whether it reports success) hold up when someone other than this session tries any of the five exercises?
- Would an independent, blind grading pass agree with this session's own grading and diagnosis of its own constructed attempts?

## Next recommended session

Human review of all five modules' evidence (`runs/2026-07-03-module-0{1,2,3,4,5}-dry-run/`), then the Workshop Review Panel re-run against real content, per `docs/coachgremlin-implementation-plan.md`'s sequencing (§6, step 7).
