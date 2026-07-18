from app.schemas.task import TaskCreate

# Temporary in-memory storage
tasks = []

def get_all_tasks():
    return tasks

def get_task_by_id(Id: int):
    for i in tasks:
        if i["id"] == Id:
            return i
    return None

def create_task(task: TaskCreate):

    task_data = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "pilu": task.pilu,
        "due_date": task.due_date,
        "completed": task.completed
    }

    tasks.append(task_data)

    return task_data