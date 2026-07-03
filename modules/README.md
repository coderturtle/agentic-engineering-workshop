# Modules

Terminal Velocity's spine is the evolution of agentic-engineering practice, in order: **prompt engineering → context engineering → harness engineering → loop engineering**, then a synthesis capstone. Work through them in order — each module assumes the ones before it, and the capstone only makes sense once you've done all four.

Every module's core exercise is run through your own coding-agent harness (Claude Code, Codex, Cursor, or equivalent) — you drive it, Coachgremlin frames the task and gives feedback against your actual attempt. See the top-level README and `docs/workshop-design.md` for the full thesis.

> Content status: skeleton only. Module READMEs below state the question each module answers and what it will draw on — not the exercises themselves. Exercise specs and rubrics are a later, one-concept-at-a-time Coachgremlin content-building pass (see `docs/next-actions.md`).

## The arc

| # | Module | The question it answers |
|---|---|---|
| 01 | [Prompt engineering](01-prompt-engineering/README.md) | What's the single best instruction for this one turn? |
| 02 | [Context engineering](02-context-engineering/README.md) | What does the model actually need to see, and what should be left out? |
| 03 | [Harness engineering](03-harness-engineering/README.md) | What can it reach, and how is the work organized? |
| 04 | [Loop engineering](04-loop-engineering/README.md) | When does it stop, how do we know it's right, and how does it get better without me watching every turn? |
| 05 | [Synthesis capstone](05-synthesis-capstone/README.md) | Given a broken agent task, which of the four layers is actually the bottleneck? |

## Why this order

Prompt and context engineering are about a single turn: what you say and what the model can see while you say it. Harness engineering is structural and (mostly) decided before anything runs: what the agent can reach and how its work is organized. Loop engineering is behavioral and only exists once the harness is running: when it stops, how it's verified, how it improves. Each layer assumes the ones before it exist — you can't sensibly design stop conditions (loop) for a harness you haven't defined (harness) around instructions that aren't precise (prompt) in a window you haven't curated (context). Full reasoning: `docs/workshop-design.md`.

## Loop taxonomy (module 04 uses this vocabulary throughout)

| Layer | What it is |
|---|---|
| Agent loop | The base case: the model calls tools in a loop until a task is complete. |
| Verification loop | An added grading pass: output is checked against a rubric and sent back on failure. |
| Event-driven loop | The agent loop is triggered by something external (webhook, schedule, message). |
| Hill-climbing loop | The frontier case: traces from real runs feed an analysis pass that *proposes* rewrites to the harness's own config or prompts — reviewed and verified before adoption, never auto-applied. |
