from playwright.sync_api import Page

def test_valid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")

    page.click("button[type='submit']")

    assert "You logged into a secure area!" in page.inner_text("#flash")


def test_invalid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith2")
    page.fill("#password", "SuperSecretPassword!2")

    page.click("button[type='submit']")

    assert "Your username is invalid!" in page.inner_text("#flash")