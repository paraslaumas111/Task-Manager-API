from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def get_all_tasks():
    return {
        "message": "Get all tasks"
    }


@router.post("/")
def create_task():
    return {
        "message": "Create a task"
    }


@router.get("/papa")
def get_all_tasks():
    return {
        "Yo": "Imma Hustler"
    }


@router.post("/mama")
def create_task():
    return {
        "message": "Imma Nurturer"
    }