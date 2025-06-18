class Coordinate:
    """Data class for representing a geographical coordinate."""
    
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def to_dict(self):
        """Convert the Coordinate instance to a dictionary."""
        return {"lat": self.lat, "lng": self.lng}


class Drone:
    """Data class for representing a drone."""
    
    def __init__(self, id: str, name: str, model: str, status: str, battery_level: int, location: Coordinate, organization_id: str, last_updated: datetime):
        self.id = id
        self.name = name
        self.model = model
        self.status = status
        self.battery_level = battery_level
        self.location = location
        self.organization_id = organization_id
        self.last_updated = last_updated

    def to_dict(self):
        """Convert the Drone instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "status": self.status,
            "battery_level": self.battery_level,
            "location": self.location.to_dict(),
            "organization_id": self.organization_id,
            "last_updated": self.last_updated.isoformat()
        }


class Mission:
    """Data class for representing a mission."""
    
    def __init__(self, id: str, name: str, organization_id: str, drone_id: str, config: dict, status: str, created_at: datetime, progress_percentage: float = 0.0):
        self.id = id
        self.name = name
        self.organization_id = organization_id
        self.drone_id = drone_id
        self.config = config
        self.status = status
        self.created_at = created_at
        self.progress_percentage = progress_percentage

    def to_dict(self):
        """Convert the Mission instance to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "organization_id": self.organization_id,
            "drone_id": self.drone_id,
            "config": self.config,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "progress_percentage": self.progress_percentage
        }