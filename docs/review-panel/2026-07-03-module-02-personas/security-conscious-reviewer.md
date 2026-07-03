# Persona: Security-Conscious Reviewer — Module 02 — 2026-07-03

Scope check, not a full audit. Read `modules/02-context-engineering/README.md` and `.claude/skills/context-budgeting/SKILL.md`.

**Finding.** The Skill's core heuristic — "cut anything the check doesn't touch" (step 3), reinforced by "default to cut, not summarize, for anything not in the verification path" — has no carve-out for security-relevant code. It defines "load-bearing" purely as "read by the verification step." In the exercise's fixture that's fine, since nothing security-sensitive is in scope. But as a portable, reusable checklist (which is the explicit point of the takeaway — "loadable in future sessions"), this teaches a habit that doesn't generalize safely: auth checks, input validation, and permission logic are frequently *not* directly exercised by the specific test a task is scoped against, yet are exactly the code you don't want an agent silently dropping from context while it works nearby. A learner who internalizes "not in the verification path → cut it" and applies that reflex to a real codebase could curate away the very code that would have kept a change safe.

**Suggested fix.** One line added to the checklist (e.g., between steps 3 and 4): "Auth, validation, and permission-check code get kept even if the test in scope doesn't touch them directly — flag this as a deliberate exception, not silence." Cheap to add, and it's the one case where "the check didn't read it" is the wrong test for relevance.

No other concerns — the red herring (`tax_rates.yaml`) and other cuts in the exercise are not security-related, so nothing else in scope warrants a flag.
