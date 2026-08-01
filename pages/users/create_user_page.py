from pages.base_page import BasePage


class CreateUserPage(BasePage):
    NAME = "input[placeholder='Name']"
    EMAIL = "input[placeholder='Email']"
    PASSWORD = "input[placeholder='Password']"
    CONFIRM_PASSWORD = "input[placeholder='Confirm Password']"
    PLAN_DROPDOWN = "[role='combobox']"
    DEFAULT_PLAN = "text=Default Plan"
    CREATE_BUTTON = "button:has-text('Create')"

    def enter_name(self, name):
        self.page.fill(self.NAME, name)

    def enter_email(self, email):
        self.page.fill(self.EMAIL, email)

    def enter_password(self, password):
        self.page.fill(self.PASSWORD, password)

    def enter_confirm_password(self, password):
        self.page.fill(self.CONFIRM_PASSWORD, password)
        self.page.wait_for_timeout(1000)

    def select_plan(self):
        self.page.locator(self.PLAN_DROPDOWN).click()
        self.page.wait_for_timeout(2000)

    def select_default_plan(self):
        self.page.locator(self.DEFAULT_PLAN).first.click()

    def click_create(self):
        self.page.locator(self.CREATE_BUTTON).click()
        self.page.wait_for_timeout(5000)

    def create_user(self, name, email, password, plan):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.select_plan()
        self.select_default_plan()
        self.click_create()