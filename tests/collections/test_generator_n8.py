import pytest
from typing import Iterable, Iterator, Any


def successful_events(events: Iterable[dict[str, Any]]) -> Iterator[dict[str, Any]]:
    for event in events:
        if event["status"] == "success":
            yield event


def slow_events(
        events: Iterable[dict[str, Any]], threshold: int
) -> Iterator[dict[str, Any]]:
    for event in events:
        if event["duration"] > threshold:
            yield event


def event_durations(events: Iterable[dict[str, Any]]) -> Iterator[int]:
    for event in events:
        yield event["duration"]


def first_failed_event(events: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    for event in events:
        if event["status"] == "failed":
            return event
    return None


def test_successful_events_success():
    input_events = [
        {"tool": "search", "status": "success", "duration": 120},
        {"tool": "db", "status": "failed", "duration": 300},
        {"tool": "api", "status": "success", "duration": 80},
    ]

    result: list[dict[str, Any]] = list(successful_events(iter(input_events)))

    expected: list[dict[str, Any]] = [
        {"tool": "search", "status": "success", "duration": 120},
        {"tool": "api", "status": "success", "duration": 80},
    ]
    assert result == expected


def test_slow_events_success():
    input_events = [
        {"tool": "search", "status": "success", "duration": 120},
        {"tool": "db", "status": "failed", "duration": 300},
        {"tool": "api", "status": "success", "duration": 150},
        {"tool": "search", "status": "success", "duration": 200},
    ]
    input_threshold = 150

    result: list[dict[str, Any]] = list(slow_events(iter(input_events), input_threshold))

    expected: list[dict[str, Any]] = [
        {"tool": "db", "status": "failed", "duration": 300},
        {"tool": "search", "status": "success", "duration": 200},
    ]
    assert result == expected


def test_event_durations_success():
    input_events = [
        {"tool": "search", "status": "success", "duration": 120},
        {"tool": "db", "status": "failed", "duration": 300},
        {"tool": "api", "status": "success", "duration": 80},
    ]

    result: list[int] = list(event_durations(iter(input_events)))

    expected: list[int] = [120, 300, 80]
    assert result == expected


def test_first_failed_event_success():
    input_events = [
        {"tool": "search", "status": "success", "duration": 120},
        {"tool": "db", "status": "failed", "duration": 300},
        {"tool": "api", "status": "failed", "duration": 80},
    ]

    result: dict[str, Any] | None = first_failed_event(iter(input_events))

    expected: dict[str, Any] | None = {"tool": "db", "status": "failed", "duration": 300}
    assert result == expected


def test_lazy_evaluation_success():
    input_events = [
        {"tool": "search", "status": "success", "duration": 120},
        {"tool": "db", "status": "failed", "duration": 300},
        {"tool": "api", "status": "success", "duration": 80},
    ]
    consumed = []

    def source():
        for event in input_events:
            consumed.append(event)
            yield event

    successful_events(source())

    result: int = len(consumed)

    expected: int = 0
    assert result == expected


def test_stop_after_first_failure_success():
    input_events = [
        {"tool": "search", "status": "success", "duration": 120},
        {"tool": "db", "status": "failed", "duration": 300},
        {"tool": "api", "status": "success", "duration": 80},
    ]
    consumed = []

    def source():
        for event in input_events:
            consumed.append(event)
            yield event

    first_failed_event(source())

    result: int = len(consumed)

    expected: int = 2
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
