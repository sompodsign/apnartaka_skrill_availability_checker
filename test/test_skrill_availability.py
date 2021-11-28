from pages.all_pages import CommonPage
from test.base import Base


class TestSkrillAvailability(Base):

    def test_apnar_taka(self):
        page = CommonPage(self.driver)
        page.login()
        page.go_to_wallet_sell_page_check_send_notification()
