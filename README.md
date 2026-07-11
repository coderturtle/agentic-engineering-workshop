# Terminal Velocity

Learn agentic engineering by running it in a harness, not reading about it.

## What this is

A self-paced workshop on how prompt engineering, context engineering, harness engineering, and loop engineering fit together right now: one evolving practice, not four unrelated topics. Every exercise runs through your own coding-agent harness. Coachgremlin, this workshop's teaching agent (a role you run yourself, inside your own harness, not a hosted service), frames the task and gives you feedback on your actual attempt. It does not lecture, and it does not hand you the solution. No module here completes by reading it: each one states a required gate, an artifact you produce or an action you're observed doing, checked against a rubric.

**Who it's for:** advanced practitioners already using coding agents daily (Claude Code, Codex, Cursor, or similar). This is not an intro-to-AI workshop. The only vocabulary this workshop assumes you don't already know is "context engineering" and "loop engineering" themselves: that's exactly what it teaches.

## Prerequisites

- Comfortable with git, the CLI, and reading a diff.
- Already using at least one coding-agent harness regularly.
- A working harness installed on your machine.

## See it in action

Before you clone anything: [`docs/sample-attempt-preview.md`](docs/sample-attempt-preview.md) is real, condensed output from an actual attempt at Module 04's core exercise, reproduce a bug, root-cause it, fix it, prove it, in that order. Not a mockup: a script extracts the text straight from the transcript, unedited. Which attempt gets featured is a choice (this is the successful one, not a weaker one graded alongside it, see `runs/2026-07-03-module-04-dry-run/` for both), the transcript text itself isn't. The raw, un-condensed version is [`runs/2026-07-03-module-04-dry-run/attempt-good/transcript.txt`](runs/2026-07-03-module-04-dry-run/attempt-good/transcript.txt).

## How to start

```bash
git clone git@github.com:coderturtle/terminal-velocity.git
cd terminal-velocity
cat modules/README.md
```

Then work through `modules/` in order, one at a time. Each module's core exercise is run through your own harness: you drive it, Coachgremlin evaluates the actual result.

## How the modules connect

Prompt engineering is one turn's instruction. Context engineering is what that turn can see. Harness engineering decides what the agent can reach and how its work is organized, mostly settled before anything runs. Loop engineering decides when it stops, how it's verified, and how it improves, only relevant once the harness is already running. The capstone has you diagnose which layer is the actual bottleneck in a deliberately broken agent task, then fix it (two of the four layers currently have a built scenario; see `modules/README.md` for the honest scope note). Full arc: [`modules/README.md`](modules/README.md).

## What you keep

Every module leaves you with something, not just a passed check: a reusable prompt template, a context-budgeting Skill, a real sub-agent or harness config you can drop into a real project, a loop template, a diagnostic playbook. See [`modules/README.md`](modules/README.md#what-you-keep) for the full list.

## The teaching method

Our working hypothesis, not yet a testable finding: the harness is the classroom. You learn this material by doing it inside a real agent session, with Coachgremlin setting the rubric up front and grading your actual attempt, not by reading a guide. See [`docs/workshop-design.md`](docs/workshop-design.md) for the full reasoning, including where we admit this is a bet we haven't yet built a way to actually test, not proven pedagogy. If you're willing to help test it for real, see "Did you try a module?" below.

## Build in public

This workshop's own build is published as a dated journal at [coderturtle.github.io/terminal-velocity](https://coderturtle.github.io/terminal-velocity/): the maintainer's record of building the workshop and its reusable Gremlin tooling at the same time, written deliberately rather than auto-generated from session logs. That page also has a short guide to the workshop itself, a different entry point than this README, aimed at someone landing on the site directly rather than the repo.

## Something wrong?

This is early and imperfect by design (see "Content status" notes throughout `modules/`). If a module reduces to "read this, then move on" instead of a real gate, or a link here is broken, [open an issue](https://github.com/coderturtle/terminal-velocity/issues).

## Did you try a module?

Tell us what happened, using the [attempt report template](https://github.com/coderturtle/terminal-velocity/issues/new?template=attempt-report.yml) — completed, partial, or abandoned, all equally useful. Nothing in this repo phones home; that form is the only way any information about your attempt reaches us. It's also the only feedback channel this workshop currently has, since as of now nobody outside the people who built it has ever attempted a module.

## Key docs

- [Workshop Design](docs/workshop-design.md): audience, format, teaching method, full module arc
- [Maintainers](docs/maintainers.md): internal/agent-facing docs, classification, documentation contract
