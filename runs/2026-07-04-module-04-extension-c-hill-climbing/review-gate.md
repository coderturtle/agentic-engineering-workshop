# Human review gate: proposed rewrite to `.claude/commands/ticket-to-pr-ready.md`

**This is a gate, not a formality.** Per Module 04's hill-climbing safety rule and
`docs/agent-native-interaction-plan.md`'s Human Gate extension, a proposed self-rewrite of a loop's
own prompt/config is never auto-applied, regardless of how clean the regression check looks.

## What's being proposed

Add a new step 6 ("Check blast radius") to `.claude/commands/ticket-to-pr-ready.md`, running
`scripts/blast-radius-check.sh` against the fix's diff before trusting a green rerun. Full diff:
`proposed-diff.patch`. Full reasoning: `analysis.md`.

## Verification already done (regression-free, not sufficient on its own)

- The real `attempt-good/` diff still passes under the proposed check.
- The real `attempt-gaming/` diff still fails under the proposed check, for the reason a human
  grader originally caught it.
- The proposed diff was generated and reviewed as a patch; `.claude/commands/ticket-to-pr-ready.md`
  itself has not been modified by this analysis.

Passing regression is necessary, not sufficient. It confirms the change doesn't break known
history. It does not confirm the change is worth making, has no side effects on tickets shaped
differently from these three, or reads clearly to a learner encountering it for the first time.
That judgment is this gate's job, not the regression check's.

## Attestation required (not just an artifact existing)

| Field | Value |
|---|---|
| `human_confirmed` | `false` |
| `human_notes` | *(leave for the reviewing human to write in their own words; not pre-filled here)* |
| `reviewed_diff` | `proposed-diff.patch` |
| `adoption_action_if_approved` | Apply `proposed-diff.patch` to `.claude/commands/ticket-to-pr-ready.md` directly; do not re-derive the change from `analysis.md` by hand, to avoid drift between what was reviewed and what gets applied. |

See the matching run-ledger entry, `runs/run-20260704-AEW-003.yaml` (`task_type: review`,
`human_confirmed: false`), for the machine-readable record of this gate.
