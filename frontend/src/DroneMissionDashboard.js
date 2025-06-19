// Main Dashboard Component
import React from 'react';
import MissionPlanner from './components/MissionPlanner.js';
import FleetDashboard from './components/FleetDashboard.js';
import LiveMonitoring from './components/LiveMonitoring.js';
import SurveyReports from './components/SurveyReports.js';

export default function Dashboard() {
  return (
    <div className="p-4 grid grid-cols-1 md:grid-cols-2 gap-4 bg-gray-100 min-h-screen">
      <MissionPlanner />
      <FleetDashboard />
      <LiveMonitoring />
      <SurveyReports />
    </div>
  );
}

// MissionPlanner.js
import React from 'react';

export default function MissionPlanner() {
  return (
    <div className="bg-white rounded-2xl p-4 shadow-md">
      <h2 className="text-xl font-bold mb-2">Mission Planner</h2>
      <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Create New Mission</button>
    </div>
  );
}

// FleetDashboard.js
import React from 'react';

export default function FleetDashboard() {
  return (
    <div className="bg-white rounded-2xl p-4 shadow-md">
      <h2 className="text-xl font-bold mb-2">Fleet Dashboard</h2>
      <ul className="space-y-2">
        <li className="text-sm">🚁 Drone A - Battery: 78% - Status: In Mission</li>
        <li className="text-sm">🚁 Drone B - Battery: 95% - Status: Available</li>
      </ul>
    </div>
  );
}

// LiveMonitoring.js
import React, { useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

export default function LiveMonitoring() {
  useEffect(() => {
    // any map setup or WebSocket connection here
  }, []);

  return (
    <div className="bg-white rounded-2xl p-4 shadow-md">
      <h2 className="text-xl font-bold mb-2">Live Monitoring</h2>
      <div className="h-64">
        <MapContainer center={[51.505, -0.09]} zoom={13} className="h-full rounded">
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <Marker position={[51.505, -0.09]}>
            <Popup>Drone Location</Popup>
          </Marker>
        </MapContainer>
      </div>
      <p className="mt-2">Mission Progress: 60%</p>
      <div className="flex gap-2 mt-2">
        <button className="bg-yellow-500 text-white px-3 py-1 rounded hover:bg-yellow-600">Pause</button>
        <button className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700">Resume</button>
        <button className="bg-red-600 text-white px-3 py-1 rounded hover:bg-red-700">Abort</button>
      </div>
    </div>
  );
}

// SurveyReports.js
import React from 'react';

export default function SurveyReports() {
  return (
    <div className="bg-white rounded-2xl p-4 shadow-md">
      <h2 className="text-xl font-bold mb-2">Survey Reports</h2>
      <ul className="space-y-2 text-sm">
        <li>📊 Survey #1 - Duration: 15 min - Distance: 2.5km</li>
        <li>📊 Survey #2 - Duration: 22 min - Distance: 3.8km</li>
      </ul>
    </div>
  );
}
