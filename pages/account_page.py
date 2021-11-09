from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountPage(BasePage):

    slug = ""
    insect_store_name_field_locator = (By.CSS_SELECTOR, "input[type='text']")
    insect_store_password_field_locator = (By.CSS_SELECTOR, "input[type='password']")
    insect_store_register_button_locator = (By.CSS_SELECTOR, "button[name='register']")
    insect_store_user_registered_locator = (By.XPATH, "//p[@data-testid='message']")
    insect_store_login_button_locator = (By.CSS_SELECTOR, "button[name='login']")
    insect_store_delete_user_locator = (By.CSS_SELECTOR, "button[name='delete']")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def insect_store_name_field(self):
        return self.get_present_element(self.insect_store_name_field_locator)

    @property
    def insect_store_password_field(self):
        return self.get_present_element(self.insect_store_password_field_locator)

    @property
    def insect_store_register_button(self):
        return self.get_present_element(self.insect_store_register_button_locator)

    @property
    def insect_store_user_registered(self):
        return self.get_present_element(self.insect_store_user_registered_locator)

    @property
    def insect_store_login_button(self):
        return self.get_present_element(self.insect_store_login_button_locator)

    @property
    def insect_store_delete_user(self):
        return self.get_present_element(self.insect_store_delete_user_locator)