from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Settings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_settings(self, locator_type, locator_value):
        self.click_element((locator_type, locator_value))
    
    def upload_image(self):
        pass

    def order_options(self, locator_type, locator_value):
        self.click_element(locator_type, locator_value)
        

    def tax_options(self):
        TAX = ''
        AVG_ORDER_TIME = ''
        DELIVERY_DISTANCE = ''
        self.click_element(self.TAX, TAX)
        self.enter_text(self.TAX, TAX)
        self.enter_text(self.AVG_ORDER_TIME_PATH, AVG_ORDER_TIME)
        self.enter_text(self.DELIVERY_DISTANCE_PATH, DELIVERY_DISTANCE)
        self.click_element(self.APPLY_TAX)

    
    def select_time_zone(self):
        TIME_ZONE = ''
        self.click_element(self.TIME_ZONE, TIME_ZONE)

    
    def update_store_hours(self):
        pass    


    def select_accept_preorders(self):
        self.click_element(self.ACCEPT_PREORDERS)

    def save(self):
        self.click_element(self.SAVE_BUTTON)