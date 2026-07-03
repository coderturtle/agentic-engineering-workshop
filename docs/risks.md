# Risks: Terminal Velocity

## Risk Register

Machine-readable risk state lives in `.hekton/risk-register.yaml`. Keep this
Markdown file as the human-readable explanation of material risks and mitigations.

| ID | Date | Risk | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|---|
| RISK-0001 | 2026-07-03 | Initial governance baseline needs first human/agent review | Medium | Medium | Run governance preflight and end-session review during the first material session | Open |
| RISK-0002 | 2026-07-03 | GitHub push blocked: SSH alias `github.com-coderturtle` and the cached macOS Keychain credential both authenticate as `dermdunc`, not `coderturtle` | Medium | Certain (reproduced) | User to fix the SSH key/account mapping or clear the stale Keychain entry for github.com, then run `git push -u origin main` | Open |
| RISK-0003 | 2026-07-03 | `labs/hekton-cli-lab`'s only branch has substantial uncommitted WIP from a prior (Codex) session, no remote to fall back on | Low | N/A (avoided) | The commit-signature change was made in an isolated git worktree (`hekton-cli-lab--extend-commit-signature`) branched from the last real commit, not the dirty tree — no data touched. Whoever owns that WIP should commit or discard it before the two branches are reconciled. | Open |
| RISK-0004 | 2026-07-03 | Coachgremlin's dry-run grading (Module 04) was self-graded: one session built both attempts and graded them, already knowing which was meant to be weak | Medium | Medium | The rubric-gaming gap this dry run found (`runs/2026-07-03-module-04-dry-run/grading.md`) was closed in the rubric text itself, so it no longer depends on the grader already knowing the answer. Residual risk: a blind, independent grading pass on the same transcripts hasn't been run. Do that before treating Coachgremlin's rubric-discrimination claim as proven, not just plausible. | Open |
