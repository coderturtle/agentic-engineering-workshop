# Risks: Terminal Velocity

## Risk Register

Machine-readable risk state lives in `.hekton/risk-register.yaml`. Keep this
Markdown file as the human-readable explanation of material risks and mitigations.

| ID | Date | Risk | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|---|
| RISK-0001 | 2026-07-03 | Initial governance baseline needs first human/agent review | Medium | Medium | Run governance preflight and end-session review during the first material session | Open |
| RISK-0002 | 2026-07-03 | GitHub push blocked: SSH alias `github.com-coderturtle` and the cached macOS Keychain credential both authenticate as `dermdunc`, not `coderturtle` | Medium | Certain (reproduced) | User to fix the SSH key/account mapping or clear the stale Keychain entry for github.com, then run `git push -u origin main` | Open |
| RISK-0003 | 2026-07-03 | `labs/hekton-cli-lab`'s only branch has substantial uncommitted WIP from a prior (Codex) session, no remote to fall back on | Low | N/A (avoided) | The commit-signature change was made in an isolated git worktree (`hekton-cli-lab--extend-commit-signature`) branched from the last real commit, not the dirty tree — no data touched. Whoever owns that WIP should commit or discard it before the two branches are reconciled. | Open |
| RISK-0004 | 2026-07-03 | Every module's rubric/diagnosis was self-validated: one session authored each exercise and also ran and judged the attempt(s) against it, already knowing the intended answer | Medium | Medium (was Medium, partially addressed) | All five modules have since been through the Workshop Review Panel against real content (`docs/review-panel/2026-07-03-module-0{1,2,3,4,5}-content.md`), a genuinely different-lens check (seven independent personas) that found and fixed real issues in every module, including two real fixture bugs and one rubric-vs-evidence inconsistency the authoring session itself had missed. This is real independent signal, but the panel was still run by the same overall session/operator in one sitting, not a separate human or a blind pass by someone with no context. Residual risk: no module has been checked by a party with zero involvement in building it. | Open |
