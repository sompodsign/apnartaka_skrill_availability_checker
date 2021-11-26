from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage:
    def __init__(self, driver, base_url=''):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def click(self, locator):
        self.driver.implicitly_wait(1)
        self.driver.find_element(*locator).click()

    def clear_data(self, locator):
        self.driver.find_element_by_xpath(locator).clear()

    def send_data(self, data, *locator):
        self.driver.implicitly_wait(1)
        self.find_element(*locator).send_keys(data)

    def find_element(self, *locator):
        # self.wait_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):  # method to grab multiple elements
        return self.driver.find_elements(*locator)

    def get(self, url):
        return self.driver.get(url)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            print(locator)
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            # self.driver.quit()

    # Method to explicitly wait for user defined time.
    def wait_element_custom_time(self, *locator, time):
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.driver.quit()
