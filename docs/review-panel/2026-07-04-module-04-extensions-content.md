# Workshop Review Panel — Module 04 Extensions Content Review

**Date:** 2026-07-04
**Scope:** `modules/04-loop-engineering/README.md`'s "Extensions" section (three optional extensions authored this session), `scripts/blast-radius-check.sh`, `runs/2026-07-04-module-04-extension-{a,b,c}*` (verification records, hill-climbing analysis/proposal/review-gate).
**Run:** a scoped, full seven-persona run against newly authored content, not a design-level checkpoint. All seven personas reviewed independently and in parallel.

## Agreements (2+ personas, independently)

### 1. Extension C had no real learner action, despite the module claiming it was "hands-on" (Developer Evangelist, End-User/Learner, Instructional Designer)

Three personas independently converged on the same gap. Extensions A and B each ended with an explicit "Try it:" imperative giving the learner a real command to run; Extension C's paragraph was entirely past-tense, maintainer-authored narration ("an analysis... found," "Verified regression-free... before proposing it," "Not adopted") with no verb telling the learner what to do. The Instructional Designer went further: the learning-objectives section's claim that objective 4 is "hands-on in Extension C" was flatly false as written, since even the objective's own phrasing ("Explain... why") doesn't ask for a hill-climbing attempt, and the extension gave the learner nothing to submit, run, or produce.

**Status: fixed in this pass.** Extension C now ends with a concrete action: read `review-gate.md` and write your own review-gate verdict, in your own words, before looking at the actual outcome. The learning-objectives line was reworded to make that verdict, not the analysis itself, the hands-on artifact.

### 2. "Verified"/"regression-free" language overclaimed what a 2-diff sample proves (Skeptical Practitioner/Critic, AI/ML Practitioner)

Both personas independently flagged the same issue from different angles: the two diffs checked against Extensions A and C (`attempt-good`, `attempt-gaming`) are exactly the pair the blast-radius check was purpose-built to distinguish, not held-out validation. Calling this "regression-free against known history" or "verified" without that caveat reads as more complete than it is. The AI/ML Practitioner additionally noted the one available third case (`takeaway-validation`) was never actually run through the script, since no patch file exists for it.

**Status: fixed in this pass.** Reworded in `modules/04-loop-engineering/README.md`, `runs/2026-07-04-module-04-extension-a-verification.md`, `analysis.md`, and `review-gate.md` to state plainly that both diffs are the design examples, not held-out cases, and that this confirms the mechanism works as built, not that it's proven against the general case.

### 3. `blast-radius-check.sh` mishandles non-content-change diff entries (Security-Conscious Reviewer, AI/ML Practitioner)

The AI/ML Practitioner directly reproduced a real bug: a pure file deletion renders as `+++ /dev/null` in a unified diff, and the script was reporting `/dev/null` itself as the touched (and therefore always out-of-scope) file, rather than the file that was actually deleted. The Security-Conscious Reviewer independently flagged the sibling gap: a pure rename with no content change emits neither a `---` nor a `+++` line at all, so a renamed out-of-scope file could pass undetected. Both are real correctness gaps in a script about to be proposed for adoption into the canonical loop template.

**Status: fixed in this pass.** The script now resolves a deletion to the file named on the matching `---` line instead of `/dev/null`, and additionally parses git's `rename from`/`rename to` lines so pure renames are checked too. Reverified against both original diffs (unchanged PASS/FAIL outcomes) plus new deletion and allowed-deletion test cases.

## Single-persona findings

### 4. Extension B's "verified live" claim conflated the check running with the event actually firing (Skeptical Practitioner/Critic)

The original writeup ran `scripts/check-brand-lint.sh --check` by hand and called this "verified live," without separately confirming the pre-push hook itself (the actual event trigger) had ever fired. The persona also noted the hook is warn-only, so even a caught violation wouldn't have blocked anything.

**Status: fixed in this pass, and strengthened rather than just caveated.** `git push --dry-run` still triggers `pre-push` hooks without touching the remote; ran it for real and captured the hook firing both the mirror-drift and brand-lint checks automatically. The writeup and README now cite this as genuine evidence of the event path, distinct from the manual check, with the warn-only behavior stated explicitly.

### 5. Hill-climbing's attestation gate is a documented convention, not a structural block (Security-Conscious Reviewer)

`human_confirmed: false` in the run ledger and `review-gate.md` is real and currently accurate, but nothing in this repo's tooling (no hook, no CI check) would actually stop someone from running `git apply proposed-diff.patch` regardless of that field's value. The module's own text calling this "a gate, not a formality" slightly overstates the current enforcement.

**Status: fixed in this pass.** Added an explicit caveat to `review-gate.md`: the gate holds only as long as whoever applies changes actually checks it; nothing currently enforces this structurally.

### 6. "Blast radius" is a narrower usage than its standard meaning (AI/ML Practitioner)

In SRE/security usage, "blast radius" describes the scope of impact of a failure, not literally "which files a diff touches." The script is closer to a touched-files/scope-allowlist check. Not wrong, but an unflagged narrowing of a term of art in a workshop that otherwise cares about precise vocabulary.

**Status: fixed in this pass.** Added a one-clause acknowledgment in the README the first time the term is used.

### 7. Five em dashes in content outside the brand-lint tool's own scope (Professional Technical Writer)

`docs/brand.md`'s hard rule applies repo-wide in spirit, but `scripts/check-brand-lint.sh` only scans published content, not `runs/` or `scripts/`. Four em dashes were sitting in `runs/2026-07-04-module-04-extension-a-verification.md` and one in a user-facing CLI message inside `scripts/blast-radius-check.sh` itself, the latter notable since it's output every learner running the tool would actually see.

**Status: fixed in this pass.**

### 8. The proposed diff's own added provenance text asserted an approval that hadn't happened yet (Professional Technical Writer)

`proposed-diff.patch` added a sentence to `ticket-to-pr-ready.md`'s Provenance section stating "Human-reviewed and approved before landing here, not auto-applied" as present fact, while the surrounding documents (`review-gate.md`, the run ledger) correctly record `human_confirmed: false`. A learner reading just the patch would be misled about current state. A related, milder instance: "landing this requires the sign-off recorded in `review-gate.md`" implied a sign-off already existed there.

**Status: fixed in this pass.** Reworded both: the provenance note now describes the requirement ("ships only once reviewed and approved... which was pending as of this proposal") rather than asserting it as done, and the sign-off line now reads "the sign-off that `review-gate.md` asks for and does not yet have."

## Not acted on

- The Instructional Designer's broader observation that Extension B "exercises pre-existing repo content, not a learner artifact" is accurate and left as-is: Extension B is deliberately the lightest-weight of the three (wiring an existing mechanism to a trigger), and the fix for finding #4 above (actually triggering the hook) already strengthens its evidentiary weight without changing what it fundamentally asks of a learner.
- The AI/ML Practitioner's note that the suffix-match glob logic (`"$f" == */$glob`) is "untested against anything adversarial" is true but no concrete false-positive was produced against realistic paths (checked directly: `notreceipts/grouping.py` does not match `receipts/grouping.py` under this logic). Left as a known, not a wrong, property; not worth a defensive rewrite without a real failing case.

## What this run doesn't cover

Module 05's two new variants (prompt-bottleneck, context-bottleneck) were still being built and honestly reported as negative findings while this panel ran; they get their own review once that content lands in its final form.
