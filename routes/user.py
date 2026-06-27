from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from services import user_service

router = APIRouter()

@router.get("/profile")
def profile():
    return {
        "message": "Protected Route"
    }


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = user_service.get_all_users(db)
    return {
        "total_users": len(users),
        "users": [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
            for user in users
        ]
    }
