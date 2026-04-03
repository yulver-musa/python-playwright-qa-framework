import pytest
from data.login_cases import LOGIN_TEST_CASES

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("case", LOGIN_TEST_CASES)
def test_login(login_page, case):
    login_page.login(case["username"], case["password"])

    assert case["expected_message"] in login_page.get_flash_message()
