# Persona: Developer Evangelist — User Docs — 2026-07-03

**1. The two "front doors" duplicate instead of differentiating.** The site's guide page claims a distinct job — "Nothing here substitutes for cloning it; this is orientation, not the content" — but then reproduces README almost verbatim: the same four-layer thesis, an identical "How to start"/"runbook" step list, and a near word-for-word "See it in action" pitch. A visitor who hits the site first, then clicks through to GitHub, rereads the same pitch twice. The only genuinely unique content on the site is the "Recent from the build log" teaser at the bottom, everything else should either be cut from one of the two or clearly reframed (e.g., site = pitch + build-log hub, README = the actual how-to-start).

**2. "Coachgremlin" lands with zero setup.** README's second paragraph drops "Coachgremlin frames the task and gives you feedback" with no appositive, no link, nothing, a first-time reader can't tell if it's a bot, a persona, or a Claude Code skill. That's friction right in the ten-second window that's supposed to hook people.

**3. The `modules/README.md` arc gets buried under an internal QA memo.** The actual hook content, the five-row arc table, sits below a giant italicized blockquote reciting review-panel process detail. This reads like an internal changelog, not onboarding copy, and it's the first thing hit after `cat modules/README.md` from the README's own quickstart.

**4. Dead-end mention in README.** "Build in public... published as a dated journal on GitHub Pages" has no link at all, a genuinely interesting hook (watch the workshop get built) with no click-through.

**5. Sample-attempt-preview.md is the strongest asset in scope**, concrete, real, "not cherry-picked," and it's exactly the kind of proof that would make me share this. It deserves more prominence than a single bullet link in both entry points.
