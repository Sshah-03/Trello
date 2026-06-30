import pytest
from sqlalchemy.orm import Session

from app.models.user import User
from app.services.auth_service import login_user, register_user
from app.utils.security import verify_password
from app.schemas.user import UserCreate


class TestUserRegistration:
    """Test suite for user registration functionality."""

    def test_register_user_creates_new_user(self, db_session: Session):
        """Test that registering a user creates a new user in the database."""
        data = UserCreate(
            email="unit@example.com",
            password="TestPass1!",
            first_name="Unit",
            last_name="Tester"
        )

        user = register_user(data, db_session)

        assert user.id is not None
        assert user.email == "unit@example.com"
        assert user.first_name == "Unit"
        assert verify_password("TestPass1!", user.hashed_password)

    def test_register_user_raises_when_email_exists(self, db_session: Session):
        """Test that registering a duplicate email raises an exception."""
        data = UserCreate(
            email="duplicate@example.com",
            password="Pass123$",
            first_name="Duplicate",
            last_name="User"
        )
        register_user(data, db_session)

        with pytest.raises(Exception):
            register_user(data, db_session)


class TestUserLogin:
    """Test suite for user login functionality."""

    def test_login_user_returns_token(self, db_session: Session):
        """Test that logging in returns a valid JWT token."""
        data = UserCreate(
            email="login@example.com",
            password="LoginPass1!",
            first_name="Login",
            last_name="User"
        )
        register_user(data, db_session)

        token_response = login_user("login@example.com", "LoginPass1!", db_session)

        assert token_response["token_type"] == "bearer"
        assert "access_token" in token_response
