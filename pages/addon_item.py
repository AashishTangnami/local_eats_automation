
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import element_path as ep

class AddOnItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_addon_item(self):
        self.click_element(ep.XPATH, ep.ADDON_ITEM_NAV_XPATH) 

    def add_new_addon_item(self):
        self.click_element(ep.XPATH, ep.ADDON_NEW_ITEM_XPATH)

    def enter_addon_item_name(self, addon_item_name):
        self.enter_text(ep.ID, ep.ADD_ON_ITEM_NAME_ID, addon_item_name)

    def enter_addon_item_description(self, addon_item_description=None):
        self.enter_text(ep.ID, ep.ADD_ON_ITEM_DESC_ID, addon_item_description)

    def enter_addon_item_price(self, addon_item_price=None):
        self.enter_text(ep.ID, ep.ADDON_ITEM_PRICE_ID, addon_item_price)

    def select_addon_category(self, addon_category):
        try:
            # Find the common element using the provided XPath
            check_element = self.driver.find_element(By.XPATH, ep.ADDON_ITEM_CATEGORY_XPATH)
            self.driver.implicitly_wait(5)
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

    def save(self):   
        self.click_element(ep.XPATH, ep.ADDON_ITEM_SAVE)