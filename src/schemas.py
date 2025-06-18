from pydantic import BaseModel
from typing import List, Optional

class Coordinate(BaseModel):
    lat: float
    lng: float

class MissionConfig(BaseModel):
    survey_area: List[Coordinate]
    altitude: float
    pattern: str
    overlap_percentage: float
    waypoints: List[Coordinate]
    sensors: List[str]
    data_collection_frequency: int

class Drone(BaseModel):
    id: str
    name: str
    model: str
    status: str
    battery_level: int
    location: Coordinate
    organization_id: str
    last_updated: str

class Mission(BaseModel):
    id: str
    name: str
    organization_id: str
    drone_id: str
    config: MissionConfig
    status: str
    created_at: str
    progress_percentage: Optional[float] = 0.0

class HealthCheckResponse(BaseModel):
    status: str
    timestamp: str

class FleetResponse(BaseModel):
    drones: List[Drone]

class MissionResponse(BaseModel):
    mission: Mission

class AnalyticsResponse(BaseModel):
    total_missions: int
    active_missions: int
    fleet_utilization: float
    total_drones: int
    available_drones: int