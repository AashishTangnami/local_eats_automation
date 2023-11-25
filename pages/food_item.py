
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import element_path as ep


class FoodItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_food_item(self):
        self.click_element(ep.XPATH, ep.FOOD_ITEM_NAV_XPATH)

    def enter_food_item_name(self, food_item_name):
        self.enter_text(ep.ID, ep.ADD_NEW_FOOD_ITEM_XPATH, food_item_name)
    
    def enter_food_item_description(self, food_item_description):
        self.enter_text(ep.CLASS_NAME, ep.FOOD_ITEM_SELECTOR, food_item_description)

    def select_addon_category(self, addon_category):
        BASE_XPATH = '//*[@id="forms"]/div[1]/div[2]/div[11]/ul'
        category_checkbox_xpath = f"{BASE_XPATH}/li[contains(text(), '{addon_category}')]/input[@type='checkbox']"
        self.click_element(ep.XPATH, category_checkbox_xpath)

    def select_addon_items(self, addon_items):
        pass
    def process_addon_options(self, addon_options, addon_category):
        for i in range(len(addon_category)):
            if addon_category[i] == addon_options['Addon Category Name']:
                if addon_options['Addon Type'] == 'Can Select Only One':
                    addon_options['Addon Items']
                    self.click_element(ep.XPATH, ep.addon_options['Addon Items'])
            elif addon_category[i] == addon_options['Addon Category Name']:
                if addon_options['Addon Type'] == 'Can Select Multiple':
                    addon_options['Addon Items']
            elif addon_category[i] == addon_options['Addon Category Name']:
                if addon_options['Addon Type'] == 'Custom':
                    addon_options['Addon Items']       
                self.select_size(addon_options[i])
            self.select_addon_category(addon_category[i])
            self.select_addon_items(addon_options[i])

        checkbox_xpath = f"//input[@type='checkbox' and following-sibling::text()[contains(., '{text}')]]"
        checkbox_element = self.driver.find_element(By.XPATH, checkbox_xpath)
        if not checkbox_element.is_selected():
            checkbox_element.click()

    def save_food_item(self):
        self.click_element(self.SAVE_BUTTON)