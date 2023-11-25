from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_page import BasePage
from utils import element_path as ep



class MerchantInfo(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_merchant_info(self):
        self.click_element(ep.XPATH, ep.MERCHANT_NAV_XPATH)

    def navigate_to_resturant_info(self):
        self.click_element(ep.XPATH, ep.MERCHANT_RESTURANT_INFORMATION_XPATH)

    def navigate_to_informatin(self):
        self.click_element(ep.XPATH, ep.MERCHANT_INFORMATION_XPATH)
    
    def navigate_to_google_maps(self):
        self.click_element(ep.XPATH, ep.GOOGLE_MAPS_XPATH)

    def enter_merchnat_information(self, text):
        self.enter_text(ep.CLASS_NAME, ep.JTQE_EDITOR, text)
        self.save()


    
    def clear_input_field_if_not_empty(self, locator):
        try:
            input_element = self.wait.until(
                EC.visibility_of_element_located(
                    (locator)))
            if input_element.get_attribute("value") != "":
                input_element.clear()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error clearing input field: {e}")


    def automate_restaurant_info(self, restaurant_data):
        try:
            for field_id, data in restaurant_data.items():
                input_xpath = f"//*[@id='{field_id}']"
                self.clear_input_field_if_not_empty(input_xpath)  # Method from BasePage
                self.enter_text((By.XPATH, input_xpath), data)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error filling out restaurant data: {e}")
        

    def update_information(self, 
                           locator_type, 
                           locator_value, 
                           info_locator_type, 
                           info_locator_value, 
                           text=None):
        INFO = " This is test "
        self.click_element(locator_type, locator_value)
        self.enter_text(info_locator_type, info_locator_value, INFO)
        # self.click_element(ep.XPATH, SAVE_BUTTON_XPATH)


    def save(self):    
        self.click_element(ep.XPATH, ep.SAVE_BUTTON_XPATH)    