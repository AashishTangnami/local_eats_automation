
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import element_path as ep


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
            check_element = self.driver.find_element(By.XPATH, ep.FOOD_ITEM_FOOD_CATEGORY_XPATH)
            # Find all checkbox inputs within the element
            checkbox_inputs = check_element.find_elements(By.XPATH, './/ul/li/input[@type="checkbox"]')

            if checkbox_inputs:
                food_category_name = food_category['Food Category Name']
                found_checkbox = False

                for checkbox_input in checkbox_inputs:
                    label_text = checkbox_input.get_attribute('value').strip()
                    if food_category_name in label_text:
                        checkbox_input.click()
                        found_checkbox = True
                        break

                if not found_checkbox:
                    print(f"Food category '{food_category_name}' not found.")
            else:
                print("No checkboxes found within the element.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def select_food_item_addon_category(self, addon_category):
        try:
            # Find the common element using the provided XPath
            check_element = self.driver.find_element(By.XPATH, ep.FOOD_ITEM_ADDON_CATEGORY_XPATH)
            # Find all checkbox labels within the element
            checkbox_labels = check_element.find_elements(By.XPATH, './/ul/li')

            if checkbox_labels:
                addon_category_name = addon_category['Addon Category Name']
                found_checkbox = False

                for label in checkbox_labels:
                    label_text = label.text.strip()
                    if addon_category_name in label_text:
                        checkbox_input = label.find_element(By.XPATH, './/input[@type="checkbox"]')
                        checkbox_input.click()
                        found_checkbox = True
                        break

                if not found_checkbox:
                    print(f"Addon category '{addon_category_name}' not found.")
            else:
                print("No checkboxes found within the element.")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def select_food_item_addon_item(self, addon_items):
        try:
            for addon_item in addon_items:
                addon_item_name = addon_item['Addon Item Name']
                addon_category_name = addon_item['Addon Category Name']
                addon_category_element = self.driver.find_element(By.XPATH, f'//li[b[text()="{addon_category_name}"]]')

                addon_item_element = addon_category_element.find_element(
                    By.XPATH, f'.//input[@value="{addon_item_name}"]')
                addon_item_element.click()

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def save_food_item(self):
        self.click_element(ep.XPATH, ep.SAVE_FOOD_ITEM_BUTTON_XPATH)