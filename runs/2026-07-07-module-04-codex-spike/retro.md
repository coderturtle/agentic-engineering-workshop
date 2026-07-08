# Codex CLI spike retro: Module 04, an independent full-harness fresh-agent test

Bounded spike, run alongside (not instead of) the `local-agentic-coding-lab` student-gremlin
spike (`runs/2026-07-07-module-04-student-gremlin-spike/`). Where that spike drives a bounded,
harness-orchestrated pipeline with a small local model doing the diagnosis/patch cognition, this
spike points a real agentic coding harness (Codex CLI, `codex exec`, model `gpt-5.5`) directly at
a fresh copy of the fixture, cold, with no involvement from the authoring session and no
intermediate pipeline at all — the harness chooses its own tool calls end to end.

## Go/no-go: **Go, cleanly**

Ran `codex exec --sandbox workspace-write -C <scratch> --json` against a fresh copy of the
canonical `receipts` fixture (same narrowed file set as the other spike: `receipts/`,
`tests/test_grouping.py` only, no `tests/test_by_category.py`), with a prompt stating the ticket
and Module 04's required behavior (state both terminal states up front; reproduce, root-cause,
smallest fix, rerun; never touch `tests/test_grouping.py`) without revealing the actual fix.

- **Stated terminal states before running**: Codex's very first message (before any command
  execution) stated both terminal states in its own words, matching the prompt's requirement.
  Confirmed from the raw `transcript.jsonl`, not a self-report.
- **Genuinely reproduced, then fixed**: ran `python3 -m unittest discover -s tests`, saw the real
  failure (`....F`), inspected `grouping.py`/`SPEC.md`/`README.md`, correctly identified that
  `tz` was accepted but never used, applied a two-line fix (`from zoneinfo import ZoneInfo`;
  `ts.astimezone(ZoneInfo(tz)).strftime("%Y-%m")`), reran the suite, saw all 5 tests green, and
  only then declared success.
- **Independently reverified, not just trusted**: `git diff --stat` confirms exactly one file
  changed (`receipts/grouping.py`, 2 lines); re-ran the test suite myself against the same
  workspace and confirmed 5/5 passing.
- **Efficient**: one shot, no retries needed. 100,121 input tokens (82,688 cached), 1,459 output
  tokens, per the run's own usage report.

## What this does and doesn't tell us

- **Does** answer the actual original question better than the local-model spike could: yes, a
  fresh, uninvolved agent (a real agentic coding harness, not a hard-coded pipeline) can complete
  Module 04 cold, correctly, with a minimal diff, on the first attempt.
- **Does not** use a local model — this is a cloud-backed harness (`gpt-5.5`), a materially
  different data point from "can a local model on this hardware do this," which was the original
  local-agentic-llm-lab framing. Both spikes are worth keeping precisely because they answer
  different questions.
- **Does not** exercise Module 04's "decision rule applied" criterion (the stable-goal-vs-
  moving-target sentence) — this spike's own prompt only asked for the two terminal states,
  not that separate instruction. An omission in the prompt, not evidence about Codex's ability.
- **Does not** touch Module 03 at all, still the harder, still-unaddressed original target (a
  local or remote agent *designing a harness*, not fixing a bug within one).
- One run. Like the other spike, this is one data point, not a proven-reliable capability claim.

## Artifacts

- `transcript.jsonl`: raw Codex CLI event stream (`--json` output).
- `final-message.txt`: the agent's last message.
- `diff.patch`: the actual applied fix, independently reproducible.
