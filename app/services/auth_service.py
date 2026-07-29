from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password
)
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


def login_user(
    db: Session,
    email: str,
    password: str
) -> str | None:

    user = get_user_by_email(
        db=db,
        email=email
    )

    if user is None:
        return None

    password_is_valid = verify_password(
        plain_password=password,
        hashed_password=user.hashed_password
    )

    if not password_is_valid:
        return None

    return create_access_token(
        subject=str(user.id)
    )