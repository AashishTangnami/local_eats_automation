from selenium.webdriver.common.by import By

ID = By.ID
XPATH = By.XPATH
LINKTEXT = By.LINK_TEXT
CSS_SELECTOR = By.CSS_SELECTOR
CLASS_NAME = By.CLASS_NAME
NAME = By.NAME
TAG_NAME = By.TAG_NAME


SIGN_IN_XPATH = '//*[@id="forms"]/div[4]/button'
RESTRO_INFO_SAVE_XPATH = '//*[@id="forms"]/div/input'
MERCHANT_INFO_XPATH = '//*[@id="forms"]/div/input'
SAVE_BUTTON_XPATH = '//*[@id="forms"]/div/input'
# //*[@id="forms"]/div/input
# //*[@id="forms"]/div/input
#//*[@id="forms"]/div/input
#//*[@id="forms"]/div[47]/input , 
SAVE_CSS_SELECTOR = "input[type='submit']"
JTQE_TOOL_ICON = 'jqte_tool_icon' #class name
JTQE_EDITOR = 'jqte_editor' #class name

## Main Pages Link - use element by link
MERCHANT_LINK_TEXT = "Merchant Info"
SETTINGS_LINK_TEXT = "Settings"
FOOD_CATEGORY_LINK_TEXT = "Food Category"
ADDON_CATEGORY_LINK_TEXT = "AddOn Category"
ADDON_ITEM_LINK_TEXT = "AddOn Item"
FOOD_ITEM_LINK_TEXT = "Food Item"

### Merchant Restaurant Info
RESTURANT_SLUG_ID = 'restaurant_slug'
RESTURANT_NAME_ID = 'restaurant_name'
RESTURANT_PHONE_ID = 'restaurant_phone'
RESTURANT_CONTACT_NAME_ID = 'contact_name'
RESTURANT_CONTACT_EMAIL_ID = 'contact_email'
RESTURANT_CONTACT_PHONE_ID = 'contact_phone'
RESTURANT_COUNTRY_ID = 'country_code'
RESTURANT_STREET_ADDRESS_ID = 'street'
RESTIRANT_CITY_ID = 'city'
RESTURANT_STATE_ID = 'state'
RESTURANT_ZIPCODE_ID = 'zipcode'
RESTURANT_CUISINE_ID = 'cuisine'
CUISINE_CHOOSEN_ID = 'cuisine_chosen'
SERVICE_PICKUP_DELIVERY_ID = 'service'

## SETTINGS

ORDER_VERIFICATION_NOTIFICATION_ID = 'order_verification'
OTP_CODE_WAIT_TIME_ID = 'order_sms_code_waiting' # DEFAULT 5 MINS
MERCHANT_TAX_ID = 'merchant_tax_number'
MARCHANT_APPLY_TAX_ID = 'merchant_apply_tax'
MERCHANT_TAX = 'merchant_tax'
MERCHANT_TIMEZONE_ID = 'merchant_timezone'
MERCHANT_PREORDER_ID = 'merchant_preorder'


### FOOD CATEGORY 
ADD_NEW_FOOD_CATEGORY_LINK_TEXT = 'Add New'
FOOD_CATEGORY_NAME_ID = 'category_name'
FOOD_CATEGORY_DESC_ID = 'category_description'


UPLOAD_IMAGE_ID = ''
SIZE_ADD_NEW_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/div/a[1]'
ADD_SIZE_NAME_ID = 'size_name'


# ADDON CATEGORY
ADDON_CATEGORY_ID = 'subcategory_name'
ADDON_CATEGORY_DESC_ID = 'subcategory_description'

# ADDON ITEM
ADD_ON_ITEM_NAME_ID = 'sub_item_name'
ADD_ON_ITEM_DESC_ID = 'item_description'
ADDON_ITEM_PRICE_ID = 'price'

## FOOD ITEM
FOOD_ITEM_NAME_ID = 'item_name'
'jqte_tool_icon unselectable'
FOOD_ITEM_SELECTOR = 'jqte_editor'

MULTI_OPTION_21 = 'multi_option_21'
MULTI_OPTION_22 = 'multi_option_22'

