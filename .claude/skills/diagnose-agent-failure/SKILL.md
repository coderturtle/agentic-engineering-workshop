---
name: diagnose-agent-failure
description: Diagnose why an agentic setup (prompt, context, harness, or loop) isn't reaching its goal, when the surface symptom (a fix that keeps failing review, a loop that never reaches done) could plausibly be caused by any of the four. Use when a setup that looks reasonable at a glance still doesn't work, before reaching for the most obvious-looking fix.
---

# Diagnose an agent failure

The Module 05 takeaway: the capstone's own method, compressed into one repeatable checklist. Built by generalizing the isolating-test method used on two real sabotaged setups (`runs/2026-07-03-module-05-dry-run/`), one where the obvious-looking culprit (a sloppy prompt, a noisy context bundle) was a red herring both times, and the real fault was somewhere less visible.

## The method, in order

1. **Name the surface symptom precisely**, not "it's broken." "The loop never reaches done," "the fix keeps failing review," "the output is subtly wrong": the exact shape of the symptom is your only clue before you start.
2. **List all four layers as suspects, explicitly, before you look closer at any one.** Prompt (was the instruction precise enough), context (did the model see what it needed), harness (could the agent reach what it needed to change), loop (does the verification step actually tell the truth about the result). Naming all four up front is what stops you from anchoring on whichever one looks worst on first read.
3. **Don't trust which one looks obvious.** A sloppy-looking prompt or a noisy context bundle is a plausible-sounding story, not evidence. The layer that's actually broken is often the one nobody's looking at because it looks fine.
4. **Isolate: fix one candidate layer, in a throwaway, and see whether the failure moves.** This is the only step that produces real evidence. Change exactly one variable, keep everything else identical, rerun. If the failure clears, that layer was load-bearing. If it doesn't, it wasn't, however guilty it looked.
5. **Rule out the other three explicitly, with what the isolating test showed.** Not "I fixed it so it must have been that": state why each of the other three couldn't have been the cause, citing the specific evidence (the identical prompt succeeded once the harness scope changed; the identical loop failed on objectively passing code).
6. **Apply the minimal fix to the diagnosed layer only.** Resist shotgun-correcting the other three "while you're in there." A minimal, localized fix is also weaker evidence to fake: it's much harder to accidentally look right for the wrong reason than a broad rewrite is.
7. **Before calling it done, check the fix didn't trade one failure for a new one.** "The original symptom is gone" is not the same claim as "nothing is worse now." Widening a harness's scope can widen it too far; fixing a verification check that was too strict can make it too lenient. Rerun the full check suite, not just the one symptom you were chasing, and look at what the fix actually grants or accepts, not just whether the terminal state flipped to success.
8. **If the evidence doesn't cleanly clear one layer, say so, don't force a verdict.** Real systems don't always cooperate with a single-cause story: two layers can both look partially load-bearing, or an isolating test can come back inconclusive. Report what you actually found ("evidence points at harness, but I couldn't rule out context with confidence") rather than pick the more confident-sounding layer to close the loop. An honest "not sure yet, here's what I'd check next" is a better diagnosis than a fabricated clean one.
9. **Write the attribution to the layer's actual job**, not just which file changed. A loop's job is to tell the truth about a result; a harness's job is to grant reach to what needs changing; a prompt's job is to specify precisely; a context's job is to supply exactly what's needed. Naming which job failed is what makes the diagnosis transferable to the next, differently-shaped failure.

## Symptom → suspect → confirm → fix, quick reference

| Symptom | Suspect layer | How to confirm | How to fix |
|---|---|---|---|
| Output is plausible but wrong, inconsistently across runs | Prompt | Rerun the identical prompt fresh 2-3 times; if it's flaky, it's underspecified, not unlucky | Name the edge cases explicitly; add output-shape constraints |
| Right idea, wrong specifics (wrong file, wrong function signature, stale info used) | Context | Check whether the specific fact the output got wrong was actually present, verbatim, in what the model saw | Include the load-bearing material verbatim; cut or summarize the rest |
| Agent can't make the change it clearly diagnosed correctly | Harness | Check the stated tool/file scope against what the fix requires | Widen scope to exactly what's needed, no further |
| Terminal state never fires, or fires on a wrong result | Loop | Isolate: apply a known-correct fix by hand, rerun the verification step unchanged, see if it still reports failure | Fix the verification step's actual check, not the code it's checking |

## When to reach for this

Any setup with more than one moving part that isn't reaching its goal and where the cause isn't already obvious from a single error message. Overkill for a one-line typo; exactly the right tool once "which of these several things is actually broken" is itself the question.
