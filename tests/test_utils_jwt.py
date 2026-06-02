from jose import jwt

from app.utils.jwt import create_access_token
from app.config import settings


def test_create_access_token_contains_subject_and_expiration():
    payload = {"sub": "123"}
    token = create_access_token(payload)

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

    assert decoded["sub"] == "123"
    assert "exp" in decoded
