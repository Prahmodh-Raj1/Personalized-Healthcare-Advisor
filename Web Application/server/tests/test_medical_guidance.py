from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_medical_guidance_success():
    test_analysis = "Patient reports persistent fatigue and frequent headaches"
    response = client.post(
        "/med_guidance",
        json={"analysis": test_analysis}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert len(response.json()) > 0

def test_empty_analysis():
    response = client.post(
        "/med_guidance",
        json={"analysis": ""}
    )
    assert response.status_code == 400

def test_guidance_invalid_json():
    response = client.post(
        "/med_guidance",
        json={"invalid_key": "some analysis"}
    )
    assert response.status_code == 422

def test_guidance_invalid_method():
    response = client.get("/med_guidance")
    assert response.status_code == 405