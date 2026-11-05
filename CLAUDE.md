# Python Save - Claude Instructions

## Writing Tests

Write unit tests for the `<function_name>` function in `<file_path>`. file_path should match file_path of method but in test section and test prefix

Goal:
Generate clean, readable, and maintainable pytest tests. Add 1 positive test.

Rules:
1. Use pytest.
2. Follow the AAA pattern:
   1. Arrange
   2. Act
   3. Assert
3. Add a blank line between Arrange, Act, and Assert sections.
4. Declare all input variables inside the test method.
5. Name input variables with the `input_` prefix.
   Example: `input_path`, `input_data`, `input_config`.
6. Name the actual result variable `result`.
7. Add a full type annotation to `result`.
   Example: `result: list[dict[str, str]]`.
8. Declare `expected` in the Assert section.
9. Add a full type annotation to `expected`.
10. In the positive test, use only one assert:
   `assert result == expected`
11. For exception cases, use `pytest.raises`.
12. For empty-return cases, use:
   `assert result == []`
13. For file-based functions, use the `tmp_path` fixture.
14. Write file content as triple-quoted multiline strings.
15. Do not use mocks.
16. Do not use monkeypatching.
17. Do not use module-level constants.
18. Keep tests small, independent, and fast.
19. If extra test dependencies are needed, propose them first.
20. Name tests using the pattern: test_<function_name>_<success|failed>[_<one_word_case>]. Use _success or _failed suffix. Add a [_<one_word_case>] case only when multiple tests share the same succes/failed direction.
21. Duplicate expected strings inside each test method. Do not extract shared strings to module-level constants or fixtures. Each test must be readable on its own as much as possible.
22. Add this block at the bottom:

```python
import pytest

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```
