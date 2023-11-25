from utils import element_path as ep
from .base_page import BasePage

class FoodCategory(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_food_category(self):
        self.click_element(ep.XPATH, ep.FOOD_CATEGORY_NAV_XPATH)
    
    def add_new_food_category(self, ADD_NEW_FOOD_CATEGORY_XPATH):
        self.click_element(ep.XPATH,ADD_NEW_FOOD_CATEGORY_XPATH)
        self.driver.implicitly_wait(5)

    def enter_food_category_name(self, food_category_name):
        self.enter_text(ep.ID, ep.FOOD_CATEGORY_NAME_ID, food_category_name)
    
    def enter_food_category_description(self, food_category_description: None):
        self.enter_text(ep.ID, ep.FOOD_CATEGORY_DESC_ID, food_category_description)
    
    def save(self):
        self.click_element(ep.XPATH, ep.FOOD_CATEGORY_SAVE_XPATH)
        self.driver.implicitly_wait(5)