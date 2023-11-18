
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddOnCateogry(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_addon_category(self):
        addon_category_xpath = "//*[@id='yw0']/li[3]"
        self.click_element((By.XPATH, addon_category_xpath))

    def new_addon_cateogry(self):
        self.enter_text(self.ADDON_CATEGORY_NAME, "Test Addon Category")
        self.enter_text(self.ADDON_CATEGORY_DESC, "Test Description")
    
    def save(self):
        self.click_action(self.SAVE_BUTTON)