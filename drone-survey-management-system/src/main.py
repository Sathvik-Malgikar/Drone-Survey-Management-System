from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import DatabaseManager
from models import Drone, Mission
from schemas import DroneSchema, MissionSchema
from enums import DroneStatus, MissionStatus

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the database
db_manager = DatabaseManager("database.db")

@app.on_event("startup")
async def startup_event():
    await db_manager.init_db()

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

@app.post("/api/drones", response_model=DroneSchema)
async def create_drone(drone: DroneSchema):
    new_drone = Drone(**drone.dict())
    await db_manager.add_drone(new_drone)
    return new_drone

@app.get("/api/drones")
async def get_drones():
    drones = await db_manager.get_all_drones()
    return drones

@app.post("/api/missions", response_model=MissionSchema)
async def create_mission(mission: MissionSchema):
    new_mission = Mission(**mission.dict())
    await db_manager.add_mission(new_mission)
    return new_mission

@app.get("/api/missions")
async def get_missions():
    missions = await db_manager.get_all_missions()
    return missions

@app.get("/api/missions/{mission_id}", response_model=MissionSchema)
async def get_mission(mission_id: str):
    mission = await db_manager.get_mission(mission_id)
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission

# Additional routes and logic can be added here as needed.