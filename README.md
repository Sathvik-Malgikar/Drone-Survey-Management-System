# Drone Survey Management System

## 🚁 Overview

This project focuses on the mission management and reporting aspects of drone operations, providing a comprehensive solution for:

- **Mission Planning**: Define survey areas, flight paths, and data collection parameters
- **Fleet Management**: Monitor drone inventory and real-time status across organizations
- **Mission Monitoring**: Track real-time flight progress with map visualization
- **Survey Analytics**: Generate comprehensive reports and analytics

> **Note**: Live video feeds, actual data collection (images/videos), and map/model generation are outside the project scope.

## ✨ Key Features

### 🎯 Mission Planning and Configuration
- Define survey areas and flight paths
- Configure flight altitudes, waypoints, and routes
- Set data collection parameters (frequency, sensors)
- Support for advanced survey patterns (crosshatch, perimeter)
- Mission-specific parameter configuration (altitude, overlap percentage)

### 📊 Fleet Visualization and Management Dashboard
- Organization-wide drone inventory display
- Real-time drone status monitoring (available, in-mission)
- Battery levels and vital statistics tracking
- Fleet coordination across multiple sites

### 🗺️ Real-time Mission Monitoring Interface
- Interactive map visualization of drone flight paths
- Mission progress tracking (% complete, ETA)
- Live mission status updates (starting, in progress, completed, aborted)
- Mission control actions (pause, resume, abort)

### 📈 Survey Reporting and Analytics Portal
- Comprehensive survey summaries
- Individual flight statistics (duration, distance, coverage)
- Organization-wide survey analytics
- Historical mission data and trends

## Project Structure
```
drone-survey-management-system
├── frontend
├── src
│   ├── main.py          # Entry point for the application
│   ├── database.py      # Database management and operations
│   ├── models.py        # Data models for drones and missions
│   ├── schemas.py       # Pydantic schemas for data validation
│   ├── enums.py         # Enumerations for statuses and patterns
│   ├── utils.py         # Utility functions
│   └── __init__.py      # Package initialization
├── tests
│   ├── test_api.py      # Unit tests for API endpoints
│   ├── test_database.py  # Tests for database operations
│   ├── test_models.py    # Tests for data models
│   ├── test_enums.py     # Tests for enumerations
│   ├── test_error_handling.py # Tests for error handling
│   ├── test_mission_simulation.py # Tests for mission simulation
│   ├── test_websocket.py  # Tests for WebSocket functionality
│   ├── test_performance.py # Performance tests
│   └── test_integration.py # Integration tests
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Sathvik-Malgikar/drone-survey-management-system.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
uvicorn src.main:app --reload
```
This will start the FastAPI server, and you can access the API at `http://localhost:8000`.

## Testing
To run the tests, use the following command:
```
pytest
```
This will execute all the tests in the `tests` directory.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.