from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import (
    TokenResponse,
    UserCreate,
    UserResponse
)
from app.services.auth_service import (
    login_user,
    register_user
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    user = register_user(
        db=db,
        user_data=user_data
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered"
        )

    return user


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    email: str,
    password: str,
    db: Session = Depends(get_db)
):

    access_token = login_user(
        db=db,
        email=email,
        password=password
    )

    if access_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }