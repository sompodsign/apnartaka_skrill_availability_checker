from decouple import config
import time
from pages.base_page import BasePage
from utils.locators import HomePageLocators


class CommonPage(BasePage):

    def __init__(self, driver):
        self.locators = HomePageLocators
        super().__init__(driver)

    def login(self):
        self.send_data(config('login_email'), *self.locators.EMAIL_FIELD)
        self.send_data('5946644S', *self.locators.PASSWORD_FIELD)
        time.sleep(1)
        self.click(self.locators.LOGIN_BTN)

    def go_to_wallet_sell_page(self):
        self.click()