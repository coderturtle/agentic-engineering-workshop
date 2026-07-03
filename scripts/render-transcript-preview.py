#!/usr/bin/env python3
"""render-transcript-preview.py: condense a real loop transcript into a
readable preview for prospective learners.

Read-only filter, not a content generator: every fact in the output is
extracted from the real transcript at RUNS/2026-07-03-module-04-dry-run/
attempt-good/transcript.txt, not invented. It exists because raw unittest
output (five verbose test lines, a traceback, a dashed separator ritual)
is real evidence but bad marketing copy; this script keeps the evidence and
drops the ritual. The narrative lines in each step (root-cause, fix) are
already human-written prose in the transcript and pass through unchanged.

Rerun it whenever the source transcript changes, so the published preview
never drifts from what actually happened:

    python3 scripts/render-transcript-preview.py

See docs/sample-attempt-preview.md for the output and docs/decisions.md for
why this exists instead of a hand-written "sample module."
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPT = ROOT / "runs/2026-07-03-module-04-dry-run/attempt-good/transcript.txt"
OUTPUT = ROOT / "docs/sample-attempt-preview.md"

STEP_RE = re.compile(r"^--- Attempt (\d+): (.+) ---$")
TEST_LINE_RE = re.compile(r"^(test_\S+) \(.*\) \.\.\. (ok|FAIL|ERROR)$")
# Deliberately requires a space after the leading "===" and before the
# trailing "===", so unittest's own bare "======...======" divider (no
# spaces at all) doesn't get mistaken for one of this script's own banners.
# An earlier version of this script used `^===.*===$`, which does match the
# bare divider, and silently truncated the "reproduce" step's failure detail
# as a result. Left as a comment instead of a footnote because it is the
# exact class of bug this workshop's fourth module is about.
BANNER_RE = re.compile(r"^=== .+ ===$")
GREP_LINE_RE = re.compile(r"^\d+:")


def parse(text: str):
    lines = text.splitlines()
    header, footer = [], []
    steps: list[tuple[str, list[str]]] = []
    current_label, current_lines = None, []

    for line in lines:
        m = STEP_RE.match(line)
        if m:
            if current_label is not None:
                steps.append((current_label, current_lines))
            current_label, current_lines = m.group(2), []
            continue
        if current_label is None:
            header.append(line)
        elif BANNER_RE.match(line.strip()):
            steps.append((current_label, current_lines))
            current_label, current_lines = None, []
            footer.append(line)
        else:
            current_lines.append(line)
    if current_label is not None:
        steps.append((current_label, current_lines))
    return header, steps, footer


def failure_detail(block: list[str], test_name: str) -> str | None:
    for i, line in enumerate(block):
        if line.startswith(f"FAIL: {test_name}") or line.startswith(f"ERROR: {test_name}"):
            last_nonblank = None
            for follow in block[i:]:
                if follow.strip() == "":
                    if last_nonblank is not None:
                        return last_nonblank.strip()
                    continue
                last_nonblank = follow
            return last_nonblank.strip() if last_nonblank else None
    return None


def render_test_block(block: list[str]) -> list[str]:
    results = [m.groups() for m in (TEST_LINE_RE.match(l) for l in block) if m]
    if not results:
        return []

    passed = sum(1 for _, status in results if status == "ok")
    failed = [(name, status) for name, status in results if status != "ok"]
    out = [f"Ran {len(results)} tests: **{passed} passed" + (f", {len(failed)} failed**" if failed else "**")]
    out.append("")
    for name, status in failed:
        detail = failure_detail(block, name)
        out.append(f"- `{status}` `{name}`")
        if detail:
            out.append(f"  `{detail}`")
    return out


def render_narrative(lines: list[str]) -> list[str]:
    """Render leftover step lines as alternating prose paragraphs and code
    fragments (grep -n style ``N:    code`` lines), instead of one flat blob.
    The source lines are hard-wrapped at the width of the echo statements
    that produced them; consecutive prose lines get joined into one flowing
    paragraph so that wrap doesn't survive into the rendered markdown.
    """
    out: list[str] = []
    prose_buf: list[str] = []

    def flush_prose():
        if prose_buf:
            out.append(" ".join(prose_buf))
            out.append("")
            prose_buf.clear()

    for line in lines:
        if line.strip() == "":
            continue
        if GREP_LINE_RE.match(line.strip()):
            flush_prose()
            out.append(f"```\n{line.strip()}\n```")
            out.append("")
        else:
            prose_buf.append(line.strip())
    flush_prose()
    return out


def render(header, steps, footer) -> str:
    out = ["# What a Real Attempt Looks Like", ""]
    out.append(
        "This is real output, condensed, not a mockup. A learner ran Module "
        "04's core exercise (`modules/04-loop-engineering/README.md`) against "
        "the shared `receipts` fixture, and this is what the loop actually "
        "printed. The full, uncondensed transcript is at "
        "`runs/2026-07-03-module-04-dry-run/attempt-good/transcript.txt`; "
        "this page exists because that file is real but not exactly light "
        "reading."
    )
    out.append("")

    if header:
        loop_line = next((l for l in header if l.strip()), "").strip("= ").strip()
        terms_line = next((l for l in header if l.startswith("Terminal states")), "")
        out.append(f"**Running:** {loop_line}")
        out.append("")
        if terms_line:
            out.append(f"*{terms_line}, stated before the loop ran.*")
            out.append("")

    for label, block in steps:
        out.append(f"### {label.capitalize()}")
        out.append("")
        test_lines = render_test_block(block)
        if test_lines:
            out.extend(test_lines)
            out.append("")
        narrative_source = [
            l for l in block if not TEST_LINE_RE.match(l) and not l.startswith("=")
            and l.strip() not in ("", "----------------------------------------------------------------------")
            and not l.startswith("Traceback") and not l.strip().startswith("File ")
            and not l.strip().startswith("self.") and not l.strip().startswith("~")
            and "Error:" not in l and not l.startswith("FAIL:") and not l.startswith("ERROR:")
            and not l.startswith("Ran ") and l.strip() not in ("OK",)
            and not re.match(r"^FAILED \(", l)
        ]
        narrative = render_narrative(narrative_source)
        if narrative:
            out.extend(narrative)
            out.append("")

    if footer:
        state_line = next((l for l in footer if l.strip()), "").strip("= ").strip()
        out.append(f"**{state_line}**")
        out.append("")

    out.append(
        "This attempt met the rubric. A second, deliberately weak attempt at "
        "the same ticket also made its terminal state fire green, by editing "
        "the test instead of the bug; Coachgremlin caught it anyway. Full "
        "story: `runs/2026-07-03-module-04-dry-run/grading.md`."
    )
    out.append("")
    out.append(
        "If this is the kind of thing you want to be doing to your own bugs, "
        "start with [`modules/README.md`](../modules/README.md)."
    )
    out.append("")
    out.append(
        "> Generated by `scripts/render-transcript-preview.py` from a real "
        "transcript. Rerun the script if the source transcript changes; "
        "don't hand-edit this file."
    )
    text = "\n".join(out) + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def main() -> None:
    text = TRANSCRIPT.read_text()
    header, steps, footer = parse(text)
    OUTPUT.write_text(render(header, steps, footer))
    print(f"Wrote {OUTPUT.relative_to(ROOT)} from {TRANSCRIPT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
