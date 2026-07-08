# Workshop Review Panel — Module 03 Agent-Native Manifest Pilot Review

**Date:** 2026-07-04
**Scope:** `modules/.manifest.schema.yaml`, `modules/03-harness-engineering/{module.yaml,AGENT.md,README.md}`, `coachgremlin/grader.md`, `runs/.schema.yaml`, `runs/2026-07-04-module-03-manifest-dry-run/`, `runs/run-20260704-AEW-002.yaml`.
**Run:** the scoped 3-persona re-run `docs/agent-native-interaction-plan.md` §5 itself calls for before deciding on further phases (a CLI, an MCP server): Instructional Designer, Security-Conscious Reviewer, Skeptical Practitioner/Critic. All three reviewed independently and in parallel.

## Agreements (2+ personas, independently)

### 1. The Human Gate is enforced by instruction, not structurally (Security-Conscious Reviewer, Instructional Designer)

Both personas independently confirmed the same fact by grepping the repo: no CI workflow, script, or hook anywhere reads or gates on `human_confirmed`. The entire mechanism is `AGENT.md` and `coachgremlin/grader.md` telling an agent to stop and never flip the flag. The dry run demonstrates one compliant agent choosing to comply, which proves the persona *can* work as intended, not that anything *forces* compliance from a careless or adversarial one. This is exactly the risk `docs/agent-native-interaction-plan.md` §6 flags as needing to be "tested, not just documented," and it remains untested against non-compliance.

**Status: fixed in this pass.** `AGENT.md` and `coachgremlin/grader.md` now state plainly that this gate is currently unenforced by tooling. `coachgremlin-assessment.md` and `runs/run-20260704-AEW-002.yaml` carry the same caveat forward.

### 2. "Two genuinely disconnected phases" overclaimed what's actually preserved as evidence (Instructional Designer, Skeptical Practitioner/Critic)

Both personas independently found the same gap from different entry points: phase 1 (implementing `group_expenses_by_category`) was a real agent invocation the orchestrating session dispatched, but its transcript isn't preserved as a standalone artifact; only phase 2's account of finding phase 1's work "already on disk" is. `docs/decisions.md` and `docs/session-log.md` had compressed this into "two genuinely disconnected fresh-agent phases run this session" without that nuance, an overclaim relative to what the written record actually shows, even though the underlying property (phase 2 having zero access to phase 1's conversation) is real and is exactly what reset-and-resume is supposed to test.

**Status: fixed in this pass.** `docs/decisions.md`, `docs/session-log.md`, and the dry-run README now state precisely what phase 2 could and couldn't see, and why that's the intended property, not a gap in whether phase 1 happened.

## Single-persona findings

### 3. "Harness-agnostic" is a design claim about the prose, not an empirically tested property (Skeptical Practitioner/Critic)

The dry run exercised exactly one harness (Claude Code, `engine: claude-sonnet-5`, the `Agent` tool) end to end. The plan's own verification bar calls for a second harness "if available"; that's still open, tracked in `next-actions.md`, but the module's status line called the pilot "dry-run verified" without qualifying that harness-agnosticism specifically wasn't part of what got verified.

**Status: fixed in this pass.** `AGENT.md`'s "Harness-agnostic by design" section, the module README's status line, `docs/decisions.md`, and the ledger's `coachgremlin_assessment` now all state this precisely.

### 4. Soft self-certification risk in `rubric_scores`' free-text language (Security-Conscious Reviewer)

`runs/.schema.yaml` doesn't constrain the `result` string on `rubric_scores`, so language like "meets, gate cleared" for a `weight: gate` criterion reads as de facto certification even when the `human_confirmed` boolean is correctly `false`.

**Status: fixed in this pass.** `coachgremlin/grader.md` now instructs against certifying language in `rubric_scores` explicitly. `runs/run-20260704-AEW-002.yaml` and `coachgremlin-assessment.md` reworded every gate criterion's result to read as observed evidence, not settled certification.

### 5. Rubric drift: `module.yaml`'s weight field couldn't represent a criterion that's both gate and scored (Instructional Designer)

The README's criterion 3 is explicitly "gate + scored"; the schema only allowed `weight: "scored | gate"`, so the manifest silently collapsed it to `gate`, losing the dual nature.

**Status: fixed in this pass.** `modules/.manifest.schema.yaml` gained a third value, `gate_and_scored`; `module.yaml`'s criterion 3 updated to use it.

### 6. The dry run validated the pilot's own authors more than a cold learner (Instructional Designer)

Per the plan's own bar ("point an actual Claude Code session at the module... the observed behavior is the proof"), this dry run was driven by the same agent lineage that authored `AGENT.md`/`module.yaml`, with foreknowledge of the intended design, not a learner encountering it cold.

**Status: not acted on.** This is a real, structural limitation of any pilot's own first dry run (the same is true of every module's first Coachgremlin dry run in this project's history) rather than something fixable by editing prose; noted honestly in `next-actions.md` as a reason a second harness/fresh-learner pass would carry more evidentiary weight than another self-run.

### 7. `coachgremlin_assessment` field name invites reading a self-assessment as certification if seen without its prose context (Skeptical Practitioner/Critic)

**Status: fixed in this pass.** Both `runs/.schema.yaml`'s field comment and the ledger entry's own `coachgremlin_assessment` text now state explicitly that this field is a self-assessment, not a certification, so it reads correctly even in isolation from `coachgremlin-assessment.md`'s longer prose.

## Not acted on

- The Security-Conscious Reviewer's note that `human_notes: ""` was correctly not ghostwritten this run required no fix, just confirmation it held.
- No secrets/credential handling issue was found by the Security-Conscious Reviewer across the manifest, `AGENT.md`, or `grader.md`; confirmed clean, no action needed.
