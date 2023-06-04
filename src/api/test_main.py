from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

default_data = {
    "lastNumbersStored": {"a": 1, "b": 2},
    "sum": 3,
    "subtract": -1,
    "multiply": 2,
    "divide": 0.5,
    "power": 1,
}

def test_get_data():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == default_data

def test_post_data():
    response = client.post("/", json={"a": 3,"b":4})
    assert response.status_code == 201
    assert response.json() == {"lastNumbersStored": {"a": 3,"b": 4},
                                "sum": 7,
                                "subtract": 1,
                                "multiply": 12,
                                "divide": 0.75,
                                "power": 81
                                }

def test_put_data():
    response = client.post("/", json={"a": 3,"b":4})
    assert response.status_code == 201
    assert response.json() == {"lastNumbersStored": {"a": 3,"b": 4},
                                "sum": 7,
                                "subtract": 1,
                                "multiply": 12,
                                "divide": 0.75,
                                "power": 81
                                }

def test_delete_data():
    response = client.delete("/")
    assert response.status_code == 204
