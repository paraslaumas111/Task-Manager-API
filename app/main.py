from fastapi import FastAPI

from app.api.tasks import router as task_router

app = FastAPI(
    title="Task Management API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Task Management API!"
    }

@app.post("/")
def root():
    return {
        "msg": "Welcome to testing Post req on tmAPI!"
    }

app.include_router(task_router)