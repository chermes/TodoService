"""Main entry point for the API service."""
from typing import List

from fastapi import FastAPI, status
import uvicorn

from models import User
import data_access

app = FastAPI()

@app.get("/users",
         response_model=List[User])
def get_users():
    """Return all available user names."""
    coll = data_access.get_user_collection()
    users = [User(**u) for u in coll.find()]
    return users


@app.put("/user",
         responses={
             status.HTTP_201_CREATED: {"description": "user has been added."},
         },
         status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    """Create a user in the system."""
    coll = data_access.get_user_collection()
    if coll.find_one(user.dict()) is None:
        coll.insert_one(user.dict())

    return status.HTTP_201_CREATED


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
