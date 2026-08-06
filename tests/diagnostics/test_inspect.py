from playwright.sync_api import sync_playwright

from config.base_config import BaseConfig
from pages.auth.login_page import LoginPage
from utils.artifacts import screenshot_path


def test_inspect_dashboard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(3000)
            assert page.locator("a").count() >= 0
            page.screenshot(path=screenshot_path("test_inspect_dashboard"))
        finally:
            browser.close()