import pytest


def build_prompt(system_message, user_message, *examples):
    examples = [f"EXAMPLE: {example}" for example in examples]
    examples_message = ""
    if examples:
        examples_message = "\n".join(examples) + "\n"

    return (
        f"SYSTEM: {system_message}\n"
        f"{examples_message}"
        f"USER: {user_message}"
    )


def create_tool_call(tool_name, **kwargs):
    return {"tool": tool_name, "args": kwargs}


def merge_agent_config(defaults, **overrides):
    result = defaults.copy()
    result.update(overrides)
    return result


def test_build_prompt_success_without_examples():
    input_system_message = "You are helpful"
    input_user_message = "Explain Python"

    result: str = build_prompt(input_system_message, input_user_message)

    expected: str = (
        "SYSTEM: You are helpful\n"
        "USER: Explain Python"
    )
    assert result == expected


def test_build_prompt_success_with_examples():
    input_system_message = "You are helpful"
    input_user_message = "Explain Python"
    input_example1 = "Scala map is like Python comprehension"
    input_example2 = "Scala Option is close to Optional"

    result: str = build_prompt(
        input_system_message,
        input_user_message,
        input_example1,
        input_example2,
    )

    expected: str = (
        "SYSTEM: You are helpful\n"
        "EXAMPLE: Scala map is like Python comprehension\n"
        "EXAMPLE: Scala Option is close to Optional\n"
        "USER: Explain Python"
    )
    assert result == expected


def test_create_tool_call_success_without_args():
    input_tool_name = "summarize"

    result: dict = create_tool_call(input_tool_name)

    expected: dict = {
        "tool": "summarize",
        "args": {},
    }
    assert result == expected


def test_create_tool_call_success_with_args():
    input_tool_name = "search_logs"

    result: dict = create_tool_call(
        input_tool_name,
        service="api",
        limit=10,
        level="error",
    )

    expected: dict = {
        "tool": "search_logs",
        "args": {
            "service": "api",
            "limit": 10,
            "level": "error",
        },
    }
    assert result == expected


def test_merge_agent_config_success():
    input_defaults = {
        "model": "gpt",
        "temperature": 0.3,
        "retries": 1,
    }

    result: dict = merge_agent_config(
        input_defaults,
        temperature=0.7,
        timeout=30,
    )

    expected: dict = {
        "model": "gpt",
        "temperature": 0.7,
        "retries": 1,
        "timeout": 30,
    }
    assert result == expected


def test_merge_agent_config_success_immutable():
    input_defaults = {
        "model": "gpt",
        "temperature": 0.3,
    }

    merge_agent_config(input_defaults, temperature=0.9)

    result: dict = input_defaults

    expected: dict = {"model": "gpt", "temperature": 0.3}
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
