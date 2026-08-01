from playwright.sync_api import sync_playwright

from config.base_config import BaseConfig
from pages.auth.login_page import LoginPage
from utils.artifacts import screenshot_path


def test_view_dashboard_menus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            LoginPage(page).navigate(BaseConfig.BASE_URL)
            LoginPage(page).login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)
            assert page.locator("a[href*='/admin/']").count() > 0
            page.screenshot(path=screenshot_path("test_menu_dashboard_menus"))
        finally:
            browser.close()


def test_navigate_through_menus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(2000)
            for path in ("/admin/users", "/admin/categories", "/admin/quizzes"):
                page.goto(f"https://ai-quizwhiz.zluck.com{path}")
                page.wait_for_timeout(2000)
                assert path in page.url
            page.screenshot(path=screenshot_path("test_menu_navigation"))
        finally:
            browser.close()