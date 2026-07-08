# Risks: Terminal Velocity

## Risk Register

Machine-readable risk state lives in `.hekton/risk-register.yaml`. Keep this
Markdown file as the human-readable explanation of material risks and mitigations.

| ID | Date | Risk | Impact | Likelihood | Mitigation | Status |
|---|---|---|---|---|---|---|
| RISK-0001 | 2026-07-03 | Initial governance baseline needs first human/agent review | Medium | Medium | Run governance preflight and end-session review during the first material session | Open |
| RISK-0002 | 2026-07-03 | GitHub push blocked: SSH alias `github.com-coderturtle` and the cached macOS Keychain credential both authenticate as `dermdunc`, not `coderturtle` | Medium | Certain (reproduced) | User to fix the SSH key/account mapping or clear the stale Keychain entry for github.com, then run `git push -u origin main` | Open |
| RISK-0003 | 2026-07-03 | `labs/hekton-cli-lab`'s only branch has substantial uncommitted WIP from a prior (Codex) session, no remote to fall back on | Low | N/A (avoided) | The commit-signature change was made in an isolated git worktree (`hekton-cli-lab--extend-commit-signature`) branched from the last real commit, not the dirty tree — no data touched. Whoever owns that WIP should commit or discard it before the two branches are reconciled. | Open |
| RISK-0004 | 2026-07-03 | Every module's rubric/diagnosis was self-validated: one session authored each exercise and also ran and judged the attempt(s) against it, already knowing the intended answer | Medium | Medium (was Medium, partially addressed) | All five modules have since been through the Workshop Review Panel against real content (`docs/review-panel/2026-07-03-module-0{1,2,3,4,5}-content.md`), a genuinely different-lens check (seven independent personas) that found and fixed real issues in every module, including two real fixture bugs and one rubric-vs-evidence inconsistency the authoring session itself had missed. **2026-07-07 addition**: a local, blind, multi-persona judging panel (`local-llm-lab`, `qwen2.5:14b-instruct`, three personas) independently re-graded Module 04's already-graded good/gaming transcripts with zero access to the original verdict, and reproduced the original pass/fail split, every persona catching the exact gaming behavior the original grading flagged (full record: `local-llm-lab/docs/workshop-judge-panel-spike-retro.md`, referenced from `runs/2026-07-07-module-04-student-gremlin-spike/retro.md`'s sibling spike). This is real, non-Claude, zero-authorship-involvement signal, genuinely different in kind from the Review Panel (a different model family scoring blind, not another persona lens on the same underlying grader). Still a bounded spike, not a standing process: one rubric, two transcripts, one run (reproduced once). Residual risk, updated: no module has been checked by a human with zero involvement in building it, and no standing practice yet repeats this local-panel check across other modules or on fresh (not-already-graded) attempts. | Open |
| RISK-0005 | 2026-07-08 | (Vulnerability Gremlin run) `site/` dependencies carry 4 inherited vulnerabilities (`npm audit`: 1 high, 3 low, Astro <=7.0.0-alpha.1 / esbuild chain via `@astrojs/mdx`/`@astrojs/tailwind`) — never triaged since scaffolding | Low - triaged 2026-07-08, see below | Certain (present on every `npm install`) | **Triaged and accepted, not fixed.** See rationale below. Re-open if `output` mode ever changes from `"static"`. | Closed |
| RISK-0006 | 2026-07-08 | (Vulnerability Gremlin run) `fixtures/receipts/` (the Python exercise fixture) has no third-party dependencies to audit | N/A - nothing to check | N/A | Confirmed via direct inspection: no `requirements.txt`/`pyproject.toml`/`setup.cfg` anywhere under `fixtures/receipts/`, and every import in `receipts/*.py` resolves to the standard library (`collections`, `dataclasses`, `datetime`, `argparse`, `csv`, `sys`, `__future__`). Recorded so a future audit doesn't have to re-derive that there's genuinely nothing here, not silently skipped. | Closed (informational) |

## RISK-0005 triage detail (2026-07-08, Vulnerability Gremlin's third real run)

Third real run, after `half-life`'s RISK-0002 and `borrow-native`'s RISK-0002/RISK-0003 (both
2026-07-08). Same npm/Astro finding as both prior runs, but this is the first time it's caught
here at all - unlike the other two projects, this one had never had the finding flagged during
scaffolding, so it was a genuinely new discovery here, not a pre-flagged-but-unclosed one.

**Checked directly against this project's own code:** `grep -rn "define:vars\|server:island"
site/src/` returns nothing. `site/astro.config.mjs` sets `output: "static"`. `.github/workflows/
*.yml` only runs `npm run build`. Same reachability conclusion as both prior runs: none of the 5
Astro/esbuild advisories apply given this project's actual configuration.

**Attempted the upgrade for real, not assumed from the prior two runs**, because the offered target
version differed (`astro@7.0.7` here vs. `7.0.6` seen in `half-life`/`borrow-native` - a newer
patch had been published between sessions): `npm audit fix --force` upgraded cleanly (0
vulnerabilities), the same first mechanical failure reproduced (legacy `src/content/config.ts`
path, fixed by moving it), and after that fix, the same `@astrojs/tailwind` failure reproduced
identically (`Cannot read properties of undefined (reading 'postcss')`) - confirming this is a
structural incompatibility (Astro dropped the integration API `@astrojs/tailwind` depends on), not
something a newer patch release fixes. Reverted fully (`git reset`/`git checkout HEAD --
site/`, re-installed original dependencies, re-confirmed `npm run build` clean, 8 pages).

**Decision:** accept the risk as-is, same reasoning as the other two projects' RISK-0002 entries.
All three of this factory's public workshops now carry the identical, documented, accepted risk and
the identical known upgrade path (a real `@astrojs/tailwind`-to-Tailwind's-own-Vite-plugin
migration) - worth doing once, across all three sites together, rather than three separate future
sessions rediscovering the same blocker.

## RISK-0006 detail: `fixtures/receipts` has nothing to audit (2026-07-08)

Per the Vulnerability Gremlin's own Workflow (audit every package-manager ecosystem present, not
just the one with findings): `fixtures/receipts/` is a Python exercise fixture with zero
third-party dependencies. Checked directly, not assumed from the absence of a lockfile alone:
grepped every `import`/`from` statement in `receipts/*.py` and confirmed each resolves to the
Python standard library. There is no `pip-audit`/`safety` run to perform here because there is no
dependency tree to run it against.
