from fastapi import APIRouter, status

from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):

    return {
        "id": 1,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "pilu": task.pilu,
        "due_date": task.due_date,
        "completed": task.completed
    }