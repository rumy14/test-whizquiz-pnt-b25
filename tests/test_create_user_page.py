from playwright.sync_api import sync_playwright
from config.base_config import BaseConfig
from pages.inventory.inventory_page import InventoryPage
from pages.auth.login_page import LoginPage
from pages.users.user_page import UsersPage
from pages.users.create_user_page import CreateUserPage
from pages.users.all_user_page import AllUserPage
import time


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate(BaseConfig.BASE_URL)

        login_page.login("admin@gmail.com", "123456")
        page.wait_for_timeout(4000)
        inventory_page = InventoryPage(page)
        inventory_page.is_logged_in()
        user_page = UsersPage(page)
        user_page.open_users()
        user_page.click_new_user()

        create_user_page = CreateUserPage(page)
        timestamp = str(int(time.time()))
        create_user_page.create_user(f"TestUser{timestamp}", f"test{timestamp}@example.com", "123456789", "Default")
        
        # Wait for redirect to users page
        page.wait_for_url("**/admin/users")
        page.wait_for_timeout(2000)
        
        all_user_page = AllUserPage(page)

        assert all_user_page.verify_user_created(),  "User creation failed"
