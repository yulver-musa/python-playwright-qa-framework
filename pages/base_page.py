from utils.config import BASE_URL


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, path):
        self.page.goto(f"{BASE_URL}{path}")

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def get_text(self, selector):
        return self.page.inner_text(selector)