from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options


class Base(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument("--headless")
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://apnartaka.com')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

