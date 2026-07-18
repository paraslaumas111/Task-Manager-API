from fastapi import APIRouter, status

from app.schemas.task import TaskCreate, TaskResponse

from app.services.task_service import create_new_task, list_tasks, find_task


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def get_all_tasks():

    return list_tasks()


@router.get("/{ID}",)
def get_specific_task(ID: int):

    return find_task(ID)


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):
    return create_new_task(task)