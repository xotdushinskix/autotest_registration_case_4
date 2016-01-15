#function for searching by field in BO
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

#search by BO text fields
def searchForBOFields(driver, searchButton, fieldPath, data, emptyTable, resultAfterSearch, columnPath, resetButton):
    WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(searchButton)).click()
    driver.find_element_by_xpath(fieldPath).send_keys(data)
    driver.find_element_by_xpath(emptyTable).click()
    time.sleep(1)
    searchInfo = driver.find_element_by_xpath(resultAfterSearch).text
    searchingColumn = driver.find_element_by_xpath(columnPath).text
    if data == searchInfo:
        print('Search by ' + searchingColumn + ' successfully displayed')
    else:
        print('Search by ' + searchingColumn + ' was not displayed')
        driver.save_screenshot('/home/nikita/SeleniumGepard/ThirdCase/searchByFieldWasNotWorked.png')
    driver.find_element_by_xpath(searchButton).click()
    driver.find_element_by_xpath(resetButton).click()


#function for searching by select dropdown
def searchForBOSelectDropDown(driver, searchButton, dropDownPath, dropdownData, nameOfColumnHead, selectResult, resetButton):
    driver.find_element_by_xpath(searchButton).click()
    select = Select(driver.find_element_by_xpath(dropDownPath))
    select.select_by_visible_text(dropdownData)
    time.sleep(3)
    dropdownName = driver.find_element_by_xpath(nameOfColumnHead).text
    dropdownResultText = driver.find_element_by_xpath(selectResult).text
    print(dropdownData)
    print(dropdownResultText)
    if dropdownData == dropdownResultText:
        print('Search by ' + dropdownName + ' successfully displayed')
    else:
        print('Search by ' + dropdownName + ' was not displayed')
        driver.save_screenshot('/home/nikita/SeleniumGepard/ThirdCase/searchBySelectDropDownWasNotWorked.png')
    driver.find_element_by_xpath(searchButton).click()
    driver.find_element_by_xpath(resetButton).click()
