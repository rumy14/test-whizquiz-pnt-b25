from pages.base_page import BasePage


class PlansPage(BasePage):

    PLANS_MENU = "text=Plans"
    NEW_PLAN_BUTTON = "a:has-text('New')"

    def open_plans(self):
        self.page.locator(self.PLANS_MENU).click()

    def click_new_plan(self):
        self.page.locator(self.NEW_PLAN_BUTTON).first.click()
