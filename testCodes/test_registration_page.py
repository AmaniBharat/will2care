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
from testData import project_registration_data

class TestWill2care:
       url = "https://www.will2care.com/"

       url1 = 'https://accounts.google.com/'
       # Booting Method for running the project

       @pytest.fixture

       def booting_function(self):

           self.driver = webdriver.Chrome()

           yield

           self.driver.close()



############### Giving details in the registration page################

       def test_registration(self,booting_function):

           try:

               actions = ActionChains(self.driver)

               self.driver.get(self.url)

               self.driver.maximize_window()


#########Clicking on the registration button(individual)############

               register_individualdropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, project_navigation_pages_data.TestSelectors.registration_dropdown_id)))
               register_individualdropdown.click()
               actions.send_keys(Keys.TAB).perform()
               actions.send_keys(Keys.ENTER).perform()

###############filling the details of the registration pages###############

####################giving first name details###################

               firstname = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.firstname_id)))

               firstname.send_keys(project_registration_data.registrationdata.firstname_data)

########################3giving lastname details###################

               lastname = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.lastname_id)))

               lastname.send_keys(project_registration_data.registrationdata.lastname_data)

##################### giving password details #####################
               password  = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.password_id)))

               password.send_keys(project_registration_data.registrationdata.password_data)

##################### giving confirm password details ########################

               confirmpassword = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.confirmpassword_id)))

               confirmpassword.send_keys(project_registration_data.registrationdata.confirmpassword_data)

################## giving email details ###################################

               email = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.email_id)))

               email.send_keys(project_registration_data.registrationdata.email_data)

##################giving mobile number details#####################

               mobile = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.mobile_id)))

               mobile.send_keys(project_registration_data.registrationdata.mobile_data)

################## selecting the checkbox #######################

               checkbox = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.checkbox_xpath)))

               checkbox.click()

               #time.sleep(5)

######################## clicking on the register button ######################

               register = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.register_xpath)))

               register.click()

               time.sleep(5)


########################testing validations##############
               #input_otp_email = input("please enter the otp")



#####################Switching to gmail webpage##############

#                self.driver.get(self.url1)
#
# ######################login details############################
#
# #############################User name details####################
#
#                gmail_username = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.gmail_username_id)))
#
#                gmail_username.send_keys(project_registration_data.registrationdata.email_data)
#
#                next_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.next_xpath)))
#
#                next_click.click()
#
#                time.sleep(5)
#
# #############################Password Details###############################
#
#                gmail_password = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.gmail_password_xpath)))
#
#                gmail_password.send_keys(project_registration_data.registrationdata.email_password_data)
#
#                password_next_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.password_next_xpath)))
#
#                password_next_click.click()

           except:
               print("element not found")
