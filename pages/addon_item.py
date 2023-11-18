
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddOnItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_addon_item(self):
        addon_item_xpath = "//*[@id='yw0']/li[2]"
        self.click_element((By.XPATH, addon_item_xpath))    

    def new_addon_item(self):
        self.enter_text(self.ADDON_ITEM_NAME, "Test Addon Item")
        self.enter_text(self.ADDON_ITEM_DESC, "Test Description")
        self.enter_text(self.ADDON_ITEM_PRICE, "10.00")
        self.select_by_option(self.SELECT_BY_OPTION, "option")
        
    def save(self):   
        self.click_action(self.SAVE_BUTTON)