from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_TITLE = ".fi-header-heading"
    MENU_BUTTON = "nav a, .sidebar a, [role='navigation'] a"
    USER_MENU = "button[aria-label='User menu'], .user-menu, [data-menu='user']"
    SETTINGS_MENU = "a:has-text('Settings'), [href*='settings']"
    
    def is_logged_in(self):
        return bool(self.page.locator(self.DASHBOARD_TITLE).text_content())
    
    def get_dashboard_title(self):
        return self.page.locator(self.DASHBOARD_TITLE).text_content()
    
    def get_all_menu_items(self):
        menu_items = self.page.locator("nav a, .sidebar a, [role='navigation'] a")
        return menu_items
    
    def click_menu(self, menu_name):
        self.page.locator(f"a:has-text('{menu_name}'), [href*='{menu_name.lower()}']").click()
    
    def wait_for_dashboard_load(self, timeout=30000):
        self.page.wait_for_selector(self.DASHBOARD_TITLE, timeout=timeout)
