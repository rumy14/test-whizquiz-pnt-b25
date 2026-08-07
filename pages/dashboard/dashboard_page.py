<<<<<<< HEAD
"""Dashboard page object for QuizWhiz Admin"""
=======
>>>>>>> 77c80fd7483add4b1789892f2ed53b1cc4ecb958
from pages.base_page import BasePage


class DashboardPage(BasePage):
<<<<<<< HEAD
    """Dashboard page with statistics and overview"""

    # Locators
    DASHBOARD_TITLE = "//h1[contains(text(), 'Dashboard')]"
    
    # Stats Cards
    ACTIVE_USERS_CARD = "//text()='Active Users'"
    ACTIVE_USERS_COUNT = "//text()='Active Users'/../following-sibling::*//text()[contains(., '38')]"
    ACTIVE_USERS_TOTAL = "//text()='Total Users:'"
    
    PAID_USERS_CARD = "//text()='Paid Users'"
    PAID_USERS_COUNT = "//text()='Paid Users'/../following-sibling::*//text()[contains(., '39')]"
    PAID_USERS_EARNINGS = "//text()='Total Earnings'"
    
    ACTIVE_QUIZZES_CARD = "//text()='Active Quizzes'"
    ACTIVE_QUIZZES_COUNT = "//text()='Active Quizzes'/../following-sibling::*//text()[contains(., '26')]"
    ACTIVE_QUIZZES_TOTAL = "//text()='Total Quizzes:'"
    
    PARTICIPANTS_CARD = "//text()='Participants'"
    PARTICIPANTS_COUNT = "//text()='Participants'/../following-sibling::*//text()[contains(., '222')]"
    PARTICIPANTS_COMPLETED = "//text()='Participants Completed Quiz'"
    
    # Tables
    RECENT_USERS_TABLE = "//text()='Recent Users'/../following-sibling::table"
    RECENT_USERS_ROWS = RECENT_USERS_TABLE + "//tr"
    RECENT_USERS_FIRST_USER = RECENT_USERS_ROWS + "[1]//td[1]"
    
    TOP_QUIZZES_TABLE = "//text()='Top Quizzes By Participants'/../following-sibling::table"
    TOP_QUIZZES_ROWS = TOP_QUIZZES_TABLE + "//tr"
    TOP_QUIZZES_FIRST = TOP_QUIZZES_ROWS + "[1]//td[1]"
    
    REVENUE_CHART = "//text()='Revenue By Dates'"
    REVENUE_PERIOD_SELECTOR = "//button[contains(text(), 'Last Week')]"
    
    def is_dashboard_loaded(self):
        """Verify dashboard is loaded with title visible"""
        return self.is_visible(self.DASHBOARD_TITLE)
    
    def get_active_users_count(self):
        """Get active users count"""
        text = self.get_text(self.ACTIVE_USERS_COUNT)
        return int(text.strip()) if text else None
    
    def get_paid_users_count(self):
        """Get paid users count"""
        text = self.get_text(self.PAID_USERS_COUNT)
        return int(text.strip()) if text else None
    
    def get_active_quizzes_count(self):
        """Get active quizzes count"""
        text = self.get_text(self.ACTIVE_QUIZZES_COUNT)
        return int(text.strip()) if text else None
    
    def get_participants_count(self):
        """Get participants count"""
        text = self.get_text(self.PARTICIPANTS_COUNT)
        return int(text.strip()) if text else None
    
    def get_recent_users_table_data(self):
        """Get recent users table data"""
        rows = self.get_elements(self.RECENT_USERS_ROWS)
        data = []
        for row in rows[1:]:  # Skip header
            cells = row.query_selector_all("td")
            if len(cells) >= 3:
                data.append({
                    'username': cells[0].text_content(),
                    'plan': cells[1].text_content(),
                    'created_at': cells[2].text_content()
                })
        return data
    
    def get_top_quizzes_table_data(self):
        """Get top quizzes table data"""
        rows = self.get_elements(self.TOP_QUIZZES_ROWS)
        data = []
        for row in rows[1:]:  # Skip header
            cells = row.query_selector_all("td")
            if len(cells) >= 2:
                data.append({
                    'quiz_name': cells[0].text_content(),
                    'participants': cells[1].text_content()
                })
        return data
    
    def verify_all_stats_visible(self):
        """Verify all statistics cards are visible"""
        return (
            self.is_visible(self.ACTIVE_USERS_CARD) and
            self.is_visible(self.PAID_USERS_CARD) and
            self.is_visible(self.ACTIVE_QUIZZES_CARD) and
            self.is_visible(self.PARTICIPANTS_CARD)
        )
    
    def verify_all_tables_visible(self):
        """Verify all data tables are visible"""
        return (
            self.is_visible(self.RECENT_USERS_TABLE) and
            self.is_visible(self.TOP_QUIZZES_TABLE) and
            self.is_visible(self.REVENUE_CHART)
        )
    
    def select_revenue_period(self, period):
        """Select revenue period (Last Week, Last Month, Last Year)"""
        selector = f"//button[contains(text(), '{period}')]"
        self.click(selector)
        self.wait_for_load_state("networkidle")
=======
    DASHBOARD_TITLE = ".fi-header-heading"
    MENU_BUTTON = "nav a, .sidebar a, [role='navigation'] a"
    USER_MENU = "button[aria-label='User menu'], .user-menu, [data-menu='user']"
    SETTINGS_MENU = "a:has-text('Settings'), [href*='settings']"

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
>>>>>>> 77c80fd7483add4b1789892f2ed53b1cc4ecb958
