from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.tasks import router as task_router
from app.api.auth import router as auth_router  
from app.core.config import settings
from app.database.session import get_db


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
        "ENVIRONMENT": f"The working environment is: {settings.environment}!",
        "debug": settings.debug
    }

@app.get("/debug/database")
def test_database(db: Session = Depends(get_db)):

    result = db.execute(
        text("SELECT count(*) FROM users")
    )

    return {
        "user_count": result.scalar()
    }

app.include_router(task_router)
app.include_router(auth_router)