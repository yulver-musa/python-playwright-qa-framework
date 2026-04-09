from pages.base_page import BasePage

class SecurePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.header = "h2"

    def get_header(self):
        return self.get_text(self.header)