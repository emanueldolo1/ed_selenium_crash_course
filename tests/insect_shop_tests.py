import string

from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.insect_shop_page import BlogPage
import time
import random


class BlogTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.blog_page = BlogPage(self.driver)

    def test_navigate_to_shameless_posts(self):
        log_message("Navigates to Shameless blog posts and verifies that the topic label is Shameless.")

        self.blog_page.navigate_to_page()
        self.blog_page.shameless_link.click()
        self.blog_page.save_screenshot(self._testMethodName)

        self.assertTrue(self.blog_page.topic_label.text == "Shameless")

        time.sleep(5)


    def test_navigate_to_technology_posts(self):
        log_message("Navigates to Technology blog posts and verifies that the topic label is Technology.")
        self.blog_page.navigate_to_page()
        self.blog_page.technology_link.click()

        self.assertTrue(self.blog_page.topic_label.text == "Technology")

        time.sleep(5)

    def test_navigate_to_business_posts(self):
        log_message("Navigates to Business blog posts and verifies that the topic label is Business.")
        self.blog_page.navigate_to_page()
        self.blog_page.business_link.click()

        self.assertTrue(self.blog_page.topic_label.text == "Business")

        time.sleep(5)

    def test_insect_shop_registration(self):
        letters = string.ascii_letters
        username = ''.join(random.choice(letters) for i in range(10))
        password = ''.join(random.choice(letters) for i in range(10))

        self.blog_page.navigate_to_page()
        log_message("Otvorili smo stranicu")
        self.blog_page.insect_store_name_field.click()
        log_message("Kliknuli smo u Store Name field")
        self.blog_page.insect_store_name_field.send_keys(username)
        log_message("Upisali username")
        self.blog_page.insect_store_password_field.click()
        self.blog_page.insect_store_password_field.send_keys(password)
        log_message("Upisali smo password")
        self.blog_page.insect_store_register_button.click()
        time.sleep(2)

