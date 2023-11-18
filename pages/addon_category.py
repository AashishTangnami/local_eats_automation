
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddOnCateogry(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_addon_category(self, locator_type, locator_value):
        self.click_element((locator_type, locator_value))

    def new_addon_cateogry(self):
        self.enter_text(self.ADDON_CATEGORY_NAME, "Test Addon Category")
        self.enter_text(self.ADDON_CATEGORY_DESC, "Test Description")
    
    def save(self):
        self.click_element(self.SAVE_BUTTON)