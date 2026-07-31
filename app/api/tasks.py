from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.models.user import User
from app.services.current_user import get_current_user
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


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_all_tasks(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return list_tasks(
        db=db,
        owner_id=current_user.id,
        page=page,
        size=size
    )

@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = find_task(
        db=db,
        task_id=task_id,
        owner_id=current_user.id
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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_new_task(
        db=db,
        task_data=task_data,
        owner_id=current_user.id
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = edit_task(
        db=db,
        task_id=task_id,
        task_data=task_data,
        owner_id=current_user.id
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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    delete = remove_task(
        db=db,
        task_id=task_id,
        owner_id=current_user.id
    )

    if not delete:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Couldn't delete since couldn't find this id in the database"
        )
