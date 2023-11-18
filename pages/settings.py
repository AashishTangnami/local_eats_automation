from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Settings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_settings(self):
        settings_xpath = "//*[@id='yw0']/li[3]"
        self.click_element((By.XPATH, settings_xpath))
    
    def upload_image(self):
        pass

    def order_options(self):
        NOTIFICATION = ''
        self.click_action(self.ORD, NOTIFICATION)

    def tax_options(self):
        TAX = ''
        AVG_ORDER_TIME = ''
        DELIVERY_DISTANCE = ''
        self.click_action(self.TAX, TAX)
        self.enter_text(self.TAX, TAX)
        self.enter_text(self.AVG_ORDER_TIME_PATH, AVG_ORDER_TIME)
        self.enter_text(self.DELIVERY_DISTANCE_PATH, DELIVERY_DISTANCE)
        self.click_action(self.APPLY_TAX)

    
    def select_time_zone(self):
        TIME_ZONE = ''
        self.click_action(self.TIME_ZONE, TIME_ZONE)

    
    def update_store_hours(self):
        pass    


    def select_accept_preorders(self):
        self.click_action(self.ACCEPT_PREORDERS)

    def save(self):
        self.click_action(self.SAVE_BUTTON)