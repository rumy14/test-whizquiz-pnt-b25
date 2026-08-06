from pages.base_page import BasePage


class MenuPage(BasePage):
    ADD_MENU_BUTTON = "button:has-text('Add Menu'), button:has-text('Create Menu'), [data-action='add-menu']"
    MENU_NAME_INPUT = "[id*='menu_name'], [placeholder*='Menu Name'], input[name*='menu']"
    MENU_DESCRIPTION_INPUT = "[id*='description'], [placeholder*='Description'], textarea[name*='description']"
    SAVE_MENU_BUTTON = "button:has-text('Save'), button:has-text('Create'), button[type='submit']"
    SUCCESS_MESSAGE = ".alert-success, [role='alert']:has-text('Success'), .toast-success"
    MENU_TABLE = "table tbody tr, .menu-list .item"

    def click_add_menu(self):
        self.page.locator(self.ADD_MENU_BUTTON).first.click()
        self.page.wait_for_timeout(1000)

    def create_menu(self, menu_name, description=""):
        self.click_add_menu()
        self.page.wait_for_timeout(500)
        self.page.locator(self.MENU_NAME_INPUT).first.fill(menu_name)

        description_fields = self.page.locator(self.MENU_DESCRIPTION_INPUT)
        if description and description_fields.count() > 0:
            description_fields.first.fill(description)

        self.page.locator(self.SAVE_MENU_BUTTON).first.click()
        self.page.wait_for_timeout(2000)

    def is_menu_created_successfully(self):
        try:
            self.page.locator(self.SUCCESS_MESSAGE).first.wait_for(timeout=5000)
            return True
        except Exception:
            return False

    def get_menu_count(self):
        return self.page.locator(self.MENU_TABLE).count()

    def search_menu(self, menu_name):
        search_input = self.page.locator("input[placeholder*='Search'], [type='search']")
        if search_input.count() > 0:
            search_input.first.fill(menu_name)
            self.page.wait_for_timeout(1000)