# Persona: Security-Conscious Reviewer — Module 01 — 2026-07-03

Read both target files (`modules/01-prompt-engineering/README.md` and `.claude/commands/spec-impl.md`). Findings below, in the Security-Conscious Reviewer lens only (narrow: does this content teach or imply a bad habit).

Mostly clean. The template scopes file access narrowly (`{file_path}` + "do not modify any other file, including the test file"), and requires the agent to run a verification command and confirm the pass condition *before* reporting done — both good habits, not bad ones, and worth calling out as a positive model since a weaker template could easily have skipped either.

One real gap: the module's own rationale (in "Why each slot is there," citing `runs/2026-07-03-module-04-dry-run/grading.md`) explicitly acknowledges that a fix can "still make everything green" while missing the point — i.e., tests passing isn't proof of correctness. But the exercise's actual success criteria (Rubric item 1, "Required to advance," the Stop Condition) define done purely as automated: tests pass, three-for-three, no touched test file. Nowhere does the exercise or rubric ask the learner to actually read the generated diff before accepting a run as a pass. So the module states the "green isn't proof" lesson in prose but doesn't carry it into the workflow it's teaching — a learner walks away with a template that self-certifies via its own verification command and reports done, with no habit of a human glance at the output before treating it as final. Worth a line in the rubric or takeaway: skim the diff, not just the test result, before counting a run as a pass.

No findings on tool/file-access scope beyond that — the template itself is appropriately narrow.
