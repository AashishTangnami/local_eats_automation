from pages.base_page import BasePage
from utils import element_path as ep

class Settings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_settings(self):
        self.click_element(ep.XPATH, ep.SETTINGS_NAV_XPATH)
    
    def enter_tax_rate(self, tax_rate='13'):
        self.enter_text(ep.ID, ep.MERCHANT_TAX_ID, tax_rate)

    def apply_merchant_tax(self):
        self.click_element(ep.ID, ep.MERCHANT_APPLY_TAX_ID)

    def enter_delivery_estimation(self, delivery_estimation):
        self.enter_text(ep.ID, ep.MERCHANT_DELIVERY_ESTIMATION_ID, delivery_estimation)
    
    def enter_delivery_distance(self, delivery_distance):
        self.enter_text(ep.ID, ep.MERCHANT_DELIVERY_DISTANCE_ID, delivery_distance)
    
    def select_timezone(self, timezone):
        self.select_by_option(ep.ID, ep.MERCHANT_TIMEZONE_ID, timezone)
    
    def apply_preorder(self):
        self.click_element(ep.XPATH, ep.MERCHANT_APPLY_PREORDER_XPATH)
    
    def save(self):
        self.click_element(ep.XPATH, ep.SAVE_SETTINGS_XPATH)