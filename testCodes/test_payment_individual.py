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
from testData import individual_payment_data
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

            self.driver.execute_script("window.scrollTo(0,100)")
            time.sleep(3)

################## clicking on the Payment button############

            palns_individual_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,individual_payment_data.PaymentSelectors.plans_click_xpath)))

            palns_individual_click.click()


#########################clicking on quickwill button#########

            plans_individual_quick_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,individual_payment_data.PaymentSelectors.plans_quick_click_xpath)))

            plans_individual_quick_click.click()

##########################clicking on payment of quickwill#########

            plans_individual_quick_payment_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,individual_payment_data.PaymentSelectors.plans_quick_payment_click_xpath)))

            plans_individual_quick_payment_click.click()

            time.sleep(3)

#####################

        except:

            print("element not found")