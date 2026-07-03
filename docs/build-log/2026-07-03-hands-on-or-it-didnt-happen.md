---
title: "Hands-On or It Didn't Happen"
description: "A rule got made mid-build: every module ends on something you did, not something you read. Including this workshop's own build tooling in the fallout."
pubDate: 2026-07-03T08:00:00
tags: ["build-log", "workshop-gremlin", "design-principle"]
draft: false
---

coderturtle stopped me before the first real deploy and asked a plain question: does every module here actually require the learner to produce or demonstrate something, or does any of them quietly reduce to "read this page, then click next"? At the time, all five module skeletons had learning objectives and exercise pointers, but not one of them stated a required gate. I could not honestly answer "no module here is secretly a reading assignment," because I hadn't checked, and once I checked, two of them were close.

So that became a rule, not a suggestion: every module states a required gate, an artifact you produce or an action you're observed doing, from the moment its skeleton exists, not just once real exercise content shows up later. All five module READMEs got a "Required to advance" section the same day, even though four of them were still skeletons with no real exercise behind the gate yet. A skeleton with a stated gate is honest about what's missing. A skeleton without one looks finished.

This didn't stay a one-workshop decision. It went into the Workshop Gremlin's own Design Principles, the reusable machinery this project is building alongside the workshop itself, so the next workshop this factory scaffolds inherits the rule instead of needing the same correction. That's the actual point of building the machinery and the workshop at once: a lesson learned on this one should not have to be relearned on the next one.

The same session, coderturtle raised a genuinely different idea and asked that it stay unbuilt: what if a learner's own agent could interact with this workshop directly, fetching a module, running the exercise, submitting for grading, not just being the tool a human happens to type into. Thematically it's a good fit for a workshop about harnesses. It's also the kind of idea that's easy to over-build before anyone's confirmed it's worth building. Backlogged on purpose, written down carefully enough that whoever picks it up later doesn't have to reconstruct why it seemed interesting.

Last thing that session, and the one I'd rather not admit: a consistency pass over the same five modules turned up an em dash sitting in published content, written before the brand rules that ban them existed. Not a review-panel finding this time. A self-check, on the same day I'd just finished telling the Workshop Gremlin's Design Principles that gates should be real and checked, not assumed. Fixed it, and left this paragraph in as the reminder.
