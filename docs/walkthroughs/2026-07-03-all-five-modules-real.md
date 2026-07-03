# Walkthrough: All Five Modules Went From Placeholder to Real

**Date:** 2026-07-03
**Project:** Terminal Velocity
**Prompt / Session:** "ok lets loop through the rest of the modules"

## What changed in plain English

This workshop has five lessons. Until today, only one of them (loop engineering, the fourth) had a real exercise behind it; the other four were essentially placeholders describing what would eventually be there. This session filled in all four remaining ones, and, like the first, didn't just write descriptions of exercises: it actually built the broken practice materials, then actually attempted each exercise (sometimes several times, with a fresh AI assistant that had never seen the task before) to make sure it genuinely works before calling it done.

## Why this matters

A workshop exercise that's only ever been written, never attempted, is a hypothesis, not a lesson. Three different real bugs got caught this way today: a test that would have failed for the wrong reason on a certain date range, a scope boundary that silently blocked a fix from ever landing, and (on purpose, as part of the last lesson) a "checker" script that lied about whether tests had actually passed. All three were things you'd only find by actually running the exercise, not by reading it over carefully.

## The simple analogy

Imagine a cookbook where four of five recipes were never actually cooked, just written from a general sense of "this should work." Today's work is going back and actually cooking all four, in a real kitchen, sometimes twice, and fixing the parts that turned out not to work as written before publishing the recipe.

## How this ties to Terminal Velocity

The five lessons build on each other: write a precise instruction, curate what the AI can see, configure what it's allowed to touch, build a supervised retry loop, then diagnose which of those four things is actually broken when something goes wrong. Today's work made the second, third, and fifth of those real for the first time, and the first one (which already had a description) got its exercise built out too. All five now have something you can actually do, not just read about.

## How this ties to the Hekton factory vision

The reusable pieces a learner keeps (a prompt template, a curation checklist, a bounded AI assistant configuration, a diagnostic playbook) are all saved as real files in this repository now, in the same format any Claude Code user could drop into their own project. They're not abstract descriptions of what a takeaway should look like; they're the actual files, built from actually solving the actual exercise, twice in one case, to prove they generalize past the one problem they were built for.

## What remains uncertain

Every one of these five lessons was built, attempted, and judged by the same session, working alone. Nobody who didn't already know the intended answer has tried any of them yet. That's the next real test, not this one.

## What you should check next

- Skim any of the five `modules/*/README.md` files, they now describe a real, doable exercise, not a placeholder.
- If you want to see the evidence behind the claims, each module has a `runs/2026-07-03-module-0N-dry-run/` folder with the actual transcripts.
- The next honest step is someone other than this session trying one of these exercises for real.

## Changed files

- `modules/01-prompt-engineering/README.md`, `modules/02-context-engineering/README.md`, `modules/03-harness-engineering/README.md`, `modules/05-synthesis-capstone/README.md`: real content, replacing placeholders.
- `fixtures/receipts/variants/`: four new broken/incomplete versions of the practice tool, one per lesson that needed one.
- `.claude/commands/spec-impl.md`, `.claude/skills/context-budgeting/SKILL.md`, `.claude/agents/receipts-category-summary.md`, `.claude/skills/diagnose-agent-failure/SKILL.md`: the keepable takeaways.
- `runs/2026-07-03-module-01-dry-run/`, `-02-`, `-03-`, `-05-`: the evidence behind each one.
- `docs/session-log.md`, `docs/decisions.md`, `docs/next-actions.md`, `docs/risks.md`: session record.
