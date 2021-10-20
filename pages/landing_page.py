from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):

    slug = ""
    agree_button_link_locator = (By.XPATH, "/html/body//div[@class='gdpr-modal__content gdpr-modal__content--basic js-gdpr-modal-screen-basic']/button")
    technology_link_locator = (By.LINK_TEXT, "Technology")
    business_link_locator = (By.LINK_TEXT, "Business")
    topic_label_locator = (By.CLASS_NAME, "__highlight")
    button_exists_locator = (By.XPATH, "/html/body//span[@class='gdpr-modal__intro']")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def agree_button_link(self):
        return self.get_present_element(self.agree_button_link_locator)

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
    def button_exists_link(self):
        return self.get_present_element(self.button_exists_locator)