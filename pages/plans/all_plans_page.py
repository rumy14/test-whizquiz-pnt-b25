from pages.base_page import BasePage


class AllPlansPage(BasePage):

    PLAN_NAME_CELL = ".text-sm.text-gray-500.dark\\:text-gray-400"

    def verify_plan_created(self):
        return bool(self.page.locator(self.PLAN_NAME_CELL).first.text_content())
