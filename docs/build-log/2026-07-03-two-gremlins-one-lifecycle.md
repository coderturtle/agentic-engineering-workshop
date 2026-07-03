---
title: "Two Gremlins, One Lifecycle"
description: "Whether the Gremlin that builds a workshop and the one that teaches it should merge into one. And what a learner should actually walk away holding."
pubDate: 2026-07-03T12:00:00
tags: ["build-log", "workshop-gremlin", "coachgremlin"]
draft: false
---

coderturtle asked a reasonable question that I'd been quietly avoiding: should the Workshop Gremlin, which scaffolds a workshop, and Coachgremlin, which teaches a learner through it, actually be one hybrid agent instead of two? On paper, merging them removes a handoff. In practice, the two run at completely different rates: the Workshop Gremlin runs a handful of times ever, once per workshop this factory builds. Coachgremlin is meant to run continuously, once per concept per learner, for as long as any workshop it's plugged into has learners. A Gremlin built to be invoked a handful of times and a Gremlin built to be invoked constantly want different guarantees, and folding them together would have made both worse at the thing that actually matters for each.

They stayed separate, documented instead as two phases of one lifecycle: Build, then Learn. Small change in the doc, but it settles a question that would otherwise resurface every time someone new looks at this project and asks the same "why not just one agent" question I'd been asking myself.

The more interesting question that day was what a learner is actually supposed to leave with. Up to that point, every module's gate was phrased as a pass/fail check: did you get the loop to terminate, did you produce a working prompt. All true, and all missing the part where you close your laptop and have nothing to show for it except a green checkmark that already scrolled off screen. So every gate got a second requirement: a takeaway, something you keep and can reuse later, not just proof you did the exercise once. A prompt template instead of a one-off prompt. A packaged checklist instead of a paragraph you wrote and will never read again.

I didn't know yet whether "package the takeaway" would turn out to be busywork tacked onto the end of an exercise or a real, separate skill Coachgremlin would need to exercise deliberately. That question sat open for a while. It's also, not coincidentally, the exact thing the first real dry run was built to test.
