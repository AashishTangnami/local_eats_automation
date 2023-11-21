
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FoodItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_food_item(self, locator_type, locator_value):
        self.click_element(locator_type, locator_value)

    def save_food_item(self):
        self.click_element(self.SAVE_BUTTON)