#!/usr/bin/env python3
"""generate-bloated-variant.py: build Module 02's bloated fixture variant.

Takes the unimplemented variant (Module 01's task) and buries it under
noise: a long README, a CHANGELOG, an unrelated legacy module, stale docs,
and a red-herring config, per docs/coachgremlin-implementation-plan.md's
Module 02 spec. The noise is generated, not hand-written, so the line count
is reproducible and the generator can be re-run if the budget needs to move.
The real code (receipts/, tests/, SPEC.md) is copied through unchanged.

Usage: python3 scripts/generate-bloated-variant.py
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "fixtures/receipts/variants/unimplemented"
DST = ROOT / "fixtures/receipts/variants/bloated"

FEATURES = [
    "multi-currency normalization", "OCR receipt scanning", "SSO login",
    "role-based access control", "audit log export", "webhook notifications",
    "custom approval chains", "mobile capture", "offline sync",
    "bulk CSV import", "vendor deduplication", "spend forecasting",
    "policy violation flags", "per-department budgets", "PDF report export",
    "Slack integration", "email digest", "receipt tagging", "expense splitting",
    "mileage tracking", "per-diem calculation", "corporate card feed sync",
    "multi-entity consolidation", "custom fields", "API rate limiting",
    "dark mode", "keyboard shortcuts", "saved filters", "scheduled exports",
    "two-factor authentication", "IP allowlisting", "data retention policies",
    "GDPR export requests", "SOC 2 audit trail", "custom approval SLAs",
    "receipt image compression", "duplicate detection heuristics",
    "currency conversion caching", "timezone-aware reminders",
    "quarterly close checklists", "vendor scorecards", "spend anomaly alerts",
    "custom report builder", "org chart-based approvals", "delegate approvers",
    "receipt retention archival", "single sign-on via SAML",
    "custom branding for reports", "batch receipt merging", "line-item splitting",
]

CONTRIBUTORS = [
    f"contributor{n:03d}" for n in range(1, 121)
]

ROADMAP_ITEMS = [
    "Investigate GraphQL API layer", "Evaluate Rust rewrite of the parser",
    "Support Google Sheets export", "Add Zapier integration",
    "Explore on-device OCR", "Redesign onboarding flow",
    "Add per-team spend dashboards", "Support multi-language receipts",
    "Evaluate serverless deployment", "Add anomaly detection ML model",
    "Support cryptocurrency expense tracking", "Add voice-to-expense capture",
    "Explore blockchain audit trail", "Support ISO 20022 export",
    "Add carbon footprint estimation per expense",
]


def build_readme() -> str:
    lines = [
        "# Receipts: Enterprise Expense Intelligence Platform",
        "",
        "> This README predates the current CLI-focused direction and was never",
        "> trimmed down. Kept here as historical bloat for Module 02.",
        "",
        "## Overview",
        "",
    ]
    for i in range(1, 220):
        lines += [
            f"### Overview section {i}",
            "",
            (
                f"Paragraph {i} of general platform framing, repeated with minor "
                "variation across historical README revisions. Describes the "
                "product vision, market positioning, and competitive landscape "
                "in language that has not been updated to match the current "
                "small CLI tool this repository actually ships."
            ),
            "",
        ]
    lines += ["## Features", ""]
    for i, feat in enumerate(FEATURES, start=1):
        lines += [
            f"### {i}. {feat.capitalize()}",
            "",
            (
                f"Description of {feat}: a planned or historical feature not "
                "implemented by anything in this repository. Included here "
                "purely as README bloat."
            ),
            "",
        ]
    lines += ["## Installation", ""]
    for platform in ["macOS (Homebrew)", "macOS (manual)", "Ubuntu/Debian",
                      "Fedora/RHEL", "Windows (WSL)", "Windows (native)",
                      "Docker", "Docker Compose", "Kubernetes (Helm)", "Nix"]:
        lines += [
            f"### {platform}",
            "",
            f"Step-by-step instructions for installing on {platform}, none of "
            "which apply to the actual stdlib-only Python fixture in this "
            "directory.",
            "",
            "```bash",
            f"# placeholder install commands for {platform}",
            "echo 'not a real install path'",
            "```",
            "",
        ]
    lines += ["## FAQ", ""]
    for i in range(1, 150):
        lines += [
            f"**Q{i}: Frequently asked question number {i}?**",
            "",
            f"A{i}: Generic answer text padding out the FAQ section.",
            "",
        ]
    lines += ["## Roadmap", ""]
    for item in ROADMAP_ITEMS * 3:
        lines.append(f"- [ ] {item}")
    lines += ["", "## Contributors", ""]
    for c in CONTRIBUTORS:
        lines.append(f"- {c}")
    lines.append("")
    return "\n".join(lines)


def build_changelog() -> str:
    lines = ["# Changelog", ""]
    for major in range(16, 0, -1):
        for minor in range(20, 0, -1):
            lines += [f"## v{major}.{minor}.0 - 2024-{(minor % 12) + 1:02d}-{(major * minor) % 28 + 1:02d}", ""]
            for j in range(1, 6):
                lines.append(f"- {['Fixed', 'Added', 'Changed', 'Removed', 'Deprecated'][j % 5]} item {j} in this release, unrelated to the receipts CLI's current scope.")
            lines.append("")
    return "\n".join(lines)


def build_legacy_export() -> str:
    lines = [
        '"""legacy_export.py: unrelated legacy export pipeline, kept for',
        'historical reasons. Nothing in receipts/grouping.py imports this.',
        'A red herring by inclusion, not by content: it looks like it might',
        'matter to a nervous reader and does not."""',
        "",
        "from __future__ import annotations",
        "",
        "import xml.etree.ElementTree as ET",
        "",
        "",
    ]
    for i in range(1, 220):
        lines += [
            f"class LegacyFormatterV{i}:",
            f'    """Formats records for the discontinued export target #{i}."""',
            "",
            "    def __init__(self, options=None):",
            "        self.options = options or {}",
            "",
            "    def format(self, records):",
            f"        root = ET.Element('legacy_export_v{i}')",
            "        for record in records:",
            "            item = ET.SubElement(root, 'item')",
            "            for key, value in record.items():",
            "                child = ET.SubElement(item, key)",
            "                child.text = str(value)",
            "        return ET.tostring(root)",
            "",
            "",
        ]
    return "\n".join(lines)


def build_stale_doc(title: str, n_paragraphs: int) -> str:
    lines = [f"# {title}", "", "> Stale, predates the current CLI. Not maintained.", ""]
    for i in range(n_paragraphs):
        lines += [
            f"## Section {i + 1}",
            "",
            (
                f"Paragraph describing an architectural decision or API design "
                f"from an earlier version of this project, section {i + 1}. "
                "None of this reflects the current receipts/grouping.py "
                "implementation."
            ),
            "",
        ]
    return "\n".join(lines)


def build_tax_rates_yaml() -> str:
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID",
        "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
        "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
        "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV",
        "WI", "WY",
    ]
    lines = [
        "# tax_rates.yaml",
        "#",
        "# Red herring: per-state tax rate tables. Looks like it could matter",
        "# to expense totals; group_expenses_by_month never reads this file.",
        "",
        "tax_rates:",
    ]
    for i, state in enumerate(states):
        lines += [
            f"  {state}:",
            f"    sales_tax: {(i % 10) / 100 + 0.02:.3f}",
            f"    use_tax: {(i % 7) / 100 + 0.01:.3f}",
            f"    local_surcharge_min: {(i % 5) / 1000:.4f}",
            f"    local_surcharge_max: {(i % 5) / 500:.4f}",
            "    rounding: nearest_cent",
            f"    effective_date: 2024-0{(i % 9) + 1}-01",
        ]
    return "\n".join(lines)


def main() -> None:
    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC / "receipts", DST / "receipts")
    shutil.copytree(SRC / "tests", DST / "tests")
    shutil.copy(SRC / "SPEC.md", DST / "SPEC.md")
    for pycache in DST.rglob("__pycache__"):
        shutil.rmtree(pycache)

    (DST / "README.md").write_text(build_readme())
    (DST / "CHANGELOG.md").write_text(build_changelog())
    (DST / "legacy_export.py").write_text(build_legacy_export())

    docs_dir = DST / "docs"
    docs_dir.mkdir(exist_ok=True)
    (docs_dir / "architecture-2019.md").write_text(build_stale_doc("Architecture (2019)", 60))
    (docs_dir / "old-api-design.md").write_text(build_stale_doc("Old API Design Notes", 60))
    (docs_dir / "deprecated-features.md").write_text(build_stale_doc("Deprecated Features", 50))

    config_dir = DST / "config"
    config_dir.mkdir(exist_ok=True)
    (config_dir / "tax_rates.yaml").write_text(build_tax_rates_yaml())

    total_lines = 0
    for f in DST.rglob("*"):
        if f.is_file() and "__pycache__" not in str(f):
            total_lines += len(f.read_text(errors="ignore").splitlines())
    print(f"Wrote {DST.relative_to(ROOT)}, {total_lines} total lines.")


if __name__ == "__main__":
    main()
