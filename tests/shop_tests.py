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

    def test_micanja_fly_bube(self):
        bube = []
        current_bug = []
        indeks = 0

        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.login_and_register(login_data)
        self.shop_page.insect_store_load_sample_bugs_button.click()
        time.sleep(2)
        bube = self.shop_page.insect_inventory_lista_buba
        for bug in bube:
            if (bug.get_attribute("value")) == "Fly":
                current_bug = bug.get_attribute("value")
                indeks = bube.index(bug)
        time.sleep(5)
        self.shop_page.insect_remove_bug_buttons[3].click()
        time.sleep(5)
        #Provjera da bube vise nema u Shopu
        bube2 = self.shop_page.insect_store_lista_buba
        for bug in bube2:
            if bug.text.split()[0] == "Fly":
                print("Fly ipak nije uklonjen")
                break
        print("Good job, mission acomplished!")