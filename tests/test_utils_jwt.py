from jose import jwt

from app.utils.jwt import create_access_token
from app.config import settings


class TestJWTUtility:
    """Test suite for JWT token utility functions."""

    def test_create_access_token_contains_subject_and_expiration(self):
        """Test that generated JWT token contains subject and expiration claims."""
        payload = {"sub": "123"}
        token = create_access_token(payload)

        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        assert decoded["sub"] == "123"
        assert "exp" in decoded
