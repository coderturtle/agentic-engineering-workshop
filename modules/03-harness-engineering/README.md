# Module 03: Harness Engineering

## The question this module answers

What can it reach, and how is the work organized?

## Exercise: bounded specialist, reset, resume

Runs against the shared `receipts` fixture's canonical state (`fixtures/receipts/`), extending it: `group_expenses_by_category` is stubbed (`NotImplementedError`) and `tests/test_by_category.py` ships pre-written and failing, covering both the function and a `--by-category` CLI flag that doesn't exist yet.

> Add a `--by-category` summary to the receipts CLI, with four requirements: (a) define a sub-agent or specialist with a bounded tool and file scope, it can touch `receipts/` and run `tests/test_by_category.py`, nothing else; (b) give it persistent on-disk state, a progress/notes file it writes and re-reads; (c) demonstrate a context reset mid-task where the agent resumes from that state rather than restarting cold, not narrated, an actual fresh session with no memory of the first; (d) show it actually running, with a transcript (your own session log or terminal history; if your harness doesn't expose a raw tool-call log, a real-time, chronological action record the agent writes as it works is an acceptable substitute, not a summary written after the fact). Optionally isolate the work in a git worktree.

The gate is already "a harness config that actually runs, with a transcript." The observable that separates a real harness from a described one is the reset-and-resume: stop the first attempt deliberately partway through, start a genuinely fresh session with zero memory of it, and confirm what the second session actually needed to complete the task, not just what it happened to read. **Do this check for real, don't skip it:** rerun the second phase once more, this time without the notes file available, and see whether it still succeeds. If it does, your task's remaining state was already fully recoverable from the code itself, and the notes file wasn't load-bearing for this particular task, which is a real, useful thing to know, not a failed exercise. See "Why this is hard," below.

**Note on scope:** the rest of the test suite has a separate, known failure (Module 04's seeded timezone bug). That's not this exercise's concern; verification should run only `tests/test_by_category.py`. Deciding what's in scope and what isn't, and verifying accordingly, is itself part of "bounded reach."

## Rubric

1. **Bounded reach (scored).** The config grants only the access the task needs; over-broad access (full-repo write, running the whole suite, network) is scoped out, and the boundary is explicit in the sub-agent's own definition, not just followed by luck. Verify this the same way you verify the reset: check what's *outside* the granted scope, not just what's inside it (`git status` or a directory listing beyond the allowed path should show nothing touched).
2. **Sub-agent/specialist boundary (scored).** A named specialist with a stated single responsibility, not a monolith asked to do everything.
3. **Persistent state survives reset (gate + scored).** On-disk state exists; a demonstrated context reset, a genuinely new session with no conversational memory of the first, resumes from it and completes correctly. The notes must describe state and reasoning, not contain a finished, copy-pasteable answer: if the second session's job is just to transcribe what the first session already wrote in full, this criterion isn't demonstrated, it's staged.
4. **Actually ran (gate).** Transcript shows the configured harness executing the task correctly, not just described. Self-reported success isn't enough; the result should be independently reproducible from the transcript's own evidence (diffs, command output).
5. **Isolation, conditional (scored).** If worktrees are used, experimental work does not collide with the main checkout. Not required: a plain isolated working copy satisfies the exercise if a worktree isn't used.
6. **Reusable generality (scored).** The config is not hard-wired to one path in a way that cannot transfer to a real project.

## Required to advance / stop condition

Configure a working harness setup (defined tool access, a sub-agent or specialist boundary, persistent state across a context reset) for the `--by-category` task, and demonstrate it actually running correctly across a real reset-and-resume, not just described. Submitted harness config plus a real run transcript, checked against the rubric above. Reading this module does not count: you advance on a harness that actually ran, not on having read this page.

The reset-and-resume must be demonstrated, not asserted: independently confirm the second session's starting state (diff the working copy against the first session's stopping point), and check, for real, whether the second session's success actually depended on the notes file, not just whether it read them.

## Where it sits in the arc

Third module, after context engineering. This is where the arc turns **structural**: harness engineering is decided largely up front (what tools exist, what sub-agents are on call, what state persists, what the agent is allowed to touch), and you can describe a harness completely without ever running it. That's the hinge module 04 (loop engineering) crosses on purpose: loops are the one case where a running system reaches back in and changes the harness. See [modules/README.md](../README.md) and `docs/workshop-design.md`'s "Our view" section for the full structural-vs-behavioral framing.

## Learning objectives

- Design tool access and sub-agent/specialist boundaries for a task before running anything.
- Use persistent on-disk state to survive a context reset, and recognize when a task's remaining state is actually recoverable from the code alone versus when it genuinely needs to be written down.
- Recognize when a bad outcome is a harness problem (wrong tool access, no persistent state) rather than a prompt, context, or loop problem.

**Worktree isolation is demonstrated as optional, not exercised as a requirement.** It's real, useful practice for genuinely parallel work, but this module's core exercise doesn't force it, and the reference implementation didn't use one. Treat it as a technique to reach for when you're actually running concurrent work against a shared checkout, not a box to check here.

## Why this is hard, and what actually turned out to matter

Tool access, sub-agents/specialists, reusable skills, plugins/connectors (MCP and friends), and isolated worktrees/persistent state: the same vocabulary as `docs/workshop-design.md`'s harness-engineering description. Same underlying mechanism as Module 04's Restartable Handoff Loop material (a goal, changes, verification evidence, and open risks written well enough that a fresh session resumes cold): here it's the harness's job to hold that state, not the loop's.

**Cumulative hook, honestly scoped:** this module doesn't literally chain Module 02's curated context into the harness, or resume a Module 01 prompt; the fixture-family and CLI-shape continuity are real, but the mechanical pipeline isn't. What actually operationalizes here: Modules 01 and 02 both ran inside a human hand-driving one turn at a time; this module is the first place a bounded specialist runs a task on its own, with state that survives you stepping away.

The reset-and-resume claim was tested directly, not just asserted: after the reference two-phase run passed, phase 2 was rerun once more from the identical starting point, this time with the notes file deliberately withheld. **It also succeeded.** The remaining task (implement one function, wire one CLI flag) turned out to be fully reconstructable from the code and the one failing test alone, so the notes file wasn't actually necessary for this specific task, even though the mechanism that produced it is real and correctly built. What would have made it necessary: a decision or dead end from phase 1 that isn't visible in any diff, a partial external operation, a constraint discovered mid-task. A task whose only state is "which of two functions is done" doesn't need a notes file to reconstruct that; a task with real accumulated judgment does. Full method and result: `runs/2026-07-03-module-03-dry-run/README.md`.

## Harness

Claude-Code-leaning, explicitly, with a mandatory translation table. Sub-agents, skills, worktrees, and MCP are Claude-Code-shaped vocabulary that doesn't map cleanly onto every tool. Teach it concretely in Claude Code; translate deliberately, not by assuming the vocabulary carries over:

| Claude Code | Cursor | Codex CLI |
|---|---|---|
| Sub-agent (`.claude/agents/*.md`), `tools:` restricted | Custom mode / rules-scoped chat (tool restriction, not path enforcement) | Custom instructions scoped to a task (prompt-level, not enforced) |
| Worktree | Git worktree or a separate clone (same underlying git feature) | Git worktree or a separate clone |
| MCP server | MCP server (same protocol) or a Cursor-specific tool/plugin | MCP server (same protocol) |
| Skill (`SKILL.md`) | Rules file / custom prompt library entry | Custom instructions file |
| Context reset | New chat / new session | New session (`--resume` off, or a fresh invocation) |

Enforcement isn't equivalent across the row: a Claude Code sub-agent's `tools:` field genuinely narrows what it can call; Cursor's custom modes similarly restrict tools but not per-directory file scope; Codex's custom instructions are unenforced prompt text with no comparable sandboxing. "The boundary held" needs verifying on every harness, not assumed from the config alone.

## Takeaway

Don't open this section before your first attempt: it names the reference implementation directly.

A real, reusable sub-agent or harness-config definition (e.g. a `.claude/agents/*.md` file, an MCP server config, or your harness's equivalent) built for the exercise but written generally enough to drop into a real project afterward. This module's takeaway is the strongest fit of the five: the exercise artifact and the reusable takeaway are close to the same thing, unlike modules where the takeaway has to be distilled out of a one-off attempt. Reference implementation: `.claude/agents/receipts-category-summary.md`. Also the leading candidate for the agent-native interaction pilot (`docs/agent-native-interaction-plan.md`): a machine-readable version of this same config is what that pilot would package.

> Content status: core exercise authored 2026-07-03, restructured 2026-07-03 after the Workshop Review Panel's Module 03 run (`docs/review-panel/2026-07-03-module-03-content.md`), which found the reset-and-resume claim untested against its own stated negative control. Rerun with the notes file withheld; result and honest interpretation in "Why this is hard," above and `runs/2026-07-03-module-03-dry-run/README.md`. The agent-native manifest pilot (`docs/agent-native-interaction-plan.md`: schema, grader persona, `module.yaml`, `AGENT.md`) was built and dry-run verified 2026-07-04: see `module.yaml` and `AGENT.md` beside this file, and `runs/2026-07-04-module-03-manifest-dry-run/` for the real two-phase reset-and-resume evidence. A human-confirmation exercise and the plan's scoped review-panel re-run are still open (`docs/next-actions.md`).
