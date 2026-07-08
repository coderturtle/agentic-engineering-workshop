# Student-gremlin spike retro: Module 04, `local-agentic-coding-lab` (3 attempts, consolidated)

> **Resolved 2026-07-08**: a 4th attempt, after fully root-causing attempt 3's incident (the
> "requested 32768, observed 384000" framing below turned out to be wrong — see the corrected
> account), converged cleanly. Full record:
> `runs/2026-07-08-module-04-student-gremlin-spike/retro.md`.

Bounded spike (see `docs/decisions.md`'s 2026-07-07 entries), not a standing "student gremlin"
product. Driver: `local-agentic-coding-lab/scripts/workshop_student_spike.py`, which stages a
copy of the canonical `fixtures/receipts/` fixture (already in its seeded-bug state) and drives
that lab's existing `coding.bugfix` capability
(`src/hekton_coding/workflows/bugfix.py:run_bugfix_workflow`) against it, cold, then self-assesses
against Module 04's rubric and writes a `runs/` ledger entry (`human_confirmed: false`).

This retro consolidates all three attempts made this session, since the diagnosis evolved across
them. **A data-hygiene note first**: attempt 1's raw evidence (`run_log.json`, `transcript.jsonl`,
`evidence.json`/`.md`) was overwritten on disk by attempt 2's re-run before this consolidation —
both attempts wrote to the same date-based directory name. Attempt 1's specific findings below are
preserved from what was captured in this file at the time (the exact error strings were quoted
before being overwritten), but its raw artifacts are gone; only attempt 2's raw evidence survives
on disk. Worth stating plainly rather than pretending the record is cleaner than it is.

## Attempt 1 (no fix): No-go

`devstral-small-2:24b` (this lab's real `coder`-role default, not `qwen2.5-coder:7b` as first
assumed) correctly diagnosed the actual bug (UTC month key never converted to the target
timezone) in every localisation call, but its structured-edit JSON patch response was truncated
or malformed before `msgspec` could decode it on every patch-generation attempt across two
sub-runs (errors captured at the time: `"Input data was truncated"`, `"invalid character (byte
0)"`). No patch was ever built. Ledger: `run-20260707-AEW-008.yaml`.

## Attempt 2 (`fmt="json"` fix only): Still no-go, but a materially better diagnosis

Investigating attempt 1 further (see `local-agentic-coding-lab/docs/decisions.md`'s ADR-044)
found the real, confirmed cause: the patch-generation call requested no `format: "json"` from
Ollama, so nothing enforced valid JSON grammar. Fixed on branch
`fix/patch-generation-json-format` (local commit only, not merged/pushed). Re-ran the spike
against the patched code: **still failed**, same truncation shape
(`run_log.json` in this directory: `"Input data was truncated"` on both iterations). This proved
`fmt="json"` alone was necessary but not sufficient. Ledger: `run-20260707-AEW-010.yaml`.

## Attempt 3 (`fmt="json"` + `options.num_ctx`): Stopped for safety, not a clean result either way

Root-caused further: Ollama's own un-requested default context window is 4096 (confirmed via
`ollama ps`), too small for this call's real prompt (fix_plan + full file content) plus the
expected structured-edit JSON response. An isolated direct-API test using the *actual* captured
fix_plan text from attempt 2 (not a shortened synthetic prompt) with `options={"num_ctx": 32768}`
(this model's own `config/models.yaml` registry value) completed cleanly: `done_reason: "stop"`,
valid JSON, 2 edits, in 93.9s.

Wiring that identical `num_ctx` value into the real workflow and running it end to end did
**not** reproduce that clean result. Instead, the resident model reloaded at context **384000**
(not the requested 32768; cause unconfirmed), memory ballooned to ~49GB at a 66%/34% CPU/GPU
split, and the process sat active for 30+ minutes before being force-stopped (`ollama stop`) for
safety, on this machine's 24GB of RAM. No ledger entry or artifacts exist for this attempt — the
script crashed inside the workflow call itself (an uncaught `RuntimeError: timed out`) before
reaching the point where it would have written one. This is the right outcome: an unexplained
resource blowup should not produce a "done" artifact.

**Not shipped.** The `num_ctx` change was reverted from the fix branch; only `fmt="json"` landed.
See `local-agentic-coding-lab/docs/next-actions.md`'s updated item for the open question (why did
requested and observed context diverge) before anyone tries a context override on this call again.

## What this three-attempt arc does and doesn't tell us

- **Does** show real, iterative root-causing produces a materially better diagnosis than stopping
  at the first plausible hypothesis (timeout/`num_predict`, both directly ruled out) would have.
- **Does not** show a local model can complete Module 04 end to end yet — three attempts, zero
  successes. The complementary Codex CLI spike (`runs/2026-07-07-module-04-codex-spike/`) *did*
  succeed, cleanly, on the first try, using a full agentic harness rather than this bounded
  pipeline — a materially different, cloud-backed data point answering a related but distinct
  question (see that spike's own retro for how the two compare).
- **Does not** touch Module 03 at all — still the harder, still fully open original target.
- Surfaces a real operational lesson for running 24B-class local models on a 24GB machine:
  context-size requests can interact with model residency/reload behavior in ways that aren't
  fully understood yet, and are worth treating with real caution, not just "set a bigger number."

## Artifacts in this directory

- `run_log.json`, `transcript.jsonl`, `evidence.json`/`.md`, `traceback.txt`: attempt 2's raw
  evidence (the only attempt whose raw artifacts survived; see the data-hygiene note above).
- `diff.patch`: empty — no attempt ever successfully built a patch.
