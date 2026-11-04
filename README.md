# python-save

A personal Python practice repo. Covers core language topics and includes a small FastAPI server.

## What's inside

**`src/`** - source code:
- `json/reader_main.json.py` - JSON serialization examples (`dumps`, `loads`, `dump`, `load`)
- `server/server_main.py` - FastAPI server with in-memory user storage
- `server/client_main.py` - HTTP client for the server

**`tests/`** - pytest test files organized by topic:
- `json/json_reader.py` - JSON module (`dumps`, `loads`, `dump`, `load`, pretty print)
- `test_dict.py` - dicts, lists, sets
- `test_collections_module.py`, `test_collection_n7.py` - `Counter`, `defaultdict`, `deque`
- `test_dataclass_agent.py` - Python dataclasses
- `test_types.py` - type hints and typing module
- `test_generator_n8.py` - generators and lazy evaluation
- `test_functions.py` - args, kwargs, function patterns
- `test_two_arrary.py` - LeetCode-style array problems

## Run tests

```bash
uv run pytest tests/
```

## Run the server

```bash
uv run uvicorn src.server.server_main:app --reload
```

Server starts at `http://127.0.0.1:8000`.

## Dependency management

This project uses [uv](https://docs.astral.sh/uv/) - a fast Python package manager.

```bash
uv sync                    # install all dependencies from uv.lock
uv add <package>           # add a new dependency
uv add --dev <package>     # add a dev-only dependency
```

## Requirements

- Python 3.12+
- uv
