import pytest
from src.enums import DroneStatus, MissionStatus, SurveyPattern

class TestEnums:
    def test_drone_status_enum(self):
        assert DroneStatus.AVAILABLE == "available"
        assert DroneStatus.IN_MISSION == "in_mission"
        assert DroneStatus.MAINTENANCE == "maintenance"
        assert DroneStatus.OFFLINE == "offline"

    def test_mission_status_enum(self):
        assert MissionStatus.PLANNED == "planned"
        assert MissionStatus.IN_PROGRESS == "in_progress"
        assert MissionStatus.COMPLETED == "completed"
        assert MissionStatus.ABORTED == "aborted"

    def test_survey_pattern_enum(self):
        assert SurveyPattern.GRID == "grid"
        assert SurveyPattern.CROSSHATCH == "crosshatch"
        assert SurveyPattern.PERIMETER == "perimeter"
        assert SurveyPattern.WAYPOINT == "waypoint"