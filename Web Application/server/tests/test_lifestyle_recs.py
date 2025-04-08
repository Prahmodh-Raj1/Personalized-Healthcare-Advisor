from fastapi.testclient import TestClient
import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# Initialize TestClient with the correct argument
client = TestClient(app)

def test_lifestyle_recommendations_success():
    test_data = {
        "analysis": "Patient reports persistent fatigue and frequent headaches",
        "guidance": "Consider consulting a neurologist for headache evaluation"
    }
    response = client.post("/lifestyle", json=test_data)
    assert response.status_code == 200
    assert response.json() is not None
    assert len(response.json()) > 0

def test_empty_lifestyle_data():
    test_data = {
        "analysis": "",
        "guidance": ""
    }
    response = client.post("/lifestyle", json=test_data)
    assert response.status_code in [400, 422]  # Both are valid for invalid input

def test_partial_lifestyle_data():
    test_data = {
        "analysis": "Some analysis",
        "guidance": ""
    }
    response = client.post("/lifestyle", json=test_data)
    assert response.status_code in [400, 422]  # Both are valid for invalid input

def test_lifestyle_invalid_json():
    response = client.post(
        "/lifestyle",
        json={"invalid_key": "some data"}
    )
    assert response.status_code == 422

def test_lifestyle_invalid_method():
    response = client.get("/lifestyle")
    assert response.status_code == 405