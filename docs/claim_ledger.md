# Claim-to-Artifact Ledger

This table maps central survey claims to the artifact fields or files that support them.

| Claim | Artifact check | Boundary |
|---|---|---|
| Message-level credit is sparse | `credit_granularity=message` has two retained tags; only C3 is counterfactual message credit | Tag count includes message-level reward/signal, not only explicit credit mechanisms |
| Orchestrator-level credit is sparse | `credit_granularity=orchestrator` has seven retained tags after Kimi K2.6 is treated as deployment evidence | Explicit RL credit mechanisms are narrower than orchestrator-level design or evolution signals |
| Kimi provides the industrial trained-orchestrator anchor | K2.5 row: `is_rl=yes`, `reward_type=orchestration`; K2.6 row: `is_rl=partial`, `reward_type=NA` | K2.6 is used for deployment-envelope pressure, not as an independent training claim |
| Open MAS-native evaluation remains incomplete | Benchmark rows plus the trace schema and reporting checklist | The claim is restricted to open, auditable retained entries under the stated protocol |
| Trace reporting is mechanically inspectable | `trace-schema/trace_schema.json`, `trace-schema/example_trace.json`, and `trace-schema/validate_trace.py` | The checker validates core structural constraints, not the full JSON Schema standard |

Use this ledger as a reading guide. The CSV is the source of truth for controlled tags; the manuscript interprets those tags under the evidence boundaries stated in the paper.

## Sparse Credit-Tag Rationale

`credit_granularity` records the finest level where an entry exposes a reward, credit, or design signal. It is broader than explicit counterfactual credit.

| Row | Tagged level | Rationale | Mechanism boundary |
|---|---|---|---|
| `puppeteer` | orchestrator | Learned central critic over orchestrator delegation | Explicit RL credit |
| `paramanager` | orchestrator | Unified agent/tool orchestration action space | Orchestrator-level design signal, not counterfactual credit |
| `hera` | orchestrator | Evolving orchestration policy and prompts | Evolution signal over orchestration choices |
| `agentspawn` | orchestrator | Runtime spawn decisions and memory transfer | Runtime design signal; no disclosed RL credit estimator |
| `kimi-k2-5` | orchestrator | PARL with Critical-Steps reward for Agent Swarm | Explicit public training signal; full traces are not released |
| `owl2025` | orchestrator | Planner/workforce optimization for modular agents | Planner-level training signal |
| `mas-zero2025` | orchestrator | Meta-level MAS design feedback and verification | Non-RL design-search signal |
| `c3` | message | Counterfactual causal credit at message level | Explicit counterfactual message credit |
| `debate-as-reward` | message | Debate messages supply a reward signal | Message-level reward signal, not counterfactual credit |
