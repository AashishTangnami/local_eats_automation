import os
from dotenv import load_dotenv
from utils import element_path as ep
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from pages.merchant_info import MerchantInfo
from pages.settings import Settings
from pages.food_category import FoodCategory
from pages.addon_category import AddOnCateogry
from pages.food_item import FoodItem
from pages.addon_item import AddOnItem
from pages.food_item_size import FoodItemSize
from utils.data import food_categories, addon_categories, addon_item_values

def login_page(driver):
    load_dotenv()
    login_page = LoginPage(driver)
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')
    login_page.login(username, password, ep.CSS_SELECTOR, ep.RECAPTCHA)
    driver.implicitly_wait(10)
    print("---------Login Successful")

def merchant_info(driver):
    print('Merchant Info====================')
    merchant_page = MerchantInfo(driver)
    merchant_page.navigate_to_merchant_info()
    merchant_page.update_information(ep.XPATH, ep.MERCHANT_INFORMATION_XPATH, 
                                     ep.CLASS_NAME, ep.JTQE_EDITOR)
    merchant_page.save(ep.XPATH, ep.SAVE_BUTTON_XPATH)
    print("---------Merchant Info Successful")

def settings(driver):
    print('Settings=====================')
    settings_page = Settings(driver)
    settings_page.navigate_to_settings()

    print(" Ignoring image upload ")
    settings_page.enter_tax_rate("13")
    settings_page.apply_merchant_tax()
    settings_page.enter_delivery_estimation("30")
    settings_page.enter_delivery_distance("10")
    settings_page.select_timezone("America/Chicago")
    settings_page.apply_preorder()
    settings_page.save(ep.XPATH, ep.SAVE_SETTINGS_XPATH)
    print("---------Settings Successful")

# def food_category(driver, food_categories):
#     print('Food Category================')
#     food_category_obj = FoodCategory(driver)
#     for food_category in food_categories:
#         food_category_obj.navigate_to_food_category()
#         food_category_obj.add_new_food_category()
#         food_category_obj.enter_food_category_name(food_category)
#         food_category_obj.enter_food_category_description(food_category['Food Category Description'])
#         food_category_obj.save(ep.XPATH, ep.FOOD_CATEGORY_SAVE_XPATH)

#     print("---------Food Category Successful")
def food_category(driver, food_categories):
    print('Food Category================')
    food_category_obj = FoodCategory(driver)
    food_category_obj.navigate_to_food_category()
    for category_data in food_categories:

        category_name = category_data['Category Name']
        category_desc = category_data['Category Desc']
        food_category_obj.add_new_food_category()
        food_category_obj.enter_food_category_name(category_name)
        food_category_obj.enter_food_category_description(category_desc)  
        food_category_obj.save()

    print("---------Food Category Successful")

# def addon_category(driver):
#     print('Addon Category==================')
#     category_addon = AddOnCateogry(driver)
#     category_addon.click_element()
#     category_addon.click_element()
#     category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_ID, "Test Category")
#     category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_DESC_ID, "Test Description")
#     category_addon.click_element(ep.XPATH, ep.ADD_ON_CATEGORY_SAVE)
#     print("---------Addon Category Successful")
def addon_category(driver, addon_categories):
    print('Addon Category==================')
    category_addon = AddOnCateogry(driver)
    category_addon.navigate_to_addon_category()

    for addon_category in addon_categories:
        category_addon.add_new_addon_category()
        category_name = addon_category['Category Name']
        category_desc = addon_category['Category Desc']
        category_addon.enter_addon_category_name(category_name)
        category_addon.enter_addon_category_description(category_desc)
        category_addon.save()

    print("---------Addon Category Successful")


def addon_item(driver, addon_item_values):
    print('Addon Item====================')
    addon_item_page = AddOnItem(driver)
    addon_item_page.navigate_to_addon_item()

    addon_category_name = addon_item_values['Addon Category Name']
    addon_items = addon_item_values['Addon Items']
    for addon_item in addon_items:
        addon_item_page.add_new_addon_item()
        addon_item_page.enter_addon_item_name(addon_item)
        addon_item_page.enter_addon_item_description("")  # You can provide a description if needed
        addon_item_page.select_addon_category({'Addon Category Name': addon_category_name})
        addon_item_page.save()
    print("---------Addon Item Successful")

def food_item(driver):
    print('Food Item====================')
    food_item_obj = FoodItem(driver)
    food_item_obj.navigate_to_food_item(ep.XPATH, ep.FOOD_ITEM_NAV_XPATH)
    food_item_obj.click_element(ep.XPATH, ep.ADD_NEW_FOOD_ITEM_XPATH)
    food_item_obj.enter_text(ep.ID, ep.FOOD_ITEM_NAME_ID, "Test Food Item")
    food_item_obj.enter_text(ep.CLASS_NAME, ep.FOOD_ITEM_SELECTOR, "Test Description")
    food_item_obj.click_element(ep.XPATH, ep.FOOD_ITEM_SAVE)
    print("---------Food Item Successful")

def food_item_size(driver):
    food_item_size = FoodItemSize(driver)
    food_item_size.navigate_to_food_item_size(By.XPATH, ep.FOOD_ITEM_SIZE)
    # food_item_size.add_new_size()
    

def main():

    url = "https://fareeats.coop/merchant/login"
    driver = DriverFactory.get_chrome_driver()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    login_page(driver)
    merchant_info(driver)
    settings(driver)
    food_category(driver, food_categories)
    addon_category(driver, addon_categories)
    addon_item(driver, addon_item_values)
    food_item(driver)

if __name__ == '__main__':
    main()
