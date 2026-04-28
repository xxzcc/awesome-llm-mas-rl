# Artifact Protocol

This repository is a taxonomy artifact for a survey, not a complete systematic-review database.

## Inclusion Rule

An entry is retained when it satisfies at least one condition:

- It trains or post-trains an LLM-based multi-agent system component.
- It documents an industrial system whose public interface constrains RL design.
- It provides a benchmark, safety case, critic/verifier method, or classical MARL primitive used by the survey taxonomy.

## Evidence Levels

The paper distinguishes evidence types:

- Peer-reviewed and arXiv methods support algorithmic claims.
- Company technical reports support disclosed training shapes and scale claims.
- Product documentation and blogs support deployment-shape, harness, and workflow claims unless they disclose training details.
- Engineering case studies support workflow and systems-pressure claims, not reproducible optimizer-level claims.

## Update Checklist

When updating the artifact:

1. Add or edit the record in `papers/papers.csv` or `papers/excluded.csv`.
2. Keep controlled vocabulary values consistent with `README.md`.
3. Regenerate statistics with `python scripts/generate_stats.py`.
4. If the update changes headline counts, update `docs/STATS.md`.
5. In the pull request or commit message, state which taxonomy cell or claim changed.
