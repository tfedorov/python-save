import unittest


# =========================
# Tasks to implement
# =========================

def build_prompt(system_message, user_message, *examples):
    examples = [f"EXAMPLE: {example}" for example in examples]
    examples_message=""
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
    #return {**defaults, **overrides}
    result = defaults.copy()
    result.update(overrides)
    return result


# =========================
# Tests
# =========================

class FunctionsArgsKwargsTestCase(unittest.TestCase):

    def test_build_prompt_without_examples(self):
        result = build_prompt(
            "You are helpful",
            "Explain Python"
        )

        expected = (
            "SYSTEM: You are helpful\n"
            "USER: Explain Python"
        )

        self.assertEqual(expected, result)

    def test_build_prompt_with_examples(self):
        result = build_prompt(
            "You are helpful",
            "Explain Python",
            "Scala map is like Python comprehension",
            "Scala Option is close to Optional"
        )

        expected = (
            "SYSTEM: You are helpful\n"
            "EXAMPLE: Scala map is like Python comprehension\n"
            "EXAMPLE: Scala Option is close to Optional\n"
            "USER: Explain Python"
        )

        self.assertEqual(expected, result)

    def test_create_tool_call_without_args(self):
        result = create_tool_call("summarize")

        expected = {
            "tool": "summarize",
            "args": {}
        }

        self.assertEqual(expected, result)

    def test_create_tool_call_with_args(self):
        result = create_tool_call(
            "search_logs",
            service="api",
            limit=10,
            level="error"
        )

        expected = {
            "tool": "search_logs",
            "args": {
                "service": "api",
                "limit": 10,
                "level": "error",
            }
        }

        self.assertEqual(expected, result)

    def test_merge_agent_config(self):
        defaults = {
            "model": "gpt",
            "temperature": 0.3,
            "retries": 1,
        }

        result = merge_agent_config(
            defaults,
            temperature=0.7,
            timeout=30
        )

        expected = {
            "model": "gpt",
            "temperature": 0.7,
            "retries": 1,
            "timeout": 30,
        }
        self.assertEqual(expected, result)

    def test_merge_agent_config_does_not_mutate_defaults(self):
        defaults = {
            "model": "gpt",
            "temperature": 0.3,
        }

        result = merge_agent_config(defaults, temperature=0.9)

        self.assertEqual(
            {"model": "gpt", "temperature": 0.3},
            defaults
        )

        self.assertEqual(
            {"model": "gpt", "temperature": 0.9},
            result
        )


if __name__ == "__main__":
    unittest.main()