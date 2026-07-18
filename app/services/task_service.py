from app.schemas.task import TaskCreate
from app.repositories.task_repository import create_task, get_all_tasks, get_task_by_id

def list_tasks():
    return get_all_tasks()

def find_task(ID: int):
    return get_task_by_id(ID)

def create_new_task(task: TaskCreate):

    # Business rules go here

    return create_task(task)