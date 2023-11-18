
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FoodItem(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_food_item(self):
        food_item_xpath = "//*[@id='yw0']/li[1]"
        self.click_element((By.XPATH, food_item_xpath))


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
            self.click_action(self.REQUIRED_OPTION)
            self.select_by_option(self.ONLY_ONE_OPTION_PATH, ONLY_ONE_OPTION)
    
    def select_custom_options(self, required= None, CUSTOM_REQUIRED= None, ITEMS= None):
        if required and CUSTOM_REQUIRED:
            self.click_action(self.REQUIRED_OPTION)
            self.click_action(self.CUSTOM_REQUIRED)
            self.enter_text(self.ITEMS_REQUIRED, ITEMS)

    def select_multiple_options(self, required= None, MULTIPLE_REQUIRED= None, ITEMS= None):
        if required and MULTIPLE_REQUIRED:
            self.click_action(self.REQUIRED_OPTION)
            self.click_action(self.MULTIPLE_REQUIRED)
            self.enter_text(self.ITEMS_REQUIRED, ITEMS)


    def save_food_item(self):
        self.click_action(self.SAVE_BUTTON)