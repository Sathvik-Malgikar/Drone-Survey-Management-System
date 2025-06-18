def update_mission_status(mission, new_status):
    """Update the status of a mission."""
    mission.status = new_status

def calculate_progress_percentage(current, total):
    """Calculate the progress percentage."""
    if total <= 0:
        return 0
    return (current / total) * 100

def validate_coordinates(coordinates):
    """Validate a list of coordinates."""
    for coord in coordinates:
        if not isinstance(coord, Coordinate):
            raise ValueError("Invalid coordinate: must be an instance of Coordinate")
    return True

def format_mission_data(mission):
    """Format mission data for output."""
    return {
        "id": mission.id,
        "name": mission.name,
        "status": mission.status,
        "progress": mission.progress_percentage,
        "created_at": mission.created_at.isoformat(),
        "config": mission.config.to_dict()
    }