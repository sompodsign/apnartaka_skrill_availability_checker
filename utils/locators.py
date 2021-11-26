from selenium.webdriver.common.by import By


class HomePageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='pwd']")
    LOGIN_BTN = (By.XPATH, "//button[@name='submit']")
    SKRILL_OPTION = (By.XPATH, "//option[@value='25']")