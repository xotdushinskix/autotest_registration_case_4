# -*- coding: utf-8 -*-
import json
import random
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
import Data
from RandomHelper import RandomHelper
from DBClass import DB
import unittest
import searchFunctions

dbClass = DB()
randomHelper = RandomHelper()


class MyTestCase(unittest.TestCase, RandomHelper):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://admin:skdf%24%23%26%26%25tg@gepard.bintime.com/')
        self.random_string_generator()

    def testLogin(self):
        driver = self.driver
        driver.maximize_window()
        self.random_string_generator()

        self.selectAndSearch()
    def selectAndSearch(self):
        driver = self.driver
        #select a random category
        randomCategory = ['notebooks', 'all-in-one pcs/workstations', 'tablet cases', 'laser/led printers', 'bar code readers',
                              'handheld mobile computers', 'software licenses/upgrades', 'antivirus security software',
                              'peripheral device cases']
        category = random.choice(randomCategory)
        print(category)

        #all categories select drop down clicking
        driver.find_element_by_xpath(Data.allCategoriesDropDown).click()

        #search scanner
        driver.find_element_by_xpath(Data.allCategoriesSearchField).send_keys(category)
        driver.find_element_by_xpath(Data.allCategoriesSearchField).send_keys(Keys.ENTER)

        #click on search button
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.searchButton)).click()
        time.sleep(3)


        self.dbActionAllProducts(category)
    def dbActionAllProducts(self, category):
        driver = self.driver
        dataAll = dbClass.dbActionsWithAllProducts(category)
        dbCategory = json.dumps(dataAll["count"]).strip("")
        dbCategory = int(dbCategory)
        timeVar = driver.find_element_by_xpath(Data.categoryNameTextInfo)
        resultCategory = (timeVar.text).split(" ")[0]
        resultCategory = int(resultCategory)
        if dbCategory == resultCategory:
            print('All ' + category + ' successfully displayed in compared with database')
        else:
            print('All ' + category + ' was not displayed')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/allProductsWasNotDisplayedInComparedWithDB.png')


        self.dbActionInStockProducts(category)
    def dbActionInStockProducts(self, category):
        driver = self.driver
        #click on "In Stock" checkbox
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.inStock)).click()
        time.sleep(2)
        dataInStock = dbClass.dbActionsWithInStockProducts(category)
        dbCategory = json.dumps(dataInStock["count"]).strip("")
        dbCategory = int(dbCategory)
        timeVar = driver.find_element_by_xpath(Data.categoryNameTextInfo)
        resultCategory = (timeVar.text).split(" ")[0]
        resultCategory = int(resultCategory)
        if dbCategory == resultCategory:
            print('In stock ' + category + ' successfully displayed in compared with database')
        else:
            print('In stock ' + category + ' was not displayed in compared with database')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/inStockProductsWasNotDisplayedInComparedWithDB.png')


        self.addToCart()
    def addToCart(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.addInStockRandomProduct)).click()


        self.addToCartSuggestionChecker()
    def addToCartSuggestionChecker(self):
        driver = self.driver
        #check a add to cart suggestion
        suggestionAddToCart = driver.find_element_by_xpath(Data.sussestionToAdd)
        t = suggestionAddToCart.text
        if t == 'Product has been added to the cart':
            print('Add to cart suggestion worked')
        elif t == 'Error: There are no such quantity for this product. Max available in stock: 1':
            print('There are no such quantity for this product. Max available in stock: 1, notification worked')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/suggestionWorkedThereAreNoSuchQuantity.png')
        else:
            print('Notification was not worked')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/suggestionWasNotWorked.png')
        time.sleep(1)


        self.purchaseActionFirst()
    def purchaseActionFirst(self):
        driver = self.driver
        #navigate to the shopping cart
        driver.find_element_by_xpath(Data.shoppingCart).click()

        #check the Shopping Cart page
        helpShopCartPage = driver.find_element_by_xpath(Data.shoppingCartTitle)
        shopCartPage = helpShopCartPage.text
        shopCartPage = str(shopCartPage)

        if shopCartPage == 'Your Cart':
            print('Your Cart page successfully displayed')
        else:
            print('Your Cart page was not displayed')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/yourCartPageWasNotWorked.png')

        #ckick on proceed to checkout button
        driver.find_element_by_xpath(Data.proccedToCheckOutFirst).click()

        #check the Sign In page
        helpSignInPage = driver.find_element_by_xpath(Data.signInTitle)
        signInPage = helpSignInPage.text
        signInPage = str(signInPage)

        if signInPage == 'Sign In':
            print('Sign in page successfully displayed')
        else:
            print('Sign In page was not displayed')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/signInPageeWasNotDisplayed.png')


        self.fillAllFields()
    def fillAllFields(self):
        driver = self.driver
        firstNameFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.firstNameField))
        fn = randomHelper.random_string_generator()
        firstNameFieldElement.send_keys(fn)

        #last name field filling
        lastNameFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.lastNameField))
        ln = randomHelper.random_string_generator()
        lastNameFieldElement.send_keys(ln)

        #email filed filling
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.emailField))
        em = randomHelper.random_string_generator() + '@gmail.com'
        emailFieldElement.send_keys(em)

        #password field filling
        driver.find_element_by_xpath(Data.passwordField).send_keys(Data.password)

        #retype password field filling
        driver.find_element_by_xpath(Data.passwordFieldRetype).send_keys(Data.password)

        #business type radio button
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.businessRadioButton)).click()
        typeCustomer = driver.find_element_by_xpath(Data.bussinessTypeForText).text

        #company field filling
        companyFieldElement = driver.find_element_by_xpath(Data.companyField)
        comp = randomHelper.random_string_generator()
        companyFieldElement.send_keys(comp)

        #job title field filling
        jobTitleElement = driver.find_element_by_xpath(Data.jobTitle)
        jobT = randomHelper.random_string_generator()
        jobTitleElement.send_keys(jobT)

        #postal code field filling
        driver.find_element_by_xpath(Data.postalCodeField).send_keys(randomHelper.random_int_generator())

        #phone field filling
        phoneFieldElement = driver.find_element_by_xpath(Data.phoneField)
        ph = randomHelper.random_int_generator()
        phoneFieldElement.send_keys(ph)

        #address field filling
        addressLine1FieldElement = driver.find_element_by_xpath(Data.addressLine1)
        addressLine1FieldElement.send_keys(randomHelper.random_string_generator())

        #city field filling
        driver.find_element_by_xpath(Data.cityXPath).send_keys(randomHelper.random_string_generator())

        #select country
        selectRandomCountry = Select(driver.find_element_by_xpath(Data.countrySelect))
        a = [o.get_attribute('value') for o in selectRandomCountry.options]
        randomCountry = (random.choice(a))
        randomCountry = str(randomCountry)
        selectRandomCountry.select_by_value(randomCountry)
        print('Selected country is ' + randomCountry)

        #I accept checkbox clicking
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.iAcceptCheckBox)).click()

        #capcha field filling
        driver.find_element_by_xpath(Data.capchaField).send_keys(Data.capcha)

        #second proceed to checkout button clicking
        driver.find_element_by_xpath(Data.proccedToCheckOutSecond).click()
        time.sleep(2)

        #user login checking method
        loginChecker = driver.find_element_by_xpath(Data.userSuccessfullyLogIn)
        q = loginChecker.text
        if q != 'Welcome, Guest':
            print('User successfully logged in')
        else:
            print('User was not logged in')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/userWasNotLoggedIn.png')

        #check the Choose Shipping and Payment Methods page
        helpChooseShipping = driver.find_element_by_xpath(Data.chooseShippingPaymentMethod)
        chooseShipping = helpChooseShipping.text
        chooseShipping = str(chooseShipping)

        if chooseShipping == 'Choose Shipping and Payment Methods':
            print('Choose Shipping and Payment Methods page successfully displayed')
        else:
            print('Choose Shipping and Payment Methods page was not displayed')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/chooseShippingandPaymentMethodsWasNotWorked.png')

        #select a random shipping method radiobutton
        randomShippingList = [Data.shipingMethodFirst, Data.shipingMethodSecond, Data.shippingMethodThird]
        randomShipping = random.choice(randomShippingList)
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(randomShipping)).click()

        #select a random payment method radiobutton
        randomPaymentList = [Data.paymentMethodFirst, Data.paymentMethodSecond]
        randomPayment = random.choice(randomPaymentList)
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(randomPayment)).click()

        #confirm order button clicking
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(Data.confirmOrderButton)).click()

        #check the Please Check All Details Before Placing Order page
        helpCheckAllDetails = driver.find_element_by_xpath(Data.checkAllDetails)
        checkAllDetails = helpCheckAllDetails.text
        checkAllDetails = str(checkAllDetails)

        if checkAllDetails == 'Please Check All Details Before Placing Order':
            print('Please Check All Details Before Placing Order page successfully displayed')
        else:
            print('Please Check All Details Before Placing Order page was not displayed')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/pleaseCheckAllDetailsBeforePlacingOrderWasNotWorked.png')

        #place order button clicking
        driver.find_element_by_xpath(Data.placeOrderButton).click()
        time.sleep(2)

        #verifying a successfully purchase
        purchChecker = driver.find_element_by_xpath(Data.purchaseCheck)
        e = purchChecker.text
        if e == 'Thank you for your purchase!':
            print('Purchase successfully accomplished')
        else:
            print('Purchase was not accomplished')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/purchaseWasNotAccomplished.png')

        # helpOrderIdElement = driver.find_element_by_xpath(Data.orderId)
        # orderIdElement = helpOrderIdElement.text
        # orderIdElement = str(orderIdElement)
        time.sleep(2)


        self.logOut(fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer)
    def logOut(self, fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer):
        driver = self.driver
        #logout button clicking
        driver.find_element_by_xpath(Data.logOutButton).click()

        #logout checking method
        logOutChecker = driver.find_element_by_xpath(Data.userSuccessfullyLogIn)
        r = logOutChecker.text
        if r == 'Welcome, Guest':
            print('User successfully logged out')
        else:
            print('User was not logged out')
            driver.save_screenshot('/home/nikita/SeleniumGepard/FourthCase/userWasNotLoggedOut.png')


        #BO part:
        self.boPart(fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer)
        #добавить поиск по "Customer ID"
    def boPart(self, fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer):
        print("------BO part------:")
        print("------Actions with Customers Management------")
        driver = self.driver

        time.sleep(1)

        #opening a new window in browser
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        driver.get('http://admin:adming@gepard.bintime.com/admin')
        time.sleep(1)

        #email field filling
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(Data.boEmailField)).send_keys(Data.boEmailData)

        #password field filling
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id(Data.boPasswordField)).send_keys(Data.boPasswordData)

        #login button clicking
        driver.find_element_by_xpath(Data.boLoginButton).click()

        time.sleep(2)

        #customers management panel clicking
        driver.find_element_by_xpath(Data.customersButton).click()
        #driver.find_element_by_link_text('Customers').click()
        #driver.find_element_by_class_name('submenu_wrap').click()

        #customers management clicking
        driver.find_element_by_xpath(Data.customersManagementButton).click()
        time.sleep(1)


        #search by fields in customers management page
        self.checkRandomFields(fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer)
    def checkRandomFields(self, fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer):
        driver = self.driver

        #search by first name
        searchFunctions.searchForBOFields(driver, Data.cusManageSearchButton, Data.fnBoField, fn, Data.emptyTableClicking,
                          Data.boFirstNameForChecking, Data.boFirtsNameColumnName, Data.cusManageResetButton)

        #search by last name
        searchFunctions.searchForBOFields(driver, Data.cusManageSearchButton, Data.lnBoField, ln, Data.emptyTableClicking,
                          Data.boLastNameForChecking, Data.boLastNameColumnName, Data.cusManageResetButton)

        #search by phone
        searchFunctions.searchForBOFields(driver, Data.cusManageSearchButton, Data.phoneBOField, ph, Data.emptyTableClicking,
                          Data.boPhoneForChecking, Data.boPhoneColumnName, Data.cusManageResetButton)

        #search by email
        searchFunctions.searchForBOFields(driver, Data.cusManageSearchButton, Data.emailBoField, em, Data.emptyTableClicking,
                          Data.boEmailForChecking, Data.boEmailColumnName, Data.cusManageResetButton)

        #search by country
        searchFunctions.searchForBOFields(driver, Data.cusManageSearchButton, Data.countryBoField, randomCountry, Data.emptyTableClicking,
                          Data.boCountryForChecking, Data.boCountryColumnName, Data.cusManageResetButton)

        #search by company
        searchFunctions.searchForBOFields(driver, Data.cusManageSearchButton, Data.companyBOField, comp, Data.emptyTableClicking,
                          Data.boCompanyForChecking, Data.boCompanyColumnName, Data.cusManageResetButton)

        #search by job title
        searchFunctions.searchForBOFields(driver, Data.cusManageSearchButton, Data.jobTitleBOField, jobT, Data.emptyTableClicking,
                          Data.boJobTitleForChecking, Data.boJobTitleColumnName, Data.cusManageResetButton)



        self.checkRandomDropdownSelects(fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer)
    def checkRandomDropdownSelects(self, fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer):
        driver  = self.driver

        #search by type
        searchFunctions.searchForBOSelectDropDown(driver,Data.cusManageSearchButton, Data.typeSelectDropDown, typeCustomer,
                                  Data.boTypeSelectDropDownColumnName, Data.boTypeSelectDropDownForChecking ,Data.cusManageResetButton)
        time.sleep(1)


        self.actionsWithOrdersManagement(fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer)
    def actionsWithOrdersManagement(self, fn, ln, ph, em, randomCountry, comp, jobT, typeCustomer):
        driver = self.driver
        print('------Actions with Orders Management------')

        #orders button clicking on management panel
        driver.find_element_by_xpath(Data.boOrdersButton).click()

        #orders management button clicking
        driver.find_element_by_xpath(Data.boOrdersManagementButton).click()
        time.sleep(1)
        #make refactoring after id will be available

        #search by first name
        searchFunctions.searchForBOFields(driver, Data.ordersManageSearchButton, Data.boBillingFNameField, fn, Data.ordersEmptyTable,
                          Data.ordersResultFirstName,Data.ordersFirstNameColumnName, Data.boOrdersResetButton)

        #search by last name
        searchFunctions.searchForBOFields(driver, Data.ordersManageSearchButton, Data.boBillingLNameField, ln, Data.ordersEmptyTable,
                          Data.ordersResultLastName, Data.ordersLastNameColumnName, Data.boOrdersResetButton)

        #search by company
        searchFunctions.searchForBOFields(driver, Data.ordersManageSearchButton, Data.boBillingCompanyField, comp, Data.ordersEmptyTable,
                          Data.ordersResultCompany, Data.ordersCompanyColumnName, Data.boOrdersResetButton)

         #search by Created At field
        self.searchByDate()
    def searchByDate(self):
        driver = self.driver
        driver.find_element_by_xpath(Data.ordersManageSearchButton).click()
        i = datetime.now()
        date = i.strftime('%Y-%m-%d')
        driver.find_element_by_xpath(Data.boCreatedAtField).send_keys(date)
        driver.find_element_by_xpath('//*[@id="order-grid"]/div[1]/div').click()
        time.sleep(1)
        dateText = driver.find_element_by_xpath(Data.ordersResultCreatedAt).text
        dateTextWithoutHours = dateText[:-9]
        if dateTextWithoutHours == date:
            print("Created At date successfully displayed")
        else:
            print("Created At date was not displayed")
            driver.save_screenshot('/home/nikita/SeleniumGepard/ThirdCase/createdAtDateWasNotDisplayed.png')
        driver.find_element_by_xpath(Data.ordersManageSearchButton).click()
        driver.find_element_by_xpath(Data.boOrdersResetButton).click()


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
