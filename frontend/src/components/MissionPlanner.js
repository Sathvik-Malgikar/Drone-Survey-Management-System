import React, { useState } from 'react';
import { MapContainer, TileLayer, useMapEvents, Polygon } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

function AreaSelector({ setPolygon }) {
  useMapEvents({
    click(e) {
      setPolygon((prev) => [...prev, [e.latlng.lat, e.latlng.lng]]);
    }
  });
  return null;
}

export default function MissionPlanner() {
  const [formData, setFormData] = useState({
    area: '',
    altitude: 100,
    overlap: 20,
    pattern: 'crosshatch'
  });
  const [polygon, setPolygon] = useState([]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (polygon.length < 3) {
      alert('Please mark at least 3 points to define the survey area.');
      return;
    }
    const payload = { ...formData, polygon };
    console.log('Mission Config:', payload);
    alert('Mission Created Successfully!');
  };

  return (
    <div className="bg-white rounded-2xl p-4 shadow-md">
      <h2 className="text-xl font-bold mb-4">Mission Planner</h2>

      <form className="space-y-4" onSubmit={handleSubmit}>
        <div>
          <label className="block text-sm font-medium">Survey Area Name</label>
          <input type="text" name="area" value={formData.area} onChange={handleChange}
            className="mt-1 block w-full rounded border border-gray-300 p-2" required />
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium">Flight Altitude (m)</label>
            <input type="number" name="altitude" value={formData.altitude} onChange={handleChange}
              className="mt-1 block w-full rounded border border-gray-300 p-2" required />
          </div>
          <div>
            <label className="block text-sm font-medium">Overlap (%)</label>
            <input type="number" name="overlap" value={formData.overlap} onChange={handleChange}
              className="mt-1 block w-full rounded border border-gray-300 p-2" required />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium">Pattern</label>
          <select name="pattern" value={formData.pattern} onChange={handleChange}
            className="mt-1 block w-full rounded border border-gray-300 p-2">
            <option value="crosshatch">Crosshatch</option>
            <option value="perimeter">Perimeter</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium">Define Survey Area</label>
          <p className="text-xs text-gray-500 mb-2">Click on the map to mark the boundary (min 3 points).</p>
          <div className="h-64 rounded border border-gray-300 overflow-hidden">
            <MapContainer center={[20.5937, 78.9629]} zoom={5} className="h-full">
              <TileLayer
                attribution='&copy; OpenStreetMap contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />
              <AreaSelector setPolygon={setPolygon} />
              {polygon.length > 2 && <Polygon positions={polygon} pathOptions={{ color: 'blue' }} />}
            </MapContainer>
          </div>
        </div>

        <button type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
          Create Mission
        </button>
      </form>
    </div>
  );
}
