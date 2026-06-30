import pytest
from app.utils.security import hash_password, verify_password


class TestPasswordHashing:
    """Test suite for password hashing functionality."""

    def test_hash_password_returns_string(self):
        """Test that hash_password returns a string that differs from the original."""
        password = "MySecret123!"
        hashed = hash_password(password)

        assert isinstance(hashed, str)
        assert hashed != password


class TestPasswordVerification:
    """Test suite for password verification functionality."""

    def test_verify_password_success(self):
        """Test that verify_password returns True for correct password."""
        password = "AnotherSecret!"
        hashed = hash_password(password)

        assert verify_password(password, hashed) is True

    def test_verify_password_failure(self):
        """Test that verify_password returns False for incorrect password."""
        password = "MySecret123!"
        hashed = hash_password(password)

        assert verify_password("WrongPassword", hashed) is False
