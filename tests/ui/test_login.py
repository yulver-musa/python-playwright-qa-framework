import pytest
from pages.login_page import LoginPage
from data.login_cases import LOGIN_TEST_CASES

@pytest.mark.parametrize("case", LOGIN_TEST_CASES)
def test_login(page, case):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(case["username"], case["password"])

    assert case["expected_message"] in login_page.get_flash_message()
