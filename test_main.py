from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_data():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"responsibility": "Placeholder"}

def test_post_data():
    response = client.post("/", json={"responsibility": "Test"})
    assert response.status_code == 201
    assert response.json() == {"responsibility": "Test"}

def test_put_data():
    response = client.put("/", json={"responsibility": "Test"})
    assert response.status_code == 200
    assert response.json() == {"responsibility": "Test"}

def test_delete_data():
    response = client.delete("/")
    assert response.status_code == 204
    assert response.content == b'{}'

