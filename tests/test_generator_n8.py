
import unittest
from typing import Iterable, Iterator, Any

Event = dict[str, Any]


# =========================
# Tasks to implement
# =========================

def successful_events(events: Iterable[Event]) -> Iterator[Event]:
    for event in events:
        if event["status"] == "success":
            yield event

def slow_events(
        events: Iterable[Event], threshold: int
) -> Iterator[Event]:
    for event in events:
        if event["duration"] > threshold:
            yield event


def event_durations(events: Iterable[Event]) -> Iterator[int]:
    for event in events:
        yield event["duration"]


def first_failed_event(events: Iterable[Event]) -> Event | None:
    for event in events:
        if event["status"] == "failed":
            return event
    return None

# =========================
# Unit Tests
# =========================

class TestEventStream(unittest.TestCase):

    def test_successful_events(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "api", "status": "success", "duration": 80},
        ]

        result = successful_events(iter(events))

        self.assertEqual(
            list(result),
            [events[0], events[2]]
        )

    def test_slow_events(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "api", "status": "success", "duration": 150},
            {"tool": "search", "status": "success", "duration": 200},
        ]

        self.assertEqual(
            list(slow_events(iter(events), 150)),
            [events[1], events[3]]
        )

    def test_event_durations(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "api", "status": "success", "duration": 80},
        ]

        self.assertEqual(
            list(event_durations(iter(events))),
            [120, 300, 80]
        )

    def test_first_failed_event(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "api", "status": "failed", "duration": 80},
        ]

        self.assertEqual(
            first_failed_event(iter(events)),
            events[1]
        )
        self.assertIsNone(first_failed_event(iter([])))

    def test_lazy_evaluation(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "api", "status": "success", "duration": 80},
        ]

        consumed = []

        def source():
            for event in events:
                consumed.append(event)
                yield event

        result = successful_events(source())

        # Generator must not consume events immediately
        self.assertEqual(consumed, [])

        first = next(result)

        self.assertEqual(first, events[0])
        self.assertEqual(len(consumed), 1)

    def test_stop_after_first_failure(self):
        events = [
            {"tool": "search", "status": "success", "duration": 120},
            {"tool": "db", "status": "failed", "duration": 300},
            {"tool": "api", "status": "success", "duration": 80},
        ]

        consumed = []

        def source():
            for event in events:
                consumed.append(event)
                yield event

        result = first_failed_event(source())

        self.assertEqual(result, events[1])
        self.assertEqual(len(consumed), 2)


if __name__ == "__main__":
    unittest.main()
