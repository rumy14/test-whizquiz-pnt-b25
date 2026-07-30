from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = "[id='data.email']"
    PASSWORD_INPUT = "[id='data.password']"
    SIGN_IN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = "p[data-validation-error]"

    def login(self, email, password):
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.locator(self.SIGN_IN_BUTTON).click()

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).text_content()