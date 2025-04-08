from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_symptoms_analysis_success():
    response = client.post(
        "/symptoms",
        json={"symptoms": "I have been experiencing persistent fatigue and frequent headaches"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert len(response.json()) > 0

def test_empty_symptoms():
    response = client.post(
        "/symptoms",
        json={"symptoms": ""}
    )
    assert response.status_code == 400

def test_symptoms_invalid_json():
    response = client.post(
        "/symptoms",
        json={"invalid_key": "some symptoms"}
    )
    assert response.status_code == 422

def test_symptoms_invalid_method():
    response = client.get("/symptoms")
    assert response.status_code == 405