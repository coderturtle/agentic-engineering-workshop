# Brand / Style Layer: Terminal Velocity

> The only place this workshop's personality lives. `README.md`, `site/`'s `BaseLayout`, and `astro.config.mjs` all read from this file — they don't redefine voice, banned language, or visual identity independently. Adapted from blog-factory-lab's `templates/brand-style-layer-template.md` and `examples/hekton-blog/brand-style-layer.md`.

## Site identity

**Name:** Terminal Velocity
**Tagline:** Learn agentic engineering by running it in a harness, not reading about it.
**Parent brand:** Hekton
**Slug:** `terminal-velocity`

The tagline leads with the doing-not-reading thesis rather than listing the four module names — per the Workshop Review Panel's Developer Evangelist finding (`docs/review-panel/2026-07-03-initial-design.md`), a tagline that's a list of jargon terms doesn't land in ten seconds.

## Tone and voice

**Core voice:** A competent peer, not an instructor. Specific, dryly funny, anti-hype by default. Treats the reader as someone who already ships agentic code daily — because they do.

**Tone rules:**
- Prefer plain verbs and concrete nouns; show the mechanism, don't just assert the result.
- Any claim about what a method achieves ("teaches better," "produces X outcome") must be marked as a hypothesis unless there's actual evidence behind it — this workshop's own design docs got caught overclaiming by its own review panel; the fix is a permanent voice rule, not a one-time edit.
- First person for build-log entries. System/instructional language for module content and workshop structure.
- Admit uncertainty directly rather than smoothing over it — an "open question" section is a feature, not a weakness, for this audience.
- Let a build-log entry have real tension (a constraint, a wrong turn, a fix) rather than a highlight reel.
- Never imply a technique is magic; name the mechanism.

## Hard rules

- **No em dash characters.** Use period, colon, semicolon, comma, parenthesis, or a plain hyphen instead. (Applies to all published workshop content — README, site, module READMEs, build-log entries. Design/planning docs in `docs/` are working documents, not published content, and are exempt.)
- No AI-slop openers ("In today's fast-paced world...", "It's important to note...").
- No unqualified efficacy superlatives ("game-changing," "revolutionary," "10x," "unlock your potential") — this is the direct fix for the Skeptical Practitioner/Critic's "prove it or cut it" findings against the design docs. If a claim can't be qualified with evidence or explicitly marked as a hypothesis, cut it.
- No engagement bait, fake scarcity, or "one weird trick" framing — this is a workshop for practitioners who already do this daily, not a funnel.

## Banned phrases

Reused from the wider Hekton house style (`blog-factory-lab/examples/hekton-blog/brand-style-layer.md`), plus workshop-specific additions:

- delve, tapestry, unlock, seamless, game-changing, revolutionize, transform your workflow, supercharge, effortlessly, cutting-edge, thought leader
- "in today's fast-paced world," "it's important to note," "at scale" (unless the content proves the scale)
- Workshop-specific: "master the art of," "in this comprehensive guide," "unlock your potential," "10x your skills" — standard online-course marketing language this workshop should never sound like, since the whole pitch is that the harness is the classroom, not a marketing page.

## Visual identity

Inherit the Astro starter's neutral tokens rather than invent a new palette: `--accent`, `ink`/`paper` Tailwind tokens, the `.post-body` typography rhythm, and the "no section dividers, whitespace only" layout rule (see `docs/implementation-plan.md` §4a).

| Element | Direction |
|---|---|
| Overall mood | Clean technical workshop notebook. Not a marketing landing page. |
| Colour approach | Dark-on-light default; restrained palette; dark mode optional later |
| Typography | Crisp, generous whitespace, readable code blocks |
| Imagery | Artifact-led: diffs, terminal output, architecture sketches — not stock photos or decorative AI art |
| Decoration | No neon AI aesthetic, no hero banners, no gradient-mesh backgrounds |

## Gremlin and factory language rules

- Coachgremlin and the Workshop Gremlin are real, documented agents with concrete responsibilities (`~/hekton/gremlins/`) — reference them plainly when explaining how the workshop works, don't decorate every heading with gremlin language.
- A module README is a production artifact: plain. A build-log entry can be funny where the actual events were funny.

## Anti-goals

- Not an AI-hype funnel or a marketing page for Hekton.
- Not a certification mill — no claim that completing this workshop credentials anything (matches the workshop design's "leaning self-assessed, no facilitator, no external credential" decision).
- Not a place to publish unverified efficacy claims — every claim about what the teaching method achieves gets the hypothesis treatment above until there's real evidence.
- Not overrun with gremlin language to the point of reading childish.
- Not a substitute for the repo's own docs, decisions, or design rationale — the site is a build-in-public journal, not the source of truth (`docs/` is).

## Application map

Artifacts that read from this file rather than redefining voice/identity independently:

| Artifact | Reads |
|---|---|
| `README.md` | Title + tagline |
| `site/` `BaseLayout.astro` | Header wordmark + footer |
| `astro.config.mjs` | `site` title |
| Site homepage copy | Tone, hard rules, banned phrases |
| Build-log entries | Tone and voice rules (first person, tension, no hype) |

## Title patterns (build-log entries)

- `What Broke When [Module] Met [Constraint]`
- `[Feature] or It Didn't Happen`
- `Field Notes: Building the Harness-Engineering Module`
- `The Boring Fix Behind [Interesting Result]`

## [TBD]: items for later

- [ ] Exact accent colour token
- [ ] Favicon / wordmark treatment
- [ ] Dark mode colour tokens
- [ ] Whether module pages get a distinct visual treatment from build-log entries
