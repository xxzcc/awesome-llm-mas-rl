# Awesome LLM-MAS RL

Paper pool, taxonomy artifact, and trace schema for:

> Reinforcement Learning for LLM-based Multi-Agent Systems: An Orchestration-Trace Taxonomy

This repository accompanies a survey of reinforcement learning and post-training methods for LLM-based multi-agent systems. The central organizing idea is the **orchestration trace**: a temporal event graph recording orchestrator decisions, sub-agent spawns, inter-agent messages, tool calls, returns, aggregation steps, rewards, and costs.

The repository is designed for auditability. It lets readers inspect which papers support each taxonomy cell, regenerate corpus statistics, and validate whether a multi-agent rollout log satisfies the minimal trace schema proposed in the paper.

## Repository Status

- Target GitHub URL: <https://github.com/xxzcc/awesome-llm-mas-rl>
- Retained paper pool: 73 entries
- Exclusion log: 32 screened-but-excluded records
- Audited records total: 105
- Trace artifact: JSON Schema, example trace, and dependency-free validator

This repository supersedes the earlier related credit-assignment list at <https://github.com/xxzcc/Awesome-Credit-Assignment-in-LLM-RL> for the LLM-MAS survey artifact.

## What Is Included

| Path | Contents |
|---|---|
| `papers/papers.csv` | Retained paper pool with 18 taxonomy fields |
| `papers/excluded.csv` | Screening-decision log for excluded records |
| `papers/papers.bib` | BibTeX database used by the manuscript |
| `scripts/generate_stats.py` | Recomputes corpus counts and cross-tabs |
| `docs/STATS.md` | Static statistics snapshot used by the paper |
| `docs/claim_ledger.md` | Maps central claims to artifact fields and boundaries |
| `trace-schema/trace_schema.json` | Minimal orchestration-trace JSON Schema |
| `trace-schema/example_trace.json` | Valid illustrative trace |
| `trace-schema/validate_trace.py` | Dependency-free trace validator |

## Quick Start

Regenerate the corpus statistics:

```bash
python scripts/generate_stats.py
```

Validate the example orchestration trace:

```bash
python trace-schema/validate_trace.py trace-schema/example_trace.json
```

Both commands use only the Python standard library.

## Taxonomy Fields

Each retained entry in `papers/papers.csv` is tagged with:

```text
key,title,first_author,affiliation,year,arxiv_id,venue,url,
category,is_rl,reward_type,credit_granularity,orchestration_form,
scenario,is_core,one_liner,verified,notes
```

The main controlled fields are:

| Field | Values |
|---|---|
| `category` | `rl_method`, `survey`, `benchmark`, `framework`, `industry`, `classical_marl` |
| `is_rl` | `yes`, `no`, `partial` |
| `reward_type` | `shared`, `individual`, `role`, `process`, `tool`, `debate`, `verifier`, `orchestration`, `hybrid`, `NA` |
| `credit_granularity` | `token`, `turn`, `message`, `tool`, `agent`, `role`, `orchestrator`, `team`, `NA` |
| `orchestration_form` | `centralized`, `planner_executor_critic`, `debate`, `swarm`, `hierarchical`, `harness`, `NA` |
| `scenario` | `coding`, `web`, `research`, `math`, `tool_use`, `debate`, `general`, `NA` |
| `is_core` | `core`, `supporting`, `case` |
| `verified` | `yes`, `partial`, `no` |

## Headline Counts

Current retained categories:

| Category | Entries |
|---|---:|
| RL methods | 31 |
| Benchmarks | 18 |
| Classical MARL foundations | 10 |
| Industrial systems and reports | 6 |
| Surveys | 5 |
| Frameworks | 3 |

Current sparsity signals:

| Axis | Observation |
|---|---|
| Reward type | `shared` and `hybrid` each appear in 9 retained entries; `orchestration` appears in 6 |
| Credit granularity | `agent` appears in 18 entries; `orchestrator` in 7; `message` in only 2 |
| Orchestration form | `centralized` appears in 15 entries; `hierarchical` in 9; `swarm` in 4 |

These counts are intended to support taxonomy claims, not field-wide prevalence estimates.

## Orchestration Trace Schema

The trace schema records the minimum event graph needed to recompute reward, credit, parallelism, cost, and trace-level safety metrics without forcing authors to expose raw prompt or tool content.

Required top-level fields:

```json
{
  "trace_id": "...",
  "task_id": "...",
  "events": [],
  "edges": [],
  "rewards": {},
  "costs": {}
}
```

Supported event types:

```text
orchestrator_decision, spawn, despawn, message, tool_call,
tool_result, return, aggregate, human_intervention, safety_event
```

Supported edge types:

```text
temporal, causal, spawn, message, tool_dependency, return,
aggregate, safety_flow
```

## Update Policy

Pull requests and issues are most useful when they identify one of:

- A missing LLM-MAS RL or post-training method that changes a reward, credit, or orchestration taxonomy cell.
- A public industrial report with explicit multi-agent training evidence rather than only deployment-shape evidence.
- A benchmark that measures collaboration quality, parallel efficiency, protocol overhead, trace-level safety, or long-trace credit behavior.
- A correction to an existing tag in `papers/papers.csv`, with a citation and short justification.

When adding a paper, update `papers/papers.csv`, regenerate statistics with `python scripts/generate_stats.py`, and explain which taxonomy claim changes.

## Citation

```bibtex
@misc{zhang2026rl4llmmas,
  title  = {Reinforcement Learning for LLM-based Multi-Agent Systems:
            An Orchestration-Trace Taxonomy},
  author = {Chenchen Zhang},
  year   = {2026},
  note   = {Working draft and artifact repository},
  url    = {https://github.com/xxzcc/awesome-llm-mas-rl}
}
```

## License

Paper-pool metadata and trace examples are released under CC0-1.0. Scripts are released under the MIT License.
