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


def test_create_empty_user(patch_mongo):
    """Try to create an empty user name (should fail)."""
    user = {
        "name": ""
    }

    response = client.put("/user", json=user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


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
        response = client.post("/item", json=item)
        assert response.status_code == status.HTTP_200_OK

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

    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1

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
        response = client.post("/item", json=item)
        assert response.status_code == status.HTTP_200_OK

    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    assert len(msg) == len(item_list)

    response = client.get("/items?status=backlog")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    assert len(msg) == 1

    response = client.get("/items?ignore_user=John")
    assert response.status_code == status.HTTP_200_OK
    msg = response.json()
    assert len(msg) == 0


def test_items_create_no_user(patch_mongo):
    """Check if we can create an item without a user."""
    item = {
        "content": "lorem ipsum",
        "priority": "high",
        "status": "backlog",
        "users": ["John"],
    }

    response = client.post("/item", json=item)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_items_create_empty_user(patch_mongo):
    """Check if we can create an item without a user."""
    item = {
        "content": "lorem ipsum",
        "priority": "high",
        "status": "backlog",
        "users": [],
    }

    response = client.post("/item", json=item)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_items_create_empty_content(patch_mongo):
    """Check if we can create an item with no content."""
    # create a user, first
    response = client.put("/user",
                          json={"name": "John"})
    assert response.status_code == status.HTTP_201_CREATED

    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1

    item = {
        "content": "",
        "priority": "high",
        "status": "backlog",
        "users": ["John"],
    }
    response = client.post("/item", json=item)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_items_delete(patch_mongo):
    """Check if we can delete an items."""
    # create a user, first
    response = client.put("/user",
                          json={"name": "John"})
    assert response.status_code == status.HTTP_201_CREATED

    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1

    item = {
        "content": "lorem ipsum",
        "priority": "high",
        "status": "backlog",
        "users": ["John"],
    }
    response = client.post("/item", json=item)
    assert response.status_code == status.HTTP_200_OK

    # get the items back enriched with an ID
    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    item_list = response.json()

    # delete the first item
    response = client.delete("/items/" + item_list[0]["item_id"])
    assert response.status_code == status.HTTP_200_OK

    # check if the item has been deleted
    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    item_list = response.json()
    assert not item_list


def test_items_status_update(patch_mongo):
    """Check if we can update the status of an item."""
    # create a user, first
    response = client.put("/user",
                          json={"name": "John"})
    assert response.status_code == status.HTTP_201_CREATED

    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1

    item = {
        "content": "lorem ipsum",
        "priority": "high",
        "status": "backlog",
        "users": ["John"],
    }
    response = client.post("/item", json=item)
    assert response.status_code == status.HTTP_200_OK

    # get the item back enriched by an ID
    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    item = response.json()[0]

    # update the status
    response = client.post("/items/" + item["item_id"] + "/status/in_progress")
    assert response.status_code == status.HTTP_200_OK
    #
    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    item = response.json()[0]
    assert item["status"] == "in_progress"

    response = client.post("/items/" + item["item_id"] + "/status/done")
    assert response.status_code == status.HTTP_200_OK
    #
    response = client.get("/items")
    assert response.status_code == status.HTTP_200_OK
    item = response.json()[0]
    assert item["status"] == "done"
