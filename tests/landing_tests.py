from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.landing_page import LandingPage
import time


class LandingTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.landing_page = LandingPage(self.driver)

    def test_I_agree_button(self):
        log_message("Navigates to Productive and clicks on button.")

        self.landing_page.navigate_to_page()
        log_message("Otvorila se stranica")
        self.landing_page.agree_button_link.click()
        log_message("Button I agree je kliknut")
        time.sleep(5)
        self.assertTrue(self, self.landing_page.button_exists_link == 0)
        log_message("Provjera jel i dalje postoji I agree button")
