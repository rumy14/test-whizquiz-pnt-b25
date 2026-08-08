from pages.base_page import BasePage

class SubscriptionsPage(BasePage):
    # Navigation
    SUBSCRIPTIONS_MENU = "[href*='subscriptions']"
    
    # Page Elements
    PAGE_TITLE = "text='Subscribed Plans'"
    SEARCH_INPUT = "input[placeholder='Search']"
    
    # Table Headers
    USER_NAME_HEADER = "th:has-text('User Name')"
    PLAN_NAME_HEADER = "th:has-text('Plan Name')"
    PLAN_AMOUNT_HEADER = "th:has-text('Plan Amount')"
    START_DATE_HEADER = "th:has-text('Start Date')"
    END_DATE_HEADER = "th:has-text('End Date')"
    STATUS_HEADER = "th:has-text('Status')"
    ACTION_HEADER = "th:has-text('Action')"
    
    # Table Rows & Data
    TABLE_ROWS = "tbody tr"
    TABLE_CELLS = "tbody td"
    
    # Buttons & Actions
    VIEW_BUTTON = "button:has-text('View')"
    EDIT_BUTTON = "[data-testid='edit-button'], a:has-text('Edit')"
    STATUS_TOGGLE = "input[type='checkbox']"
    
    # Pagination
    PAGINATION_INFO = "text=/Showing.*of.*results/"
    ITEMS_PER_PAGE_SELECT = "select"
    NEXT_PAGE_BUTTON = "button[aria-label='Next']"
    PREV_PAGE_BUTTON = "button[aria-label='Previous']"
    PAGE_NUMBERS = "button[role='tab']"
    
    # Filters & Sorting
    SORT_BUTTON = "th button"
    
    # Status Messages
    EMPTY_STATE = "text=/No subscriptions found/i"
    SUCCESS_MESSAGE = "[role='alert']"
    ERROR_MESSAGE = "p[data-validation-error]"
    
    def navigate_to_subscriptions(self):
        """Navigate to subscriptions page"""
        self.page.click(self.SUBSCRIPTIONS_MENU)
        self.page.wait_for_load_state("networkidle")
    
    def is_page_loaded(self):
        """Verify subscriptions page is loaded"""
        try:
            self.page.wait_for_selector("text='Subscribed Plans'", timeout=5000)
            return True
        except:
            return False
    
    def search_subscription(self, search_term):
        """Search for subscription by user name or email"""
        self.page.fill(self.SEARCH_INPUT, search_term)
        self.page.wait_for_timeout(1000)
    
    def clear_search(self):
        """Clear search field"""
        self.page.fill(self.SEARCH_INPUT, "")
        self.page.wait_for_timeout(1000)
    
    def get_table_row_count(self):
        """Get number of subscription rows in current page"""
        return self.page.locator(self.TABLE_ROWS).count()
    
    def get_row_data(self, row_index):
        """Get data from a specific row"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        cells = row.locator("td")
        
        # Helper to safely get cell text
        def cell_text(n):
            if cells.count() > n:
                txt = cells.nth(n).text_content()
                return txt.strip() if txt else ""
            return ""

        # Determine status: prefer checkbox if present
        status = ""
        if cells.count() > 5:
            status_cell = cells.nth(5)
            try:
                checkbox = status_cell.locator("input[type='checkbox']")
                if checkbox.count() > 0:
                    status = "Active" if checkbox.first.is_checked() else "Inactive"
                else:
                    status = cell_text(5)
            except Exception:
                status = cell_text(5)

        return {
            "user_name": cell_text(0),
            "plan_name": cell_text(1),
            "plan_amount": cell_text(2),
            "start_date": cell_text(3),
            "end_date": cell_text(4),
            "status": status,
        }
    
    def get_all_rows_data(self):
        """Get all subscription rows data from current page"""
        rows = []
        row_count = self.get_table_row_count()
        for i in range(row_count):
            rows.append(self.get_row_data(i))
        return rows
    
    def click_view_subscription(self, row_index):
        """Click View button for a subscription"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        row.locator("button:has-text('View')").click()
        self.page.wait_for_load_state("networkidle")
    
    def click_edit_subscription(self, row_index):
        """Click Edit button for a subscription"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        row.locator("a:has-text('Edit')").click()
        self.page.wait_for_load_state("networkidle")
    
    def toggle_subscription_status(self, row_index):
        """Toggle subscription status (active/inactive)"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        toggle = row.locator("input[type='checkbox']")
        toggle.click()
        self.page.wait_for_timeout(500)
    
    def is_subscription_active(self, row_index):
        """Check if subscription is active"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        toggle = row.locator("input[type='checkbox']")
        return toggle.is_checked()
    
    def sort_by_column(self, column_name):
        """Sort table by column"""
        header = self.page.locator(f"th:has-text('{column_name}')").first
        header.click()
        self.page.wait_for_timeout(500)
    
    def set_items_per_page(self, count):
        """Set number of items displayed per page"""
        self.page.select_option(self.ITEMS_PER_PAGE_SELECT, str(count))
        self.page.wait_for_timeout(1000)
    
    def get_pagination_info(self):
        """Get pagination information (e.g., 'Showing 21 to 30 of 39 results')"""
        try:
            return self.page.locator(self.PAGINATION_INFO).text_content()
        except:
            return None
    
    def go_to_next_page(self):
        """Go to next page"""
        self.page.click(self.NEXT_PAGE_BUTTON)
        self.page.wait_for_timeout(1000)
    
    def go_to_previous_page(self):
        """Go to previous page"""
        self.page.click(self.PREV_PAGE_BUTTON)
        self.page.wait_for_timeout(1000)
    
    def go_to_page(self, page_number):
        """Go to specific page number"""
        buttons = self.page.locator(self.PAGE_NUMBERS)
        for i in range(buttons.count()):
            btn = buttons.nth(i)
            if btn.text_content().strip() == str(page_number):
                btn.click()
                self.page.wait_for_timeout(1000)
                return True
        return False
    
    def is_empty_state(self):
        """Check if there are no subscriptions"""
        try:
            self.page.wait_for_selector(self.EMPTY_STATE, timeout=2000)
            return True
        except:
            return False
    
    def get_success_message(self):
        """Get success notification message"""
        try:
            return self.page.locator(self.SUCCESS_MESSAGE).text_content()
        except:
            return None
    
    def get_error_message(self):
        """Get error notification message"""
        try:
            return self.page.locator(self.ERROR_MESSAGE).text_content()
        except:
            return None
    
    def verify_all_columns_visible(self):
        """Verify all expected table columns are visible"""
        headers = [
            "User Name",
            "Plan Name",
            "Plan Amount",
            "Start Date",
            "End Date",
            "Status",
            "Action"
        ]
        for header in headers:
            try:
                self.page.wait_for_selector(f"th:has-text('{header}')", timeout=2000)
            except:
                return False
        return True
    
    def verify_all_columns_have_data(self):
        """Verify all table columns have data"""
        if self.is_empty_state():
            return False
        
        row_data = self.get_row_data(0)
        for key, value in row_data.items():
            if not value or value == "":
                return False
        return True
    
    def get_user_name_from_row(self, row_index):
        """Get user name from a row"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        return row.locator("td").nth(0).text_content().strip()
    
    def get_plan_name_from_row(self, row_index):
        """Get plan name from a row"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        return row.locator("td").nth(1).text_content().strip()
    
    def get_plan_amount_from_row(self, row_index):
        """Get plan amount from a row"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        return row.locator("td").nth(2).text_content().strip()
    
    def get_start_date_from_row(self, row_index):
        """Get start date from a row"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        return row.locator("td").nth(3).text_content().strip()
    
    def get_end_date_from_row(self, row_index):
        """Get end date from a row"""
        row = self.page.locator(self.TABLE_ROWS).nth(row_index)
        return row.locator("td").nth(4).text_content().strip()
    
    def verify_date_format(self, date_string):
        """Verify date is in correct format (DD/MM/YYYY)"""
        import re
        pattern = r'^\d{2}/\d{2}/\d{4}$'
        return re.match(pattern, date_string) is not None
    
    def verify_currency_format(self, amount_string):
        """Verify amount is in correct currency format"""
        import re
        if not amount_string:
            return False
        # Normalize: remove whitespace and currency spacing like "$ 599.00"
        s = amount_string.strip()
        s = s.replace(' ', '')
        pattern = r'^\$[\d,]+\.\d{2}$'
        return re.match(pattern, s) is not None
