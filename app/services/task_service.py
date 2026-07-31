from sqlalchemy.orm import Session

from app.repositories.task_repository import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
    update_task
)
from app.schemas.task import TaskCreate, TaskUpdate

def create_new_task(
    db: Session,
    task_data: TaskCreate,
    owner_id: int
):
    return create_task(
        db=db,
        task_data=task_data,
        owner_id=owner_id
    )

def list_tasks(
    db: Session,
    owner_id: int,
    page: int = 1,
    size: int = 10
):

    offset = (page - 1) * size

    return get_all_tasks(
        db=db,
        owner_id=owner_id,
        offset=offset,
        limit=size
    )

def find_task(
    db: Session,
    task_id: int,
    owner_id: int
):
    return get_task_by_id(
        db=db,
        task_id=task_id,
        owner_id=owner_id
    )

def edit_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate,
    owner_id: int
):
    task = get_task_by_id(
        db=db,
        task_id=task_id,
        owner_id=owner_id
    )

    if task is None:
        return None

    return update_task(
        db=db,
        task=task,
        task_data=task_data
    )

def remove_task(
    db: Session,
    task_id: int,
    owner_id: int
):
    task = get_task_by_id(
        db=db,
        task_id=task_id,
        owner_id=owner_id
    )

    if task is None:
        return None

    delete_task(
        db=db,
        task=task
    )

    return True