from playwright.sync_api import sync_playwright
from config.base_config import BaseConfig
from pages.login_page import LoginPage
from utils.artifacts import screenshot_path


def test_view_dashboard_menus():
    """Test viewing dashboard and all available menu items"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Login
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)

            # Get all menu links from sidebar
            menu_links = page.locator("a[href*='/admin/']")
            menu_count = menu_links.count()
            print(f"\nDashboard Menus Found: {menu_count}")

            # Print all available menus
            for i in range(menu_count):
                menu_text = menu_links.nth(i).text_content().strip()
                href = menu_links.nth(i).get_attribute("href")
                if menu_text and href:
                    print(f"  - {menu_text.replace(chr(10), ' ')}")

            page.screenshot(path=screenshot_path("test_menu_dashboard_menus"))
            print("\nDashboard menus inspection completed")

        finally:
            browser.close()


def test_navigate_through_menus():
    """Test navigating through different dashboard menus"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Login
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)

            # List of menus to navigate to
            menus = [
                ("Users", "/admin/users"),
                ("Categories", "/admin/categories"),
                ("Quizzes", "/admin/quizzes"),
            ]

            for menu_name, path in menus:
                page.goto(f"https://ai-quizwhiz.zluck.com{path}")
                page.wait_for_timeout(2000)

                # Verify navigation
                current_url = page.url
                assert path in current_url, f"Failed to navigate to {menu_name}"
                print(f"Successfully navigated to: {menu_name}")

            page.screenshot(path=screenshot_path("test_menu_navigation"))

        finally:
            browser.close()

