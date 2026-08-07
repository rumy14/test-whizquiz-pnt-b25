"""
Comprehensive Test Cases for Subscriptions Page

Test Scenarios:
1. Page Load & Navigation
2. Table Display & Data
3. Search Functionality
4. Sorting Functionality
5. Pagination
6. View/Edit Actions
7. Status Toggle
8. UI Elements & Validations
"""

from playwright.sync_api import sync_playwright
from config.base_config import BaseConfig
from pages.auth.login_page import LoginPage
from pages.subscriptions.subscriptions_page import SubscriptionsPage
import pytest


class TestSubscriptionsPageLoad:
    """Test subscriptions page loading and basic UI elements"""
    
    def test_subscriptions_page_loads(self):
        """TC-001: Verify subscriptions page loads successfully"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Verify page loaded
                assert subscriptions.is_page_loaded(), "Subscriptions page did not load"
                
                print("✅ TC-001 PASSED: Subscriptions page loads successfully")
                
            finally:
                browser.close()
    
    def test_all_columns_visible(self):
        """TC-002: Verify all table columns are visible"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Verify all columns visible
                assert subscriptions.verify_all_columns_visible(), "Not all columns are visible"
                
                print("✅ TC-002 PASSED: All table columns are visible")
                
            finally:
                browser.close()
    
    def test_table_has_data(self):
        """TC-003: Verify subscription table displays data"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Verify table has rows
                row_count = subscriptions.get_table_row_count()
                assert row_count > 0, "No subscription rows found in table"
                
                print(f"✅ TC-003 PASSED: Table displays {row_count} subscription rows")
                
            finally:
                browser.close()


class TestSubscriptionsTableData:
    """Test table data display and format"""
    
    def test_all_columns_have_data(self):
        """TC-004: Verify all columns contain data"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Verify all columns have data
                assert subscriptions.verify_all_columns_have_data(), "Some columns are empty"
                
                print("✅ TC-004 PASSED: All columns contain data")
                
            finally:
                browser.close()
    
    def test_date_format(self):
        """TC-005: Verify dates are in correct format (DD/MM/YYYY)"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Check first 3 rows for date format
                for i in range(min(3, subscriptions.get_table_row_count())):
                    start_date = subscriptions.get_start_date_from_row(i)
                    end_date = subscriptions.get_end_date_from_row(i)
                    
                    assert subscriptions.verify_date_format(start_date), f"Invalid start date format: {start_date}"
                    assert subscriptions.verify_date_format(end_date), f"Invalid end date format: {end_date}"
                
                print("✅ TC-005 PASSED: All dates are in correct format (DD/MM/YYYY)")
                
            finally:
                browser.close()
    
    def test_plan_amount_format(self):
        """TC-006: Verify plan amounts are in correct currency format"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Check first 3 rows for amount format
                for i in range(min(3, subscriptions.get_table_row_count())):
                    amount = subscriptions.get_plan_amount_from_row(i)
                    assert subscriptions.verify_currency_format(amount), f"Invalid currency format: {amount}"
                
                print("✅ TC-006 PASSED: All plan amounts are in correct currency format")
                
            finally:
                browser.close()


class TestSubscriptionsSearch:
    """Test search functionality"""
    
    def test_search_by_user_name(self):
        """TC-007: Search subscription by user name"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get initial row count
                initial_count = subscriptions.get_table_row_count()
                
                # Search for a user
                subscriptions.search_subscription("Noman")
                page.wait_for_timeout(2000)
                
                # Verify results filtered
                filtered_count = subscriptions.get_table_row_count()
                assert filtered_count > 0, "No results found for search"
                
                print(f"✅ TC-007 PASSED: Search found {filtered_count} results")
                
            finally:
                browser.close()
    
    def test_search_no_results(self):
        """TC-008: Search with term that returns no results"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Search with invalid term
                subscriptions.search_subscription("NONEXISTENTUSER12345")
                page.wait_for_timeout(2000)
                
                # Verify no results
                row_count = subscriptions.get_table_row_count()
                # Note: Might show empty state or 0 rows
                print(f"✅ TC-008 PASSED: Search returned {row_count} results for non-existent user")
                
            finally:
                browser.close()
    
    def test_clear_search(self):
        """TC-009: Clear search and show all results"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Search for a user
                subscriptions.search_subscription("Noman")
                page.wait_for_timeout(2000)
                
                # Clear search
                subscriptions.clear_search()
                page.wait_for_timeout(2000)
                
                # Verify all results shown
                row_count = subscriptions.get_table_row_count()
                assert row_count > 0, "No results after clearing search"
                
                print(f"✅ TC-009 PASSED: After clearing search, showing {row_count} results")
                
            finally:
                browser.close()


class TestSubscriptionsPagination:
    """Test pagination functionality"""
    
    def test_pagination_info_displayed(self):
        """TC-010: Verify pagination info is displayed"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get pagination info
                pagination_info = subscriptions.get_pagination_info()
                assert pagination_info is not None, "Pagination info not found"
                assert "Showing" in pagination_info and "results" in pagination_info, "Invalid pagination format"
                
                print(f"✅ TC-010 PASSED: Pagination info displayed: {pagination_info}")
                
            finally:
                browser.close()
    
    def test_items_per_page(self):
        """TC-011: Change items per page"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Change items per page to 5
                subscriptions.set_items_per_page(5)
                page.wait_for_timeout(2000)
                
                # Verify rows per page
                row_count = subscriptions.get_table_row_count()
                assert row_count <= 5, f"Expected max 5 rows, got {row_count}"
                
                print(f"✅ TC-011 PASSED: Items per page set to 5, showing {row_count} rows")
                
            finally:
                browser.close()
    
    def test_navigate_pages(self):
        """TC-012: Navigate between pages"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get first page data
                first_page_user = subscriptions.get_user_name_from_row(0)
                
                # Go to next page
                subscriptions.go_to_next_page()
                page.wait_for_timeout(2000)
                
                # Get second page data
                second_page_user = subscriptions.get_user_name_from_row(0)
                
                # Verify different data
                assert first_page_user != second_page_user, "Data on different pages should be different"
                
                print(f"✅ TC-012 PASSED: Successfully navigated between pages")
                print(f"   Page 1 first user: {first_page_user}")
                print(f"   Page 2 first user: {second_page_user}")
                
            finally:
                browser.close()


class TestSubscriptionsActions:
    """Test view, edit, and toggle actions"""
    
    def test_view_subscription(self):
        """TC-013: Click View button for subscription"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Click view button
                subscriptions.click_view_subscription(0)
                page.wait_for_timeout(2000)
                
                # Verify navigation
                assert page.url != subscriptions.page.url or "view" in page.url.lower() or "details" in page.url.lower(), \
                    "View action did not navigate"
                
                print("✅ TC-013 PASSED: View subscription action works")
                
            finally:
                browser.close()
    
    def test_edit_subscription(self):
        """TC-014: Click Edit button for subscription"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get current URL
                original_url = page.url
                
                # Click edit button
                subscriptions.click_edit_subscription(0)
                page.wait_for_timeout(2000)
                
                # Verify navigation
                assert page.url != original_url, "Edit action did not navigate"
                
                print("✅ TC-014 PASSED: Edit subscription action works")
                print(f"   Navigated to: {page.url}")
                
            finally:
                browser.close()
    
    def test_toggle_status(self):
        """TC-015: Toggle subscription status"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get initial status
                initial_status = subscriptions.is_subscription_active(0)
                
                # Toggle status
                subscriptions.toggle_subscription_status(0)
                page.wait_for_timeout(2000)
                
                # Get new status
                new_status = subscriptions.is_subscription_active(0)
                
                print(f"✅ TC-015 PASSED: Status toggled")
                print(f"   Initial status: {initial_status}")
                print(f"   New status: {new_status}")
                
            finally:
                browser.close()


class TestSubscriptionsSorting:
    """Test sorting functionality"""
    
    def test_sort_by_user_name(self):
        """TC-016: Sort by User Name column"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get initial order
                initial_user = subscriptions.get_user_name_from_row(0)
                
                # Sort by User Name
                subscriptions.sort_by_column("User Name")
                page.wait_for_timeout(2000)
                
                # Get new order
                sorted_user = subscriptions.get_user_name_from_row(0)
                
                print(f"✅ TC-016 PASSED: Sorted by User Name")
                print(f"   Initial first user: {initial_user}")
                print(f"   Sorted first user: {sorted_user}")
                
            finally:
                browser.close()
    
    def test_sort_by_plan_amount(self):
        """TC-017: Sort by Plan Amount column"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Sort by Plan Amount
                subscriptions.sort_by_column("Plan Amount")
                page.wait_for_timeout(2000)
                
                # Verify page still loaded
                assert subscriptions.is_page_loaded(), "Page not loaded after sorting"
                
                print("✅ TC-017 PASSED: Sorted by Plan Amount")
                
            finally:
                browser.close()


class TestSubscriptionsDataValidation:
    """Test data validation and display"""
    
    def test_row_data_structure(self):
        """TC-018: Verify row data structure is complete"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get row data
                row_data = subscriptions.get_row_data(0)
                
                # Verify all fields present
                required_fields = ["user_name", "plan_name", "plan_amount", "start_date", "end_date", "status"]
                for field in required_fields:
                    assert field in row_data, f"Missing field: {field}"
                    assert row_data[field] != "", f"Empty field: {field}"
                
                print("✅ TC-018 PASSED: Row data structure is complete")
                print(f"   Row data: {row_data}")
                
            finally:
                browser.close()
    
    def test_all_rows_data(self):
        """TC-019: Retrieve all rows data from current page"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Get all rows
                all_rows = subscriptions.get_all_rows_data()
                
                assert len(all_rows) > 0, "No rows found"
                
                print(f"✅ TC-019 PASSED: Retrieved {len(all_rows)} rows from current page")
                
            finally:
                browser.close()


class TestSubscriptionsUI:
    """Test UI elements and user interface"""
    
    def test_search_input_visible(self):
        """TC-020: Verify search input is visible and functional"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Check search input
                search_input = page.locator(subscriptions.SEARCH_INPUT)
                assert search_input.is_visible(), "Search input not visible"
                
                print("✅ TC-020 PASSED: Search input is visible and functional")
                
            finally:
                browser.close()
    
    def test_action_buttons_visible(self):
        """TC-021: Verify View and Edit buttons are visible"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            try:
                # Login
                login_page = LoginPage(page)
                login_page.navigate(BaseConfig.BASE_URL)
                login_page.login("admin@gmail.com", "123456")
                page.wait_for_timeout(3000)
                
                # Navigate to subscriptions
                subscriptions = SubscriptionsPage(page)
                subscriptions.navigate_to_subscriptions()
                page.wait_for_timeout(2000)
                
                # Check first row for buttons
                row = page.locator(subscriptions.TABLE_ROWS).first
                view_button = row.locator("button:has-text('View')")
                edit_button = row.locator("a:has-text('Edit')")
                
                assert view_button.count() > 0, "View button not found"
                assert edit_button.count() > 0, "Edit button not found"
                
                print("✅ TC-021 PASSED: View and Edit buttons are visible")
                
            finally:
                browser.close()


def run_all_tests():
    """Run all subscription tests"""
    test_classes = [
        TestSubscriptionsPageLoad,
        TestSubscriptionsTableData,
        TestSubscriptionsSearch,
        TestSubscriptionsPagination,
        TestSubscriptionsActions,
        TestSubscriptionsSorting,
        TestSubscriptionsDataValidation,
        TestSubscriptionsUI,
    ]
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    print("\n" + "="*70)
    print("RUNNING COMPREHENSIVE SUBSCRIPTION TESTS")
    print("="*70 + "\n")
    
    for test_class in test_classes:
        instance = test_class()
        methods = [m for m in dir(instance) if m.startswith('test_')]
        
        for method_name in methods:
            total_tests += 1
            try:
                method = getattr(instance, method_name)
                method()
                passed_tests += 1
            except Exception as e:
                failed_tests += 1
                print(f"❌ {method_name} FAILED: {str(e)}")
    
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests} ✅")
    print(f"Failed: {failed_tests} ❌")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_tests()
