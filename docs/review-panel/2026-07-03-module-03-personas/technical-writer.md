# Persona: Professional Technical Writer / Editor — Module 03 — 2026-07-03

Module 03 repeats the Module 01/02 pre-fix pattern; it was not carried forward.

**1. The exercise is buried again, worse than Module 02's original.** Reading order is: title → "The question this module answers" → "Where it sits in the arc" → "Learning objectives" → "Exercise material this module draws from" → finally "Exercise: bounded specialist, reset, resume" at line 24. That's five headers of front matter, the same defect the panel fixed twice already (Module 01 finding #1, Module 02 finding #1: "reads like the pre-fix version of Module 01"). Both prior modules' fix moved the Exercise to the *second* section, right after the one-line framing question. Module 03 reverts to the unfixed layout.

**2. An internal review-panel citation leaks into learner-facing prose.** The "Harness" section states: "Sub-agents, skills, worktrees, and MCP are Claude-Code-shaped vocabulary that doesn't map cleanly onto every tool (flagged by the Workshop Review Panel's End-User/Learner persona)." This is exactly the audit-trail-in-prose problem Module 01 finding #1 called out and the fix explicitly handled by "keeping the underlying reasoning, cutting the audit-trail citation." Here the citation survived; a learner has no reason to know or care which panel persona flagged what.

**3. "Required to advance" / "Takeaway" / "Stop condition" ordering reproduces Module 01's spoiler bug.** Section order is Exercise → Rubric → Required to advance → Takeaway → Stop condition — the identical sequence Module 01 finding #4 flagged, because Takeaway (here naming the reference implementation `.claude/agents/receipts-category-summary.md` and its dry-run) sits before Stop condition on a top-to-bottom read, and unlike Module 01's Takeaway, this one lacks the "don't open this before your first attempt" guard added in that fix.

**4. Required-to-advance and Stop condition are still separate and near-redundant** — both describe "harness config runs correctly, transcript shows reset-and-resume, demonstrated not asserted." Module 01 finding #10 named this exact redundancy and both prior modules merged the two into one section; Module 03 did not.

No em dashes, no banned phrases, sentence density and voice are otherwise clean — the recurring problem is structural placement, not prose quality, exactly as in the prior two reports.
