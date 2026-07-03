# Workshop Design (Track B)

> Working title: **"Prompt → Loop"**. Final name is a deliverable of the Workshop Gremlin's naming agent (see `docs/workshop-gremlin-design.md` and `docs/next-actions.md`) — this doc uses the working title until the human picks from the naming agent's candidates.

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
- The harness *is* the classroom. This is the workshop's punchy thesis and the reason it can't just be a written guide: the medium of instruction matches the skill being taught.

## The three-part arc

The workshop's spine is the evolution of practice, in order, with an explicit "how they fit together" synthesis at the end rather than treating them as three unrelated topics.

1. **Prompt engineering** — the atomic unit: getting a single turn to do what you want. Precision, structure, examples, constraints. Framed as necessary but insufficient once tasks span more than one turn.
2. **Context engineering** — what surrounds the prompt: what's in the window, what's retrieved, what's summarized versus preserved verbatim, what's excluded on purpose. The shift from "write a good instruction" to "curate what the model can see."
3. **Loop engineering** — the current frontier: designing the harness itself — stop conditions, tool access, feedback loops, verification steps, multi-turn state. Where prompt and context engineering become inputs to a system that runs itself toward a goal.
4. **Synthesis capstone** — how the three actually compose in a real harness today: a prompt is one turn's context; context engineering shapes what a loop iteration sees; loop engineering decides when to stop asking. The capstone exercise has the learner diagnose which of the three is the bottleneck in a deliberately broken agent task, then fix it.

Each of the four gets at least one Coachgremlin-run exercise with its own rubric; exact exercise specs are a later Workshop Gremlin run (deliverables/branding + content-building), not this design pass.

## Build-in-public build log

The build of this workshop itself is published as a dated build-log/journal via GitHub Pages (Astro, see `docs/workshop-gremlin-design.md`), separate from the module content. It's the maintainer's own record of building the workshop and the Gremlin simultaneously — a real demonstration of the practices being taught, not auto-generated from session logs.

## What's explicitly out of scope for this design pass

- Exact exercise specs and rubrics per module (Coachgremlin's job, run later, one concept at a time).
- The final workshop name (naming agent's job — human picks from candidates).
- The actual Astro site content and first Pages deploy.

## Open questions for the next run

- Exact number of exercises per module (one deep exercise vs. several short ones)?
- Whether the capstone is graded/certified in any way, or purely self-assessed (leaning self-assessed, given no facilitator and no external credential currently planned).
