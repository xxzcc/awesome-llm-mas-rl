#!/usr/bin/env python3
"""Generate reproducible paper-pool statistics for the survey artifact."""

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers" / "papers.csv"
EXCLUDED = ROOT / "papers" / "excluded.csv"


def load_csv(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def print_counter(title, values):
    counts = Counter(values)
    print(f"\n## {title}")
    for key, value in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"- {key}: {value}")


def cross_tab(rows, left, right):
    left_values = sorted({r[left] for r in rows})
    right_values = sorted({r[right] for r in rows})
    table = defaultdict(Counter)
    for row in rows:
        table[row[left]][row[right]] += 1
    print(f"\n## Cross-tab: {left} x {right}")
    print("| " + left + " | " + " | ".join(right_values) + " |")
    print("|" + "---|" * (len(right_values) + 1))
    for lv in left_values:
        cells = [str(table[lv][rv]) for rv in right_values]
        print("| " + lv + " | " + " | ".join(cells) + " |")


def main():
    papers = load_csv(PAPERS)
    excluded = load_csv(EXCLUDED)

    print("# LLM-MAS RL Survey Artifact Statistics")
    print(f"\nRetained entries: {len(papers)}")
    print(f"Excluded decisions: {len(excluded)}")
    print(f"Audited records: {len(papers) + len(excluded)}")

    for field in [
        "category",
        "is_rl",
        "reward_type",
        "credit_granularity",
        "orchestration_form",
        "scenario",
        "is_core",
        "verified",
    ]:
        print_counter(field, [r[field] for r in papers])

    cross_tab(papers, "reward_type", "credit_granularity")
    cross_tab(papers, "orchestration_form", "credit_granularity")
    cross_tab(papers, "category", "verified")

    print_counter("excluded_stage", [r["stage"] for r in excluded])
    print_counter("excluded_source", [r["source"] for r in excluded])
    print_counter("excluded_query_family", [r["query_family"] for r in excluded])


if __name__ == "__main__":
    main()
