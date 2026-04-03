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
            "expected_message": "Your username is invalid!",
        },
        id="invalid_login",
    ),
    pytest.param(
        {
            "username": "tomsmith ",
            "password": "SuperSecretPassword!",
            "expected_message": "Your username is invalid!",
        },
        id="valid_username_with_trailing_space"
    ),
]