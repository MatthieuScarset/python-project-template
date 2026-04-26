"""Tests for MyPackage API."""

from fastapi.testclient import TestClient
from typing import Any


def test_root_endpoint(client: TestClient):
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "MyPackage API" in data["message"]
    assert "version" in data


def test_health_endpoint(client: TestClient):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "MyPackage" in data["service"]
    assert "components" in data


def test_custom_thing_endpoint(client: TestClient, lorem_ipsum: str):
    """Test the custom-thing endpoint."""
    payload = {"data": lorem_ipsum}
    response = client.post("/custom-thing", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"
    assert "message" in data


def test_custom_thing_empty_payload(client: TestClient):
    """Test custom-thing with empty payload."""
    payload = {"data": ""}
    response = client.post("/custom-thing", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"


def test_custom_thing_invalid_payload(client: TestClient):
    """Test custom-thing with invalid payload."""
    # Missing required 'data' field
    payload: dict[str, Any] = {}
    response = client.post("/custom-thing", json=payload)

    assert response.status_code == 422  # Validation error


def test_custom_thing_large_payload(client: TestClient):
    """Test custom-thing with large payload."""
    large_data = "line\n" * 1000
    payload = {"data": large_data}
    response = client.post("/custom-thing", json=payload)

    # Should still work or return validation error for max_length
    assert response.status_code in [200, 422]
