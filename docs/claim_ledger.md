# Claim-to-Artifact Ledger

This table maps central survey claims to the artifact fields or files that support them.

| Claim | Artifact check | Boundary |
|---|---|---|
| Message-level credit is sparse | `credit_granularity=message` has two retained tags; only C3 is counterfactual message credit | Tag count includes message-level reward/signal, not only explicit credit mechanisms |
| Orchestrator-level credit is sparse | `credit_granularity=orchestrator` has eight retained tags after Kimi K2.6 is treated as deployment evidence and WideSeek-R1 is added | Explicit RL credit mechanisms are narrower than orchestrator-level design or evolution signals |
| O5 stopping is uncovered by explicit RL training | O1--O4 have retained anchors in spawn/decomposition, delegation, communication, and aggregation; no retained row exposes an explicit RL update for learned stopping | This is a claim-level coverage audit, not a disjoint prevalence count, because one system can touch several orchestration sub-decisions |
| Kimi provides the industrial trained-orchestrator anchor | K2.5 row: `is_rl=yes`, `reward_type=orchestration`; K2.6 row: `is_rl=partial`, `reward_type=NA` | K2.6 is used for deployment-envelope pressure, not as an independent training claim |
| Open MAS-native evaluation remains incomplete | Benchmark rows plus the trace schema and reporting checklist | The claim is restricted to open, auditable retained entries under the stated protocol |
| Trace reporting is mechanically inspectable | `trace-schema/trace_schema.json`, `trace-schema/example_trace.json`, and `trace-schema/validate_trace.py` | The checker validates core structural constraints, not the full JSON Schema standard |
| Sparse-credit claims are robust to near-miss exclusions | `docs/audits/coverage_stress_test_2026-05-03.md` reviews prompted frameworks, routers, product pages, and adjacent benchmarks from `papers/excluded.csv` | These rows add context but do not disclose strict counterfactual message credit or explicit learned O5 stopping |

Use this ledger as a reading guide. The CSV is the source of truth for controlled tags; the manuscript interprets those tags under the evidence boundaries stated in the paper.

## Reliability Spot-Check

An independent second-pass spot-check is recorded in
`docs/audits/independent_spotcheck_2026-05-03.csv` and
`docs/audits/independent_spotcheck_2026-05-03.md`. It covers 32 retained
rows, including all sparse-credit and industrial anchor rows. Agreement
under the broad controlled-field definitions was 32/32 for category,
is-RL status, reward type, and orchestration form, and 31/32 for credit
granularity. The disagreement was `halo`, where the independent reader
preferred an orchestrator-level broad signal tag over the original
role-level tag. This is a reliability spot-check, not a multi-annotator
agreement statistic.

## Sparse Credit-Tag Rationale

`credit_granularity` records the finest level where an entry exposes a reward, credit, or design signal. It is broader than explicit counterfactual credit.

Strict explicit-credit reading:

| Cell | Broad tags | Strict or near-strict subset | Boundary |
|---|---:|---:|---|
| message | 2 | 1 | C3 is strict counterfactual message credit; Debate-as-Reward is a message-level reward signal |
| orchestrator | 8 | 5 | Puppeteer, ParaManager, Kimi K2.5, OWL, and WideSeek-R1 are strict or near-strict trained-orchestrator signals; Hera, AgentSpawn, and MAS-Zero are broad design/evolution signals |
| O5 stopping | 0 | 0 | No retained row exposes explicit RL training for learned stopping |

| Row | Tagged level | Rationale | Mechanism boundary |
|---|---|---|---|
| `puppeteer` | orchestrator | Learned central critic over orchestrator delegation | Explicit RL credit |
| `paramanager` | orchestrator | Unified agent/tool orchestration action space | Orchestrator-level design signal, not counterfactual credit |
| `hera` | orchestrator | Evolving orchestration policy and prompts | Evolution signal over orchestration choices |
| `agentspawn` | orchestrator | Runtime spawn decisions and memory transfer | Runtime design signal; no disclosed RL credit estimator |
| `kimi-k2-5` | orchestrator | PARL with Critical-Steps reward for Agent Swarm | Explicit public training signal; full traces are not released |
| `owl2025` | orchestrator | Planner/workforce optimization for modular agents | Planner-level training signal |
| `mas-zero2025` | orchestrator | Meta-level MAS design feedback and verification | Non-RL design-search signal |
| `wideseek-r1-2026` | orchestrator | Lead-agent/subagent width scaling with MARL | Explicit orchestration-training signal, but not dynamic-spawn counterfactual credit |
| `c3` | message | Counterfactual causal credit at message level | Explicit counterfactual message credit |
| `debate-as-reward` | message | Debate messages supply a reward signal | Message-level reward signal, not counterfactual credit |
