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
