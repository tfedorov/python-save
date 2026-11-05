import pytest
from dataclasses import dataclass
from typing import Any


@dataclass
class ToolCall:
    name: str
    args: dict[str, Any]
    status: str


def create_tool_call(name: str, status: str = "pending", **kwargs: Any) -> ToolCall:
    return ToolCall(name, kwargs, status)


def successful_tools(calls: list[ToolCall]) -> list[str]:
    grouped: dict[str, list[ToolCall]] = group_by_status(calls)
    return [g.name for g in grouped.get("success", [])]


def group_by_status(calls: list[ToolCall]) -> dict[str, list[ToolCall]]:
    key_vals = [(call.status, call) for call in calls]
    result: dict[str, list[ToolCall]] = {}
    dict_one: tuple[str, list[ToolCall]]
    for key_val in key_vals:
        values: list[ToolCall] = result.get(key_val[0], [])
        values.append(key_val[1])
        result.update({key_val[0]: values})
    return result


def test_create_tool_call_success():
    input_name = "search_logs"

    result: ToolCall = create_tool_call(input_name, service="api", limit=10)

    expected: ToolCall = ToolCall(
        name="search_logs",
        args={"service": "api", "limit": 10},
        status="pending",
    )
    assert result == expected


def test_create_tool_call_success_with_status():
    input_name = "fetch_metrics"
    input_status = "success"

    result: ToolCall = create_tool_call(input_name, status=input_status, metric="cpu")

    expected: ToolCall = ToolCall(
        name="fetch_metrics",
        args={"metric": "cpu"},
        status="success",
    )
    assert result == expected


def test_successful_tools_success():
    input_calls = [
        ToolCall("search_logs", {}, "success"),
        ToolCall("fetch_metrics", {}, "error"),
        ToolCall("summarize", {}, "success"),
    ]

    result: list[str] = successful_tools(input_calls)

    expected: list[str] = ["search_logs", "summarize"]
    assert result == expected


def test_group_by_status_success():
    input_call1 = ToolCall("search_logs", {}, "success")
    input_call2 = ToolCall("fetch_metrics", {}, "error")
    input_call3 = ToolCall("summarize", {}, "success")

    result: dict[str, list[ToolCall]] = group_by_status([input_call1, input_call2, input_call3])

    expected: dict[str, list[ToolCall]] = {
        "success": [input_call1, input_call3],
        "error": [input_call2],
    }
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
