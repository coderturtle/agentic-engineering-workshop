# Persona: End-User / Target Learner — Module 05 — 2026-07-03

**Biggest problem: the four provided files never explain how they connect into one runnable attempt.** `loop.sh` just runs `unittest discover` twice with nothing in between (`while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do ... "Still failing after attempt $attempt" ...`), no agent invocation, no fix applied between passes. As an advanced practitioner reading this cold, I don't know if I'm supposed to (a) manually act as the agent, respecting `harness-config.md`'s scope, edit files, then rerun `loop.sh` to check; or (b) point an actual Claude Code session at these four files somehow, with `harness-config.md` becoming a real subagent config. The README's "Each variant runs `./loop.sh` to `TERMINAL STATE: FAILURE`" reads like the script itself demonstrates the bug, but running it as shipped fails trivially and uninformatively regardless of diagnosis, it never attempts anything.

**"You get one; you don't know which" has no assignment mechanism.** Nothing says who picks, random draw, Coachgremlin, my own coin flip? As written I'd just open both `sabotaged-harness/` and `sabotaged-loop/` myself, which defeats the stated design intent.

**"Instrument it" and "isolate by fixing one layer in a throwaway" are pure abstraction, zero worked example.** No sample command, no "here's what a throwaway harness-config edit looks like." I can infer the intent (copy the config, loosen the scope, rerun, see if the failure moves) as an experienced practitioner, but that's me filling a gap the module should close, not something the module taught.

**The layer-to-file mapping is never stated explicitly**, `harness-config.md` = harness layer, `loop.sh` = loop layer, etc. is implicit from filenames, never confirmed in prose.

That said, the fixture design itself is genuinely good: `harness-config.md` scopes edits to `docs/` (a directory that doesn't even exist), which is a real, findable red herring once you know to look at scope.

**Verdict: No**, not as currently written. I'd stall at "how do I actually run an attempt," not at the diagnosis itself, which is the wrong place to lose an advanced learner.
