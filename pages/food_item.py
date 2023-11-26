
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import element_path as ep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException, TimeoutException, NoSuchElementException,
    ElementNotInteractableException, ElementClickInterceptedException, WebDriverException
)

class FoodItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_food_item(self):
        self.click_element(ep.XPATH, ep.FOOD_ITEM_NAV_XPATH)
        
    def add_new_food_item(self):
        self.click_element(ep.XPATH, ep.ADD_NEW_FOOD_ITEM_XPATH)
        self.driver.implicitly_wait(5)

    def enter_food_item_name(self, food_item_name):
        self.enter_text(ep.ID, ep.FOOD_ITEM_NAME_ID, food_item_name)
    
    def enter_food_item_description(self, food_item_description):
        self.enter_text(ep.CLASS_NAME, ep.FOOD_ITEM_SELECTOR, food_item_description)

    def enter_food_item_price(self, food_item_price):
        self.enter_text(ep.ID, ep.FOOD_ITEM_PRICE_ID, food_item_price)
    
    def select_food_category(self, food_category):
        try:
            # Find the common element using the provided XPath
            check_element = self.driver.find_element(By.XPATH, ep.FOOD_ITEM_ADDON_CATEGORY_XPATH)
            # Find all checkbox inputs within the element
            checkbox_inputs = check_element.find_elements(By.XPATH, './/ul/li')

            if checkbox_inputs:
                food_category_name = food_category['Food Category']
                found_checkbox = False

                for label in checkbox_inputs:
                    label_text = label.text.strip()
                    if food_category_name in label_text:
                        checkbox_input = label.find_element(By.XPATH, './/input[@type="checkbox"]')
                        checkbox_input.click()
                        found_checkbox = True
                        break

                if not found_checkbox:
                    print(f"Food category '{food_category_name}' not found.")
            else:
                print("No checkboxes found within the element.")

        except Exception as e:
            print(f"Select Food Categgory An error occurred: {str(e)}")

    def select_addon_category(self, food_item):
        for addon_category in food_item[0]['Addon Category']:
            addon_name = addon_category['Addon Category Name']
            addon_type = addon_category['Addon Type']
            required = addon_category['Required']
            custom_value = addon_category['Custom Value']

            # Locate the addon category element by its name
            addon_category_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//b[contains(text(), '{addon_name}')]/ancestor::div[@class='uk-grid']"))
            )
            
            # Select the dropdown option
            select_element = Select(addon_category_element.find_element(By.CLASS_NAME, "multi_option"))
            select_element.select_by_visible_text(addon_type)

            if addon_type in ['Can Select Only One', 'Can Select Multiple']:
                if required:
                    required_checkbox = addon_category_element.find_element(By.CLASS_NAME, "require_addon")
                    if not required_checkbox.is_selected():
                        required_checkbox.click()
                check_all_checkbox = addon_category_element.find_element(By.CLASS_NAME, "check_all")
                if not check_all_checkbox.is_selected():
                    check_all_checkbox.click()

            elif addon_type == 'Custom':
                check_all_checkbox = addon_category_element.find_element(By.CLASS_NAME, "check_all")
                if not check_all_checkbox.is_selected():
                    check_all_checkbox.click()

                custom_input = addon_category_element.find_element(By.CLASS_NAME, "numeric_only")
                if not check_all_checkbox.is_selected():
                    check_all_checkbox.click()
                custom_input.send_keys(custom_value)
    '''
    def select_addon_category(self, food_item):
        for addon_category in food_item[0]['Addon Category']:
            addon_name = addon_category['Addon Category Name']
            addon_type = addon_category['Addon Type']
            required = addon_category['Required']
            custom_value = addon_category.get('Custom Value', '')

            addon_category_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, f"//b[contains(text(), '{addon_name}')]/ancestor::div[@class='uk-grid']/ancestor::li"))
            )

            for element in addon_category_elements:
                select_element = Select(element.find_element(By.CLASS_NAME, "multi_option"))
                select_element.select_by_visible_text(addon_type)

                if required:
                    try:
                        required_checkbox = element.find_element(By.CLASS_NAME, "require_addon")
                        if not required_checkbox.is_selected():
                            required_checkbox.click()
                    except NoSuchElementException:
                        print(f"Required checkbox not found for {addon_name}")

                if addon_type in ['Can Select Only One', 'Can Select Multiple']:
                    check_all_checkbox = element.find_element(By.CLASS_NAME, "check_all")
                    if not check_all_checkbox.is_selected():
                        check_all_checkbox.click()

                elif addon_type == 'Custom':
                    custom_input = element.find_element(By.CLASS_NAME, "numeric_only")
                    custom_input.clear()
                    custom_input.send_keys(custom_value)
    '''
                    
    def save(self):
        self.click_element(ep.XPATH, ep.SAVE_FOOD_ITEM_BUTTON_XPATH)
