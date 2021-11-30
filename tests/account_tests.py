import common.test_data
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

    def test_insect_shop_registration(self):
        expected_message = "User registered"
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.register(login_data)

        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)

    def test_insect_shop_password(self):
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.insect_store_password_field.send_keys(login_data)
        self.account_page.insect_store_register_button.click()

        self.assertTrue(self.account_page.insect_store_user_registered.text == "Input fields can't be blank")

    def test_insect_shop_same_name(self):
        expected_message = "User already exists"
        self.account_page.navigate_to_page()

        self.account_page.insect_store_name_field.send_keys(common.test_data.VALID_STORE_NAME)
        self.account_page.insect_store_password_field.send_keys(common.test_data.VALID_PASSWORD)

        self.account_page.insect_store_register_button.click()
        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)

    def test_insect_shop_wrong_password(self):
        expected_message = "Wrong password, try again."
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.insect_store_name_field.send_keys(common.test_data.VALID_STORE_NAME)
        self.account_page.insect_store_password_field.send_keys(login_data)
        self.account_page.insect_store_login_button.click()

        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)

    def test_insect_shop_delete_user(self):
        expected_message = "User deleted!"
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.register(login_data)
        time.sleep(1)
        self.account_page.delete_store_name(login_data)
        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)

    def test_insect_shop_login(self):
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.login_and_register(login_data)

        self.assertTrue(self.shop_page.insect_store_load_sample_bugs_button)

        self.account_page.delete_store_name(login_data)

    def test_login_method(self):
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.login_and_register(login_data)
        self.assertTrue(self.shop_page.insect_store_load_sample_bugs_button)

        self.account_page.delete_store_name(login_data)



    def test_micanja_buba(self):
        login_data = get_timestamp()
        self.account_page.navigate_to_page()

        self.account_page.login_and_register(login_data)
        self.shop_page.insect_store_load_sample_bugs_button.click()
        prijasnje_stanje_liste = len(self.shop_page.insect_store_lista_buba)

        self.shop_page.insect_store_remove_bug_button.click()
        self.assertTrue(len(self.shop_page.insect_store_lista_buba) < prijasnje_stanje_liste)

        self.account_page.delete_store_name(login_data)


