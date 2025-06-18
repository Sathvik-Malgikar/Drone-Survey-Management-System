from datetime import datetime
import pytest
from src.models import Drone, Mission, Coordinate
from src.enums import DroneStatus, MissionStatus, SurveyPattern

class TestCoordinate:
    """Test Coordinate data model functionality"""
    
    def test_coordinate_creation(self):
        coord = Coordinate(lat=37.7749, lng=-122.4194)
        assert coord.lat == 37.7749
        assert coord.lng == -122.4194

class TestDrone:
    """Test Drone data model functionality"""
    
    def test_drone_creation(self):
        drone = Drone(
            id="test_drone_001",
            name="Test Drone Alpha",
            model="DJI Test Pro",
            status=DroneStatus.AVAILABLE,
            battery_level=85,
            location=Coordinate(37.7749, -122.4194),
            organization_id="test_org_001",
            last_updated=datetime.now()
        )
        
        assert drone.id == "test_drone_001"
        assert drone.status == DroneStatus.AVAILABLE
        assert drone.battery_level == 85
        
        drone_dict = drone.to_dict()
        assert isinstance(drone_dict, dict)
        assert drone_dict["id"] == "test_drone_001"
        assert "last_updated" in drone_dict

class TestMission:
    """Test Mission data model functionality"""
    
    def test_mission_creation(self):
        mission = Mission(
            id="test_mission_001",
            name="Test Mission",
            organization_id="test_org_001",
            drone_id="test_drone_001",
            config=None,  # Assuming config is not required for this test
            status=MissionStatus.PLANNED,
            created_at=datetime.now()
        )
        
        assert mission.id == "test_mission_001"
        assert mission.status == MissionStatus.PLANNED
        assert mission.progress_percentage == 0.0
        
        mission_dict = mission.to_dict()
        assert isinstance(mission_dict, dict)
        assert mission_dict["name"] == "Test Mission"
        assert "config" in mission_dict