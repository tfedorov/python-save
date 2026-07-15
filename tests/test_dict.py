import unittest


# =========================
# Tasks to implement
# =========================

def extract_active_names(users):
    """
    Task 1.
    Return names of users where active == True.

    Expected:
    ["Taras", "Bob"]

    Use:
    - list
    - dict
    - list comprehension
    """
    pass


def unique_tools(events):
    """
    Task 2.
    Return unique tool names from agent events.

    Expected:
    {"search_logs", "fetch_metrics", "summarize"}

    Use:
    - set
    - dict access
    - set comprehension
    """
    pass


def count_by_status(events):
    """
    Task 3.
    Return dict: status -> count.

    Expected:
    {
        "success": 2,
        "error": 1,
        "skipped": 1,
    }

    Use:
    - dict
    - loop
    """
    pass


# =========================
# Tests
# =========================

class DictListSetTestCase(unittest.TestCase):

    def test_extract_active_names(self):
        users = [
            {"name": "Taras", "active": True},
            {"name": "Anna", "active": False},
            {"name": "Bob", "active": True},
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