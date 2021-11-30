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
    insect_store_remove_fly_button_locator = (By.CSS_SELECTOR, "div:nth-of-type(4) > button")

    def navigate_to_page(self):
        self.navigate(self.slug)

    def login(self, login_data):
        self.insect_store_name_field.send_keys(login_data)
        self.insect_store_password_field.send_keys(login_data)
        self.insect_store_login_button.click()

    def login_and_register(self, login_data):
        self.insect_store_name_field.send_keys(login_data)
        self.insect_store_password_field.send_keys(login_data)
        self.insect_store_register_button.click()
        self.insect_store_login_button.click()

    def register(self, login_data):
        self.insect_store_name_field.send_keys(login_data)
        self.insect_store_password_field.send_keys(login_data)
        self.insect_store_register_button.click()

    def delete_store_name(self, login_data):
        self.navigate_to_page()
        self.insect_store_name_field.send_keys(login_data)
        self.insect_store_password_field.send_keys(login_data)
        self.insect_store_delete_user.click()

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

    @property
    def insect_store_fly_button(self):
        return self.get_present_element(self.insect_store_remove_fly_button_locator)