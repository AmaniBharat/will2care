from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from testData import project_immovable_property_data
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

#########################entering amani login details###############

            individual_login_email = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_user_id)))

            individual_login_email.send_keys(project_immovable_property_data.propertydata.individual_login_proemail_data)

            individual_login_password = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_password_id)))

            individual_login_password.send_keys(project_immovable_property_data.propertydata.individual_login_propwd_data)

            individual_login_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_login_xpath)))

            individual_login_click.click()

            individual_edit_will_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_edit_will_xpath)))

            individual_edit_will_click.click()

            #self.driver.execute_script("window.scrollTo(0,300)")

            individual_property_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_property_allocation_click)))

            individual_property_click.click()

#######################Current Account Details#########################

            actions.send_keys(Keys.PAGE_DOWN).perform()

            individual_ca_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_ca_click_xpath)))

            individual_ca_click.click()

            individual_ca_name = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_ca_name_xpath)))

            individual_ca_name.send_keys(project_immovable_property_data.propertydata.individual_ca_name_data)

            individual_ca_number = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_ca_accountnum_xpath)))

            individual_ca_number.send_keys(project_immovable_property_data.propertydata.individual_ca_number_data)

            individual_ca_ifsc = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_ca_ifsc_xpath)))

            individual_ca_ifsc.send_keys(project_immovable_property_data.propertydata.individual_ca_ifsc_data)

            individual_ca_nominee = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_ca_nominee_xpath)))

            individual_ca_nominee.send_keys(project_immovable_property_data.propertydata.individual_ca_nominee_data)

            individual_ca_joint = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_ca_joint_xpath)))

            individual_ca_joint.send_keys(project_immovable_property_data.propertydata.individual_ca_joint_data)

            individual_ca_remarks = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_immovable_property_data.proprtyselectors.individual_ca_remarks_id)))

            individual_ca_remarks.send_keys(project_immovable_property_data.propertydata.individual_ca_remarks_data)

            individual_ca_successor = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_immovable_property_data.proprtyselectors.individual_ca_successor_id)))

            select = Select(individual_ca_successor)

            select.select_by_visible_text("Sequential")

            individual_ca_ben1 = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_immovable_property_data.proprtyselectors.individual_ca_ben1_xpath)))

            select1 = Select(individual_ca_ben1)

            select1.select_by_visible_text("Ramesh thiruveedi")

            individual_ca_save = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_immovable_property_data.proprtyselectors.individual_ca_save_id)))

            individual_ca_save.click()

            time.sleep(3)

        except:

            print("element not found")





