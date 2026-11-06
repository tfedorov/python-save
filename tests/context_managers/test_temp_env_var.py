import os
import pytest


class TempEnvVar:
    def __init__(self, key: str, value: str) -> None:
        self.key = key
        self.value = value
        self._original = os.environ.get(self.key)

    def __enter__(self) -> "TempEnvVar":
        os.environ[self.key] = self.value
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self._original is None:
            os.environ.pop(self.key, None)
        else:
            os.environ[self.key] = self._original
        return True

def test_temp_env_var_success_set():
    input_key = "MY_TEST_KEY"
    input_value = "hello"
    os.environ.pop(input_key, None)

    with TempEnvVar(input_key, input_value):
        result: str = os.environ[input_key]

    expected: str = "hello"
    assert result == expected


def test_temp_env_var_success_cleanup():
    input_key = "MY_CLEANUP_KEY"
    os.environ.pop(input_key, None)

    with TempEnvVar(input_key, "temp"):
        pass

    result: bool = input_key in os.environ

    expected: bool = False
    assert result == expected


def test_temp_env_var_success_restore():
    input_key = "MY_RESTORE_KEY"
    os.environ[input_key] = "original"

    with TempEnvVar(input_key, "temporary"):
        pass

    result: str = os.environ.get(input_key, "")
    del os.environ[input_key]

    expected: str = "original"
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
