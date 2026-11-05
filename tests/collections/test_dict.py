import pytest


def extract_active_names(users):
    return [user["name"] for user in users if user.get("active", False)]


def unique_tools(events):
    return {event["tool"] for event in events if "tool" in event}


def count_by_status(events):
    result = {}
    for event in events:
        if "status" not in event:
            continue
        key = event["status"]
        result[key] = result.get(key, 0) + 1
    return result


def test_extract_active_names_success():
    input_users = [
        {"name": "Taras", "active": True},
        {"name": "Anna", "active": False},
        {"name": "Bob", "active": True},
        {"no": "Bob", "a": True},
    ]

    result: list[str] = extract_active_names(input_users)

    expected: list[str] = ["Taras", "Bob"]
    assert result == expected


def test_unique_tools_success():
    input_events = [
        {"tool": "search_logs", "status": "success"},
        {"tool": "fetch_metrics", "status": "error"},
        {"tool": "search_logs", "status": "success"},
        {"tool": "summarize", "status": "success"},
    ]

    result: set[str] = unique_tools(input_events)

    expected: set[str] = {"search_logs", "fetch_metrics", "summarize"}
    assert result == expected


def test_count_by_status_success():
    input_events = [
        {"tool": "search_logs", "status": "success"},
        {"tool": "fetch_metrics", "status": "error"},
        {"tool": "summarize", "status": "success"},
        {"tool": "search_logs", "status": "skipped"},
    ]

    result: dict[str, int] = count_by_status(input_events)

    expected: dict[str, int] = {
        "success": 2,
        "error": 1,
        "skipped": 1,
    }
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
