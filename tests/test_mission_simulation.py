from datetime import datetime
import pytest
from src.models import Mission
from src.enums import MissionStatus

class TestMissionSimulation:
    """Test mission simulation functionality"""
    
    @pytest.mark.asyncio
    async def test_mission_progress_simulation(self, sample_mission_config):
        """Test mission progress simulation"""
        mission = Mission(
            id="test_sim_mission",
            name="Simulation Test",
            organization_id="test_org",
            drone_id="test_drone",
            config=sample_mission_config,
            status=MissionStatus.PLANNED,
            created_at=datetime.now()
        )
        
        # Test mission status transitions
        assert mission.status == MissionStatus.PLANNED
        
        # Simulate starting
        mission.status = MissionStatus.STARTING
        assert mission.status == MissionStatus.STARTING
        
        # Simulate in progress
        mission.status = MissionStatus.IN_PROGRESS
        mission.progress_percentage = 50.0
        assert mission.progress_percentage == 50.0
        
        # Simulate completion
        mission.status = MissionStatus.COMPLETED
        mission.progress_percentage = 100.0
        assert mission.status == MissionStatus.COMPLETED
        assert mission.progress_percentage == 100.0