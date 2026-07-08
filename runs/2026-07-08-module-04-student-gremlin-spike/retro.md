# Student-gremlin spike retro: Module 04, `local-agentic-coding-lab` — attempt 4 (resolution)

Continuation of `runs/2026-07-07-module-04-student-gremlin-spike/retro.md` (attempts 1-3, all
no-go). This is attempt 4, after fully root-causing attempt 3's resource-exhaustion incident.

## Go/no-go: **Go.** Ledger: `run-20260708-AEW-011.yaml` (`human_confirmed: false`).

`devstral-small-2:24b`, driven cold by `local-agentic-coding-lab`'s existing `coding.bugfix`
capability, reached a genuine tests-green terminal state on Module 04's seeded bug, in 4
iterations (the full cap — it didn't converge quickly, but it did converge, on a real terminal
state, not a manual kill). Diff confined to exactly `receipts/grouping.py`; `tests/test_grouping.py`
untouched. Independently reviewed (`run_log.json`'s per-iteration record): iteration 0 errored on
load, iterations 1-2 produced a real patch that still failed the target test, iteration 3's patch
correctly converts the parsed UTC timestamp to the target timezone before computing the month key
— a valid, if more defensive-than-minimal, fix (it adds a `_localize_utc_to_tz` helper with a
`pytz` fallback for older Python, not the two-line change a human reference solution uses, but
still confined to the right file and the right mechanism).

## The real root cause of attempt 3's incident (corrected)

Attempt 3's retro (in the 2026-07-07 directory) initially described this as an "unexplained
requested-vs-observed context discrepancy" (requested `num_ctx: 32768`, observed context
`384000`). **That framing was wrong**, found by checking the Ollama server log
(`/opt/homebrew/var/log/ollama.log`) directly rather than continuing to guess:

- The isolated tests that had verified `32768` as "safe" were checking a **different model's**
  registered context (`qwen2.5-coder:7b`'s, confused with devstral's) — not a real value ever
  used by the actual code path.
- The real code (`coder_model.context`) correctly read **384000** the entire time, from *both*
  `config/models.yaml` (the real, gitignored, machine-specific file) and
  `config/models.example.yaml` (the tracked fallback) — they agree. There was no discrepancy.
- `384000` is devstral-small-2:24b's own genuine max supported context (confirmed via
  `ollama show`), not a typo. Its KV cache alone at that size is ~32GB (`llama_kv_cache: size =
  31875.00 MiB`, confirmed in the Ollama log) — larger than this machine's entire 24GB of RAM.
  The blowup was simply what happens when that value is honored on hardware that can't fit it.
  Not a bug, not a race, not thermal throttling (a hypothesis floated and also wrong).
- Separately: `config/models.yaml` is gitignored and was genuinely absent from the isolated
  `git worktree` attempt 3 ran from, so *that specific test* fell back to
  `config/models.example.yaml` — but both files agreed on `384000` anyway, so this wasn't the
  actual cause either, just a contributing factor in how the incident was first (mis)diagnosed.

## The actual fix (schema-level, not a hardcoded number)

`context: 384000` is correct and left unchanged (correct for the `mac_64gb` profile also listed
for this model). New optional `context_by_profile` field on the model registry
(`models/registry.py:ModelInfo`), read via a new `effective_context(profile_name)` method, falls
back to `context` for any profile without an override. `mac_air_m5_24gb: 8192` is now declared for
devstral (live-verified: ~15GB total vs. the profile's 18GB `large_model_ceiling_gb`, ~3x headroom
over the real observed prompt need of ~2800 tokens). `ModelPlane` gained a public `.profile_name`
attribute (previously only exposed the profile's data dict, not its name) so callers can resolve
this. Both `workflows/bugfix.py` and `workflows/refactor.py`'s patch-generation calls now pass
`options={"num_ctx": coder_model.effective_context(plane.profile_name)}`. 464/464 tests pass (458
+ 6 new: 3 registry tests, 1 real-config regression test, 2 `ModelPlane.profile_name` tests).

## A separate, real, still-open observation

While this final attempt was running, a genuinely concurrent process (`local-llm-lab`'s
`hekton_llm.judge_calibration`, a different active Claude Code session, confirmed via `ps aux`
showing a different shell-snapshot ID) hit the same shared Ollama instance, briefly loading
`qwen2.5:14b-instruct` mid-run. This did not cause any instability this time (the run still
completed cleanly, just slower: ~24 minutes vs. ~2-4 minutes in earlier isolated tests, plausibly
due to real GPU contention) — but it's genuine, current evidence that multiple sessions do
concurrently share this machine's one Ollama instance, which was the user's original hypothesis
for attempt 3's incident. It wasn't the cause of that specific incident (the config/context-size
issue above was, fully confirmed), but it's a real, separate, still-open concern worth its own
attention — logged as a backlog item, not built now, per the user's own framing that this "likely
belongs in local LLM control plane [`local-llm-lab`] to be shared functionality" and needs its own
dedicated planning session rather than an ad-hoc fix here.

## Updated overall verdict for the student-gremlin line of work

Across 4 attempts: **go**, once correctly configured. `devstral-small-2:24b`, via
`local-agentic-coding-lab`'s existing bounded pipeline, can complete Module 04 cold. This joins
the Codex CLI spike (`runs/2026-07-07-module-04-codex-spike/`, also go, faster and with a more
minimal diff) as a second, independent positive data point for Module 04 — still not evidence for
Module 03, which remains untouched by any of this work.
