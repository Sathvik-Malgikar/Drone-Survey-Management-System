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