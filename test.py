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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


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


# def addon_category(driver):
#     print('Addon Category==================')
#     category_addon = AddOnCateogry(driver)
#     category_addon.click_element(ep.XPATH, ep.ADDON_CATEGORY_NAV_XPATH)
#     category_addon.click_element(ep.XPATH, ep.ADDON_NEW_FOOD_CATEGORY_XPATH)
#     category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_ID, "Test Category")
#     category_addon.enter_text(ep.ID, ep.ADDON_CATEGORY_DESC_ID, "Test Description")
#     category_addon.click_element(ep.XPATH, ep.ADD_ON_CATEGORY_SAVE)
#     print("---------Addon Category Successful")

def addon_category(driver, categories):
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

# def addon_item(driver):
#     print('Addon Item====================')
#     addon_item_obj = AddOnItem(driver)
#     addon_item_obj.click_element(ep.XPATH, ep.ADDON_ITEM_NAV_XPATH)
#     addon_item_obj.click_element(ep.XPATH, ep.ADDON_NEW_ITEM_XPATH)
#     addon_item_obj.enter_text(ep.ID, ep.ADD_ON_ITEM_NAME_ID, "Test Category Addon")
#     addon_item_obj.enter_text(ep.ID, ep.ADD_ON_ITEM_DESC_ID, "Test Description Addon")
#     addon_item_obj.enter_text(ep.ID, ep.ADDON_ITEM_PRICE_ID, "10.00")
#     addon_item_obj.click_element(ep.XPATH, ep.ADDON_ITEM_SAVE)
#     print("---------Addon Item Successful")


def addon_item(driver, addon_items):
    """
    Create multiple add-on items and associate them with addon categories.

    :param driver: The webdriver instance.
    :param addon_items: A list of dictionaries. Each dictionary contains the name,
                        description, price of the addon item, and a list of associated categories.
    """
    print('Addon Item Creation====================')

    addon_item_obj = AddOnItem(driver)
    addon_item_obj.click_element(ep.XPATH, ep.ADDON_ITEM_NAV_XPATH)

    for item in addon_items:
        name = item.get("name")
        description = item.get("description")
        price = item.get("price")
        categories = item.get("categories", [])

        if not name or not description or not price:
            print(f"Invalid addon item data: {name}, {description}, {price}. Skipping.")
            continue

        addon_item_obj.click_element(ep.XPATH, ep.ADDON_NEW_ITEM_XPATH)
        addon_item_obj.enter_text(ep.ID, ep.ADD_ON_ITEM_NAME_ID, name)
        addon_item_obj.enter_text(ep.ID, ep.ADD_ON_ITEM_DESC_ID, description)
        addon_item_obj.enter_text(ep.ID, ep.ADDON_ITEM_PRICE_ID, price)

        # Select categories for the item
        for category in categories:
            addon_item_obj.select_category(category)

        addon_item_obj.click_element(ep.XPATH, ep.ADDON_ITEM_SAVE)
        print(f"Created addon item: {name}")

    print("---------Addon Item Creation Successful")

def select_category(self, category_name):
        """
        Select an add-on category for the item.

        :param category_name: The name of the category to select.
        """
        try:
            # Construct the XPath to find the checkbox for the given category name
            # We are using the following-sibling axis in XPath to find the checkbox 
            # based on the category name text
            checkbox_xpath = f"//ul[@class='uk-list uk-list-striped']/li[contains(text(), '{category_name}')]/input[@type='checkbox']"
            
            # Wait for the checkbox to be present and clickable
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, checkbox_xpath))
            )

            # Find the checkbox element and click it
            checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
            if not checkbox.is_selected():
                checkbox.click()
        except (NoSuchElementException, TimeoutException):
            print(f"Category '{category_name}' not found or checkbox not clickable.")


def food_item(driver):
    print('Food Item====================')
    food_item_obj = FoodItem(driver)
    food_item_obj.navigate_to_food_item(ep.XPATH, ep.FOOD_ITEM_NAV_XPATH)
    food_item_obj.click_element(ep.XPATH, ep.ADD_NEW_FOOD_ITEM_XPATH)
    food_item_obj.enter_text(ep.ID, ep.FOOD_ITEM_NAME_ID, "Test Food Item")
    food_item_obj.enter_text(ep.CLASS_NAME, ep.FOOD_ITEM_SELECTOR, "Test Description")
    # logics 
    food_item_obj.click_element(ep.XPATH, ep.FOOD_ITEM_SAVE)
    print("---------Food Item Successful")


'''<div class="uk-form-row">
	  <label class="uk-form-label uk-h3">Food Category</label>  
	  <div class="clear"></div>
	  	  <ul class="uk-list uk-list-striped">
	  	    <li>
	    <input value="95" data-validation="checkbox_group" data-validation-qty="min1" type="checkbox" name="category[]" id="category">	    Starters &amp; Sides	    </li>
	  	    <li>
	    <input value="96" data-validation="checkbox_group" data-validation-qty="min1" type="checkbox" name="category[]" id="category">	    Gourmet Pizzas	    </li>
	  	    <li>
	    <input value="98" data-validation="checkbox_group" data-validation-qty="min1" type="checkbox" name="category[]" id="category">	    Panzerottos	    </li>
	  	    <li>
	    <input value="2502" data-validation="checkbox_group" data-validation-qty="min1" type="checkbox" name="category[]" id="category">	    Test Category	    </li>
	  	  </ul>
	  	</div>
    '''

'''<ul class="uk-list uk-list-striped">
	 	 	 	 <li>
	    <div class="uk-grid">
	      <div class="uk-width-1-3">
	       <b>FINAL CATE</b>
	      </div>
	      <div class="uk-width-1-3">
	      <select class="multi_option" data-id="23" name="multi_option[23][]" id="multi_option_23">
<option value="one" selected="selected">Can Select Only One</option>
<option value="multiple">Can Select Multiple</option>
<option value="custom">Custom</option>
</select>	      </div>
	      <div class="uk-width-1-3">
	      	      <input class="numeric_only multi_option_value " type="text" value="" name="multi_option_value[23][]" id="multi_option_value_23">	      </div>
	      	      	      
	      <div class="uk-width-1-3">
	       <select class="two_flavors_position" data-id="23" name="two_flavors_position[23][]" id="two_flavors_position_23" style="display: none;">
<option value="" selected="selected"></option>
<option value="left">left</option>
<option value="right">Right</option>
</select>	      </div>
	    </div>
	 </li>
	 
	   <!--required add on-->	   
	   <li>
	   Required? 	   <input class="require_addon" value="2" type="checkbox" name="require_addon[23][]" id="require_addon_23">	   
	   &nbsp;&nbsp;
	   Check all/uncheck	   <input class="check_all" value="23" type="checkbox" name="check_all" id="check_all">	   
	   </li>
	   
	   	    <ul class="uk-list uk-list-striped">
	     	     <li>
	      	      <input value="80" class="check_all_23" type="checkbox" name="sub_item_id[23][]" id="sub_item_id_23">	      FINAL ADD ON ITEM ($16.00)	     </li>
	     	    </ul>
	   	 	 	 	 <li>
	    <div class="uk-grid">
	      <div class="uk-width-1-3">
	       <b>Test Category</b>
	      </div>
	      <div class="uk-width-1-3">
	      <select class="multi_option" data-id="39" name="multi_option[39][]" id="multi_option_39">
<option value="one" selected="selected">Can Select Only One</option>
<option value="multiple">Can Select Multiple</option>
<option value="custom">Custom</option>
</select>	      </div>
	      <div class="uk-width-1-3">
	      	      <input class="numeric_only multi_option_value " type="text" value="" name="multi_option_value[39][]" id="multi_option_value_39">	      </div>
	      	      	      
	      <div class="uk-width-1-3">
	       <select class="two_flavors_position" data-id="39" name="two_flavors_position[39][]" id="two_flavors_position_39" style="display: none;">
<option value="" selected="selected"></option>
<option value="left">left</option>
<option value="right">Right</option>
</select>	      </div>
	    </div>
	 </li>
	 
	   <!--required add on-->	   
	   <li>
	   Required? 	   <input class="require_addon" value="2" type="checkbox" name="require_addon[39][]" id="require_addon_39">	   
	   &nbsp;&nbsp;
	   Check all/uncheck	   <input class="check_all" value="39" type="checkbox" name="check_all" id="check_all">	   
	   </li>
	   
	   	    <ul class="uk-list uk-list-striped">
	     	     <li>
	      	      <input value="133" class="check_all_39" type="checkbox" name="sub_item_id[39][]" id="sub_item_id_39">	      test addon item 1 ($12.00)	     </li>
	     	    </ul>
	   	 	 	 	 <li>
	    <div class="uk-grid">
	      <div class="uk-width-1-3">
	       <b>test category 2</b>
	      </div>
	      <div class="uk-width-1-3">
	      <select class="multi_option" data-id="40" name="multi_option[40][]" id="multi_option_40">
<option value="one" selected="selected">Can Select Only One</option>
<option value="multiple">Can Select Multiple</option>
<option value="custom">Custom</option>
</select>	      </div>
	      <div class="uk-width-1-3">
	      	      <input class="numeric_only multi_option_value " type="text" value="" name="multi_option_value[40][]" id="multi_option_value_40">	      </div>
	      	      	      
	      <div class="uk-width-1-3">
	       <select class="two_flavors_position" data-id="40" name="two_flavors_position[40][]" id="two_flavors_position_40" style="display: none;">
<option value="" selected="selected"></option>
<option value="left">left</option>
<option value="right">Right</option>
</select>	      </div>
	    </div>
	 </li>
	 
	   <!--required add on-->	   
	   <li>
	   Required? 	   <input class="require_addon" value="2" type="checkbox" name="require_addon[40][]" id="require_addon_40">	   
	   &nbsp;&nbsp;
	   Check all/uncheck	   <input class="check_all" value="40" type="checkbox" name="check_all" id="check_all">	   
	   </li>
	   
	   	 	 	 	 <li>
	    <div class="uk-grid">
	      <div class="uk-width-1-3">
	       <b>test category 3 </b>
	      </div>
	      <div class="uk-width-1-3">
	      <select class="multi_option" data-id="41" name="multi_option[41][]" id="multi_option_41">
<option value="one" selected="selected">Can Select Only One</option>
<option value="multiple">Can Select Multiple</option>
<option value="custom">Custom</option>
</select>	      </div>
	      <div class="uk-width-1-3">
	      	      <input class="numeric_only multi_option_value " type="text" value="" name="multi_option_value[41][]" id="multi_option_value_41">	      </div>
	      	      	      
	      <div class="uk-width-1-3">
	       <select class="two_flavors_position" data-id="41" name="two_flavors_position[41][]" id="two_flavors_position_41" style="display: none;">
<option value="" selected="selected"></option>
<option value="left">left</option>
<option value="right">Right</option>
</select>	      </div>
	    </div>
	 </li>
	 
	   <!--required add on-->	   
	   <li>
	   Required? 	   <input class="require_addon" value="2" type="checkbox" name="require_addon[41][]" id="require_addon_41">	   
	   &nbsp;&nbsp;
	   Check all/uncheck	   <input class="check_all" value="41" type="checkbox" name="check_all" id="check_all">	   
	   </li>
	   
	   	 	 	 	 <li>
	    <div class="uk-grid">
	      <div class="uk-width-1-3">
	       <b>test category 5</b>
	      </div>
	      <div class="uk-width-1-3">
	      <select class="multi_option" data-id="42" name="multi_option[42][]" id="multi_option_42">
<option value="one" selected="selected">Can Select Only One</option>
<option value="multiple">Can Select Multiple</option>
<option value="custom">Custom</option>
</select>	      </div>
	      <div class="uk-width-1-3">
	      	      <input class="numeric_only multi_option_value " type="text" value="" name="multi_option_value[42][]" id="multi_option_value_42">	      </div>
	      	      	      
	      <div class="uk-width-1-3">
	       <select class="two_flavors_position" data-id="42" name="two_flavors_position[42][]" id="two_flavors_position_42" style="display: none;">
<option value="" selected="selected"></option>
<option value="left">left</option>
<option value="right">Right</option>
</select>	      </div>
	    </div>
	 </li>
	 
	   <!--required add on-->	   
	   <li>
	   Required? 	   <input class="require_addon" value="2" type="checkbox" name="require_addon[42][]" id="require_addon_42">	   
	   &nbsp;&nbsp;
	   Check all/uncheck	   <input class="check_all" value="42" type="checkbox" name="check_all" id="check_all">	   
	   </li>
	   
	   	 	</ul>
            '''
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
    
    addon_items = [
    {
        "name": "Test Category Addon 1",
        "description": "Test Description Addon 1",
        "price": "10.00",
        "categories": ["FINAL CATE", "Test Category"]
    },
    {
        "name": "Test Category Addon 2",
        "description": "Test Description Addon 2",
        "price": "15.00",
        "categories": ["test category 2"]
    },
    # Add more items as needed
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
    addon_item(driver, addon_items)
    food_item(driver)

if __name__ == '__main__':
    main()
