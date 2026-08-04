from pages.base_page import BasePage


class CreatePlanPage(BasePage):

    NAME = "input[placeholder='Name']"
    DESCRIPTION = "textarea[placeholder='Description']"
    TRIAL_DAYS = "input[id='data.trial_days']"
    NO_OF_QUIZZES = "input[id='data.no_of_quiz']"
    PRICE = "input[id='data.price']"
    CURRENCY_DROPDOWN = "[role='combobox']"
    USD_CURRENCY = "text=USD Dollar"
    
    # Frequency options
    FREQUENCY_WEEKLY = "input[id='data.frequency-1']"
    FREQUENCY_MONTHLY = "input[id='data.frequency-2']"
    FREQUENCY_YEARLY = "input[id='data.frequency-3']"
    
    CREATE_BUTTON = "button:has-text('Create')"

    def enter_name(self, name):
        self.page.fill(self.NAME, name)

    def enter_description(self, description):
        self.page.fill(self.DESCRIPTION, description)

    def enter_trial_days(self, days):
        self.page.fill(self.TRIAL_DAYS, str(days))

    def enter_no_of_quizzes(self, quizzes):
        self.page.fill(self.NO_OF_QUIZZES, str(quizzes))

    def enter_price(self, price):
        self.page.fill(self.PRICE, str(price))

    def select_frequency_weekly(self):
        self.page.locator("label[for='data.frequency-1']").click()

    def select_frequency_monthly(self):
        self.page.locator("label[for='data.frequency-2']").click()

    def select_frequency_yearly(self):
        self.page.locator("label[for='data.frequency-3']").click()

    def select_currency_usd(self):
        # Open dropdown
        self.page.locator(self.CURRENCY_DROPDOWN).click()
        self.page.wait_for_timeout(2000)
        # Select USD
        self.page.locator(self.USD_CURRENCY).first.click()

    def click_create(self):
        self.page.locator(self.CREATE_BUTTON).click()
        self.page.wait_for_timeout(5000)

    def create_plan(self, name, description, frequency, trial_days, no_of_quizzes, price):
        self.enter_name(name)
        self.enter_description(description)
        self.enter_trial_days(trial_days)
        self.enter_no_of_quizzes(no_of_quizzes)
        self.enter_price(price)
        
        # Select frequency
        if frequency.lower() == "weekly":
            self.select_frequency_weekly()
        elif frequency.lower() == "monthly":
            self.select_frequency_monthly()
        elif frequency.lower() == "yearly":
            self.select_frequency_yearly()
        
        self.select_currency_usd()
        self.click_create()
