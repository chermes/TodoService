from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(description="User name. Best kept short.", max_length=20)