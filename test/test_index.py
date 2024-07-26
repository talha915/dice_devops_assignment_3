from fastapi.testclient import TestClient   # type: ignore
from app.index import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def get_user():
    response = client.get("/user")
    assert response.status_code == 200
    assert response.json() == {"user": "Talha Zafar"}