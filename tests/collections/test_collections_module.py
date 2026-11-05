from collections import Counter, defaultdict, deque

import pytest


def count_tools(events: list[dict[str, str]]) -> dict[str, int]:
    result: Counter[str] = Counter(event["tool"] for event in events)
    return dict(result)


def group_events_by_tool(events: list[dict[str, str]]):
    grouped = defaultdict(list)
    [grouped[event["tool"]].append(event) for event in events]
    return grouped


def last_n_events(events: list[dict[str, int | str]], n):
    result = deque(events, n)
    return list(result)


def test_count_tools_success():
    input_events: list[dict[str, str]] = [
        {"tool": "search_logs", "status": "success"},
        {"tool": "fetch_metrics", "status": "error"},
        {"tool": "search_logs", "status": "success"},
        {"tool": "summarize", "status": "success"},
    ]

    result: dict[str, int] = count_tools(input_events)

    expected: dict[str, int] = {
        "search_logs": 2,
        "fetch_metrics": 1,
        "summarize": 1,
    }
    assert result == expected


def test_group_events_by_tool_success():
    input_event1: dict[str, str] = {"tool": "search_logs", "status": "success"}
    input_event2: dict[str, str] = {"tool": "fetch_metrics", "status": "error"}
    input_event3: dict[str, str] = {"tool": "search_logs", "status": "skipped"}

    result = group_events_by_tool([input_event1, input_event2, input_event3])

    expected = {
        "search_logs": [input_event1, input_event3],
        "fetch_metrics": [input_event2],
    }
    assert result == expected


def test_last_n_events_success():
    input_events: list[dict[str, int | str]] = [
        {"id": 1, "tool": "search_logs"},
        {"id": 2, "tool": "fetch_metrics"},
        {"id": 3, "tool": "summarize"},
        {"id": 4, "tool": "route"},
    ]
    input_n = 2

    result: list[dict[str, int | str]] = last_n_events(input_events, input_n)

    expected: list[dict[str, int | str]] = [
        {"id": 3, "tool": "summarize"},
        {"id": 4, "tool": "route"},
    ]
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
