import pytest

LOGIN_TEST_CASES = [
    pytest.param(
        {
            "username": "tomsmith",
            "password": "SuperSecretPassword!",
            "expected_message": "You logged into a secure area!",
        },
        id="valid_login",
    ),
    pytest.param(
        {
            "username": "wronguser",
            "password": "wrongpass",
            "expected_message": "This will fail!",
        },
        id="invalid_login",
    ),
]