
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import element_path as ep

class AddOnCateogry(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_addon_category(self):
        self.click_element(ep.XPATH, ep.ADDON_CATEGORY_NAV_XPATH)

    def add_new_addon_category(self):
        self.click_element(ep.XPATH, ep.ADDON_NEW_FOOD_CATEGORY_XPATH)

    def enter_addon_category_name(self, addon_category_name):
        self.enter_text(ep.ID, ep.ADDON_CATEGORY_ID, addon_category_name)
    
    def enter_addon_category_description(self, addon_category_description):
        self.enter_text(ep.ID, ep.ADDON_CATEGORY_DESC_ID, addon_category_description)
    
    def save(self):
        self.click_element(ep.XPATH, ep.ADD_ON_CATEGORY_SAVE)