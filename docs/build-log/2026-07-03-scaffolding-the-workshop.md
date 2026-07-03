---
title: "What Broke When the Rename Met the Prose"
description: "Scaffolding a workshop and its own build tooling at the same time, and the bug a review panel found that a find-replace script couldn't."
pubDate: 2026-07-03
tags: ["build-log", "workshop-gremlin", "review-panel"]
draft: false
---

Today I started two things at once: a workshop about how prompt engineering, context engineering, harness engineering, and loop engineering fit together, and the reusable machinery for building workshops like it again later. Building both at the same time was the point. The machinery had to survive contact with a real workshop, not just look good on paper.

The arc changed shape almost immediately. I'd planned three modules: prompt, context, loop. Then I read three different accounts of what "loop engineering" actually means right now, and all three kept describing something that wasn't quite loop engineering. They were describing the harness: what tools an agent can reach, what state persists, how work gets organized before anything runs. That's a different question from "when does it stop and how does it get better," which is what a loop actually is. So the three-module arc became four, with harness engineering as its own thing. Small change on paper. It meant rewriting the synthesis capstone, the exercise-pattern list, and every place I'd already written "three modules."

Naming came next. Terminal Velocity won out over Loop Native, Bounded Autonomy, and just keeping the working title. The pun works twice: terminal as in the thing you type into, and terminal as in a loop's stop condition. Renaming a public repo mid-build is exactly as mechanical as it sounds: GitHub rename, local directory, git remote, every doc that said the old name.

Except it wasn't fully mechanical, and this is the part worth writing down. The rename script found and replaced every literal occurrence of the old project name. What it couldn't find was the prose sitting next to those names that said "the naming pass hasn't happened yet." That sentence never contained the old name as a string, so a find-replace had nothing to match. Four documents shipped with the real name in the title and a paragraph two lines down insisting the name was still pending. Nobody would have caught that by rereading, because rereading your own rename doesn't feel like a place a bug could hide.

A seven-person review panel caught it, run before any of this went further. Not a metaphor: seven independently prompted reviews, each one told to look at exactly one thing and ignore everything else. The technical reviewer and the developer-evangelist reviewer flagged the stale prose independently, from different angles, without seeing each other's notes first. That agreement is the actual signal. It also found a real design flaw I'd have shipped otherwise: I'd written that harness engineering is static and then, three lines later, described a loop that rewrites the harness at runtime. Both true. Neither reconciled. Fixed now, with an explicit line that a rewrite like that gets reviewed before it's adopted, not applied automatically.

Next: the module skeleton, a real brand file, and this site. All still ahead of any actual exercise content, which is the harder and more honest part still to come.
