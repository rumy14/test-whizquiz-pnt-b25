from playwright.sync_api import sync_playwright

from config.base_config import BaseConfig
from pages.auth.login_page import LoginPage
from utils.artifacts import screenshot_path


def test_valid_login():
    """Test valid login and dashboard access."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)

            title = page.title()
            assert "Dashboard" in title or "QuizWhiz" in title, "Dashboard failed to load"
            page.screenshot(path=screenshot_path("test_login_valid_login"))
        finally:
            browser.close()


def test_navigate_to_users_menu():
    """Test navigating to Users menu."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)

            page.goto("https://ai-quizwhiz.zluck.com/admin/users")
            page.wait_for_timeout(2000)

            assert "/users" in page.url, "Users page failed to load"
            page.screenshot(path=screenshot_path("test_login_users_menu"))
        finally:
            browser.close()