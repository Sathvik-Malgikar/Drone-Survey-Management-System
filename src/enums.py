class DroneStatus(str):
    AVAILABLE = "available"
    IN_MISSION = "in_mission"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"

class MissionStatus(str):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ABORTED = "aborted"

class SurveyPattern(str):
    GRID = "grid"
    CROSSHATCH = "crosshatch"
    PERIMETER = "perimeter"
    WAYPOINT = "waypoint"