##### for html report pip install pytest-html##########
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pynput.keyboard import Key,Controller
from testData import project_navigation_pages_data

class TestWill2care:
       url = "https://www.will2care.com/"

       # Booting Method for running the project

       @pytest.fixture

       def booting_function(self):

           self.driver = webdriver.Chrome()

           yield

           self.driver.close()

############### Giving details in the registration page################

       def test_navigation(self,booting_function):

           try:

               actions = ActionChains(self.driver)

               self.driver.get(self.url)

               self.driver.maximize_window()



###########clicking on about us page##########

               aboutus_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.aboutus_xpath)))

               aboutus_click.click()

               #assert self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div/div/div[1]/h1') == 'One-stop platform for creating any Kind of Will.'

               aboutustitle = self.driver.title

               assert aboutustitle == 'Will2Care :: About Us'

               print("We are in About Us page successfully")

################# clicking on Services dropdown Quickwill ######

               services_quickclick = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.services_fullxpath)))
               services_quickclick.click()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.ENTER).perform()
               servicestitle = self.driver.title

               assert servicestitle == 'Will2Care :: Quick Will'

               print("We are in Quick will services page successfully")



###################  clicking on Services dropdown Comprehensive will ######

               services_comprehensiveclick = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.services_fullxpath)))
               services_comprehensiveclick.click()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.ENTER).perform()
               servicestitle1 = self.driver.title

               assert servicestitle1 == 'Will2Care :: Comprehensive Will'

               print("We are in Comprehensive will services page successfully")


################# clicking on pricing button #########

               pricing_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.prices_xpath)))
               pricing_click.click()
               pricingtitle = self.driver.title

               assert pricingtitle == 'Will2Care :: Pricing'

               print("We are in Pricing page successfully")



################# clicking on Helpcenter buttnon ##########
               helpcenter_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.helpcenter_xpath)))
               helpcenter_click.click()
               helpcenter_title = self.driver.title

               assert helpcenter_title == 'Will2Care :: Help Center'

               print("We are in Help Center Page Successfully")

################# Clicking on Login button(individual)##########

               login_individualclick = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.login_fullxpath)))
               login_individualclick.click()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.ENTER).perform()
               login_individual_title = self.driver.title

               assert login_individual_title == 'Will2Care :: Sign In'

               print("We are in Individual login page successfully")

############# Clicking on home button#######

               home_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.home_Xpath)))
               home_click.click()

               home_title = self.driver.title

               assert home_title == 'Will2Care :: Home'

               print("We are in Home Page successfully")

############### Clicking on Login Button(Business) ############

               login_businessclick = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_navigation_pages_data.TestSelectors.login_fullxpath)))
               login_businessclick.click()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.ENTER).perform()
               login_business_title = self.driver.title

               assert login_business_title == 'Will2Care :: Sign In'

               print("We are in business login page successfully")

               ############# Clicking on home button#######

               home_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, project_navigation_pages_data.TestSelectors.home_Xpath)))
               home_click.click()

               home_title = self.driver.title

               assert home_title == 'Will2Care :: Home'

               print("We are in Home Page successfully")

               ############### Clicking on the register(individual) button#########

               register_individualdropdown =WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_navigation_pages_data.TestSelectors.registration_dropdown_id)))
               register_individualdropdown.click()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.ENTER).perform()

               register_individual_title = self.driver.title

               assert register_individual_title == 'Will2Care :: User Registration'

               print("We are in individual Registration page successfully")


############# Clicking on home button#######

               home_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, project_navigation_pages_data.TestSelectors.home_Xpath)))
               home_click.click()

               home_title = self.driver.title

               assert home_title == 'Will2Care :: Home'

               print("We are in Home Page successfully")

               ############ Clicking on the register(Business) button #############

               register_businessdropdown = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_navigation_pages_data.TestSelectors.registration_dropdown_id)))
               register_businessdropdown.click()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.ENTER).perform()

               register_business_title = self.driver.title

               assert register_business_title == 'Will2Care :: User Registration'

               print("We are in Business Registration page successfully")


           except:

               print("element not found")














