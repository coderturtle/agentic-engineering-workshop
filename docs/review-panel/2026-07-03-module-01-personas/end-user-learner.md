# Persona: End-User / Target Learner — Module 01 — 2026-07-03

**1. The takeaway section spoils the exercise if you read top to bottom.** Reading order in the README is Exercise → Rubric → Required to advance → Takeaway → Stop condition. The Takeaway paragraph links straight to `.claude/commands/spec-impl.md`, a fill-in-the-blank template with a "why each slot is there" breakdown that explicitly states the winning move ("all four edge cases named explicitly, not implied," "run verification command... before reporting done"). I read the page in order like any normal learner would before opening a terminal, and by the time I reached "Exercise" I'd already have the answer's shape handed to me. There's no "don't open this until after your first attempt" gate — for an exercise whose entire discriminator is *discovering* this structure yourself, that's a real integrity hole, not a nitpick.

**2. "Fresh copy of the fixture" isn't explained anywhere.** The exercise requires three clean runs "each against a fresh copy of the fixture," but neither the module README, the variant's own README, nor SPEC.md says how — git checkout, `cp -r`, a reset script? I went looking in `fixtures/receipts/` for a reset tool and found none. I'd have to improvise.

**3. SPEC.md's own "Running it" section points at the wrong directory.** It says `cd fixtures/receipts`, but Module 01 works against `fixtures/receipts/variants/unimplemented/` (whose own README correctly says `cd .../variants/unimplemented`). Following the module's pointer into SPEC.md and then following SPEC.md's literal run instructions lands you in the base fixture, not the stub you're supposed to implement against — a genuine "which directory am I even in" stall.

**4. No stated submission/grading mechanism on the page itself.** "Required to advance" says the prompt+outputs are "checked against the rubric" but never says how or to whom — Coachgremlin is only named in the arc-level `modules/README.md`, not here.

**On the positive side:** the exercise itself is appropriately hard, doesn't talk down, and the "osmosis problem" framing in the Exercise-material section respects that I already write decent prompts daily — good.

**Verdict: No, not as written** — not because the exercise is bad, but because reading the page as designed spoils the thing it's testing, and getting to a first attempt requires guessing at fixture-reset mechanics the page never states.
