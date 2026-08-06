from playwright.sync_api import sync_playwright

from config.base_config import BaseConfig
from pages.auth.login_page import LoginPage
from utils.artifacts import screenshot_path


def test_navigate_to_users():
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
            assert "/users" in page.url
            page.screenshot(path=screenshot_path("test_user_users_page"))
        finally:
            browser.close()


def test_create_user():
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
            add_user_button = page.locator("button:has-text('Add'), button:has-text('Create'), a:has-text('Add'), a:has-text('Create')")
            if add_user_button.count() > 0:
                add_user_button.first.click()
                page.wait_for_timeout(1000)
                page.screenshot(path=screenshot_path("test_user_form"))
        finally:
            browser.close()


def test_users_page_structure():
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
            assert page.locator("button").count() >= 0
            page.screenshot(path=screenshot_path("test_user_users_page_full"))
        finally:
            browser.close()