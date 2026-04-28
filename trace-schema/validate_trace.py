#!/usr/bin/env python3
"""Lightweight validator for orchestration trace JSON files.

This intentionally avoids third-party dependencies. It checks the core
constraints used by the survey artifact: required top-level fields,
allowed event/edge types, unique event ids, edge references, and
non-negative costs.
"""

import json
import sys
from pathlib import Path


ALLOWED_EVENT_TYPES = {
    "orchestrator_decision",
    "spawn",
    "despawn",
    "message",
    "tool_call",
    "tool_result",
    "return",
    "aggregate",
    "human_intervention",
    "safety_event",
}

ALLOWED_EDGE_TYPES = {
    "temporal",
    "causal",
    "spawn",
    "message",
    "tool_dependency",
    "return",
    "aggregate",
    "safety_flow",
}

REQUIRED_TOP_LEVEL = {"trace_id", "task_id", "events", "edges", "rewards", "costs"}
REQUIRED_EVENT = {"id", "t", "type", "agent"}
REQUIRED_EDGE = {"src", "dst", "type"}


def fail(message):
    raise SystemExit("validation failed: " + message)


def validate(path):
    data = json.loads(Path(path).read_text())

    missing = REQUIRED_TOP_LEVEL - set(data)
    if missing:
        fail("missing top-level fields: " + ", ".join(sorted(missing)))

    if not isinstance(data["events"], list) or not data["events"]:
        fail("events must be a non-empty list")
    if not isinstance(data["edges"], list):
        fail("edges must be a list")

    event_ids = set()
    for event in data["events"]:
        missing_event = REQUIRED_EVENT - set(event)
        if missing_event:
            fail("event missing fields: " + ", ".join(sorted(missing_event)))
        if event["type"] not in ALLOWED_EVENT_TYPES:
            fail("unknown event type: " + event["type"])
        if event["id"] in event_ids:
            fail("duplicate event id: " + event["id"])
        if event["t"] < 0:
            fail("negative event timestamp: " + event["id"])
        event_ids.add(event["id"])

    for edge in data["edges"]:
        missing_edge = REQUIRED_EDGE - set(edge)
        if missing_edge:
            fail("edge missing fields: " + ", ".join(sorted(missing_edge)))
        if edge["type"] not in ALLOWED_EDGE_TYPES:
            fail("unknown edge type: " + edge["type"])
        if edge["src"] not in event_ids:
            fail("edge src not found: " + edge["src"])
        if edge["dst"] not in event_ids:
            fail("edge dst not found: " + edge["dst"])

    for key, value in data["costs"].items():
        if value < 0:
            fail("negative cost field: " + key)

    print("valid trace:", path)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "trace-schema/example_trace.json"
    validate(path)


if __name__ == "__main__":
    main()
