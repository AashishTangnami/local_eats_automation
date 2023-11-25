from selenium.webdriver.common.by import By


############################# ELEMENT PATHS #############################
ID = By.ID
XPATH = By.XPATH
LINKTEXT = By.LINK_TEXT
CSS_SELECTOR = By.CSS_SELECTOR
CLASS_NAME = By.CLASS_NAME
NAME = By.NAME
TAG_NAME = By.TAG_NAME


############################# ELEMENT PATHS #############################
RECAPTCHA = "iframe[title='reCAPTCHA']"
SIGN_IN_XPATH = '//*[@id="forms"]/div[4]/button'
RESTRO_INFO_SAVE_XPATH = '//*[@id="forms"]/div/input'
MERCHANT_INFO_XPATH = '//*[@id="forms"]/div/input'
SAVE_BUTTON_XPATH = '//*[@id="forms"]/div/input'
SAVE_CSS_SELECTOR = "input[type='submit']"
JTQE_TOOL_ICON = 'jqte_tool_icon' #class name
JTQE_EDITOR = 'jqte_editor' #class name

###################### MENU NAVIGATION PATHS ######################
MERCHANT_NAV_XPATH = '//*[@id="yw0"]/li[2]/a'
SETTINGS_NAV_XPATH = '//*[@id="yw0"]/li[3]/a'
FOOD_CATEGORY_NAV_XPATH = '//*[@id="yw0"]/li[6]/a'
ADDON_CATEGORY_NAV_XPATH = '//*[@id="yw0"]/li[9]/a'
ADDON_ITEM_NAV_XPATH = '//*[@id="yw0"]/li[10]/a'
FOOD_ITEM_NAV_XPATH = '//*[@id="yw0"]/li[13]/a'

###### ---------------------------------- ######
MERCHANT_INFORMATION_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/ul/li[2]/a'
'//*[@id="yw0"]/li[2]/a'
'//*[@id="merchant"]/div[2]/div[2]/div/div[2]/ul/li[2]/a'
GOOGLE_MAPS_XPATH = '//*[@id="tab-content"]/li[4]/div[3]/a'
MERCHANT_RESTURANT_INFORMATION_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/ul/li[1]/a'
TAB_CONTENT = '//*[@id="tab-content"]/li[2]/div/div[3]/p[3]'
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



GET_CORDINATES = '//*[@id="tab-content"]/li[4]/div[3]/a'



################## SETTINGS ELEMENT PATH BY ID ##################
ORDER_VERIFICATION_NOTIFICATION_ID = 'order_verification'
OTP_CODE_WAIT_TIME_ID = 'order_sms_code_waiting' # DEFAULT 5 MINS
MERCHANT_TAX_NUMBER_ID = 'merchant_tax_number'
MERCHANT_APPLY_TAX_ID = 'merchant_apply_tax'
MERCHANT_TAX_ID = 'merchant_tax'
MERCHANT_TIMEZONE_ID = 'merchant_timezone'
MERCHANT_PREORDER_ID = 'merchant_preorder'
MERCHANT_APPLY_PREORDER_XPATH = '//*[@id="forms"]/div[43]/div'
MERCHANT_DELIVERY_ESTIMATION_ID ='merchant_delivery_estimation'
MERCHANT_DELIVERY_DISTANCE_ID = 'merchant_delivery_miles'
SAVE_SETTINGS_XPATH = '//*[@id="forms"]/div[47]/input'

################## FOOD CATEGORY ELEMENT PATH ##################
ADD_NEW_FOOD_CATEGORY_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/div/a[1]'
ADD_NEW_FOOD_CATEGORY_CSS_SELECTOR = '#yw0 > li:nth-child(6)'
FOOD_CATEGORY_NAME_ID = 'category_name'
FOOD_CATEGORY_DESC_ID = 'category_description'
FOOD_CATEGORY_SAVE_XPATH = '//*[@id="forms"]/div/div[8]/input'


UPLOAD_IMAGE_ID = ''
SIZE_ADD_NEW_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/div/a[1]'
ADD_SIZE_NAME_ID = 'size_name'


################## ADDON CATEGORY ELEMENT PATH ##################
ADDON_NEW_FOOD_CATEGORY_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/div[1]/a[1]'
ADDON_CATEGORY_ID = 'subcategory_name'
ADDON_CATEGORY_DESC_ID = 'subcategory_description'
ADD_ON_CATEGORY_SAVE = '//*[@id="forms"]/div[4]/input'

################## ADDON ITEM ELEMENT PATH ##################
# ADDON_ITEM_NAV_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/div/a[1]'
ADDON_NEW_ITEM_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/div/a[1]'
ADD_ON_ITEM_NAME_ID = 'sub_item_name'
ADD_ON_ITEM_DESC_ID = 'item_description'
ADDON_ITEM_PRICE_ID = 'price'
ADDON_ITEM_CATEGORY_XPATH = '//*[@id="forms"]/div[1]/div[2]'
ADDON_ITEM_SAVE = '//*[@id="forms"]/div[3]/input'

################## FOOD ITEM ELEMENT PATH ##################
FOOD_ITEM_NAME_ID = 'item_name'
ADD_NEW_FOOD_ITEM_XPATH = '//*[@id="merchant"]/div[2]/div[2]/div/div[2]/div/a[1]'
'jqte_tool_icon unselectable'
FOOD_ITEM_SELECTOR = 'jqte_editor'
FOOD_ITEM_SAVE = '//*[@id="forms"]/div[3]/input'


MULTI_OPTION_21 = 'multi_option_21'
MULTI_OPTION_22 = 'multi_option_22'

