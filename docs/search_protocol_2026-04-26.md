# Search and Screening Protocol

Date cutoff: 2026-05-04

This artifact is a structured mapping review rather than a PRISMA
systematic review. The goal is to map reward, credit, orchestration,
evaluation, and safety evidence for RL in LLM-based multi-agent systems.
The protocol below records the sources, query families, inclusion rule,
exclusion stages, and audit hooks used by the paper.

## Sources

Searches covered these source families:

- arXiv
- ACL Anthology
- OpenReview
- Semantic Scholar and citation links from retained papers
- official project pages
- company technical reports and product documentation
- classical MARL references needed to define credit-assignment cells

## Query Families

The search used query families rather than one database-specific query
string, because arXiv, ACL Anthology, OpenReview, product docs, and
company blogs expose different search interfaces. The families were:

| Family | Query terms |
|---|---|
| Multi-agent LLM RL | multi-agent LLM, multi-agent language model, LLM-MAS, reinforcement learning, RL, post-training, fine-tuning |
| Credit assignment | credit assignment, counterfactual credit, Shapley credit, message credit, role credit, multi-agent credit |
| Orchestration | orchestration, orchestrator, manager-worker, delegation, dynamic spawning, agent swarm, routing, aggregation |
| Tool and software agents | tool-use LLM, software agent, coding agent, browser agent, web agent, reinforcement learning |
| Safety | prompt injection, jailbreak, adversarial, security, safety, multi-agent, agent benchmark |
| Classical MARL | centralized critic, value decomposition, COMA, QMIX, VDN, difference rewards, Dec-POMDP, Markov game |
| Industrial systems | Kimi Agent Swarm, Codex, Claude Code, subagents, parallel agents, cloud coding agent, agent harness |

## Inclusion Rule

An entry is retained if it satisfies at least one of the following:

1. It trains or post-trains an LLM-based multi-agent process, controller,
   router, critic, role, or team.
2. It provides an evaluation setting for agent teams with enough detail
   to support trace-level evaluation or safety discussion.
3. It reports a public industrial system that exposes an orchestration
   boundary, scale envelope, sub-agent interface, harness, or workflow
   relevant to RL design.
4. It is a classical MARL or single-agent LLM-RL foundation needed to
   define a taxonomy cell.
5. It is an adjacent survey needed to distinguish the paper's
   trace-centered contribution from prior survey lines.

## Exclusion Rule

An entry is excluded when it is only a prompted agent framework, a
single-agent RL method not used as a foundation, a product page without
enough technical detail, a duplicate/overlapping signal, or a safety or
benchmark paper without trace-level MAS relevance for the paper's claims.

## Screening Stages

The retained pool contains 84 entries, and the exclusion log records
32 screened-but-excluded entries:

- 16 abstract-screen exclusions
- 9 full-text-screen exclusions
- 6 artifact-screen exclusions
- 1 duplicate/overlap exclusion

Each exclusion includes source, query family, public identifier, URL,
screening date, stage, and reason.

## Tagging and Audit Hooks

Retained rows are tagged with controlled fields in `papers/papers.csv`.
The statistics script recomputes the headline counts and cross-tabs:

```bash
python scripts/generate_stats.py
```

The claim ledger maps central claims to exact filters. The independent
spot-check files record a second-pass audit over 32 retained rows. The
coverage stress-test file records how near-miss and broad-signal rows
affect sparse-credit claims.
