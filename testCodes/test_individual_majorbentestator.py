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

##############################clicking on the beneficiary page##############

            individual_benpage_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_bclick_xpath)))

            individual_benpage_click.click()

#################### ben name details#####################

            individual_bfname = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_bfname_id)))

            individual_bfname.send_keys(project_login_data.logindata.individual_ben2_fname_data)

            individual_blname = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_blnmae_id)))

            individual_blname.send_keys(project_login_data.logindata.individual_ben2_lname_data)

            individual_bdob = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_bf_dob_id)))

            individual_bdob.send_keys(project_login_data.logindata.individual_ben2_dob_data)

            individual_bgender = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_bf_gender_xpath)))

            select = Select(individual_bgender)

            select.select_by_visible_text("Female")

            individual_bemail = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_bf_email_id)))

            individual_bemail.send_keys(project_login_data.logindata.individual_ben2_email_data)

            individual_bmobile = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_bf_mobile_id)))

            individual_bmobile.send_keys(project_login_data.logindata.individual_ben2_mobile_data)

            individual_btestator_check = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_bf_stestator_id)))

            individual_btestator_check.click()

            time.sleep(3)

            individual_sanben2 =WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_bf_sanewb_id)))

            individual_sanben2.click()
            time.sleep(3)

        except:

            print("element not found")
