from datetime import datetime, timedelta
from jose import jwt

from app.config import settings

# Generate a JWT token
def create_access_token(data: dict):
    to_encode = data.copy()

    # Set the expiration time for the token
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Encode the token using the secret key and algorithm
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
