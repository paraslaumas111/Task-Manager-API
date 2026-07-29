from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import (
    create_new_task,
    edit_task,
    find_task,
    list_tasks,
    remove_task
)


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

TEMPORARY_OWNER_ID = 1

@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_all_tasks(
    db: Session = Depends(get_db)
):
    return list_tasks(
        db=db,
        owner_id=TEMPORARY_OWNER_ID
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = find_task(
        db=db,
        task_id=task_id,
        owner_id=TEMPORARY_OWNER_ID
    )
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The task was not found in the database"
        )
    return task


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):
    return create_new_task(
        db=db,
        task_data=task_data,
        owner_id=TEMPORARY_OWNER_ID
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = edit_task(
        db=db,
        task_id=task_id,
        task_data=task_data,
        owner_id=TEMPORARY_OWNER_ID
    )
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Couldn't find a task with this id"
        )
    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    delete = remove_task(
        db=db,
        task_id=task_id,
        owner_id=TEMPORARY_OWNER_ID
    )

    if not delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Couldn't delete since couldn't find this id in the database"
        )
