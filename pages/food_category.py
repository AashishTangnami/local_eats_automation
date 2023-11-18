from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

from .base_page import BasePage

class FoodCategory(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_food_category(self,locator_type, locator_value):
        self.click_element((locator_type, locator_value))
    
    def add_new_category(self):
        FOOD_CATGEGORY_NAME = 'Test Category'
        FOOD_CATGEGORY_FIELD_PATH = 'test/path'
        FOOD_CATEGORY_DESC = 'Test Description'
        FOOD_CATEGORY_DESC_PATH = 'test/description/path'
        self.click_element(self.ADD_NEW_CATEGORY)
        self.enter_text(self.FOOD_CATGEGORY_NAME, FOOD_CATGEGORY_NAME)  
        self.enter_text(self.FOOD_CATEGORY_DESC_PATH, FOOD_CATEGORY_DESC)
        self.click_element(self.SAVE_BUTTON)

    def save(self):
        self.click_element(self.SAVE_BUTTON)