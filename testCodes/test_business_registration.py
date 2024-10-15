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
import time


class TestWill2care:
    url = "https://www.will2care.com/"

    # Booting Method for running the project

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()

        yield

        self.driver.close()

    ############### Giving details in the registration page################

    def test_navigation(self, booting_function):
        try:
            actions = ActionChains(self.driver)

            self.driver.get(self.url)

            self.driver.maximize_window()

############## cicking on register(business) button###############

            register_business_dropdown = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_navigation_pages_data.TestSelectors.registration_dropdown_id)))

            register_business_dropdown.click()

            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.TAB).perform()
            actions.send_keys(Keys.ENTER).perform()

# ######################filling the business page details ######################
#
# #######################Giving first name details###################

            firstname_business_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.firstname_id)))

            firstname_business_click.send_keys(project_registration_data.registrationdata.firstname_data)

##################### Giving last name details######################

            lastname_business_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.lastname_id)))

            lastname_business_click.send_keys(project_registration_data.registrationdata.lastname_data)

##########################Giving Password Details###################

            password_business = WebDriverWait(self.driver,10).until((EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.password_id))))

            password_business.send_keys(project_registration_data.registrationdata.password_data)

##############################Confirm password data################

            confirm_password_business = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.confirmpassword_id)))

            confirm_password_business.send_keys(project_registration_data.registrationdata.confirmpassword_data)

############################Giving Email details#####################

            Email_business = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.email_id)))

            Email_business.send_keys(project_registration_data.registrationdata.email_data)

###############################Giving Mobile details#####################

            Mobile_business = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.mobile_id)))

            Mobile_business.send_keys(project_registration_data.registrationdata.mobile_data)


##############################Giving Gender Details####################

            self.driver.execute_script("window.scrollTo(0, 500)")

            gender_business_dropdown = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_gender_id)))
            select = Select(gender_business_dropdown)
            select.select_by_visible_text("Female")

###########################Filling Experience details######################

            business_experience = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_experience_id)))

            business_experience.send_keys(project_registration_data.registrationdata.business_Experience_data)

######################Practice area details #######################
            practice_business_details = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_practice_id)))
            practice_business_details.send_keys(project_registration_data.registrationdata.business_Practice_data)

#######################Filling User type details###############

            user_type_business = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.business_User_type_id)))
            user_type_business.click()

######################Filling Adrdess1 and 2 details####################
            address1_business = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_address1_id)))
            address1_business.send_keys(project_registration_data.registrationdata.business_address1_data)

            address2_business = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_address2_id)))
            address2_business.send_keys(project_registration_data.registrationdata.business_address2_data)

################  Filling PostCode Details #####################

            postcode_business = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_postcode_id)))
            postcode_business.send_keys(project_registration_data.registrationdata.business_postcode_data)
            time.sleep(5)
            #self.driver.implicitly_wait(5)
################# filling country details#################

            self.driver.execute_script("window.scrollTo(0,700)")

            country_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, project_registration_data.registrationselectors.business_country_id)))
            select = Select(country_select)
            select.select_by_visible_text("India")

####################filling the state details##########
            state = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_State_id)))

            state.send_keys(project_registration_data.registrationdata.business_state_data)
###########################filling the city details##########

            city = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_registration_data.registrationselectors.business_city_id)))
            city.send_keys(project_registration_data.registrationdata.business_city_data)


##############clciking on terms checkbox############

            terms_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.business_ckeckbox_xpath)))
            terms_click.click()

#############Clicking on register button############

            register_business_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_registration_data.registrationselectors.business_register_xpath)))
            register_business_click.click()
            time.sleep(10)
            #self.driver.implicitly_wait(5)


        except:

            print("element not found")

