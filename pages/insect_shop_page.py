from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class BlogPage(BasePage):

    slug = ""
    shameless_link_locator = (By.LINK_TEXT, "Shameless")
    technology_link_locator = (By.LINK_TEXT, "Technology")
    business_link_locator = (By.LINK_TEXT, "Business")
    topic_label_locator = (By.CLASS_NAME, "__highlight")
    insect_store_name_field_locator = (By.CSS_SELECTOR, "input[type='text']")
    insect_store_password_field_locator = (By.CSS_SELECTOR, "input[type='password']")
    insect_store_register_button_locator = (By.CSS_SELECTOR, "button[name='register']")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def shameless_link(self):
        return self.get_present_element(self.shameless_link_locator)

    @property
    def topic_label(self):
        return self.get_present_element(self.topic_label_locator)

    @property
    def technology_link(self):
        return self.get_present_element(self.technology_link_locator)

    @property
    def business_link(self):
        return self.get_present_element(self.business_link_locator)

    @property
    def insect_store_name_field(self):
        return self.get_present_element(self.insect_store_name_field_locator)

    @property
    def insect_store_password_field(self):
        return self.get_present_element(self.insect_store_password_field_locator)

    @property
    def insect_store_register_button(self):
        return self.get_present_element(self.insect_store_register_button_locator)