from utilities.base_test import BaseTest
from utilities.loggers import log_message
from pages.blog_page import BlogPage
import time


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


    def test_navigate_to_technology_posts(self):
        log_message("Navigates to Technology blog posts and verifies that the topic label is Shameless.")
        self.blog_page.navigate_to_page()
        self.blog_page.technology_link.click()

        self.assertTrue(self.blog_page.topic_label.text == "Technology")


        time.sleep(5)

