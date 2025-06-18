from fastapi.testclient import TestClient
import pytest
from datetime import datetime
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_mission_config():
    return {
        "survey_area": [
            {"lat": 37.7749, "lng": -122.4194},
            {"lat": 37.7849, "lng": -122.4194},
            {"lat": 37.7849, "lng": -122.4094},
            {"lat": 37.7749, "lng": -122.4094}
        ],
        "altitude": 120.0,
        "pattern": "grid",
        "overlap_percentage": 75.0,
        "waypoints": [
            {"lat": 37.7749, "lng": -122.4194},
            {"lat": 37.7799, "lng": -122.4144},
            {"lat": 37.7849, "lng": -122.4094}
        ],
        "sensors": ["camera", "lidar"],
        "data_collection_frequency": 2
    }

def test_complete_mission_workflow(client, sample_mission_config):
    fleet_response = client.get("/api/fleet")
    assert fleet_response.status_code == 200
    fleet = fleet_response.json()
    available_drones = [d for d in fleet if d["status"] == "available"]

    if not available_drones:
        pytest.skip("No available drones for integration test")

    mission_data = {
        "name": "Integration Test Mission",
        "drone_id": available_drones[0]["id"],
        "config": sample_mission_config
    }

    create_response = client.post("/api/missions", json=mission_data)
    assert create_response.status_code == 200
    mission = create_response.json()
    mission_id = mission["id"]

    mission_response = client.get(f"/api/missions/{mission_id}")
    assert mission_response.status_code == 200

    analytics_response = client.get("/api/analytics")
    analytics = analytics_response.json()
    assert analytics["total_missions"] > 0

    # Simulate mission progress
    client.put(f"/api/missions/{mission_id}/start")
    assert client.get(f"/api/missions/{mission_id}").json()["status"] == "in_progress"

    client.put(f"/api/missions/{mission_id}/complete")
    assert client.get(f"/api/missions/{mission_id}").json()["status"] == "completed"