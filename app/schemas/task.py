from datetime import date
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Pilu(str, Enum):
    kela = "23"
    ers = "84"
    HIGH = "50"

class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Task title"
    )

    description: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Task description"
    )

    priority: Priority

    pilu: Pilu

    due_date: date

    completed: bool = False

    notes: Optional[str] = Field(...,
                                 max_length=10)

class TaskResponse(BaseModel):
    id: int

    title: str

    description: str

    priority: Priority

    pilu: Pilu

    due_date: date

    completed: bool