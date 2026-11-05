import pytest
from typing import Any


def extract_tool_names(events: list[dict[str, Any]]) -> list[str]:
    return [e["tool"] for e in events if "tool" in e]


def find_first_error(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    return next((e for e in events if e.get("status") == "error"), None)


def build_agent_state(
        user_input: str,
        tools: list[str],
        metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "input": user_input,
        "tools": tools,
        "metadata": metadata if metadata is not None else {},
    }


def test_extract_tool_names_success():
    input_events = [
        {"tool": "search_logs", "status": "success"},
        {"status": "error"},
        {"tool": "summarize", "status": "success"},
    ]

    result: list[str] = extract_tool_names(input_events)

    expected: list[str] = ["search_logs", "summarize"]
    assert result == expected


def test_find_first_error_success():
    input_events = [
        {"tool": "search_logs", "status": "success"},
        {"tool": "fetch_metrics", "status": "error"},
        {"tool": "summarize", "status": "success"},
    ]

    result: dict[str, Any] | None = find_first_error(input_events)

    expected: dict[str, Any] | None = {"tool": "fetch_metrics", "status": "error"}
    assert result == expected


def test_find_first_error_success_none():
    input_events = [
        {"tool": "search_logs", "status": "success"},
        {"tool": "summarize", "status": "success"},
    ]

    result: dict[str, Any] | None = find_first_error(input_events)

    expected: dict[str, Any] | None = None
    assert result == expected


def test_build_agent_state_success_without_metadata():
    input_user_input = "Check logs"
    input_tools = ["search_logs", "summarize"]

    result: dict[str, Any] = build_agent_state(input_user_input, input_tools)

    expected: dict[str, Any] = {
        "input": "Check logs",
        "tools": ["search_logs", "summarize"],
        "metadata": {},
    }
    assert result == expected


def test_build_agent_state_success_with_metadata():
    input_user_input = "Check logs"
    input_tools = ["search_logs"]
    input_metadata = {"request_id": "abc-123"}

    result: dict[str, Any] = build_agent_state(
        input_user_input,
        input_tools,
        metadata=input_metadata,
    )

    expected: dict[str, Any] = {
        "input": "Check logs",
        "tools": ["search_logs"],
        "metadata": {"request_id": "abc-123"},
    }
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
