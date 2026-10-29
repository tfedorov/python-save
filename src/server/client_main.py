import requests


def main():
    response_post = requests.post(
        "http://127.0.0.1:8000/users_json",
        timeout=5,
        json={"name": "Taras", "age": 40}
    )

    response_post.raise_for_status()

    response_get = requests.get(
        "http://127.0.0.1:8000/users/",
        timeout=5,
    )
    print(response_get.status_code)  # 200
    print(response_get.json())  # {'id': 123, 'name': 'Alex'}


if __name__ == "__main__":
    main()
