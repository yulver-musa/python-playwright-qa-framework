from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
        self.flash_message = "#flash"

    def login(self, username, password):
        self.navigate("/login")
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

    def get_flash_message(self):
        return self.get_text(self.flash_message)