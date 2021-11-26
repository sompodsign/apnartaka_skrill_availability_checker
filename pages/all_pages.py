from decouple import config
import time
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from utils.locators import HomePageLocators
from data.data import wallet_sell_url
from utils.email import send_mail


class CommonPage(BasePage):

    def __init__(self, driver):
        self.locators = HomePageLocators
        super().__init__(driver)

    def login(self):
        self.send_data(config('login_email'), *self.locators.EMAIL_FIELD)
        self.send_data('5946644S', *self.locators.PASSWORD_FIELD)
        time.sleep(1)
        self.click(self.locators.LOGIN_BTN)

    def go_to_wallet_sell_page_check_send_notification(self):
        self.get(wallet_sell_url)
        try:
            self.find_element(*self.locators.SKRILL_OPTION)
            send_mail('Skrill Enabled. You can sell now. Hurry!')
        except NoSuchElementException:
            send_mail('Skrill option is disabled now. SAD!!')
