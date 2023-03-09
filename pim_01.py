from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import login_data
import login_locators


# Executing Class
class Create_Arun():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Method to access webpage
    def __init__(self):
        self.driver.maximize_window()
# fetch the URL of the webpage
        self.driver.get(login_data.Data().url)

# Method to login into the Portal 
    def create(self):
        self.driver.implicitly_wait(5)
         
        self.driver.find_element(By.NAME,value=login_locators.Locators().Username_Locator).send_keys(login_data.Data().Employee_Username)
        self.driver.find_element(By.NAME,value=login_locators.Locators().Password_Locator).send_keys(login_data.Data().Employee_Password)
        self.driver.find_element(By.XPATH,value=login_locators.Locators().Loginbutton_Locator).click()

# Method for Create and save
        self.driver.find_element(By.XPATH,value=login_locators.Locators().PIM_LOCATOR).click()
        self.driver.find_element(By.XPATH,value=login_locators.Locators().Addbutton_Locator).click()
        self.driver.find_element(By.NAME,value=login_locators.Locators().Firstname_Locator).send_keys(login_data.Data().First_Name)
        self.driver.find_element(By.NAME,value=login_locators.Locators().Lastname_Locator).send_keys(login_data.Data().Last_Name)
        self.driver.find_element(By.XPATH,value=login_locators.Locators().Savebutton_Locator).click()


Create_Arun().create()
