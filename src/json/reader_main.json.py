import json

data = {"name": "Alice", "age": 30, "active": True, "score": None}


def main():
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
