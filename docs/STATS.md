# Paper-Pool Statistics Snapshot

Generated from `papers/papers.csv` and `papers/excluded.csv` with:

```bash
python scripts/generate_stats.py
```

## Headline Counts

- Retained entries: 73
- Excluded decisions: 32
- Audited records: 105

## Retained Category Counts

- `rl_method`: 31
- `benchmark`: 18
- `classical_marl`: 10
- `industry`: 6
- `survey`: 5
- `framework`: 3

## Reward Type Counts

- `NA`: 32
- `hybrid`: 9
- `shared`: 9
- `orchestration`: 7
- `verifier`: 5
- `individual`: 4
- `debate`: 3
- `process`: 2
- `role`: 2

## Credit Granularity Counts

- `NA`: 35
- `agent`: 18
- `orchestrator`: 8
- `role`: 6
- `turn`: 4
- `message`: 2

## Reward Type x Credit Granularity

| reward_type | NA | agent | message | orchestrator | role | turn |
|---|---:|---:|---:|---:|---:|---:|
| NA | 31 | 0 | 0 | 1 | 0 | 0 |
| debate | 0 | 2 | 1 | 0 | 0 | 0 |
| hybrid | 0 | 3 | 0 | 1 | 2 | 3 |
| individual | 0 | 4 | 0 | 0 | 0 | 0 |
| orchestration | 0 | 0 | 0 | 6 | 1 | 0 |
| process | 0 | 1 | 0 | 0 | 0 | 1 |
| role | 0 | 0 | 0 | 0 | 2 | 0 |
| shared | 0 | 8 | 1 | 0 | 0 | 0 |
| verifier | 4 | 0 | 0 | 0 | 1 | 0 |

## Orchestration Form x Credit Granularity

| orchestration_form | NA | agent | message | orchestrator | role | turn |
|---|---:|---:|---:|---:|---:|---:|
| NA | 31 | 3 | 0 | 0 | 0 | 0 |
| centralized | 0 | 11 | 1 | 3 | 0 | 0 |
| debate | 1 | 2 | 1 | 0 | 0 | 1 |
| harness | 2 | 1 | 0 | 0 | 0 | 0 |
| hierarchical | 0 | 1 | 0 | 2 | 3 | 3 |
| planner_executor_critic | 0 | 0 | 0 | 0 | 3 | 0 |
| swarm | 1 | 0 | 0 | 3 | 0 | 0 |
