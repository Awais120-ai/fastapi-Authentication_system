from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.user import UserCreate, UserLogin
from services import user_service
from utils.security import create_access_token

router = APIRouter()

@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    user_service.register_user(db, user)
    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = user_service.authenticate_user(
        db, user.email, user.password
    )
    token = create_access_token(
        {"sub": db_user.email}
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }
