import os
from pages.food_item_size import FoodItemSize
from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.merchant_info import MerchantInfo
from pages.settings import Settings
from utils.driver_factory import DriverFactory
from dotenv import load_dotenv
from utils import element_path as ep
from selenium.webdriver.common.by import By


load_dotenv()
def main():
    url = "https://fareeats.coop/merchant/login"
    driver = DriverFactory.get_chrome_driver()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    login_page = LoginPage(driver)
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    login_page.login(username, password)
    driver.implicitly_wait(10)

    food_item_size = FoodItemSize(driver)
    food_item_size.navigate_to_food_item_size(By.XPATH, ep.FOOD_ITEM_SIZE)
    food_item_size.add_new_size()
    # restaurant_data = {

    
    merchant_page = MerchantInfo(driver)
    merchant_page.navigate_to_restaurant_info(ep.XPATH, ep.MERCHANT_INFO)
    # # merchant_page.automate_restaurant_info(restaurant_data)
    merchant_page.automate_information()
    # merchant_page.google_maps()

    # settings = Settings(driver)

if __name__ == '__main__':
    main()
