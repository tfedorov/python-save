import json
import pytest


def test_dumps_success():
    # Arrange
    input_data = {"name": "Alice", "age": 30}

    # Act
    # Key rule
    # json.dumps / json.loads work with strings.
    # json.dump / json.load work with files.
    result: str = json.dumps(input_data)

    # Assert
    expected: str = '{"name": "Alice", "age": 30}'
    assert result == expected


def test_loads_success():
    # Arrange
    input_string = '{"name": "Alice", "age": 30}'

    # Act
    # Key rule
    # json.dumps / json.loads work with strings.
    # json.dump / json.load work with files.
    result: dict = json.loads(input_string)

    # Assert
    expected: dict = {"name": "Alice", "age": 30}
    assert result == expected


def test_loads_success_type_mapping():
    # Arrange
    input_string = '{"active": true, "score": null, "items": [1, 2]}'

    # Act
    # Key rule
    # json.dumps / json.loads work with strings.
    # json.dump / json.load work with files.
    result: dict = json.loads(input_string)

    # Assert
    expected: dict = {"active": True, "score": None, "items": [1, 2]}
    assert result == expected


def test_dump_success(tmp_path):
    # Arrange
    input_data = {"name": "Alice", "age": 30}
    input_path = tmp_path / "data.json"

    # Act
    # Key rule
    # json.dumps / json.loads work with strings.
    # json.dump / json.load work with files.
    with open(input_path, "w") as f:
        json.dump(input_data, f)
    result: str = input_path.read_text()

    # Assert
    expected: str = '{"name": "Alice", "age": 30}'
    assert result == expected


def test_load_success(tmp_path):
    # Arrange
    input_path = tmp_path / "data.json"
    input_path.write_text("""\
{
  "name": "Alice",
  "age": 30
}""")

    # Act
    # Key rule
    # json.dumps / json.loads work with strings.
    # json.dump / json.load work with files.
    with open(input_path, "r") as f:
        result: dict = json.load(f)

    # Assert
    expected: dict = {"name": "Alice", "age": 30}
    assert result == expected


def test_dumps_success_pretty_print():
    # Arrange
    input_data = {"b": 2, "a": 1}

    # Act
    # Key rule
    # json.dumps / json.loads work with strings.
    # json.dump / json.load work with files.
    result: str = json.dumps(input_data, indent=2, sort_keys=True)

    # Assert
    expected: str = '{\n  "a": 1,\n  "b": 2\n}'
    assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
