from playwright.sync_api import sync_playwright
from config.base_config import BaseConfig
from pages.login_page import LoginPage


def test_inspect_dashboard():
    """Diagnostic test to inspect dashboard structure and selectors"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            # Login
            login_page = LoginPage(page)
            login_page.navigate(BaseConfig.BASE_URL)
            login_page.login("admin@gmail.com", "123456")
            page.wait_for_timeout(3000)

            # Get page content
            print("\n" + "="*80)
            print("DASHBOARD INSPECTION")
            print("="*80)

            # Get all links
            all_links = page.query_selector_all("a")
            print(f"\nTotal Links Found: {len(all_links)}")
            print("\nAll Links:")
            for i, link in enumerate(all_links):
                href = link.get_attribute("href") or ""
                text = link.text_content() or ""
                print(f"  {i+1}. Text: '{text}' | Href: '{href}'")

            # Get all buttons
            all_buttons = page.query_selector_all("button")
            print(f"\nTotal Buttons Found: {len(all_buttons)}")
            print("\nAll Buttons:")
            for i, btn in enumerate(all_buttons):
                text = btn.text_content() or ""
                data_action = btn.get_attribute("data-action") or ""
                print(f"  {i+1}. Text: '{text}' | Data-action: '{data_action}'")

            # Get navigation structure
            nav_items = page.query_selector_all("nav a, .sidebar a, [role='navigation'] a")
            print(f"\nNavigation Items: {len(nav_items)}")
            for i, item in enumerate(nav_items):
                text = item.text_content() or ""
                print(f"  {i+1}. {text}")

            # Take screenshot of full page
            page.screenshot(path="dashboard_inspection.png")
            print("\nScreenshot saved: dashboard_inspection.png")

            # Get page title
            title = page.title()
            print(f"\nPage Title: {title}")

        finally:
            browser.close()
