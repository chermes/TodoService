"""Main entry point for the API service."""
from typing import Optional, List

from fastapi import FastAPI
import uvicorn

from . import models

app = FastAPI()

@app.get("/users",
         response_model=List[models.User])
def get_users():
    """Return all available user names."""
    return []

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
