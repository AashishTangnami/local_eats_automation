from selenium.webdriver.common.by import By
from utils.element_path import ID, XPATH, SIGN_IN_XPATH
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def handle_captcha(self, locator_type, locator_value):
        """Method to handle CAPTCHA manually."""
        try:
            iframe_element = self.wait.until(
                EC.presence_of_element_located((
                    locator_type, locator_value)))
            
            self.driver.switch_to.frame(iframe_element)
            input("Please solve the CAPTCHA manually, then press Enter to continue...")
            self.driver.switch_to.default_content()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error handling CAPTCHA: {e}")

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password, locator_type, locator_value):
        self.enter_text(ID, 'username', username)
        self.enter_text(ID, 'password', password)
        # handle_captcha(self, locator_type, locator_value)
        self.click_element(XPATH, SIGN_IN_XPATH)


