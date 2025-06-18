import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    """Create a test client"""
    return TestClient(app)

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data

def test_get_fleet(client):
    """Test fleet endpoint"""
    response = client.get("/api/fleet")
    assert response.status_code == 200
    fleet_data = response.json()
    assert isinstance(fleet_data, list)

def test_get_missions(client):
    """Test missions endpoint"""
    response = client.get("/api/missions")
    assert response.status_code == 200
    missions_data = response.json()
    assert isinstance(missions_data, list)

def test_get_analytics(client):
    """Test analytics endpoint"""
    response = client.get("/api/analytics")
    assert response.status_code == 200
    analytics = response.json()
    
    required_fields = [
        "total_missions", "active_missions", 
        "fleet_utilization", "total_drones", "available_drones"
    ]
    for field in required_fields:
        assert field in analytics
        assert isinstance(analytics[field], (int, float))

def test_create_mission(client):
    """Test mission creation"""
    fleet_response = client.get("/api/fleet")
    fleet = fleet_response.json()
    available_drones = [d for d in fleet if d["status"] == "available"]
    
    if not available_drones:
        pytest.skip("No available drones for testing mission creation")
    
    mission_data = {
        "name": "Test Mission",
        "drone_id": available_drones[0]["id"],
        "config": {
            "altitude": 100,
            "pattern": "grid",
            "overlap_percentage": 70,
            "sensors": ["camera"],
            "data_collection_frequency": 3,
            "survey_area": [
                {"lat": 37.7749, "lng": -122.4194},
                {"lat": 37.7849, "lng": -122.4194},
                {"lat": 37.7849, "lng": -122.4094},
                {"lat": 37.7749, "lng": -122.4094}
            ],
            "waypoints": [
                {"lat": 37.7749, "lng": -122.4194},
                {"lat": 37.7799, "lng": -122.4144},
                {"lat": 37.7849, "lng": -122.4094}
            ]
        }
    }
    
    response = client.post("/api/missions", json=mission_data)
    assert response.status_code == 200
    
    mission = response.json()
    assert mission["name"] == "Test Mission"
    assert mission["drone_id"] == available_drones[0]["id"]
    assert "id" in mission

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