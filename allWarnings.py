from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def correctCredentials(driver):
    # Test with correct username and password
    driver.find_element_by_id("relogin_user").send_keys("TestUser")
    driver.find_element_by_id("relogin_password").send_keys("Testpass1")
    # Attempt to login
    loginbtn = driver.find_element_by_id("admin-login-btn")
    loginbtn.click()  

def selectAlertsTab(driver, delay):
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'oAlerts')))
    myElem.click()

def addNewWarning(driver, delay):
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'adminalerts-add')))
    myElem.click()

def configureWarning(driver, delay):
    # Set alert name
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'alert_name')))
    myElem.send_keys("Warnings")
    # Select all triggers
    driver.find_element_by_xpath('//*[@id="add-alert-div"]/div[2]/p[3]/input').click()
    # Select all users
    driver.find_element_by_xpath('//*[@id="add-alert-div"]/div[3]/table/tbody/tr[1]/td[1]/input').click()
    # Add selected users to be notified of alerts
    driver.find_element_by_xpath('//*[@id="add-alert-div"]/div[3]/table/tbody/tr[3]/td[2]/input[1]').click()
    # Click OK and finish adding warning
    driver.find_element_by_xpath('//*[@id="management_administration_alerts_add_ok"]/span').click()   

def deleteCreatedWarning(driver, delay):
    # Select the newly created warning
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="adminalerts-table"]/tbody/tr/td[1]/span')))
    myElem.click()
    # Click the delete button
    driver.find_element_by_id("adminalerts-delete").click()
    # Click OK on the alert box
    alert_obj = driver.switch_to.alert
    alert_obj.accept()

def loginTest():
    executable_path = "C:/Users/rubio/OneDrive/Desktop/SeleniumTest/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://cooperlibby.printercloud.com/admin")
    correctCredentials(driver)
    delay = 3 # seconds

    selectAlertsTab(driver, delay)    
    addNewWarning(driver, delay)
    configureWarning(driver, delay)
    deleteCreatedWarning(driver, delay)

    time.sleep(4)
    driver.quit()

loginTest()    