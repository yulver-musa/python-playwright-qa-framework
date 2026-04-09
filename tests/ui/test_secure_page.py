def test_secure_page_after_login(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "secure area" in login_page.get_flash_message()