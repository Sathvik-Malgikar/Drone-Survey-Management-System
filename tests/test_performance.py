import time
import concurrent.futures
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

class TestPerformance:
    def test_fleet_response_time(self, client):
        start_time = time.time()
        response = client.get("/api/fleet")
        end_time = time.time()
        
        assert response.status_code == 200
        assert (end_time - start_time) < 1.0

    def test_multiple_concurrent_requests(self, client):
        def make_request():
            response = client.get("/api/health")
            return response.status_code
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(10)]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        
        assert all(status == 200 for status in results)