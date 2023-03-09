from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import login_data
import login_locators

# Executing Class
class Loginerror_Ramesh():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Method to access webpage    
    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(login_data.Data().url)

# Method to login into the Portal
    def loginerror(self):
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.NAME,value=login_locators.Locators().Username_Locator).send_keys(login_data.Data().Employee_Username)
        self.driver.find_element(By.NAME,value=login_locators.Locators().Password_Locator).send_keys(login_data.Data().EmployeeError_Password)
        self.driver.find_element(By.XPATH,value=login_locators.Locators().Loginbutton_Locator).click()

Loginerror_Ramesh().loginerror()

