from pages.base_page import BasePage
<<<<<<< HEAD
from pages.create_user_page import CreateUserPage
from pages.user_page import UsersPage

class AllUserPage(BasePage):

=======


class AllUserPage(BasePage):
>>>>>>> 77c80fd7483add4b1789892f2ed53b1cc4ecb958
    NEW_USER = ".text-sm.text-gray-500.dark\\:text-gray-400"

    def verify_user_created(self):
        return bool(self.page.locator(self.NEW_USER).first.text_content())