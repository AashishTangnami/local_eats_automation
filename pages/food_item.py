
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FoodItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_food_item(self, locator_type, locator_value):
        self.click_element((locator_type, locator_value))


    def add_food_item_name(self):
        self.enter_text(self.FOOD_ITEM_NAME, "Test Food Item")  
        self.enter_text(self.FOOD_ITEM_DESC, "Test Description")    

    def select_food_category(self):
        self.select_by_option(self.FOOD_CATEGORY, "Test Category")
    
    def add_food_item_price(self):
        self.enter_text(self.FOOD_ITEM_PRICE, "10.00")


    def add_food_item_size(self, SIZE= None):
        self.select_by_option(self.FOOD_ITEM_SIZE, "Test Size")
        
            
    def select_only_one_option(self, required= None):
        ONLY_ONE_OPTION_PATH = '//*[@id="FoodItemForm"]/div[5]/div[2]/div[1]/div/label'
        ONLY_ONE_OPTION = 'Can Select Only One'
        if required:
            self.click_element(self.REQUIRED_OPTION)
            self.select_by_option(self.ONLY_ONE_OPTION_PATH, ONLY_ONE_OPTION)
    
    def select_custom_options(self, required= None, CUSTOM_REQUIRED= None, ITEMS= None):
        if required and CUSTOM_REQUIRED:
            self.click_element(self.REQUIRED_OPTION)
            self.click_element(self.CUSTOM_REQUIRED)
            self.enter_text(self.ITEMS_REQUIRED, ITEMS)

    def select_multiple_options(self, required= None, MULTIPLE_REQUIRED= None, ITEMS= None):
        if required and MULTIPLE_REQUIRED:
            self.click_element(self.REQUIRED_OPTION)
            self.click_element(self.MULTIPLE_REQUIRED)
            self.enter_text(self.ITEMS_REQUIRED, ITEMS)


    def save_food_item(self):
        self.click_element(self.SAVE_BUTTON)