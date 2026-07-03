# Walkthrough: Coachgremlin's First Real Run

**Date:** 2026-07-03
**Project:** Terminal Velocity
**Prompt / Session:** "let's run through docs/coachgremlin-implementation-plan.md"

## What changed in plain English

This workshop has an AI teaching assistant, Coachgremlin, whose whole job is to hand a learner a real coding task, watch them attempt it, and grade their attempt against a checklist, without ever just doing the task for them or handing over the answer. Until today, Coachgremlin had never actually done this. It was a design on paper.

This session built the first real thing for it to teach against (a small, deliberately broken command-line tool called `receipts`), wrote the first real exercise (find and fix one bug in it, using a disciplined "try, check, stop" loop), and then ran the whole teaching process for real: one good-faith attempt at the exercise, one attempt that tries to cheat, and Coachgremlin grading both.

The "good faith" attempt still managed to break, once, on the first try: the script written to verify the fix had a bug in its own verification logic and reported a real failure as "nothing to see here." Which is, if you think about it for more than a second, an extremely on-theme way for a session about verification loops to go.

## Why this matters

A grading checklist that's never been tested against a cheater is a checklist you're hoping works, not one you know works. The cheating attempt in this session found a real hole: the checklist, read literally, would have let the cheat pass, because it only checked "did the process finish successfully," not "did the process finish successfully by doing the right thing." That hole is now closed, in writing, in the checklist itself, before four more workshop modules get built using the same checklist-writing pattern.

## The simple analogy

Imagine grading a student's math homework by only checking "did they write down a final answer that matches the answer key," without checking their work. A student who peeks at the answer key and copies it down passes that check. This session is the equivalent of catching that exact move once, on purpose, so the grading process going forward actually looks at the work, not just the final answer. The student in this metaphor did not even erase the answer key first. It just changed the answer key.

## How this ties to Terminal Velocity

Terminal Velocity teaches four skills in order (writing precise instructions, curating what an AI assistant sees, configuring the tools it can use, and building supervised repeat-until-done loops), then a final module where the learner diagnoses which of the four is broken in a deliberately sabotaged setup. Coachgremlin is the thing that runs every one of those five modules. Today's session is the first real evidence that Coachgremlin's teaching process holds up, using the fourth module (loops) as the test case, before the other four modules get written on the same pattern.

## How this ties to the Hekton factory vision

Coachgremlin is designed to be reused across future workshops, not just this one. Its behavior lives in a shared file (`~/hekton/gremlins/coaching/coachgremlin.md`) outside this project, so the lesson learned here (always check what a fix actually touched, not just whether it reports success) now applies to every future workshop that uses Coachgremlin, not just Terminal Velocity.

## What remains uncertain

This session's grading was done by the same session that built the "cheating" attempt, already knowing which one was supposed to be weak. A more convincing test would have a separate, independent pass grade the same two attempts blind, without being told which one is which. That hasn't happened yet.

## What you should check next

- Read `runs/2026-07-03-module-04-dry-run/retro.md` for the full go/no-go reasoning.
- Confirm (or contest) the recommendation: it's marked `human_confirmed: false` on purpose, waiting on your review.
- If you agree, the next content-building step is Module 01, per the plan's own sequencing.

## Changed files

- `fixtures/receipts/` (new): the shared broken CLI every module will use.
- `modules/04-loop-engineering/README.md`: real exercise, rubric, and stop condition, replacing placeholders.
- `.claude/commands/ticket-to-pr-ready.md` (new): the reusable takeaway.
- `runs/2026-07-03-module-04-dry-run/`, `runs/run-20260703-AEW-001.yaml` (new): the dry run's evidence and record.
- `~/hekton/gremlins/coaching/coachgremlin.md`: grading-discipline fix fed back into Coachgremlin's own contract.
- `docs/decisions.md`, `docs/session-log.md`, `docs/next-actions.md`, `docs/risks.md`, `.hekton/risk-register.yaml`: session record.
