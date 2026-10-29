from collections import defaultdict

import uvicorn
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


memory_users = {}


@app.get("/")
def health():
    return {"status": "ok"}


@app.get("/users")
def get_user():
    return memory_users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return memory_users.get(user_id)


@app.post("/users")
def create_user(
        name: str = Form(),
        age: int = Form()
):
    user = {"name": name, "age": age}
    memory_users.update({len(memory_users) + 1: user})
    return user


@app.post("/users_json")
def create_user(user: User):
    memory_users.update({len(memory_users) + 1: user})
    return user


def main():
    uvicorn.run(
        "server_main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    main()
