"""Test the main.py API endpoints."""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_users():
    """Check if we can get a list of users."""
    response = client.get("/users")
    assert response.status_code == 200
