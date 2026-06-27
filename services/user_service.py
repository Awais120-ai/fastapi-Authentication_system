from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.user import User
from schemas.user import UserCreate
from utils.security import hash_password, verify_password

def register_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, email: str, password_plain: str):
    db_user = db.query(User).filter(
        User.email == email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid Email"
        )

    if not verify_password(password_plain, db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid Password"
        )

    return db_user

def get_all_users(db: Session):
    return db.query(User).all()
