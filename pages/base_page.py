from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator_type, locator_value):
        element = self.wait.until(
            EC.presence_of_element_located(
                (locator_type, locator_value)
            )
        )
        element.click()

    def enter_text(self, locator_type, locator_value, text):
        try:
            # ele = self.wait.until(EC.)
            element = self.wait.until(
            EC.presence_of_element_located(
                (locator_type, locator_value)
                )
            )
            element.clear()
            element.send_keys(text)
        except AttributeError:
            raise Exception(f"Element with locator {locator_type} not found or not visible.")

    def select_by_option(self, locator_type, locator_value, option):
        select = Select(self.wait.until(
            EC.visibility_of_element_located(
                locator_type, locator_value)))
        select.select_by_visible_text(option)


    def close(self):
        """Method to close the browser."""
        self.driver.quit()
    # Add other common methods...
    