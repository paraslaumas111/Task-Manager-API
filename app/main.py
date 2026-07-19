from fastapi import FastAPI
from app.api.tasks import router as task_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

@app.get("/")
def root():
    return {
        "message": f"Welcome to the {settings.app_name}!"
    }

@app.get("/debug")
def root():
    return {
        "papad": f"Papad ka size hai: {settings.papad}!",
        "debug": settings.debug
    }

app.include_router(task_router)