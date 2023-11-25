from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import (
    StaleElementReferenceException, TimeoutException, NoSuchElementException,
    ElementNotInteractableException, ElementClickInterceptedException, WebDriverException
)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_element(self, locator_type, locator_value):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable(
                    (locator_type, locator_value)
                )
            )
            element.click()
        except (StaleElementReferenceException, TimeoutException, NoSuchElementException,
                ElementNotInteractableException, ElementClickInterceptedException, WebDriverException) as e:
            # Log the exception details here
            # print(f"Exception in click_element: {e}")
            try:
                # Retry logic, with a delay or a limit on retry attempts if necessary
                element = self.wait.until(
                    EC.element_to_be_clickable(
                        (locator_type, locator_value)
                    )
                )
                element.click()
            except (StaleElementReferenceException, TimeoutException, NoSuchElementException,
                ElementNotInteractableException, ElementClickInterceptedException, WebDriverException) as e:
                # Handle the case where the second attempt also fails
                # print(f"Retried click_element failed: {e}")
                pass

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
        dropdown = self.wait.until(
            EC.visibility_of_element_located((locator_type, locator_value)))
        select = Select(dropdown)
        select.select_by_visible_text(option)


    def close(self):
        """Method to close the browser."""
        self.driver.quit()
    # Add other common methods...
    