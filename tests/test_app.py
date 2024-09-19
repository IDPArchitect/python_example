from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI"}

def test_read_item():
    response = client.get("/items/1?q=test_query")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "query": "test_query"}
