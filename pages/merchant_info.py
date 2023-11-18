from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_page import BasePage
from utils.element_path import MERCHANT_INFO, SAVE_BUTTON


class MerchantInfo(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_restaurant_info(self, locator_type, locator_value):
        self.click_action(locator_type, locator_value)

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
        

    def automate_information(self):
        INFO = " This is test "
        self.click_action(By.XPATH, MERCHANT_INFO)
        self.enter_text(By.LINK_TEXT, INFO)
        self.click_action(SAVE_BUTTON)

    def google_maps(self):
        LATTITUDE = ''
        LONGITUDE = ''
        self.click_action(self.GOOGLE_MAPS_TAB)
        self.enter_text(self.GOOGLE_MAPS_XPATH, LATTITUDE)
        self.enter_text(self.GOOGLE_MAPS_XPATH, LONGITUDE)

    def save(self):    
        self.click_action(By.XPATH, SAVE_BUTTON)    