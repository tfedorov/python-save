import unittest
from collections import defaultdict
from typing import Any
from collections import Counter


def successful_tools(events: list[dict]) -> set[str]:
    return set([e.get("tool", "") for e in events if e.get("status", "failed") == "success"])


def count_by_tool(events: list[dict]) -> dict[str, int]:
    return dict(Counter(e["tool"] for e in events))


def average_duration(events: list[dict]) -> dict[str, float]:
    result_reduced = {}
    result = {}
    for event in events:
        element_tool = event["tool"]
        element_duration = event["duration"]
        existed_duration_numb = result_reduced.get(element_tool, (0, 0))
        new_duration = element_duration + existed_duration_numb[0]
        new_count = existed_duration_numb[1] + 1
        result_reduced.update({element_tool: (new_duration, new_count)})
        result.update({element_tool: new_duration / new_count})

    return result


def slowest_successful_tool(events: list[dict]) -> str | None:
    result = {}
    for event in events:
        if event["status"] == "success" and event["duration"] > result.get("duration", -1):
            result = dict(event)
    return result.get("tool")


class TestAnalyzer(unittest.TestCase):

    def test_successful_tools(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "search", "status": "success", "duration": 80},
            {"tool": "api", "status": "success", "duration": 200},
            {"tool": "db", "status": "success", "duration": 150},
            {"tool": "search", "status": "failed", "duration": 400},
        ]
        self.assertEqual(
            successful_tools(events),
            {"search", "db", "api"}
        )
        self.assertEqual(successful_tools([]), set())

    def test_count_by_tool(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "search", "status": "success", "duration": 80},
            {"tool": "api", "status": "success", "duration": 200},
            {"tool": "db", "status": "success", "duration": 150},
            {"tool": "search", "status": "failed", "duration": 400},
        ]
        self.assertEqual(count_by_tool(events), {
            "search": 3, "db": 2, "api": 1
        })
        self.assertEqual(count_by_tool([]), {})

    def test_average_duration(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "search", "status": "success", "duration": 80},
            {"tool": "api", "status": "success", "duration": 200},
            {"tool": "db", "status": "success", "duration": 150},
            {"tool": "search", "status": "failed", "duration": 400},
        ]
        self.assertEqual(average_duration(events), {
            "search": 200.0,
            "db": 225.0,
            "api": 200.0
        })
        self.assertEqual(average_duration([]), {})

    def test_slowest_successful_tool(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "search", "status": "success", "duration": 80},
            {"tool": "api", "status": "success", "duration": 200},
            {"tool": "db", "status": "success", "duration": 150},
            {"tool": "search", "status": "failed", "duration": 400},
        ]
        self.assertEqual(
            slowest_successful_tool(events), "api"
        )
        self.assertIsNone(slowest_successful_tool([]))
        self.assertIsNone(slowest_successful_tool([
            {"tool": "db", "status": "failed", "duration": 500}
        ]))


if __name__ == "__main__":
    unittest.main()
