# Coverage Stress Test

Date: 2026-05-03

This stress test asks whether the paper's sparse-credit claims depend on
fragile inclusion choices. It is not a new literature search after the
2026-04-26 cutoff. It uses the retained pool, the exclusion log, and the
independent spot-check to test how near-miss rows would affect the core
claims.

## Claims Tested

The stress test focuses on three claims:

1. Message-level credit/signal is sparse.
2. Orchestrator-level credit/signal is sparse, and strict explicit
   orchestrator credit is narrower than the broad controlled-field tag.
3. No retained row exposes explicit RL training for O5 stopping.

## Near-Miss Exclusions

The exclusion log contains prompted MAS frameworks, routers, single-agent
RL methods, product pages, and adjacent benchmarks. The rows most likely
to affect orchestration or credit claims are:

| Excluded row | Why it was stress-tested | Effect if retained |
|---|---|---|
| E003 AutoGen | multi-agent conversation framework | Adds deployment/framework context, not RL credit |
| E006 HuggingGPT | controller workflow for model/tool choice | Adds orchestration design context, not LLM-MAS RL credit |
| E007 MetaGPT | SOP task decomposition | Adds prompted orchestration context, not credit assignment |
| E013 Diversity-Enhanced Reasoning | multi-role optimization adjacent to MAS | Borderline role/debate signal; does not create message-level counterfactual credit |
| E020 AgentBench | agent benchmark | Adds single-agent benchmark context, not MAS trace credit |
| E021 AgentBoard | multi-turn agent evaluation board | Adds benchmark context, not reward/credit instrumentation |
| E022 AgentVerse | multi-agent collaboration framework | Overlaps prompted-collaboration signal; no disclosed RL credit |
| E025 OpenAI Swarm | educational multi-agent framework | Adds framework context, not stable method evidence |
| E030 AutoDefense | multi-agent defense | Safety context, not trace-level RL/evaluation instrumentation |
| E032 RouteLLM | learned router | Pipeline routing rather than multi-agent orchestration-trace training |

None of these near-miss exclusions discloses strict counterfactual
message credit, strict orchestrator credit for an LLM-MAS controller, or
learned O5 stopping.

## Broad vs Strict Credit Stress

The retained broad `credit_granularity` tags are intentionally wider than
strict explicit credit estimators:

| Cell | Broad retained tags | Strict/near-strict subset | Boundary |
|---|---:|---:|---|
| message | 2 | 1 | C3 is strict counterfactual message credit; Debate-as-Reward is a message-level reward signal |
| orchestrator | 7 | 4 | Puppeteer, ParaManager, Kimi K2.5, and OWL are strict or near-strict trained-orchestrator signals; Hera, AgentSpawn, and MAS-Zero are broad design/evolution signals |
| O5 stopping | 0 | 0 | Retained rows use fixed budgets, external success signals, or interface termination rather than explicit RL training for stopping |

Under the strict reading, the sparse-credit conclusion becomes stronger:
the message cell narrows from 2 to 1 strict entry, and the orchestrator
cell narrows from 7 broad tags to 4 strict or near-strict rows. The O5
claim remains unchanged.

## Result

The stress test supports the paper's cautious phrasing:

- Count claims are retained-pool claims, not field-wide prevalence
  estimates.
- Adding near-miss prompted frameworks or single-agent benchmarks would
  not remove message-level or O5 sparsity.
- The main sensitivity is definitional: broad orchestrator design
  signals should not be described as strict explicit credit estimators.
  The manuscript and claim ledger therefore keep those readings separate.

