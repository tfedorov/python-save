import unittest
from collections import Counter, defaultdict, deque
from typing import Any


# =========================
# Tasks to implement
# =========================

def count_tools(events: list[dict[str, str]]) -> dict[str, int]:
    result: Counter[str] = Counter(event["tool"] for event in events)
    return dict(result)


def group_events_by_tool(events: list[dict[str, str]]):
    grouped = defaultdict(list)
    [grouped[event["tool"]].append(event) for event in events]
    return grouped


def last_n_events(events: list[dict[str, int | str]], n):
    result = deque(events,n)
    return list(result)
    #return events[-n:]


# =========================
# Tests
# =========================

class CollectionsModuleTestCase(unittest.TestCase):

    def test_count_tools(self):
        events: list[dict[str, str]] = [
            {"tool": "search_logs", "status": "success"},
            {"tool": "fetch_metrics", "status": "error"},
            {"tool": "search_logs", "status": "success"},
            {"tool": "summarize", "status": "success"},
        ]

        result = count_tools(events)

        self.assertEqual(
            {
                "search_logs": 2,
                "fetch_metrics": 1,
                "summarize": 1,
            },
            result
        )

    def test_group_events_by_tool(self):
        event1: dict[str, str] = {"tool": "search_logs", "status": "success"}
        event2: dict[str, str] = {"tool": "fetch_metrics", "status": "error"}
        event3: dict[str, str] = {"tool": "search_logs", "status": "skipped"}

        result = group_events_by_tool([event1, event2, event3])

        self.assertEqual(
            {
                "search_logs": [event1, event3],
                "fetch_metrics": [event2],
            },
            result
        )

    def test_last_n_events(self):
        events: list[dict[str, int | str]] = [
            {"id": 1, "tool": "search_logs"},
            {"id": 2, "tool": "fetch_metrics"},
            {"id": 3, "tool": "summarize"},
            {"id": 4, "tool": "route"},
        ]

        result = last_n_events(events, 2)

        self.assertEqual(
            [
                {"id": 3, "tool": "summarize"},
                {"id": 4, "tool": "route"},
            ],
            result
        )


if __name__ == "__main__":
    unittest.main()
