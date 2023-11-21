from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Settings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_settings(self, locator_type, locator_value):
        self.click_element(locator_type, locator_value)

    def save(self):
        self.click_element(self.SAVE_BUTTON)