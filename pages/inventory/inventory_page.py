from pages.base_page import BasePage

class InventoryPage(BasePage):
    DASHBOARD_TITLE = ".fi-header-heading"

    def is_logged_in(self):
      return bool(self.page.locator(self.DASHBOARD_TITLE).text_content())