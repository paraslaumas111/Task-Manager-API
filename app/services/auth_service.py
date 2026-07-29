from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user_repository import (
    create_user,
    get_user_by_email
)
from app.schemas.user import UserCreate

def register_user(
    db: Session,
    user_data: UserCreate
):
    existing_user = get_user_by_email(
        db=db,
        email=user_data.email
    )

    if existing_user is not None:
        return None

    hashed_password = hash_password(
        user_data.password
    )

    return create_user(
        db=db,
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )