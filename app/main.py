from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

app = FastAPI()


@app.get("/")
def home():
    return {"message": "hello world"}


@pytest.fixture()
def client():
    return TestClient(app)


def test_home(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello world"}
