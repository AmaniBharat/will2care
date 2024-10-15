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
from testData import project_property_allocation_data
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

            individual_login_email.send_keys(project_property_allocation_data.propertydata.individual_login_proemail_data)

            individual_login_password = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_login_data.loginselectors.individual_password_id)))

            individual_login_password.send_keys(project_property_allocation_data.propertydata.individual_login_propwd_data)

            individual_login_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_login_data.loginselectors.individual_login_xpath)))

            individual_login_click.click()

            individual_edit_will_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_property_allocation_data.proprtyselectors.individual_edit_will_xpath)))

            individual_edit_will_click.click()

            self.driver.execute_script("window.scrollTo(0,400)")

            individual_property_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_property_allocation_data.proprtyselectors.individual_property_allocation_click)))

            individual_property_click.click()

################ selecting the immovable properties############

            individual_pet_click = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_property_allocation_data.proprtyselectors.individual_pet_click_xpath)))

            individual_pet_click.click()

            individual_pet_type = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_property_allocation_data.proprtyselectors.individual_pet_type_xpath)))

            individual_pet_type.send_keys(project_property_allocation_data.propertydata.individual_pet_type_data)

            individual_pet_vaccination = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_property_allocation_data.proprtyselectors.individual_pet_vaccination_xpath)))

            individual_pet_vaccination.send_keys(project_property_allocation_data.propertydata.individual_pet_vaccination_data)

            individual_pet_address = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_property_allocation_data.proprtyselectors.individual_pet_address_xpath)))

            individual_pet_address.send_keys(project_property_allocation_data.propertydata.individual_pet_address_data)

            individual_pet_remarks = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_property_allocation_data.proprtyselectors.individual_pet_remarks_id)))

            individual_pet_remarks.send_keys(project_property_allocation_data.propertydata.individual_pet_remarks_data)

            individual_pet_successor = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,project_property_allocation_data.proprtyselectors.individual_pet_successor_id)))

            select=Select(individual_pet_successor)

            select.select_by_visible_text("Sequential")

            individual_pet_seq_ben1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, project_property_allocation_data.proprtyselectors.individual_pet_seq_ben1_xpath)))

            individual_pet_seq_ben1.click()

            actions.send_keys(Keys.ARROW_DOWN).perform()

            actions.send_keys(Keys.ARROW_DOWN).perform()

            actions.send_keys(Keys.ENTER).perform()

            individual_pet_add = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,project_property_allocation_data.proprtyselectors.individual_pet_add_xpath)))

            individual_pet_add.click()

            time.sleep(3)
        except:

            print("element not found")