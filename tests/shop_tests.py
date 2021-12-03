from utilities.base_test import BaseTest
from pages.account_page import AccountPage
import time
from common.helpers import get_timestamp
from pages.shop_page import ShopPage

class AccountTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.account_page = AccountPage(self.driver)
        self.shop_page = ShopPage(self.driver)

    def test_provjera_buba(self):
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.login_and_register(login_data)
        self.shop_page.insect_store_load_sample_bugs_button.click()
        self.assertTrue(len(self.shop_page.insect_store_lista_buba) > 1)
        print (len(self.shop_page.insect_store_lista_buba))

        self.account_page.delete_store_name(login_data)

    def test_remove_bug(self):
        bug_to_remove = "Fly"

        self.account_page.navigate_to_page()
        self.account_page.login_and_register(get_timestamp())
        self.shop_page.insect_store_load_sample_bugs_button.click()
        self.assertTrue(self.shop_page.is_bug_in_store(bug_to_remove))
        self.shop_page.remove_bug(bug_to_remove)
        self.assertTrue(self.shop_page.is_bug_in_store(bug_to_remove))
