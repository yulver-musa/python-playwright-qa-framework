from pages.login_page import LoginPage
from data.login_test_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    VALID_LOGIN_MESSAGE,
    INVALID_LOGIN_MESSAGE,
)

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert VALID_LOGIN_MESSAGE in login_page.get_flash_message()


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    assert INVALID_LOGIN_MESSAGE in login_page.get_flash_message()