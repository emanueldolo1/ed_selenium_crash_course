import common.test_data
from utilities.base_test import BaseTest
from pages.account_page import AccountPage
import time
from common.helpers import get_timestamp


class AccountTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.account_page = AccountPage(self.driver)


    def test_insect_shop_registration(self):
        expected_message = "User registered"

        self.account_page.navigate_to_page()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys(get_timestamp())
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys(get_timestamp())
        self.account_page.insect_store_register_button.click()
        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)
        time.sleep(2)

    def test_insect_shop_password(self):
        self.account_page.navigate_to_page()
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys(get_timestamp())
        self.account_page.insect_store_register_button.click()
        print(self.account_page.insect_store_user_registered.text)
        self.assertTrue(self.account_page.insect_store_user_registered.text == "Input fields can't be blank")
        time.sleep(2)

    def test_insect_shop_same_name(self):
        expected_message = "User already exists"

        self.account_page.navigate_to_page()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys(common.test_data.VALID_STORE_NAME)
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys(common.test_data.VALID_PASSWORD)
        self.account_page.insect_store_register_button.click()
        time.sleep(2)
        self.driver.refresh()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys(common.test_data.VALID_STORE_NAME)
        self.account_page.insect_store_register_button.click()
        self.account_page.insect_store_password_field.send_keys(common.test_data.VALID_PASSWORD)
        self.account_page.insect_store_register_button.click()
        time.sleep(2)
        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)

    def test_insect_shop_wrong_password(self):
        expected_message = "Wrong password, try again."

        self.account_page.navigate_to_page()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys(common.test_data.VALID_STORE_NAME)
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys(get_timestamp())
        self.account_page.insect_store_login_button.click()
        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)
        time.sleep(2)

    def test_insect_shop_delete_user(self):
        expected_message = "User deleted!"

        self.account_page.navigate_to_page()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys(get_timestamp())
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys(get_timestamp())
        self.account_page.insect_store_register_button.click()
        self.account_page.insect_store_delete_user.click()
        self.assertTrue(self.account_page.insect_store_user_registered.text == expected_message)
        time.sleep(2)
