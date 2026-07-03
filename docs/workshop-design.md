# Workshop Design (Track B)

> **Terminal Velocity.** Naming pass complete (see `docs/workshop-gremlin-design.md` and `docs/decisions.md`) — this doc was drafted under the working title "Prompt → Loop" and has since been updated throughout.

## The one-line problem

Practitioners who are already using coding agents daily have absorbed prompt engineering by osmosis, are half-aware context engineering is a thing, and mostly haven't named or systematized "loop engineering" at all — even though they're doing pieces of all three. There's no single, current account of how the three fit together, and no course that teaches them the way they actually work: inside a harness.

## Audience

Advanced practitioners already using agents daily (Claude Code, Codex, Cursor, etc.). This is **not** an intro-to-AI workshop. It assumes:
- Comfort with git, CLI tools, and reading diffs.
- Regular use of at least one coding agent/harness already.
- No assumed familiarity with the terms "context engineering" or "loop engineering" specifically — that vocabulary and its structure is exactly what's being taught.

## Format

Self-paced, public repo. Learners clone it and work through modules using their own harness. No facilitator required. This matches the "public workshop" framing and scales without a live cohort.

## The teaching method: agent-native

The workshop's core bet is that you learn agentic engineering *by doing it inside a harness*, not by reading about it. Concretely:

- Every module's core exercise is run through a real coding-agent harness — the learner drives Claude Code (or equivalent), not a notebook or quiz.
- **Coachgremlin** (see `docs/workshop-gremlin-design.md`) frames each exercise, sets the rubric up front, and gives feedback against the learner's actual attempt — it does not lecture and does not hand over the solution.
- Our working hypothesis, not a proven finding: the harness *is* the classroom. We don't yet have data or a prior pilot showing this teaches better than a well-structured written guide — it's the workshop's central bet and the reason it can't just be a written guide, but it should be read as a hypothesis this workshop is testing, not a settled claim.

## The four-module arc (+ synthesis capstone)

Harness engineering was originally folded into the loop-engineering module. After reviewing three external accounts of loop engineering (see Sources, below), we split it into its own module — the distinction is real and teachable, not cosmetic. The workshop's spine is the evolution of practice, in order, with an explicit "how they fit together" synthesis at the end rather than treating the parts as unrelated topics.

1. **Prompt engineering** — the atomic unit: getting a single turn to do what you want. Precision, structure, examples, constraints. Framed as necessary but insufficient once tasks span more than one turn.
2. **Context engineering** — what surrounds the prompt: what's in the window, what's retrieved, what's summarized versus preserved verbatim, what's excluded on purpose. The shift from "write a good instruction" to "curate what the model can see."
3. **Harness engineering** — the structural layer: what the agent can *reach* and how its work is *organized*, decided before it ever runs. Tool access, sub-agents/specialists, reusable skills, plugins/connectors to external systems (MCP and friends), isolated worktrees, and persistent on-disk state across context resets. The question this module answers is **"what can it reach, and how is the work organized?"** — a structural design decision that's stable *by default*, though module 4 covers the one case (hill-climbing) where a loop deliberately reaches back in and changes it.
4. **Loop engineering** — the behavioral layer, built *on top of* a harness that already exists. Stop conditions, verification/grading against a rubric, event-driven triggers, and the meta move where an outer loop *proposes* rewrites to the inner harness's own config or prompts based on production traces ("hill-climbing") — proposals a human reviews before they're adopted, not auto-applied changes; see the taxonomy below. The question this module answers is **"when does it stop, how do we know it's right, and how does it get better without me watching every turn?"** — dynamic, runtime, and (at the frontier) self-modifying under human review.
5. **Synthesis capstone** — how all four actually compose in a real harness today: a prompt is one turn's instruction; context engineering shapes what that turn can see; harness engineering decides what the agent can reach and how its work is organized; loop engineering decides when it stops, how it verifies, and how it rewrites itself. The capstone exercise has the learner diagnose which of the four is the bottleneck in a deliberately broken agent task, then fix it.

### Our view: how harness engineering evolved into loop engineering

This is our own synthesis, not a restatement of any one source, and it's a teaching framing we're proposing, not an independently validated pedagogical finding — we split it this way because it made the two modules teachable as distinct skills, not because it's the only correct way to carve the problem:

- **Harness engineering is a question about structure.** It's decided up front and stable by default: what tools exist, what sub-agents are on call, what state persists, what the agent is allowed to touch. You can describe a harness completely without ever running it — *unless* a hill-climbing loop is deliberately changing it (see below), which is the one case where the structural/behavioral line gets crossed on purpose.
- **Loop engineering is a question about behavior over time.** It only exists once the harness is running: how many iterations, what counts as "done," what triggers a re-run, what happens when a verifier disagrees with the agent — including, at the frontier, proposing changes back to the harness itself, gated by human review rather than applied automatically.

Our working narrative for *why* the split emerged (not a verified historical claim — we have no dates or named examples to back this beyond the three sources we read): loop engineering became worth naming separately once harnesses got good enough that "give it more tools" stopped being the obvious next question. Once tool access, sub-agents, and state felt like solved problems, the open question shifted toward *how does it know when to stop, whether it's right, and how it gets better without a human watching every turn*. That shift is why the capstone treats harness and loop as sequential dependencies (you need a harness before a loop has anything to run inside) rather than as synonyms — but treat this as our organizing story, not settled fact.

### Loop taxonomy (used inside the loop-engineering module)

Rather than teach "loop engineering" as one undifferentiated idea, the module uses a four-layer taxonomy, cleanest as a teaching tool:

1. **Agent loop** — the base case: the model calls tools in a loop until a task is complete.
2. **Verification loop** — an added grading pass: output is checked against a rubric and sent back on failure.
3. **Event-driven loop** — the agent loop is triggered by something external (a webhook, a schedule, a message), not run ad hoc.
4. **Hill-climbing loop** — the frontier case: traces from real runs feed an analysis pass that *proposes* rewrites to the harness's own config or prompts — the outer loop reaches back in and edits the inner one. **This must be taught with an explicit gate**: a proposed rewrite is only adopted if it passes verification (regression-free, per Forward Future's vocabulary above) and a human reviews it — never auto-applied. A learner copying this pattern without that gate is copying an unsafe default, not the actual practice.

**Practical rubric for learners:** not every task deserves a loop. The decision rule we teach: *stable goal → build the loop; moving target → keep it a manual, prompt-driven task.* Loops pay for their setup cost only when the success criteria hold still.

### Exercise material to draw from (content-building phase, not this design pass)

Real named patterns to base Coachgremlin exercises on, rather than inventing scenarios from scratch:
- **Ticket-to-PR-Ready Loop** — reproduce → root-cause → smallest fix → rerun tests, with an explicit "can't reproduce after two attempts" terminal state.
- **Restartable Handoff Loop** — a session-continuity exercise: state a goal, changes, verification evidence, untouched scope, and open risks well enough that a fresh session can resume cold.
- **The "ralph loop"** (Geoffrey Huntley) — a long-running loop that preserves progress via git history and external memory instead of context window state; good material for the hill-climbing/self-improving concept.

Each of the four core modules (plus the capstone) gets at least one Coachgremlin-run exercise with its own rubric; exact exercise specs are a later Workshop Gremlin run (deliverables/branding + content-building), not this design pass.

## Build-in-public build log

The build of this workshop itself is published as a dated build-log/journal via GitHub Pages (Astro, see `docs/workshop-gremlin-design.md`), separate from the module content. It's intended as the maintainer's own record of building the workshop and the Gremlin simultaneously — deliberately written, not auto-generated from session logs — but that intent hasn't been demonstrated yet; the first real entry (part of the implementation-plan.md build-log work) is what will prove or disprove it.

## What's explicitly out of scope for this design pass

- Exact exercise specs and rubrics per module (Coachgremlin's job, run later, one concept at a time).
- The final workshop name (naming agent's job — human picks from candidates).
- The actual Astro site content and first Pages deploy.

## Open questions for the next run

- Exact number of exercises per module (one deep exercise vs. several short ones)?
- Whether the capstone is graded/certified in any way, or purely self-assessed (leaning self-assessed, given no facilitator and no external credential currently planned).
- Whether to explicitly cite/engage the external framings below inside the module content (e.g. "here's one industry account, here's ours, argue with both") or fold them in silently as background research. Given the audience is advanced practitioners, an explicit "here's a live disagreement in the field" framing may teach better than a tidy consensus narrative.

## Sources reviewed (2026-07-03)

Three industry blog posts, not peer-reviewed research — they shaped the harness/loop split and the loop taxonomy above as inspiration, and the "our view" section is our own synthesis, informed by but not copied from (or validated by) these:

- Forward Future, [Loop Library](https://signals.forwardfuture.com/loop-library/) — loops as repeatable, bounded workflows; named patterns (Ticket-to-PR-Ready, Promise-to-Proof, Restartable Handoff); vocabulary (terminal states, regression-free, evidence ledger, blast radius).
- LangChain, [The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) — the four-layer taxonomy (agent / verification / event-driven / hill-climbing loop) and the "outer loop rewrites the inner loop" insight.
- CodeRabbit, [Loop Engineering](https://www.coderabbit.ai/blog/loop-engineering) — historical arc (prompt engineering → context management → harness engineering → loop engineering); Addy Osmani's five-plus-one harness architecture; the "ralph loop"; the stable-goal-vs-moving-target decision rule.
