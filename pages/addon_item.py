
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddOnItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_addon_item(self, locator_type, locator_value):
        self.click_element(locator_type, locator_value) 

    def new_addon_item(self):
        self.enter_text(self.ADDON_ITEM_NAME, "Test Addon Item")
        self.enter_text(self.ADDON_ITEM_DESC, "Test Description")
        self.enter_text(self.ADDON_ITEM_PRICE, "10.00")
        self.select_by_option(self.SELECT_BY_OPTION, "option")
        
    def save(self):   
        self.click_element(self.SAVE_BUTTON)