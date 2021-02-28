"""Main entry point for the API service."""
from typing import List, Optional
import uuid
import datetime

from fastapi import FastAPI, status
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
    if coll.find_one(user.dict()) is None:
        coll.insert_one(user.dict())


@app.post("/item",
          tags=["items"])
def create_item(item: Item):
    """Create a new item."""
    coll = data_access.get_items_collection()

    item_dict = item.dict()
    item_dict["item_id"] = uuid.uuid4()

    tm_now = datetime.datetime.now().isoformat()
    item_dict["status_change_date"] = tm_now

    coll.insert_one(item_dict)


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
    print(status, agg_pipeline)

    agg_pipeline.append({
        "$project": {
            "_id": 0,
        }})

    res = coll.aggregate(agg_pipeline)

    res = list(res)
    print(res)

    items = [ItemResponse(**i) for i in res]

    return items


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, timeout_keep_alive=0)
