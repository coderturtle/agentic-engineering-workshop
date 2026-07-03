# Persona: Developer Evangelist — Module 01 — 2026-07-03

Reviewed `modules/01-prompt-engineering/README.md`, `modules/README.md`, and the top-level `README.md`. Findings below (Developer Evangelist lens only — hook and friction, not technical correctness).

The exercise — the actual thing I'd type — doesn't appear until line 21, five sections deep. Before it: a "question this module answers" line, an "arc" positioning paragraph, an abstract learning-objectives list, and a section called "Exercise material this module draws from" that opens with "No external named pattern" and then narrates internal curriculum politics: *"flagged by the Workshop Review Panel's Instructional Designer; see `docs/review-panel/2026-07-03-initial-design.md`"*. That's a citation to a design doc I've never heard of, in the middle of what should be my on-ramp. It reads like I've opened someone's internal review notes by mistake, not an invitation to write a prompt. This is the single biggest source of friction between "opened this page" and "started typing."

Once you reach it, the exercise blockquote itself is fine — concrete signature, real fixture path, a clear three-run bar. But there's zero copy-pasteable content anywhere on the page: no `cat` command to pull up the spec, no snippet to seed a first attempt. Compare the top-level README, which at least shows a bash block for cloning. Here, I have to go find `SPEC.md` myself before I can even see what I'm prompting against.

The payoff is buried and abstract. The takeaway section (line 41) promises "a reusable prompt template... saved somewhere you'll actually use it again" — vague — and only in passing mentions the actual proof-of-concept artifact, `.claude/commands/spec-impl.md`, that was "built and validated 3-for-3." That's the most concrete, credible hook on the page (a real, working slash command exists!) and it's a footnote instead of the lead.

Tone throughout leans on workshop-internal vocabulary — "the osmosis problem," "learning objective 2 firing," "the discriminator against osmosis" — that reads like it's talking to the curriculum designer, not the learner.

Would I share this page as-is? No — I'd share just the exercise blockquote. The page needs the meta-commentary cut or deferred, and the exercise pulled toward the top.
