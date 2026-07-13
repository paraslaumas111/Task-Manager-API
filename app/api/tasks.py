from fastapi import APIRouter, status

from app.schemas.task import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/")
def get_all_tasks():
    return {
        "Msg": "Get All Tasks"
    }

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    return {
        "message": "A new task created successfully",
        "task": task
    }

@router.get("/count")
def get_task_count():
    return {
        "count": 0
    }

@router.get("/health")
def health():
    return {
        "status": "Healthy"
    }