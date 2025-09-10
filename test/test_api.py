from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healt():
    response = client.get("/api/v1/healt")
    assert response.status_code ==200
    assert response.json()["status"] =="ok"

    