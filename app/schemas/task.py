from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Status(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=5,
        max_length=150
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=500
    )

    priority: Priority

    status: Status = Status.TODO

    due_date: date

    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        default=None,
        min_length=5,
        max_length=150
    )

    description: Optional[str] = Field(
        default=None,
        min_length=5,
        max_length=500
    )

    priority: Optional[Priority] = None

    status: Optional[Status] = None

    due_date: Optional[date] = None

    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    id: int

    title: str

    description: str

    priority: Priority

    status: Status

    due_date: date

    completed: bool

    owner_id: int

    model_config = {
        "from_attributes": True
    }