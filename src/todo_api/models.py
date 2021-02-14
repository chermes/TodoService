"""Input / output model definitions for the API."""
from pydantic import BaseModel, Field


class User(BaseModel):
    """A simple user."""
    name: str = Field(description="User name. Best kept short.", max_length=20)
