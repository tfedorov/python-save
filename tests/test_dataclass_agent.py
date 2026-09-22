import unittest
from dataclasses import dataclass
from typing import Any


# =========================
# Tasks to implement
# =========================

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


# =========================
# Tests
# =========================

class DataclassAgentTestCase(unittest.TestCase):

    def test_create_tool_call(self):
        result = create_tool_call(
            "search_logs",
            service="api",
            limit=10,
        )

        expected = ToolCall(
            name="search_logs",
            args={"service": "api", "limit": 10},
            status="pending",
        )

        self.assertEqual(expected, result)

    def test_create_tool_call_with_status(self):
        result = create_tool_call(
            "fetch_metrics",
            status="success",
            metric="cpu",
        )

        expected = ToolCall(
            name="fetch_metrics",
            args={"metric": "cpu"},
            status="success",
        )

        self.assertEqual(expected, result)

    def test_successful_tools(self):
        calls = [
            ToolCall("search_logs", {}, "success"),
            ToolCall("fetch_metrics", {}, "error"),
            ToolCall("summarize", {}, "success"),
        ]

        result = successful_tools(calls)

        self.assertEqual(["search_logs", "summarize"], result)

    def test_group_by_status(self):
        call1 = ToolCall("search_logs", {}, "success")
        call2 = ToolCall("fetch_metrics", {}, "error")
        call3 = ToolCall("summarize", {}, "success")

        result = group_by_status([call1, call2, call3])

        expected = {
            "success": [call1, call3],
            "error": [call2],
        }

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
