from playwright.sync_api import sync_playwright
import time

from config.base_config import BaseConfig
from pages.auth.login_page import LoginPage
from pages.dashboard.inventory_page import InventoryPage
from pages.users.all_user_page import AllUserPage
from pages.users.create_user_page import CreateUserPage
from pages.users.user_page import UsersPage


def test_valid_user_creation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(4000)
            InventoryPage(page).is_logged_in()
            user_page = UsersPage(page)
            user_page.open_users()
            user_page.click_new_user()
            timestamp = str(int(time.time()))
            CreateUserPage(page).create_user(
                f"TestUser{timestamp}",
                f"test{timestamp}@example.com",
                "123456789",
                "Default",
            )
            page.wait_for_url("**/admin/users")
            page.wait_for_timeout(2000)
            assert AllUserPage(page).verify_user_created()
        finally:
            browser.close()