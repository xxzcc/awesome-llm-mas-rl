# Orchestration Trace Schema

This directory contains a minimal JSON Schema for replayable LLM-MAS orchestration traces.

## Files

- `trace_schema.json`: JSON Schema for typed orchestration traces.
- `example_trace.json`: Minimal valid example trace.
- `validate_trace.py`: Dependency-free validator for required fields, event types, edge references, duplicate event IDs, and non-negative costs.

## Validate

From the repository root:

```bash
python trace-schema/validate_trace.py trace-schema/example_trace.json
```

The schema is intentionally minimal. It records the event graph needed to recompute reward, credit, parallelism, cost, and trace-level safety metrics without requiring raw prompt or tool content.
