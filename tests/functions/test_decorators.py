import math
import time

import pytest
from functools import wraps
from typing import Callable, Any


def time_measure(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        before: float = time.perf_counter()
        result = func(*args, **kwargs)
        after: float = time.perf_counter()
        wrapper.last_duration = after - before
        return result

    wrapper.last_duration = 0.0
    return wrapper


def counter(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        wrapper.method_counter += 1
        return result

    wrapper.method_counter = 0
    return wrapper


def test_time_measure_2_calls():
    @time_measure
    def factor_decor(n: int) -> int:
        return math.factorial(n)

    factor_decor(5)
    result1: bool = factor_decor.last_duration
    factor_decor(100)
    result2: bool = factor_decor.last_duration

    assert result1 < result2


def test_counter_2_calls():
    @counter
    def double_decor(n: int) -> int:
        return n * 2

    input_n = 5

    double_decor(input_n)
    double_decor(input_n)

    result: int = double_decor.method_counter

    expected: int = 2
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
