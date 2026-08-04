from playwright.sync_api import sync_playwright
from config.base_config import BaseConfig
from pages.inventory.inventory_page import InventoryPage
from pages.auth.login_page import LoginPage


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate(BaseConfig.BASE_URL)

        login_page.login("admin@gmail.com", "123456")
        page.wait_for_timeout(4000)

        inventory_page = InventoryPage(page)
        assert inventory_page.is_logged_in(), "Login failed with valid credentials"

        print("Login successful with valid credentials")

        page.screenshot(path="test_valid_login.png")
        browser.close()
