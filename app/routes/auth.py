from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.schemas.user import (UserCreate, UserResponse)
from app.schemas.auth import (TokenResponse, LoginSchema)
from app.services.auth_service import (register_user, login_user)

# Router for authentication-related endpoints
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


# Endpoint for user registration
@router.post("/register", response_model=UserResponse)
def register(data: UserCreate, db: Session = Depends(get_db)):
    user = register_user(data, db)
    return user

# Endpoint for user login and token generation
@router.post("/login", response_model=TokenResponse)
def login(data: LoginSchema, db: Session = Depends(get_db)):    
    token = login_user(data.email, data.password, db)
    return token
