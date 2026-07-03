# Module 03: Harness Engineering

## The question this module answers

What can it reach, and how is the work organized?

## Where it sits in the arc

Third module, after context engineering. This is where the arc turns **structural**: harness engineering is decided largely up front (what tools exist, what sub-agents are on call, what state persists, what the agent is allowed to touch), and you can describe a harness completely without ever running it. That's the hinge module 04 (loop engineering) crosses on purpose: loops are the one case where a running system reaches back in and changes the harness. See [modules/README.md](../README.md) and `docs/workshop-design.md`'s "Our view" section for the full structural-vs-behavioral framing.

## Learning objectives

_(finalized in the Coachgremlin content pass, placeholders below)_

- Design tool access and sub-agent/specialist boundaries for a task before running anything.
- Use persistent on-disk state to survive a context reset, rather than treating every session as amnesiac.
- Isolate parallel work safely (worktrees) instead of colliding on a shared checkout.
- Recognize when a bad outcome is a harness problem (wrong tool access, no persistent state) rather than a prompt, context, or loop problem.

## Exercise material this module draws from

Tool access, sub-agents/specialists, reusable skills, plugins/connectors (MCP and friends), and isolated worktrees/persistent state: the same vocabulary as `docs/workshop-design.md`'s harness-engineering description. Open design question carried from the Workshop Review Panel (End-User/Learner persona): whether exercises here should be harness-agnostic or explicitly Claude-Code-leaning with a "translate to your tool" note, since not every harness (e.g. Cursor) maps cleanly onto skills/worktrees vocabulary. Decide during content-building, not here.

## Required to advance

Configure a working harness setup (defined tool access, a sub-agent or specialist boundary, persistent state across a context reset) for a given task, and demonstrate it actually running correctly, not just described. Submitted harness config plus a real run transcript, checked against a rubric (rubric TBD by Coachgremlin). Reading this module does not count: you advance on a harness that actually ran, not on having read this page.

## Stop condition

_(rubric + terminal state defined per exercise by Coachgremlin)_

> Content status: skeleton only. Teaching content is built one concept at a time in a later Coachgremlin run (see `docs/next-actions.md`).
