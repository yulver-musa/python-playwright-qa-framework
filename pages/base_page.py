from utils.config import BASE_URL


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, path):
        print(f"[BasePage] Navigating to: {BASE_URL}{path}")
        self.page.goto(f"{BASE_URL}{path}")

    def click(self, selector):
        print(f"[BasePage] Clicking: {selector}")
        self.page.click(selector)

    def fill(self, selector, text):
        print(f"[BasePage] Filling: {selector} with: {text}")
        self.page.fill(selector, text)

    def get_text(self, selector):
        print(f"[BasePage] Getting text from: {selector}")
        return self.page.inner_text(selector)