import pytest


class SuppressError:
    def __init__(self, *exceptions: type[BaseException]) -> None:
        self.exceptions = exceptions

    def __enter__(self) -> "SuppressError":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            return True
        return False


def test_suppress_error_success():
    input_exception = ValueError

    with SuppressError(input_exception):
        raise ValueError("ignored")

    assert True


def test_suppress_error_failed_other():
    input_exception = ValueError

    with pytest.raises(TypeError):
        with SuppressError(input_exception):
            raise TypeError("not suppressed")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
