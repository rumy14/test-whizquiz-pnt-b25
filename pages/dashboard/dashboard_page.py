from ..base_page import BasePage


class DashboardPage(BasePage):
    """Dashboard page with statistics and basic interactions."""

    DASHBOARD_TITLE = ".fi-header-heading"
    MENU_BUTTON = "nav a, .sidebar a, [role='navigation'] a"
    USER_MENU = "button[aria-label='User menu'], .user-menu, [data-menu='user']"
    SETTINGS_MENU = "a:has-text('Settings'), [href*='settings']"

    # Generic locators for stats and tables (keep selectors broad to tolerate UI changes)
    ACTIVE_USERS_CARD = "//text()='Active Users'"
    PAID_USERS_CARD = "//text()='Paid Users'"
    ACTIVE_QUIZZES_CARD = "//text()='Active Quizzes'"
    PARTICIPANTS_CARD = "//text()='Participants'"

    RECENT_USERS_TABLE = "//table[contains(@class,'recent-users')]"
    TOP_QUIZZES_TABLE = "//table[contains(@class,'top-quizzes')]"
    REVENUE_CHART = "//div[contains(@class,'revenue-chart')]"

    def is_dashboard_loaded(self):
        return self.is_visible(self.DASHBOARD_TITLE)

    def is_logged_in(self):
        return bool(self.page.locator(self.DASHBOARD_TITLE).text_content())

    def get_dashboard_title(self):
        return self.page.locator(self.DASHBOARD_TITLE).text_content()

    def get_all_menu_items(self):
        return self.page.locator(self.MENU_BUTTON)

    def click_menu(self, menu_name):
        self.page.locator(f"a:has-text('{menu_name}'), [href*='{menu_name.lower()}']").click()

    def wait_for_dashboard_load(self, timeout=30000):
        self.page.wait_for_selector(self.DASHBOARD_TITLE, timeout=timeout)
