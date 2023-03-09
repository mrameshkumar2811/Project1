from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import login_data
import login_locators


# Executing Class
class Delete_Ramesh():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
# Method to access webpage    
    def __init__(self):
        self.driver.maximize_window()
        self.driver.get(login_data.Data().url)

    def delete(self):
        self.driver.implicitly_wait(5)
          
# Method for Login
        self.driver.find_element(By.NAME,value=login_locators.Locators().Username_Locator).send_keys(login_data.Data().Employee_Username)
        self.driver.find_element(By.NAME,value=login_locators.Locators().Password_Locator).send_keys(login_data.Data().Employee_Password)
        self.driver.find_element(By.XPATH,value=login_locators.Locators().Loginbutton_Locator).click()

# Method for Delete
        self.driver.find_element(By.XPATH,value=login_locators.Locators().PIM_LOCATOR).click()
        self.driver.find_element(By.XPATH,value=login_locators.Locators().Delete).click()
        self.driver.find_element(By.XPATH,value=login_locators.Locators().Delete_button).click()
            

Delete_Ramesh().delete()



