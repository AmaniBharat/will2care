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
from testData import individual_funeral_data
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

######################clicking on the general details page###############

            individual_general_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,individual_funeral_data.FuneralSelectors.individual_generaldetails_xpath)))

            individual_general_click.click()

######################### general details page#####################

            individual_funeral_details = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,individual_funeral_data.FuneralSelectors.individual_funeral_details_id)))

            individual_funeral_details.send_keys(individual_funeral_data.FuneralData.individual_funeral_data)

            individual_funeral_debts = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,individual_funeral_data.FuneralSelectors.individual_debt_details_id)))

            individual_funeral_debts.send_keys(individual_funeral_data.FuneralData.individual_debt_data)

            individual_predecease_data = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,individual_funeral_data.FuneralSelectors.individual_predeceased_instr_id)))

            individual_predecease_data.send_keys(individual_funeral_data.FuneralData.individual_predeceased_data)

            individual_other_data = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,individual_funeral_data.FuneralSelectors.individual_otherinstr_id)))

            individual_other_data.send_keys(individual_funeral_data.FuneralData.individual_other_data)

            individual_save_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,individual_funeral_data.FuneralSelectors.individual_save_id)))

            individual_save_click.click()

            time.sleep(3)

        except:

            print("element not found")

