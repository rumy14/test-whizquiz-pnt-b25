from pages.base_page import BasePage

class UsersPage(BasePage):

    USERS_MENU = "a[href='https://ai-quizwhiz.zluck.com/admin/users']"
    NEW_USER = "a:has-text('New User')"

    def open_users(self):
        self.page.locator(self.USERS_MENU).click()

    def click_new_user(self):
        self.page.locator(self.NEW_USER).click()