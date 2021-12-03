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

    def remove_bug(self, bug_name):
        indeks = 0
        bube = self.insect_inventory_lista_buba

        for bug in bube:
            if bug.get_attribute("value") == bug_name:
                indeks = bube.index(bug)

        self.insect_remove_bug_buttons[indeks].click()

    def is_bug_in_store(self, bug_name):
        bube = self.insect_store_lista_buba

        for bug in bube:
            if bug.text.split()[0] == bug_name:
                return False
        return True


    @property
    def insect_store_load_sample_bugs_button(self):
        return self.get_present_element(self.insect_store_load_sample_bugs_locator)

    @property
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





