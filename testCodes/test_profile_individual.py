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
from testData import project_login_data
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

    def test_login_individual(self, booting_function):
        try:
            actions = ActionChains(self.driver)

            self.driver.get(self.url)

            self.driver.maximize_window()

############### clicking on individual button###############

            login_individual_dropdown = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_dropdown_id)))

            login_individual_dropdown.click()

            actions.send_keys(Keys.TAB).perform()

            actions.send_keys(Keys.ENTER).perform()

############entering the login details###############

            individual_username = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_user_id)))

            individual_username.send_keys(project_login_data.logindata.individual_username_data)

#############enering the password details#########################

            individual_password = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_password_id)))

            individual_password.send_keys(project_login_data.logindata.individual_password_data)

 ################## clicking on the login button##############

            individual_signin_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_login_xpath)))

            individual_signin_click.click()

##################opening the will document ###############

            edit_new_will_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_new_will_edit)))

            edit_new_will_click.click()


#####################opening my details page #############
            individual_dob = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.invidual_dob_id)))

            individual_dob.clear()

            individual_dob.send_keys(project_login_data.logindata.individual_dob_data)

####################gender details##########

            individual_gender = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_gender_id)))

            individual_gender.click()

            actions.send_keys(Keys.TAB).perform()

            actions.send_keys(Keys.TAB).perform()

            actions.send_keys(Keys.ENTER).perform()

###############entering aadhqr details############
            individual_aadhar_change = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_aadhar_change_xpath)))

            individual_aadhar_change.click()

            individual_aadhar_update = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.invidual_aadhar_update_id)))

            individual_aadhar_update.click()

            individual_aadhar_update.send_keys(project_login_data.logindata.individual_aadhar_data)

            individual_aadhar_update_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_aadhar_update_click)))

            individual_aadhar_update_click.click()

            time.sleep(3)

            #self.driver.execute_script("window.scrollTo(0,500)")

######################### religion details##############
            individual_religion = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, project_login_data.loginselectors.individual_religion_xpath)))

            select = Select(individual_religion)

            select.select_by_visible_text("Hindu")

            for _ in range(15):
                actions.send_keys((Keys.DOWN)).perform()


######################Marital status##################
            individual_marital_deselect = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_marriage_deselect)))

            individual_marital_deselect.click()

            individual_marital_status = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_status_married_xpath)))

            individual_marital_status.click()

            individual_spouse_name = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_spouse_id)))

            individual_spouse_name.clear()

            individual_spouse_name.send_keys(project_login_data.logindata.individual_spouse_data)

            for _ in range(15):
                actions.send_keys((Keys.DOWN)).perform()

###################### father details##############

            individual_father_name = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_father_id)))

            individual_father_name.clear()

            individual_father_name.send_keys(project_login_data.logindata.individual_father_data)

            for _ in range(15):
                actions.send_keys((Keys.DOWN)).perform()


################Zip code details##############

            individual_zipcode = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_zip_id)))

            individual_zipcode.click()

            individual_zipcode.clear()

            individual_zipcode.send_keys(project_login_data.logindata.individual_zip_data)

            time.sleep(3)

###################address details#########

            individual_line2_address = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_line2_id)))

            individual_line2_address.clear()

            individual_line2_address.send_keys(project_login_data.logindata.individual_line2_data)

            individual_line3_address = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_line3_id)))

            individual_line3_address.clear()

            individual_line3_address.send_keys(project_login_data.logindata.individual_line3_data)

######################save and cotinue click###############

            individual_save_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_sandc_xpath)))

            individual_save_click.click()

            time.sleep(3)



        except:

            print("element not found")













