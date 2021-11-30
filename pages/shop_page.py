from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class ShopPage(BasePage):

    slug = ""
    insect_store_load_sample_bugs_locator = (By.CSS_SELECTOR, "[data-testid='load-sample-bugs-button']")
    insect_store_remove_bug_button_locator = (By.CSS_SELECTOR, "[data-testid='bug-remove-button']")
    insect_store_lista_buba_locator = (By.CSS_SELECTOR, "[data-testid='bug-shop-item']")
    insect_store_inventory_lista_buba_locator = (By.CSS_SELECTOR, "[data-testid='bug-name-input']")
    insect_store_remove_bug_buttons_locator = (By.CSS_SELECTOR, "[data-testid='bug-remove-button']")


    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def insect_store_load_sample_bugs_button(self):
        return self.get_present_element(self.insect_store_load_sample_bugs_locator)

    def insect_store_remove_bug_button(self):
        return self.get_present_element(self.insect_store_remove_bug_button_locator)

    @property
    def insect_store_lista_buba(self):
        return self.get_present_elements(self.insect_store_lista_buba_locator)

    @property
    def insect_inventory_lista_buba(self):
        return self.get_present_elements(self.insect_store_inventory_lista_buba_locator)

    @property
    def insect_remove_bug_buttons(self):
        return self.get_present_elements(self.insect_store_remove_bug_buttons_locator)
