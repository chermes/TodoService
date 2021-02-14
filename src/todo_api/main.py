"""Main entry point for the API service."""
from typing import List

from fastapi import FastAPI
import uvicorn

from models import User

app = FastAPI()

@app.get("/users",
         response_model=List[User])
def get_users():
    """Return all available user names."""
    return []


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
