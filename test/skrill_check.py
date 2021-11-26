from base import Base
from pages.all_pages import CommonPage
from selenium.webdriver.common.by import By


class TestSkrillAvailability(Base):

    def test_apnar_taka(self):
        page = CommonPage(self.driver)
        page.login()
