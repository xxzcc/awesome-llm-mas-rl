#!/usr/bin/env python3
"""Generate the visible paper list in README.md from papers/papers.csv."""

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers" / "papers.csv"
README = ROOT / "README.md"

START = "<!-- BEGIN GENERATED PAPER LIST -->"
END = "<!-- END GENERATED PAPER LIST -->"

CATEGORY_ORDER = [
    "rl_method",
    "framework",
    "benchmark",
    "survey",
    "industry",
    "classical_marl",
]

CATEGORY_LABELS = {
    "rl_method": "RL and Post-Training Methods",
    "framework": "Frameworks and Systems",
    "benchmark": "Benchmarks and Evaluation",
    "survey": "Surveys and Overviews",
    "industry": "Industrial Systems and Reports",
    "classical_marl": "Classical MARL Foundations",
}


def load_papers():
    with PAPERS.open(newline="") as f:
        return list(csv.DictReader(f))


def display_author(name):
    name = name.strip()
    if "," not in name:
        return name
    last, first = [part.strip() for part in name.split(",", 1)]
    return f"{first} {last}".strip()


def link_label(row, index, url):
    if index > 1:
        return f"Link {index}"

    venue = row["venue"].lower()
    title = row["title"].lower()
    notes = row["notes"].lower()
    url_lower = url.lower()

    if any(
        host in url_lower
        for host in [
            "arxiv.org",
            "openreview.net",
            "aclanthology.org",
            "doi.org",
            "proceedings.neurips.cc",
        ]
    ) or url_lower.endswith(".pdf"):
        return "Paper"

    if "documentation" in venue or "docs" in title or "docs." in url_lower:
        return "Docs"
    if "blog" in venue or "/blog/" in url_lower:
        return "Blog"
    if "project page" in notes:
        return "Project"
    return "Paper"


def format_links(row):
    urls = [part.strip() for part in row["url"].split(";") if part.strip()]
    if not urls:
        return ""
    links = [
        f"[[{link_label(row, index, url)}]]({url})"
        for index, url in enumerate(urls, start=1)
    ]
    return " ".join(links)


def format_tags(row):
    tags = []

    if row["is_rl"] == "yes":
        tags.append("RL")
    elif row["is_rl"] == "partial":
        tags.append("partial RL")

    for field, label in [
        ("reward_type", "reward"),
        ("credit_granularity", "credit"),
        ("orchestration_form", "orchestration"),
    ]:
        value = row[field]
        if value != "NA":
            tags.append(f"{label}: {value}")

    if row["scenario"] not in {"general", "NA"}:
        tags.append(f"scenario: {row['scenario']}")

    tags.append(row["is_core"])

    if row["verified"] != "yes":
        tags.append(f"verified: {row['verified']}")

    return " ".join(f"`{tag}`" for tag in tags)


def render_entry(index, row):
    tags = format_tags(row)
    title_line = f"{index}. **{row['title']}** ({row['year']})"
    if tags:
        title_line += f" {tags}"

    details = f"   *First author: {display_author(row['first_author'])}; venue: {row['venue']}.*"
    links = format_links(row)
    summary = row["one_liner"].rstrip(".")
    if links:
        details += f" {links}"
    details += f" -- {summary}."

    return f"{title_line}\n\n{details}"


def render_paper_list(rows):
    rows_by_category = defaultdict(list)
    for row in rows:
        rows_by_category[row["category"]].append(row)

    lines = [
        "This section is generated from `papers/papers.csv` by "
        "`python scripts/generate_readme_papers.py`. Edit the CSV, not this block.",
        "",
        f"Retained corpus: **{len(rows)} entries**.",
    ]

    for category in CATEGORY_ORDER:
        category_rows = rows_by_category.get(category, [])
        if not category_rows:
            continue

        label = CATEGORY_LABELS[category]
        lines.extend(["", f"### {label} ({len(category_rows)})", ""])
        entries = [
            render_entry(index, row)
            for index, row in enumerate(category_rows, start=1)
        ]
        lines.append("\n\n".join(entries))

    return "\n".join(lines).rstrip() + "\n"


def replace_block(readme_text, generated):
    if START not in readme_text or END not in readme_text:
        raise ValueError(f"README.md must contain {START!r} and {END!r} markers")

    before, rest = readme_text.split(START, 1)
    _, after = rest.split(END, 1)
    return f"{before}{START}\n{generated}{END}{after}"


def main():
    parser = argparse.ArgumentParser(
        description="Update README.md's generated paper list from papers/papers.csv."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if README.md is not up to date.",
    )
    args = parser.parse_args()

    rows = load_papers()
    generated = render_paper_list(rows)
    current = README.read_text()
    updated = replace_block(current, generated)

    if args.check:
        if current != updated:
            print("README.md is not up to date; run python scripts/generate_readme_papers.py")
            return 1
        print("README.md is up to date")
        return 0

    README.write_text(updated)
    print(f"Updated README.md with {len(rows)} retained entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
