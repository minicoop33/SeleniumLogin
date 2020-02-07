from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def wrongUsername(driver):
    # Test with wrong username and correct password
    driver.find_element_by_id("relogin_user").send_keys("WrongUser")
    driver.find_element_by_id("relogin_password").send_keys("Testpass1")
    # Attempt to login
    loginbtn = driver.find_element_by_id("admin-login-btn")
    loginbtn.click()
    time.sleep(2)

def wrongPassword(driver):
    # Test with correct username and wrong password
    driver.find_element_by_id("relogin_user").send_keys("TestUser")
    driver.find_element_by_id("relogin_password").send_keys("Wrongpass1")
    # Attempt to login
    loginbtn = driver.find_element_by_id("admin-login-btn")
    loginbtn.click()
    time.sleep(2)
  
def wrongUsernameAndPassword(driver):
    # Test with wrong username and wrong password
    driver.find_element_by_id("relogin_user").send_keys("WrongUser")
    driver.find_element_by_id("relogin_password").send_keys("Wrongpass1")
    # Attempt to login
    loginbtn = driver.find_element_by_id("admin-login-btn")
    loginbtn.click()
    time.sleep(2)

def noCredentialsEntered(driver):
    # Test without entering any credentials
    loginbtn = driver.find_element_by_id("admin-login-btn")
    loginbtn.click()
    time.sleep(2)  

def correctCredentials(driver):
    # Test with correct username and password
    driver.find_element_by_id("relogin_user").send_keys("TestUser")
    driver.find_element_by_id("relogin_password").send_keys("Testpass1")
    # Attempt to login
    loginbtn = driver.find_element_by_id("admin-login-btn")
    loginbtn.click()


def loginTest():
    executable_path = "C:/Users/rubio/OneDrive/Desktop/SeleniumTest/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://cooperlibby.printercloud.com/admin")
    # Run separate tests on login page
    wrongUsername(driver)
    wrongPassword(driver)
    wrongUsernameAndPassword(driver)
    noCredentialsEntered(driver)
    correctCredentials(driver)

    time.sleep(4)
    driver.quit()

loginTest()    