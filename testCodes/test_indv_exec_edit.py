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
from testData import individual_executor_data
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

################ clicking on the executor page ##################

            individual_executor_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,individual_executor_data.executor_selector.individual_executor_click_xpath)))

            individual_executor_click.click()

################# Editing executor details###############

            individual_exe_edit_click_xpath = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,individual_executor_data.executor_selector.individual_exe_edit_click_xpath)))

            individual_exe_edit_click_xpath.click()

            individual_exe_edit_fname = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,individual_executor_data.executor_selector.individual_executor_firstname_id)))

            individual_exe_edit_fname.send_keys("Gnanvika")

            time.sleep(3)

            self.driver.execute_script("window.scrollTo(0,400)")

            individual_exe_update_button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,individual_executor_data.executor_selector.individual_exe_update_button_xpath)))

            individual_exe_update_button.click()

            time.sleep(3)

        except:
            print("element not found")