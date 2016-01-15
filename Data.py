# -*- coding: utf-8 -*-

searchData = 'scanners'
capcha = 'bInTimeCaPtChAfOrTeSTiNgpurPOses'
password = 'salamvsemvoram'

allCategoriesDropDown = "//div[@id='category_chzn']/a"
allCategoriesSearchField = '//*[@id="category_chzn"]//input'
searchButton = '//*[@id="searchbar"]//button'
categoryNameTextInfo = "//*[@id='search-info']"
scannersCategory = '//*[@id="wrap"]//div/ul/li[2]/a'
breadCrumbsXpath = ".//*[@id='search-results']/div[1]"
inStock = '//*[@id="filters-block"]/ul[1]//span'
addInStockRandomProduct = '//div[2]/div/div/div[2]//a[3]'

sussestionToAdd = '//ul/li/div/div'
shoppingCart = '//*[@id="cart-indicator"]/a[2]'
shoppingCartTitle = '//*[@id="main"]/h1'
proccedToCheckOutFirst = '//*[@id="cart-step4-form"]/div/button'
signInTitle = '//*[@id="main"]/h1'
firstNameField = '//*[@id="CustomerRegistrationForm_first_name"]'
lastNameField = '//*[@id="CustomerRegistrationForm_last_name"]'
emailField = '//*[@id="CustomerRegistrationForm_email"]'
passwordField = '//*[@id="CustomerRegistrationForm_password"]'
passwordFieldRetype = '//*[@id="CustomerRegistrationForm_verifyPassword"]'

businessRadioButton = '//*[@id="CustomerRegistrationForm_type"]/label[1]/span'
bussinessTypeForText = '//*[@id="CustomerRegistrationForm_type"]//label[1]/label'
companyField = "//*[@id='CustomerRegistrationForm_company']"
jobTitle = "//*[@id='CustomerRegistrationForm_job_title']"

postalCodeField = '//*[@id="CustomerRegistrationForm_postal_code"]'
phoneField = '//*[@id="CustomerRegistrationForm_phone"]'
addressLine1 = '//*[@id="CustomerRegistrationForm_address_1"]'
cityXPath = '//*[@id="CustomerRegistrationForm_city"]'

countrySelect = '//*[@id="CustomerRegistrationForm_country"]'

iAcceptCheckBox = '//*[@id="cart-billing-addr"]//div[25]/label/span'
capchaField = '//*[@id="CustomerRegistrationForm_verifyCode"]'
proccedToCheckOutSecond = '//*[@id="cart-registration-form"]/div[3]/button'

userSuccessfullyLogIn = '//*[@id="user-greeting"]'
chooseShippingPaymentMethod = '//*[@id="main"]/h1'

#Shipping method radiobuttons:
shipingMethodFirst = '//*[@id="ship_express_shipment_UK"]//span[2]'
shipingMethodSecond = '//*[@id="ship_Location"]//span[2]'
shippingMethodThird = '//*[@id="ship_standart_shipment_EU"]//span[2]'

#Payment method radiobuttons:
paymentMethodFirst = '//*[@id="cart-step3"]//div[1]/label[2]/span[2]'
paymentMethodSecond = '//*[@id="cart-step3"]//div[4]//span[2]'

confirmOrderButton = '//*[@id="cart-step3"]/div[3]/button'
checkAllDetails = '//*[@id="main"]/h1'
placeOrderButton = '//form/div/button'
purchaseCheck = '//*[@id="main"]/h1'
orderId = '//section[2]/p/b'
logOutButton = '//*[@id="user-links"]/a'

#BO Data
boEmailData = 'admin'
boPasswordData = 'admin'

userFirstName = 'Nikita'
userLastName = 'Asus'
userCompany = 'TestCompany'

boOrdersButton = '//nav/ul/li[1]/div/a'
boOrdersManagementButton = '//nav/ul/li[1]//ul/li//a'

boOrderIdField = '//div[1]/div[1]/input'
boOrderIdResult = '//table[2]//tr[1]/td[2]'

boEmailField = 'UserLogin_username'
boPasswordField = 'UserLogin_password'
boLoginButton = '//*[@id="login-form"]/div[6]/input'
customersButton = '//*[@id="top"]//nav/ul/li[3]/div/a'
customersManagementButton = '//*[@id="top"]/nav/ul/li[3]//li/div/a'

cusManageSearchButton = '//*[@id="customer-grid"]//td[2]/button'
cusManageResetButton = '//*[@id="reset-button-customer-grid"]'
emptyTableClicking = '//*[@id="customer-grid"]/div[1]/div'

fnBoField = '//*[@id="Customer_first_name"]'
boFirstNameForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[2]'
boFirtsNameColumnName = '//*[@id="customer-grid_c1"]//a'

lnBoField = '//*[@id="Customer_last_name"]'
boLastNameForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[3]'
boLastNameColumnName = '//*[@id="customer-grid_c2"]//a'

phoneBOField = '//*[@id="Customer_phone"]'
boPhoneForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[4]'
boPhoneColumnName = '//*[@id="customer-grid_c3"]//a'

emailBoField = '//*[@id="Customer_email"]'
boEmailForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[5]'
boEmailColumnName = '//*[@id="customer-grid_c4"]//a'

countryBoField = '//*[@id="Customer_country"]'
boCountryForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[6]'
boCountryColumnName = '//*[@id="customer-grid_c5"]//a'

companyBOField = '//*[@id="Customer_company"]'
boCompanyForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[7]'
boCompanyColumnName = '//*[@id="customer-grid_c6"]//a'

jobTitleBOField = '//*[@id="Customer_job_title"]'
boJobTitleForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[8]'
boJobTitleColumnName = '//*[@id="customer-grid_c7"]//a'

typeSelectDropDown = '//*[@id="Customer_type"]'
boTypeSelectDropDownForChecking = '//*[@id="customer-grid"]/table[2]/tbody/tr[1]/td[9]'
boTypeSelectDropDownColumnName = '//*[@id="customer-grid_c8"]//a'


#orders management data
boOrdersButton = '//*[@id="top"]//nav/ul/li[1]/div/a'
boOrdersManagementButton = '//*[@id="top"]//nav/ul/li[1]//li//a'

ordersManageSearchButton = '//*[@id="order-grid"]//td[2]/button'
ordersEmptyTable = '//section[2]/div/div/div/div[1]/div'
boOrdersResetButton = "//*[@id='reset-button-order-grid']"

boBillingFNameField = '//*[@id="MdOrder_billing_first_name"]'
ordersResultFirstName = '//*[@id="order-grid"]//tr[1]/td[4]'
ordersFirstNameColumnName = '//*[@id="order-grid_c3"]'

boBillingLNameField = "//*[@id='order-grid']//div[4]/input"
ordersResultLastName = '//*[@id="order-grid"]//tr[1]/td[5]'
ordersLastNameColumnName = '//*[@id="order-grid_c4"]'

boBillingCompanyField = "//*[@id='order-grid']//div[5]/input"
ordersResultCompany = '//*[@id="order-grid"]//tr[1]/td[6]'
ordersCompanyColumnName = '//*[@id="order-grid_c5"]'

boCreatedAtField = '//*[@id="MdOrder_dateCreatedSearch"]'
ordersResultCreatedAt = '//*[@id="order-grid"]//tr[1]/td[3]'
ordersCreatedAtColumnName = '//*[@id="order-grid_c2"]'

boShipMethodSelect = "//*[@id='arOrder_shipping_method_title']"
boShipMethodSelectResult = "//*[@id='order-grid']//tr[1]/td[7]"


