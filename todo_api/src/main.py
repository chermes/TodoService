"""Main entry point for the API service."""
from typing import List, Optional
import uuid
import datetime

from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from models import User, Item, ItemResponse, Status
import data_access

app = FastAPI(
    title="ToDo Service API",
    description="Provides backend access to the ToDo items.",
    version="0.1",
    openapi_tags=[
        {
            "name": "users",
            "description": "User management.",
        },
        {
            "name": "items",
            "description": "ToDo items.",
        },
    ]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users",
         response_model=List[User],
         tags=["users"])
def get_users():
    """Return all available user names."""
    coll = data_access.get_user_collection()
    users = [User(**u) for u in coll.find()]
    return users


@app.put("/user",
         responses={
             status.HTTP_201_CREATED: {"description": "user has been added."},
         },
         status_code=status.HTTP_201_CREATED,
         tags=["users"])
def create_user(user: User):
    """Create a user in the system."""
    coll = data_access.get_user_collection()

    if user.name == "":
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            "User name must not be empty.")

    if coll.find_one(user.dict()) is None:
        coll.insert_one(user.dict())


@app.delete("/users/{name}",
            tags=["users"])
def delete_user(name: str):
    """Delete user with the given name.
    This deletes also messages where only this user has been assigned.
    """
    coll_users = data_access.get_user_collection()
    coll_items = data_access.get_items_collection()

    # check if user name exists at all
    elem = coll_users.find_one({"name": name})
    if elem is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f"Could not find the user name {name}.")

    # get all items which contain this user -> update/delete
    items = coll_items.find({"users": name})
    for item in items:
        item["users"].remove(name)
        if len(item["users"]) > 0:
            # update uses in this item
            coll_items.update_one(
                {
                    "_id": item["_id"]
                },
                {
                    "$set": {
                        "users": item["users"]
                    }
                })
        else:
            # delete this item (no user left)
            coll_items.delete_one({"_id": item["_id"]})

    # delete user
    coll_users.delete_one({"name": name})


@app.post("/item",
          tags=["items"])
def create_item(item: Item):
    """Create a new item."""
    coll_users = data_access.get_user_collection()
    coll_items = data_access.get_items_collection()

    if not item.users:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            "Empty user list not allowed.")

    if not item.content:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            "No description / content given.")

    for user_name in item.users:
        if coll_users.find_one({"name": user_name}) is None:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                f"User {user_name} not exists in the user list.")

    item_dict = item.dict()
    item_dict["item_id"] = uuid.uuid4()

    tm_now = datetime.datetime.now().isoformat()
    item_dict["status_change_date"] = tm_now

    coll_items.insert_one(item_dict)


@app.get("/items",
         response_model=List[ItemResponse],
         tags=["items"])
def get_items(status: Optional[Status] = None):
    """Return ToDo items."""
    coll = data_access.get_items_collection()
    agg_pipeline = []

    if status is not None:
        agg_pipeline.append({
            "$match": {
                "status": str(status).split(".")[1]
            }
        })

    agg_pipeline.append({
        "$project": {
            "_id": 0,
        }})

    res = list(coll.aggregate(agg_pipeline))

    # update status hint
    for item in res:
        if item["status"] == Status.backlog:
            item["status_next"] = Status.in_progress
        elif item["status"] == Status.in_progress:
            item["status_prev"] = Status.backlog
            item["status_next"] = Status.done
        elif item["status"] == Status.done:
            item["status_prev"] = Status.in_progress

    items = [ItemResponse(**i) for i in res]

    return items


@app.delete("/items/{item_id}",
            tags=["items"])
def delete_item(item_id: uuid.UUID):
    """Delete a ToDo item in the database."""
    coll_items = data_access.get_items_collection()

    item = coll_items.find_one({"item_id": item_id})
    if item is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"Could not find the item with id {item_id}")

    coll_items.delete_one({"item_id": item_id})


@app.post("/items/{item_id}/status/{status}",
          tags=["items"])
def update_status(item_id: uuid.UUID, status: Status):
    """Update the status of an item."""
    coll_items = data_access.get_items_collection()

    tm_now = datetime.datetime.now().isoformat()
    coll_items.update_one(
        {
            "item_id": item_id
        },
        {
            "$set": {
                "status": status,
                "status_change_date": tm_now,
            }
        })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, timeout_keep_alive=0)
