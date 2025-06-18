import pytest
from fastapi.testclient import TestClient
from main import app

class TestWebSocketFunctionality:
    """Test WebSocket connections"""

    def test_websocket_connection(self, client):
        """Test WebSocket connection establishment"""
        with client.websocket_connect("/ws/missions") as websocket:
            # Test connection
            websocket.send_text("test message")
            data = websocket.receive_text()
            assert "Received: test message" in data

    def test_websocket_message_handling(self, client):
        """Test WebSocket message handling"""
        with client.websocket_connect("/ws/missions") as websocket:
            websocket.send_text("Hello, WebSocket!")
            response = websocket.receive_text()
            assert response == "Received: Hello, WebSocket!"  # Adjust based on actual response logic

    def test_websocket_connection_close(self, client):
        """Test WebSocket connection closure"""
        with client.websocket_connect("/ws/missions") as websocket:
            websocket.send_text("Close connection")
            websocket.close()
            assert websocket.client_state == "CLOSED"  # Check if the connection is closed properly