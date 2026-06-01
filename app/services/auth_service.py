from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.user import UserCreate

from app.utils.security import (hash_password, verify_password)

from app.utils.jwt import create_access_token

# Authentication service for user registration and login
def register_user(
    data: UserCreate,
    db: Session
):

    existing_user = db.query(User).filter(User.email == data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(
        email=data.email,
        hashed_password=hash_password(data.password),
        first_name=data.first_name,
        last_name=data.last_name
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

# Login service for user authentication and token generation
def login_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        {"sub": str(user.id)}
    )

    return {"access_token": token, "token_type": "bearer"}