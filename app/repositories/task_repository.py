from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(
    db: Session,
    task_data: TaskCreate,
    owner_id: int
) -> Task:

    task = Task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority.value,
        status=task_data.status.value,
        due_date=task_data.due_date,
        completed=task_data.completed,
        owner_id=owner_id
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task

def get_all_tasks(
    db: Session,
    owner_id: int,
    offset: int = 0,
    limit: int = 10
):

    statement = (
        select(Task)
        .where(
            Task.owner_id == owner_id
        )
        .offset(offset)
        .limit(limit)
    )

    result = db.execute(statement)

    return result.scalars().all()

def get_task_by_id(
    db: Session,
    task_id: int,
    owner_id: int
) -> Task | None:

    statement = select(Task).where(
        Task.id == task_id,
        Task.owner_id == owner_id
    )

    result = db.execute(statement)

    return result.scalar_one_or_none()

def update_task(
    db: Session,
    task: Task,
    task_data: TaskUpdate
) -> Task:

    update_data = task_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():

        if hasattr(value, "value"):
            value = value.value

        setattr(task, field, value)

    db.commit()

    db.refresh(task)

    return task

def delete_task(
    db: Session,
    task: Task
) -> None:

    db.delete(task)

    db.commit()