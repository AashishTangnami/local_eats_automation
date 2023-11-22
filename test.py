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
    merchant_page.navigate_to_restaurant_info(ep.XPATH, ep.MERCHANT_NAV_XPATH)
    merchant_page.update_information(ep.XPATH, ep.MERCHANT_INFORMATION_XPATH, 
                                     ep.CLASS_NAME, ep.JTQE_EDITOR)
    merchant_page.save(ep.XPATH, ep.SAVE_BUTTON_XPATH)
    print("---------Merchant Info Successful")

def settings(driver):
    print('Settings=====================')
    settings = Settings(driver)
    settings.navigate_to_settings(ep.XPATH, ep.SETTINGS_NAV_XPATH)

    print(" Ignoring image upload ")

    settings.enter_text(ep.ID, ep.MERCHANT_TAX_ID, "13")
    settings.click_element(ep.ID, ep.MERCHANT_APPLY_TAX_ID)
    settings.enter_text(ep.ID, ep.MERCHANT_DELIVERY_ESTIMATION_ID, "30 Mins")
    settings.enter_text(ep.ID, ep.MERCHANT_DELIVERY_DISTANCE_ID, "15")
    settings.select_by_option(ep.ID, ep.MERCHANT_TIMEZONE_ID, "America/New_York")
    settings.click_element(ep.XPATH, ep.MERCHANT_APPLY_PREORDER_XPATH)
    settings.click_element(ep.XPATH, '//*[@id="forms"]/div[47]/input')
    print("---------Settings Successful")

def food_category(driver, categories):
    """
    Create multiple food categories, handling duplicates and invalid data.

    :param driver: The webdriver instance.
    :param categories: A list of tuples, each containing the category name and description.
    """
    print('Food Categories Creation================')

    food_category_obj = FoodCategory(driver)
    food_category_obj.navigate_to_food_category(ep.XPATH, ep.FOOD_CATEGORY_NAV_XPATH)

    processed_categories = set()  # To track categories in this request

    for name, description in categories:
        # Skip if the category is already processed in this request
        if name in processed_categories:
            print(f"Duplicate category in request: {name}. Skipping.")
            continue

        # Skip invalid categories
        if not name or not description:
            print(f"Invalid category data: {name}, {description}. Skipping.")
            continue

        # Check for existing categories in the database
        if food_category_obj.is_category_already_exists(name):
            print(f"Category '{name}' already exists in the database. Skipping.")
            continue

        # Add to the processed set
        processed_categories.add(name)

        # Create category
        food_category_obj.click_element(ep.XPATH, ep.ADD_NEW_FOOD_CATEGORY_XPATH)
        food_category_obj.enter_text(ep.ID, ep.FOOD_CATEGORY_NAME_ID, name)
        food_category_obj.enter_text(ep.ID, ep.FOOD_CATEGORY_DESC_ID, description)
        food_category_obj.save_category()

        print(f"Created category: {name}")

    print("---------Food Categories Creation Successful")


def addon_category(driver):
    print('Addon Category==================')
    category_addon = AddOnCateogry(driver)
    category_addon.click_element(ep.XPATH, ep.ADDON_CATEGORY_NAV_XPATH)
    category_addon.click_element(ep.XPATH, ep.ADDON_NEW_FOOD_CATEGORY_XPATH)
    category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_ID, "Test Category")
    category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_DESC_ID, "Test Description")
    category_addon.click_element(ep.XPATH, ep.ADD_ON_CATEGORY_SAVE)
    print("---------Addon Category Successful")

def create_addon_categories(driver, categories):
    """
    Create multiple addon categories.

    :param driver: The webdriver instance.
    :param categories: A list of tuples, each containing the category name and description.
    """
    print('Addon Categories Creation================')

    category_addon = AddOnCateogry(driver)
    category_addon.click_element(ep.XPATH, ep.ADDON_CATEGORY_NAV_XPATH)

    for name, description in categories:
        if not name or not description:
            print(f"Invalid addon category data: {name}, {description}. Skipping.")
            continue

        if category_addon.is_addon_category_already_exists(name):
            print(f"Addon category '{name}' already exists. Skipping.")
            continue

        category_addon.click_element(ep.XPATH, ep.ADDON_NEW_FOOD_CATEGORY_XPATH)
        category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_ID, name)
        category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_DESC_ID, description)
        category_addon.save_addon_category()

        print(f"Created addon category: {name}")

    print("---------Addon Categories Creation Successful")

def addon_item(driver):
    print('Addon Item====================')
    addon_item_obj = AddOnItem(driver)
    addon_item_obj.click_element(ep.XPATH, ep.ADDON_ITEM_NAV_XPATH)
    addon_item_obj.click_element(ep.XPATH, ep.ADDON_NEW_ITEM_XPATH)
    addon_item_obj.enter_text(ep.ID, ep.ADD_ON_ITEM_NAME_ID, "Test Category Addon")
    addon_item_obj.enter_text(ep.ID, ep.ADD_ON_ITEM_DESC_ID, "Test Description Addon")
    addon_item_obj.enter_text(ep.ID, ep.ADDON_ITEM_PRICE_ID, "10.00")
    addon_item_obj.click_element(ep.XPATH, ep.ADDON_ITEM_SAVE)
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



    category_entries = [
    # Valid entries
    ("Fresh Produce", "Fruits and vegetables"),
    ("Bakery", "Breads, pastries, and cakes"),
    ("Dairy", "Milk, cheese, and eggs"),

    # Duplicate entries (these should be skipped on processing)
    ("Fresh Produce", "Fruits, vegetables"),
    ("Bakery", "Fresh bread and pastries"),

    # Invalid entries (empty name or description)
    ("", "Empty name category"),
    ("Invalid Category", ""),
    (None, "None as category name"),
    ("None Description", None),

    # Entries with special characters
    ("Beverages & More", "Drinks, wines, and beers"),
    ("Frozen Foods", "Frozen meals and vegetables"),

    # Long name and description
    ("Gourmet and International Foods with a Variety of Choices", "A wide range of international cuisines and gourmet choices that cater to diverse taste preferences"),
]

    url = "https://fareeats.coop/merchant/login"
    driver = DriverFactory.get_chrome_driver()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    login_page(driver)
    merchant_info(driver)
    settings(driver)
    # food_category(driver)

    # Pass these entries to the function
    food_category(driver, category_entries)

    addon_category(driver)
    addon_item(driver)
    food_item(driver)

if __name__ == '__main__':
    main()
