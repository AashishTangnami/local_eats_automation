from selenium.webdriver.common.by import By
from utils.element_path import ID, XPATH, CSS_SELECTOR, SIGN_IN
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
  # This will load variables from .env


def handle_captcha(self):
        """Method to handle CAPTCHA manually."""
        try:
            iframe_element = self.wait.until(
                EC.presence_of_element_located((
                    CSS_SELECTOR, "iframe[title='reCAPTCHA']")))
            
            self.driver.switch_to.frame(iframe_element)
            input("Please solve the CAPTCHA manually, then press Enter to continue...")
            self.driver.switch_to.default_content()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error handling CAPTCHA: {e}")

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(ID, 'username', username)
        self.enter_text(ID, 'password', password)
        handle_captcha(self)
        self.click_action(XPATH, SIGN_IN)


