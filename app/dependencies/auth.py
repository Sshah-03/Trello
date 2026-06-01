from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from app.database import get_db
from app.config import settings
from app.models.user import User

outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Get the current user from the token
def get_current_user(token: str = Depends(outh2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )
    # Decode the JWT token and get the user ID
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    # If the token is invalid, raise an exception
    except JWTError:
        raise credentials_exception
    
    # Query the database for the user with the given ID
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
    
    return user

