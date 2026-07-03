# Terminal Velocity

Learn agentic engineering by running it in a harness, not reading about it.

## What this is

A self-paced workshop on how prompt engineering, context engineering, harness engineering, and loop engineering fit together right now: one evolving practice, not four unrelated topics. Every exercise runs through your own coding-agent harness. Coachgremlin frames the task and gives you feedback on your actual attempt. It does not lecture, and it does not hand you the solution.

**Who it's for:** advanced practitioners already using coding agents daily (Claude Code, Codex, Cursor, or similar). This is not an intro-to-AI workshop. The only vocabulary this workshop assumes you don't already know is "context engineering" and "loop engineering" themselves: that's exactly what it teaches.

## Prerequisites

- Comfortable with git, the CLI, and reading a diff.
- Already using at least one coding-agent harness regularly.
- A working harness installed on your machine.

## How to start

```bash
git clone git@github.com:coderturtle/terminal-velocity.git
cd terminal-velocity
cat modules/README.md
```

Then work through `modules/` in order, one at a time. Each module's core exercise is run through your own harness: you drive it, Coachgremlin evaluates the actual result.

## How the modules connect

Prompt engineering is one turn's instruction. Context engineering is what that turn can see. Harness engineering decides what the agent can reach and how its work is organized, mostly settled before anything runs. Loop engineering decides when it stops, how it's verified, and how it improves, only relevant once the harness is already running. The capstone has you diagnose which of the four is the actual bottleneck in a deliberately broken agent task, then fix it. Full arc: [`modules/README.md`](modules/README.md).

## What you keep

Every module leaves you with something, not just a passed check: a reusable prompt template, a context-budgeting Skill, a real sub-agent or harness config you can drop into a real project, a loop template, a diagnostic playbook. See [`modules/README.md`](modules/README.md#what-you-keep) for the full list.

## The teaching method

Our working hypothesis, not a settled finding: the harness is the classroom. You learn this material by doing it inside a real agent session, with Coachgremlin setting the rubric up front and grading your actual attempt, not by reading a guide. See [`docs/workshop-design.md`](docs/workshop-design.md) for the full reasoning, including where we admit this is a bet, not proven pedagogy.

## Build in public

This workshop's own build is published as a dated journal on GitHub Pages: the maintainer's record of building the workshop and its reusable Gremlin tooling at the same time, written deliberately rather than auto-generated from session logs.

## Key docs

- [Workshop Design](docs/workshop-design.md): audience, format, teaching method, full module arc
- [Maintainers](docs/maintainers.md): internal/agent-facing docs, classification, documentation contract
