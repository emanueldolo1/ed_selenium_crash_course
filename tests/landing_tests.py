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

    def test_talk_to_sales_link(self):
        log_message("Navigates to Productive and clicks Talk to sales button.")
        expected_message = "Questions? We’ve Got Answers"
        expected_url = "https://productive.io/talk-to-sales"

        self.landing_page.navigate_to_page()
        self.landing_page.talk_to_sales_button.click()
        self.assertTrue(self.landing_page.talk_to_sales_text.text == expected_message)
        print("--------------------------------------------------------------")
        print("Stvarni tekst: ", self.landing_page.talk_to_sales_text.text)
        print("Ocekivani tekst: ", expected_message)
        self.assertTrue(self.driver.current_url == expected_url)
        print("Cak je i url tocan 0.o")
        print("--------------------------------------------------------------")
