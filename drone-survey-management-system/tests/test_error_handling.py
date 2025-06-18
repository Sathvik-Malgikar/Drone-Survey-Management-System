import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    """Create a test client"""
    return TestClient(app)

def test_invalid_drone_id(client):
    """Test mission creation with invalid drone ID"""
    mission_data = {
        "name": "Invalid Test Mission",
        "drone_id": "nonexistent_drone",
        "config": {
            "altitude": 100,
            "pattern": "grid",
            "overlap_percentage": 70,
            "sensors": ["camera"],
            "data_collection_frequency": 3,
            "survey_area": [{"lat": 37.7749, "lng": -122.4194}],
            "waypoints": [{"lat": 37.7749, "lng": -122.4194}]
        }
    }
    
    response = client.post("/api/missions", json=mission_data)
    assert response.status_code == 404

def test_nonexistent_mission(client):
    """Test getting nonexistent mission"""
    response = client.get("/api/missions/nonexistent_mission_id")
    assert response.status_code == 404

def test_nonexistent_drone(client):
    """Test getting nonexistent drone"""
    response = client.get("/api/drones/nonexistent_drone_id")
    assert response.status_code == 404

def test_invalid_mission_creation(client):
    """Test mission creation with missing fields"""
    mission_data = {
        "name": "Incomplete Mission"
        # Missing drone_id and config
    }
    
    response = client.post("/api/missions", json=mission_data)
    assert response.status_code == 422  # Unprocessable Entity for validation errors

def test_invalid_config_format(client):
    """Test mission creation with invalid config format"""
    mission_data = {
        "name": "Invalid Config Mission",
        "drone_id": "test_drone_001",
        "config": "invalid_format"  # Invalid config
    }
    
    response = client.post("/api/missions", json=mission_data)
    assert response.status_code == 422  # Unprocessable Entity for validation errors