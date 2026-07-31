from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import oauth2_scheme
from app.core.security import verify_access_token
from app.database.session import get_db
from app.models.user import User
from app.repositories.user_repository import get_user_by_id


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:

    try:

        payload = verify_access_token(token)

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    user_id = payload.get("sub")

    if user_id is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    user = get_user_by_id(
        db=db,
        user_id=int(user_id)
    )

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    return user