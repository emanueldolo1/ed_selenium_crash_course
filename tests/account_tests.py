import string
from lib2to3.pgen2 import driver

from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.account_page import AccountPage
import time
import random


class AccountTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.account_page = AccountPage(self.driver)

    def test_navigate_to_shameless_posts(self):
        log_message("Navigates to Shameless blog posts and verifies that the topic label is Shameless.")

        self.account_page.navigate_to_page()
        self.account_page.shameless_link.click()
        self.account_page.save_screenshot(self._testMethodName)

        self.assertTrue(self.account_page.topic_label.text == "Shameless")

        time.sleep(5)


    def test_navigate_to_technology_posts(self):
        log_message("Navigates to Technology blog posts and verifies that the topic label is Technology.")
        self.account_page.navigate_to_page()
        self.account_page.technology_link.click()

        self.assertTrue(self.account_page.topic_label.text == "Technology")

        time.sleep(5)

    def test_navigate_to_business_posts(self):
        log_message("Navigates to Business blog posts and verifies that the topic label is Business.")
        self.account_page.navigate_to_page()
        self.account_page.business_link.click()

        self.assertTrue(self.account_page.topic_label.text == "Business")

        time.sleep(5)

    def test_insect_shop_registration(self):
        letters = string.ascii_letters
        username = ''.join(random.choice(letters) for i in range(10))
        password = ''.join(random.choice(letters) for i in range(10))

        self.account_page.navigate_to_page()
        log_message("Otvorili smo stranicu")
        self.account_page.insect_store_name_field.click()
        log_message("Kliknuli smo u Store Name field")
        self.account_page.insect_store_name_field.send_keys(username)
        log_message("Upisali username")
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys(password)
        log_message("Upisali smo password")
        self.account_page.insect_store_register_button.click()
        self.assertTrue(self.account_page.insect_store_user_registered.text == "User registered")
        log_message("User je uspjesno registriran!")
        time.sleep(2)

    def test_insect_shop_password(self):
        self.account_page.navigate_to_page()
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys("password")
        self.account_page.insect_store_register_button.click()
        print(self.account_page.insect_store_user_registered.text)
        self.assertTrue(self.account_page.insect_store_user_registered.text == "Input fields can't be blank")

    def test_insect_shop_same_name(self):
        self.account_page.navigate_to_page()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys("username")
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys("password")
        self.account_page.insect_store_register_button.click()
        time.sleep(2)
        self.driver.refresh()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys("username")
        self.account_page.insect_store_register_button.click()
        self.account_page.insect_store_password_field.send_keys("password")
        self.account_page.insect_store_register_button.click()
        time.sleep(2)
        self.assertTrue(self.account_page.insect_store_user_registered.text == "User already exists")

    def test_insect_shop_wrong_password(self):
        self.account_page.navigate_to_page()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys("username")
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys("krivi_pass")
        self.account_page.insect_store_login_button.click()
        self.assertTrue(self.account_page.insect_store_user_registered.text == "Wrong password, try again.")
        time.sleep(2)

    def test_insect_shop_delete_user(self):
        self.account_page.navigate_to_page()
        self.account_page.insect_store_name_field.click()
        self.account_page.insect_store_name_field.send_keys("username")
        self.account_page.insect_store_password_field.click()
        self.account_page.insect_store_password_field.send_keys("password")
        self.account_page.insect_store_delete_user.click()
        time.sleep(2)
        self.assertTrue(self.account_page.insect_store_user_registered.text == "User deleted!")