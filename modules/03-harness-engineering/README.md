# Module 03: Harness Engineering

## The question this module answers

What can it reach, and how is the work organized?

## Where it sits in the arc

Third module, after context engineering. This is where the arc turns **structural**: harness engineering is decided largely up front (what tools exist, what sub-agents are on call, what state persists, what the agent is allowed to touch), and you can describe a harness completely without ever running it. That's the hinge module 04 (loop engineering) crosses on purpose: loops are the one case where a running system reaches back in and changes the harness. See [modules/README.md](../README.md) and `docs/workshop-design.md`'s "Our view" section for the full structural-vs-behavioral framing.

## Learning objectives

- Design tool access and sub-agent/specialist boundaries for a task before running anything.
- Use persistent on-disk state to survive a context reset, rather than treating every session as amnesiac.
- Isolate parallel work safely (worktrees) instead of colliding on a shared checkout.
- Recognize when a bad outcome is a harness problem (wrong tool access, no persistent state) rather than a prompt, context, or loop problem.

## Exercise material this module draws from

Tool access, sub-agents/specialists, reusable skills, plugins/connectors (MCP and friends), and isolated worktrees/persistent state: the same vocabulary as `docs/workshop-design.md`'s harness-engineering description. Same underlying mechanism as Module 04's Restartable Handoff Loop material (a goal, changes, verification evidence, and open risks written well enough that a fresh session resumes cold): here it's the harness's job to hold that state, not the loop's.

**Cumulative hook:** Modules 01 and 02 both ran inside a human hand-driving one turn at a time. This module operationalizes that: the harness runs the same kind of task, repeatedly, without you re-explaining scope every time.

## Exercise: bounded specialist, reset, resume

Runs against the shared `receipts` fixture's canonical state (`fixtures/receipts/`), extending it: `group_expenses_by_category` is stubbed (`NotImplementedError`) and `tests/test_by_category.py` ships pre-written and failing, covering both the function and a `--by-category` CLI flag that doesn't exist yet.

> Add a `--by-category` summary to the receipts CLI, with four requirements: (a) define a sub-agent or specialist with a bounded tool and file scope, it can touch `receipts/` and run `tests/test_by_category.py`, nothing else; (b) give it persistent on-disk state, a progress/notes file it writes and re-reads; (c) demonstrate a context reset mid-task where the agent resumes from that state rather than restarting cold, not narrated, an actual fresh session with no memory of the first; (d) show it actually running, with a transcript. Optionally isolate the work in a git worktree.

The gate is already "a harness config that actually runs, with a transcript." The observable that separates a real harness from a described one is the reset-and-resume: stop the first attempt deliberately partway through, start a genuinely fresh session with zero memory of it, and confirm the second session can only complete the task by reading the state the first one left behind.

**Note on scope:** the rest of the test suite has a separate, known failure (Module 04's seeded timezone bug). That's not this exercise's concern; verification should run only `tests/test_by_category.py`. Deciding what's in scope and what isn't, and verifying accordingly, is itself part of "bounded reach."

## Rubric

1. **Bounded reach (scored).** The config grants only the access the task needs; over-broad access (full-repo write, running the whole suite, network) is scoped out, and the boundary is explicit in the sub-agent's own definition, not just followed by luck.
2. **Sub-agent/specialist boundary (scored).** A named specialist with a stated single responsibility, not a monolith asked to do everything.
3. **Persistent state survives reset (gate + scored).** On-disk state exists; a demonstrated context reset, a genuinely new session with no conversational memory of the first, resumes from it and completes correctly.
4. **Actually ran (gate).** Transcript shows the configured harness executing the task correctly, not just described. Self-reported success isn't enough; the result should be independently reproducible from the transcript's own evidence (diffs, command output).
5. **Isolation, conditional (scored).** If worktrees are used, experimental work does not collide with the main checkout. Not required: a plain isolated working copy satisfies the exercise if a worktree isn't used.
6. **Reusable generality (scored).** The config is not hard-wired to one path in a way that cannot transfer to a real project.

## Required to advance

Configure a working harness setup (defined tool access, a sub-agent or specialist boundary, persistent state across a context reset) for the `--by-category` task, and demonstrate it actually running correctly across a real reset-and-resume, not just described. Submitted harness config plus a real run transcript, checked against the rubric above. Reading this module does not count: you advance on a harness that actually ran, not on having read this page.

## Takeaway

A real, reusable sub-agent or harness-config definition (e.g. a `.claude/agents/*.md` file, an MCP server config, or your harness's equivalent) built for the exercise but written generally enough to drop into a real project afterward. This module's takeaway is the strongest fit of the five: the exercise artifact and the reusable takeaway are close to the same thing, unlike modules where the takeaway has to be distilled out of a one-off attempt. Reference implementation: `.claude/agents/receipts-category-summary.md`, run through a real two-phase reset-and-resume, not just written (`runs/2026-07-03-module-03-dry-run/`). Also the leading candidate for the agent-native interaction pilot (`docs/agent-native-interaction-plan.md`): a machine-readable version of this same config is what that pilot would package.

## Stop condition

A harness config that runs the task to a correct result, with a transcript that includes a mid-task context reset, a genuinely new session, resumed from persistent state, not a session that merely claims to have "started fresh." The reset-and-resume is demonstrated, not asserted: independently confirm the second session's starting state (diff the working copy, or check what the second session could plausibly have known without the notes file).

## Harness

Claude-Code-leaning, explicitly, with a mandatory translation table. Sub-agents, skills, worktrees, and MCP are Claude-Code-shaped vocabulary that doesn't map cleanly onto every tool (flagged by the Workshop Review Panel's End-User/Learner persona). Teach it concretely in Claude Code; translate deliberately, not by assuming the vocabulary carries over:

| Claude Code | Cursor | Codex CLI |
|---|---|---|
| Sub-agent (`.claude/agents/*.md`) | Custom mode / rules-scoped chat | Custom instructions scoped to a task |
| Worktree | Git worktree or a separate clone (same underlying git feature) | Git worktree or a separate clone |
| MCP server | MCP server (same protocol) or a Cursor-specific tool/plugin | MCP server (same protocol) |
| Skill (`SKILL.md`) | Rules file / custom prompt library entry | Custom instructions file |

> Content status: core exercise authored 2026-07-03, verified end to end with a real two-phase reset-and-resume: a bounded sub-agent partially completed the task, stopped deliberately, and a second, memory-free session resumed correctly from on-disk state alone (`runs/2026-07-03-module-03-dry-run/`). The agent-native manifest co-production (`docs/agent-native-interaction-plan.md`: schema, grader persona, `module.yaml`, `AGENT.md`) is a separate, larger initiative, deliberately deferred, not part of this content pass.
