import unittest
from typing import Any


def extract_tool_names(events: list[dict[str, Any]]) -> list[str]:
    """
    Return list of tool names.

    Ignore events without "tool".
    """
    pass


def find_first_error(events: list[dict[str, Any]]) -> dict[str, Any] | None:
    """
    Return first event where status == "error".

    If no error exists, return None.
    """
    pass


def build_agent_state(
        user_input: str,
        tools: list[str],
        metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Return agent state dict.

    Expected keys:
    - input
    - tools
    - metadata

    If metadata is None, use empty dict.
    """
    pass


class TypeHintsTestCase(unittest.TestCase):

    def test_extract_tool_names(self):
        events = [
            {"tool": "search_logs", "status": "success"},
            {"status": "error"},
            {"tool": "summarize", "status": "success"},
        ]

        result = extract_tool_names(events)

        self.assertEqual(["search_logs", "summarize"], result)

    def test_find_first_error(self):
        events = [
            {"tool": "search_logs", "status": "success"},
            {"tool": "fetch_metrics", "status": "error"},
            {"tool": "summarize", "status": "success"},
        ]

        result = find_first_error(events)

        self.assertEqual(
            {"tool": "fetch_metrics", "status": "error"},
            result
        )

    def test_find_first_error_returns_none(self):
        events = [
            {"tool": "search_logs", "status": "success"},
            {"tool": "summarize", "status": "success"},
        ]

        result = find_first_error(events)

        self.assertIsNone(result)

    def test_build_agent_state_without_metadata(self):
        result = build_agent_state(
            user_input="Check logs",
            tools=["search_logs", "summarize"],
        )

        expected = {
            "input": "Check logs",
            "tools": ["search_logs", "summarize"],
            "metadata": {},
        }

        self.assertEqual(expected, result)

    def test_build_agent_state_with_metadata(self):
        result = build_agent_state(
            user_input="Check logs",
            tools=["search_logs"],
            metadata={"request_id": "abc-123"},
        )

        expected = {
            "input": "Check logs",
            "tools": ["search_logs"],
            "metadata": {"request_id": "abc-123"},
        }

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()