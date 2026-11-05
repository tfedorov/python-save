from typing import Callable, Any

import pytest


def registration() -> Callable:
    registry: list[Callable] = []

    def _register(func: Callable) -> Callable:
        registry.append(func)
        return func

    _register.all = registry  # type: ignore[attr-defined]
    return _register


def test_register_success():
    register: Callable[..., Any] = registration()

    @register
    def greet(what) -> str:
        return "hello" + what

    @register
    def farewell() -> str:
        return "bye"

    result: list[str] = [f.__name__ for f in register.all]

    expected: list[str] = ["greet", "farewell"]
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
