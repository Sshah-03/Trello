from app.utils.security import hash_password, verify_password


def test_hash_password_returns_string():
    password = "MySecret123!"
    hashed = hash_password(password)

    assert isinstance(hashed, str)
    assert hashed != password


def test_verify_password_success():
    password = "AnotherSecret!"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_verify_password_failure():
    password = "MySecret123!"
    hashed = hash_password(password)

    assert verify_password("WrongPassword", hashed) is False
