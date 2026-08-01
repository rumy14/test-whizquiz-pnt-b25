from pages.base_page import BasePage


class UsersPage(BasePage):
    ADD_USER_BUTTON = "button:has-text('Add User'), button:has-text('Create User'), button:has-text('Add'), button:has-text('Create'), a:has-text('New User'), a:has-text('Add'), a:has-text('Create'), [data-action='add-user']"
    USER_EMAIL_INPUT = "[id*='email'], [placeholder*='Email'], input[name*='email']"
    USER_NAME_INPUT = "[id*='name'], [placeholder*='Name'], input[name*='name']"
    USER_PASSWORD_INPUT = "[id*='password'], [placeholder*='Password'], input[name*='password']"
    USER_ROLE_SELECT = "select[name*='role'], [role='combobox']:has-text('Role')"
    SAVE_USER_BUTTON = "button:has-text('Save'), button:has-text('Create'), button[type='submit']"
    SUCCESS_MESSAGE = ".alert-success, [role='alert']:has-text('Success'), .toast-success"
    USER_TABLE = "table tbody tr, .user-list .item"

    def open_users(self):
        self.page.goto("https://ai-quizwhiz.zluck.com/admin/users")
        self.page.wait_for_timeout(2000)

    def click_new_user(self):
        self.click_add_user()

    def click_add_user(self):
        self.page.locator(self.ADD_USER_BUTTON).first.click()
        self.page.wait_for_timeout(1000)

    def create_user(self, email, name, password, role="User"):
        self.click_add_user()
        self.page.wait_for_timeout(500)

        for selector, value in (
            (self.USER_EMAIL_INPUT, email),
            (self.USER_NAME_INPUT, name),
            (self.USER_PASSWORD_INPUT, password),
        ):
            field = self.page.locator(selector)
            if field.count() > 0:
                field.first.fill(value)

        role_select = self.page.locator(self.USER_ROLE_SELECT)
        if role_select.count() > 0:
            role_select.first.click()
            self.page.wait_for_timeout(500)
            self.page.locator(f"option:has-text('{role}'), [role='option']:has-text('{role}')").first.click()

        self.page.locator(self.SAVE_USER_BUTTON).first.click()
        self.page.wait_for_timeout(2000)

    def is_user_created_successfully(self):
        try:
            self.page.locator(self.SUCCESS_MESSAGE).first.wait_for(timeout=5000)
            return True
        except Exception:
            return False

    def get_user_count(self):
        return self.page.locator(self.USER_TABLE).count()

    def search_user(self, email):
        search_input = self.page.locator("input[placeholder*='Search'], [type='search']")
        if search_input.count() > 0:
            search_input.first.fill(email)
            self.page.wait_for_timeout(1000)


UserPage = UsersPage