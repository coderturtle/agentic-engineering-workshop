# Module 03 Pilot Completion Plan

Continuation of `docs/agent-native-interaction-plan.md` §5's sequencing. Steps 1-5 (schema,
grader persona, manifest, agent entry point, dry-run verification) and the scoped review-panel
re-run are done (`docs/decisions.md`'s 2026-07-04 rows; `docs/review-panel/2026-07-04-module-03-
manifest-pilot-content.md`). **Steps remaining: 6 (human-confirmation exercise) and, per the
panel's Instructional Designer finding, a second harness *and* a genuinely fresh, uninvolved
attempt first** — the existing dry run validated the pilot's own authors more than a cold
learner, so another self-run wouldn't add real evidentiary weight. Step 8 (decide on the `tv` CLI
/ MCP server phases) is gated on what this evidence shows.

## Why this plan exists, and why it should run with a cleared context

Whoever executes Phase A below should start from a **fresh session with no memory of how this
pilot was built** (a new Claude Code session, `/clear`, or equivalent) — not because the process
matters ceremonially, but because the exact gap this plan closes is "does this hold up against
someone who wasn't in the room when it was designed." An orchestrating session that remembers
today's build history is not a cold reader of `AGENT.md`, and would bias exactly the thing being
tested. Read this plan document itself fresh; do not read `docs/session-log.md`'s build history,
`docs/decisions.md`'s 2026-07-03/04/07/08 entries, or this repo's other `runs/` retros before
attempting Phase A — they contain the reference solution and would spoil the exercise.

**Do not read, before attempting Phase A:**
- `modules/03-harness-engineering/README.md`'s **Takeaway** section (it names the reference
  implementation directly — the file itself warns not to read it before a first attempt).
- `.claude/agents/receipts-category-summary.md` (the reference sub-agent solution).
- Any file under `runs/2026-07-04-module-03-manifest-dry-run/` (the prior dry run's own
  transcripts and solved checkpoints).

## Phase A: second harness + genuinely fresh attempt, in one motion

**Goal:** produce real evidence for two things the panel flagged as still missing: a harness other
than Claude Code, and an attempt by a party uninvolved in building the pilot. Codex CLI satisfies
both at once here — it's already proven (this session, Module 04) to work cold via `codex exec`,
and a fresh `codex exec` invocation has no memory of anything, including this plan's own
authoring.

### Setup

1. Stage a **scratch copy** of the fixture; never run this against the live `fixtures/receipts/`
   in place — that directory stays unsolved for real learners, a deliberate policy from
   2026-07-04 (`docs/decisions.md`).
   ```bash
   SCRATCH=$(mktemp -d /tmp/module-03-pilot-attempt-XXXXXX)
   cp -r /Users/hekton/Development/hekton/factory-output/terminal-velocity/fixtures/receipts/* "$SCRATCH/"
   cd "$SCRATCH" && git init -q && git add -A && git -c user.email=pilot@local -c user.name=pilot commit -q -m "seed"
   ```
2. Confirm `codex` is available and authenticated: `codex doctor` (see this session's own
   transcript for what a healthy result looks like — `auth is configured`, a real model set).

### Phase 1 invocation (design + build)

Run `codex exec` cold, pointed at the scratch copy, with a prompt that tells it **only** what
`AGENT.md` itself tells a learner — do not paraphrase from memory of the reference solution:

```bash
codex exec \
  --sandbox workspace-write \
  -C "$SCRATCH" \
  --skip-git-repo-check \
  --json \
  -o /tmp/module-03-phase1-last-message.txt \
  "$(cat <<'PROMPT'
Read modules/03-harness-engineering/AGENT.md, module.yaml, and README.md (but NOT the
"Takeaway" section of README.md -- skip it, it names a reference solution) from the
terminal-velocity repo at /Users/hekton/Development/hekton/factory-output/terminal-velocity.
Follow AGENT.md's instructions exactly, working only in this directory (a scratch copy of the
receipts fixture). Design a bounded harness/specialist boundary appropriate to your own tool
(state explicitly what mechanism you are using and what it does and does not enforce -- your
own translation-table entry in README.md is unenforced custom-instructions-scoped prompt text,
not path-level sandboxing, so say so plainly rather than overclaiming). Implement
group_expenses_by_category and wire a --by-category CLI flag, confined to this directory.
Write your persistent progress/reasoning to .receipts-category-progress.md at the fixture root
(a sibling of receipts/ and tests/), describing state and reasoning, not a finished
copy-pasteable answer. Run the tests yourself before stopping. Then stop -- a second, separate
invocation with no memory of this one will resume from your notes file alone.
PROMPT
)" \
  < /dev/null \
  > /tmp/module-03-phase1-events.jsonl 2>&1
```

Monitor `ollama ps`/`ps aux` is not relevant here (Codex is cloud-backed, not local) but do watch
that it stays within `$SCRATCH` (check `git status`/`git diff --stat` in `$SCRATCH` after it
finishes — nothing outside the directory should be touched, and the harness boundary claim above
should be checked against what actually happened, not just what the transcript asserts).

### Phase 2 invocation (genuinely disconnected reset-and-resume)

A **separate `codex exec` invocation** (a new process; do not use `codex resume`) is itself the
context reset — per the module's own harness-translation table, this is what "context reset"
means for Codex CLI. Give it only the fixture directory and a prompt that does **not** repeat
phase 1's reasoning:

```bash
codex exec \
  --sandbox workspace-write \
  -C "$SCRATCH" \
  --skip-git-repo-check \
  --json \
  -o /tmp/module-03-phase2-last-message.txt \
  "Resume work in this directory. Read .receipts-category-progress.md for the current state and
reasoning, then finish and verify the --by-category feature per that file and
modules/03-harness-engineering/README.md's task description (terminal-velocity repo at
/Users/hekton/Development/hekton/factory-output/terminal-velocity). Run the tests yourself." \
  < /dev/null \
  > /tmp/module-03-phase2-events.jsonl 2>&1
```

Before trusting this, **independently confirm** (per `AGENT.md`'s own requirement): diff
`$SCRATCH`'s state at the start of phase 2 against phase 1's stopping point, and check whether
phase 2's success genuinely depended on the notes file, not just whether it read them.

### Negative control (required by AGENT.md/README, not optional)

Re-stage a fresh scratch copy from phase 1's *stopping point* (not from scratch), **withhold**
`.receipts-category-progress.md`, and run a third `codex exec` invocation with the same "resume
and finish" prompt but no notes file to read. Report honestly whether it still succeeds (code/
tests alone may be enough to reconstruct the remaining work, as the 2026-07-03 dry run's own
negative control found for a different session — if so, say that plainly, it's a valid and
useful finding, not a failure of the pilot).

### Self-assess and record

Load `coachgremlin/grader.md` as the grading persona. Score the attempt against
`modules/03-harness-engineering/module.yaml`'s rubric (six criteria: bounded reach, sub-agent/
specialist boundary, persistent state survives reset, actually ran, isolation, reusable
generality). Write a `runs/` entry per `runs/.schema.yaml`: `task_type: exercise`, `module_id:
03-harness-engineering`, `attempt_driver: agent`, `rubric_scores`, `coachgremlin_assessment`,
**`human_confirmed: false`**. Do not certify completion yourself — that is Phase B, and it is not
yours to do. Save the two (or three, with the negative control) sets of transcripts/events as a
new `runs/YYYY-MM-DD-module-03-second-harness-spike/` directory, matching this project's existing
`runs/` retro convention (see `runs/2026-07-07-module-04-codex-spike/` for the shape: `retro.md`,
`diff.patch` or equivalent, transcripts, a ledger `.yaml`).

**Honest reporting, not overclaiming**: state plainly whether Codex's declared harness boundary
was actually enforced or just requested (per the module's own "enforcement isn't equivalent
across the row" warning), and whether this attempt was genuinely "fresh" (it wasn't run by the
session that authored `AGENT.md`/`module.yaml`, but it *was* orchestrated by a session that read
this plan document, which itself describes the exercise — note that nuance rather than claim a
purer independence than actually held).

## Phase B: the human-confirmation exercise (human-only, not agent-executable)

Once Phase A produces real evidence, **coderturtle** reviews it: the harness config, both (or
three) transcripts, and the reset-and-resume evidence. Per `module.yaml`'s
`human_gate.attestation_requirement`, `human_confirmed: true` must mean "I reviewed the harness
config, understand exactly what it can and cannot reach, and independently confirmed the
reset-and-resume evidence myself" — not "an artifact exists." `human_notes` must be written by
the human, in their own words; an agent must not ghostwrite it (per `coachgremlin/grader.md`'s own
rule). This step cannot be delegated forward in this plan; it stops here for a human decision.

## Phase C: decide on the `tv` CLI / MCP server phases

Only after Phase B, informed by what Phase A actually revealed (e.g., if Codex's harness-boundary
claim turned out weak/unenforced in practice, that's real evidence toward whether module 03 needs
a stronger interface, per `docs/agent-native-interaction-plan.md` §5 item 8). Not scoped further
here — genuinely gated on Phase A/B's findings, per the original plan's own sequencing.

## Documentation contract for whoever runs this

Per this repo's standing rules (`CLAUDE.md`): update `docs/decisions.md` (a new dated row),
`docs/next-actions.md` (mark Phase A's items done, keep B/C as the open next step), and
`docs/session-log.md` (a full entry: what changed, decisions, assumptions, risks, next actions,
validation, mind-palace updated y/n) after Phase A completes. Do not touch the Obsidian vault
(`vault_mutation_allowed: false`) without separate, explicit authorization.

## Critical files reference (repo-relative, from this project's root)

- `modules/03-harness-engineering/AGENT.md` — the actual exercise instructions to follow
- `modules/03-harness-engineering/module.yaml` — machine-readable rubric/gate/stop_condition
- `modules/03-harness-engineering/README.md` — human-readable prose (skip the Takeaway section)
- `coachgremlin/grader.md` — the grading persona to load
- `runs/.schema.yaml` — the ledger entry schema
- `fixtures/receipts/` — the fixture to copy (never mutate in place)
- `docs/agent-native-interaction-plan.md` — the original design plan this completes
