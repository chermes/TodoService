"""Input / output model definitions for the API."""
import uuid
from enum import Enum
import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    """A simple user."""
    name: str = Field(description="User name. Best kept short.", max_length=20,
                      example="John")


class Priority(str, Enum):
    """ToDo Item priority."""
    low = "low"
    medium = "medium"
    high = "high"


class Status(str, Enum):
    """ToDo Item status."""
    backlog = "backlog"
    in_progress = "in_progress"
    done = "done"
    deleted = "deleted"


class Item(BaseModel):
    """A single ToDo item."""
    content: str = Field(description="Content of the ToDo item.", max_length=160,
                         example="lorem ipsum")
    priority: Priority
    status: Status
    status_change_date: datetime.datetime


class ItemResponse(Item):
    """Full ToDo item with id field."""
    item_id: uuid.UUID = Field(description="Item ID.")
