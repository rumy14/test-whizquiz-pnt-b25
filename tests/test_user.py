from playwright.sync_api import sync_playwright
from config.base_config import BaseConfig
from pages.login_page import LoginPage
from utils.artifacts import screenshot_path


def test_navigate_to_users():
    """Test navigating to Users management page"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Login
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)

            # Navigate to Users page
            page.goto("https://ai-quizwhiz.zluck.com/admin/users")
            page.wait_for_timeout(2000)

            # Verify Users page loaded
            current_url = page.url
            assert "/users" in current_url, "Users page failed to load"
            print("Successfully navigated to Users page")

            page.screenshot(path=screenshot_path("test_user_users_page"))

        finally:
            browser.close()


def test_create_user():
    """Test creating a new user"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Login
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)

            # Navigate to Users page
            page.goto("https://ai-quizwhiz.zluck.com/admin/users")
            page.wait_for_timeout(2000)

            # Look for "Add User" or "Create User" button
            add_user_button = page.locator("button:has-text('Add'), button:has-text('Create'), a:has-text('Add'), a:has-text('Create')")
            
            if add_user_button.count() > 0:
                add_user_button.first.click()
                page.wait_for_timeout(1000)
                print("Clicked Add User button")
                page.screenshot(path=screenshot_path("test_user_form"))
            else:
                print("Add User button not found on this page")
                # Take screenshot of current page
                page.screenshot(path=screenshot_path("test_user_users_page_structure"))

        finally:
            browser.close()


def test_users_page_structure():
    """Test to inspect Users page structure and available actions"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Login
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)

            # Navigate to Users page
            page.goto("https://ai-quizwhiz.zluck.com/admin/users")
            page.wait_for_timeout(2000)

            # Get all buttons on Users page
            all_buttons = page.locator("button")
            print(f"\nButtons found on Users page: {all_buttons.count()}")
            
            for i in range(min(10, all_buttons.count())):
                btn_text = all_buttons.nth(i).text_content().strip()
                if btn_text:
                    print(f"  - {btn_text}")

            # Get all links
            all_links = page.locator("a")
            print(f"\nLinks found on Users page: {all_links.count()}")
            
            for i in range(min(10, all_links.count())):
                link_text = all_links.nth(i).text_content().strip()
                if link_text and len(link_text) > 0:
                    print(f"  - {link_text}")

            page.screenshot(path=screenshot_path("test_user_users_page_full"))

        finally:
            browser.close()

