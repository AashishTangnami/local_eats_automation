from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.element_path import XPATH


SAVE_BUTTON = ''
class FoodItemSize(BasePage):
    def __init__(self, driver):
        super().__init__(driver) 
    
    def navigate_to_food_item_size(self, locator_type, locator_value):
        self.click_element((locator_type, locator_value))

    def add_new_size(self, locator_type, locator_value, text):
        self.enter_text(locator_type, locator_value, text)
        self.click_element((locator_type, locator_value))
        self.click_element((locator_type, SAVE_BUTTON))