import unittest
from typing import Any


# =========================
# Tasks to implement
# =========================

def extract_active_names(users):
    return [user["name"] for user in users if user.get("active", False)]


def unique_tools(events):
    return { event["tool"] for event in events if "tool" in event}

def count_by_status(events):
    result = {}
    for event in events:
        if "status" not in event:
            continue

        key = event["status"]
        result[key] = result.get(key, 0) + 1
    return result


# =========================
# Tests
# =========================

class DictListSetTestCase(unittest.TestCase):

    def test_extract_active_names(self):
        users = [
            {"name": "Taras", "active": True},
            {"name": "Anna", "active": False},
            {"name": "Bob", "active": True},
            {"no": "Bob", "a": True},
        ]

        result = extract_active_names(users)

        self.assertEqual(["Taras", "Bob"], result)

    def test_unique_tools(self):
        events = [
            {"tool": "search_logs", "status": "success"},
            {"tool": "fetch_metrics", "status": "error"},
            {"tool": "search_logs", "status": "success"},
            {"tool": "summarize", "status": "success"},
        ]

        result = unique_tools(events)

        self.assertEqual(
            {"search_logs", "fetch_metrics", "summarize"},
            result
        )

    def test_count_by_status(self):
        events = [
            {"tool": "search_logs", "status": "success"},
            {"tool": "fetch_metrics", "status": "error"},
            {"tool": "summarize", "status": "success"},
            {"tool": "search_logs", "status": "skipped"},
        ]

        result = count_by_status(events)

        self.assertEqual(
            {
                "success": 2,
                "error": 1,
                "skipped": 1,
            },
            result
        )


if __name__ == "__main__":
    unittest.main()