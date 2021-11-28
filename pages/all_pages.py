from decouple import config
import time
from selenium.common.exceptions import NoSuchElementException
from plyer import notification  # for getting notification on pc
from pages.base_page import BasePage
from utils.locators import HomePageLocators
from data.data import wallet_sell_url
from utils.email import send_mail


class CommonPage(BasePage):
    """
    This class has functionalities for all of the pages.
    """

    def __init__(self, driver):
        self.locators = HomePageLocators
        super().__init__(driver)

    def login(self):
        """
        Logs you in to the site
        :return:
        """
        self.send_data(config('login_email'), *self.locators.EMAIL_FIELD)
        self.send_data('5946644S', *self.locators.PASSWORD_FIELD)
        time.sleep(1)
        self.click(self.locators.LOGIN_BTN)

    def go_to_wallet_sell_page_check_send_notification(self):
        """
        Visits wallet sell page and check if skrill selling option is enabled
        """
        self.get(wallet_sell_url)
        skrill_element = None
        try:
            skrill_element = self.find_element(*self.locators.SKRILL_OPTION)
        except NoSuchElementException:
            pass
        if skrill_element:
            notification.notify(title='Apnartaka Skrill', message='Skrill Enabled. You can sell now. Hurry!',
                                app_name='skill checker', app_icon='data/Goescat-Macaron-Telegram.ico', ticker='Skrill Open', timeout=10, toast=True)
            send_mail('Skrill Enabled. You can sell now. Hurry!')
        else:
            notification.notify(title='Apnartaka Skrill', message='Skrill option is disabled now. SAD!!',
                                app_name='skill checker', app_icon='data/Goescat-Macaron-Telegram.ico', ticker='Skrill Closed', timeout=10, toast=False)
            send_mail('Skrill option is disabled now. SAD!!')

