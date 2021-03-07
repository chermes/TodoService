"""Test the main.py API endpoints."""
import pytest
from fastapi import status
from fastapi.testclient import TestClient
import mongomock

import main

client = TestClient(main.app)


@pytest.fixture
def patch_mongo(monkeypatch):
    """Patch the get_database method in the data_access."""
    mock_db = mongomock.MongoClient().todo_database

    def fake_get_db():
        return mock_db

    monkeypatch.setattr(main.data_access, "get_db", fake_get_db)


def test_users(patch_mongo):
    """Check if we can add and get a list of users."""
    user_list = [
        {"name": "John"},
        {"name": "Sarah"},
        {"name": "Paula"},
    ]
    for user in user_list:
        response = client.put("/user", json=user)
        assert response.status_code == status.HTTP_201_CREATED
    # insert last one again (test overwrite)
    response = client.put("/user", json=user_list[-1])
    assert response.status_code == status.HTTP_201_CREATED

    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    assert len(msg) == len(user_list)


def test_delete_user(patch_mongo):
    """Deletes users from the system."""
    user_list = [
        {"name": "John"},
        {"name": "Sarah"},
        {"name": "Paula"},
    ]
    item_list = [
        {
            "content": "lorem ipsum",
            "priority": "high",
            "status": "backlog",
            "users": ["John"],
        },
        {
            "content": "lorem ipsum",
            "priority": "high",
            "status": "in_progress",
            "users": ["John", "Sarah"],
        }
    ]

    for user in user_list:
        response = client.put("/user", json=user)
        assert response.status_code == status.HTTP_201_CREATED
    for item in item_list:
        reponse = client.post("/item", json=item)
        assert reponse.status_code == status.HTTP_200_OK

    response = client.delete("/users/John")
    assert response.status_code == status.HTTP_200_OK

    # check if the user has been deleted
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    assert "John" not in [m["name"] for m in msg]

    # check if the corresponding items have been deleted as well
    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    for item in msg:
        assert len(item["users"]) > 0
        assert "John" not in item["users"]


def test_delete_user_non_existent(patch_mongo):
    """Test to delete a non-exist user."""
    response = client.delete("/users/John")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_items_create(patch_mongo):
    """Check if we can create and get a list of items."""
    # create a user, first
    response = client.put("/user",
                          json={"name": "John"})
    assert response.status_code == status.HTTP_201_CREATED

    item_list = [
        {
            "content": "lorem ipsum",
            "priority": "high",
            "status": "backlog",
            "users": ["John"],
        },
        {
            "content": "lorem ipsum",
            "priority": "high",
            "status": "in_progress",
            "users": ["John"],
        },
        {
            "content": "lorem ipsum",
            "priority": "high",
            "status": "done",
            "users": ["John"],
        },
    ]

    for item in item_list:
        reponse = client.post("/item", json=item)
        assert reponse.status_code == status.HTTP_200_OK

    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    assert len(msg) == len(item_list)

    response = client.get("/items?status=backlog")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    assert len(msg) == 1
