# Paper-Pool Statistics Snapshot

Generated from `papers/papers.csv` and `papers/excluded.csv` with:

```bash
python scripts/generate_stats.py
```

## Headline Counts

- Retained entries: 84
- Excluded decisions: 32
- Audited records: 116

## Retained Category Counts

- `rl_method`: 42
- `benchmark`: 18
- `classical_marl`: 10
- `industry`: 6
- `survey`: 5
- `framework`: 3

## Reward Type Counts

- `NA`: 33
- `hybrid`: 15
- `shared`: 10
- `orchestration`: 7
- `verifier`: 6
- `debate`: 4
- `individual`: 4
- `role`: 3
- `process`: 2

## Credit Granularity Counts

- `NA`: 36
- `agent`: 23
- `role`: 10
- `orchestrator`: 8
- `turn`: 5
- `message`: 2

## Reward Type x Credit Granularity

| reward_type | NA | agent | message | orchestrator | role | turn |
|---|---:|---:|---:|---:|---:|---:|
| NA | 32 | 0 | 0 | 1 | 0 | 0 |
| debate | 0 | 3 | 1 | 0 | 0 | 0 |
| hybrid | 0 | 6 | 0 | 1 | 4 | 4 |
| individual | 0 | 4 | 0 | 0 | 0 | 0 |
| orchestration | 0 | 0 | 0 | 6 | 1 | 0 |
| process | 0 | 1 | 0 | 0 | 0 | 1 |
| role | 0 | 0 | 0 | 0 | 3 | 0 |
| shared | 0 | 9 | 1 | 0 | 0 | 0 |
| verifier | 4 | 0 | 0 | 0 | 2 | 0 |

## Orchestration Form x Credit Granularity

| orchestration_form | NA | agent | message | orchestrator | role | turn |
|---|---:|---:|---:|---:|---:|---:|
| NA | 31 | 3 | 0 | 0 | 0 | 0 |
| centralized | 0 | 14 | 1 | 3 | 0 | 0 |
| debate | 1 | 3 | 1 | 0 | 1 | 2 |
| harness | 2 | 1 | 0 | 0 | 0 | 0 |
| hierarchical | 0 | 2 | 0 | 3 | 5 | 3 |
| planner_executor_critic | 0 | 0 | 0 | 0 | 4 | 0 |
| swarm | 2 | 0 | 0 | 2 | 0 | 0 |
