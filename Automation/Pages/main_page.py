from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    ADD_EMPLOYEE_BTN = (By.CSS_SELECTOR, "button[id='add']")
    FIRST_NAME_FLD = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME_FLD = (By.CSS_SELECTOR, "input[name='lastName']")
    DEPENDENTS_FLD = (By.CSS_SELECTOR, "input[name='dependants']")
    ADD_BTN = (By.CSS_SELECTOR, "input[button='addEmployee']")
    CANCEL_BTN = (By.CSS_SELECTOR, "input[contains(text(), 'Cancel')]")
    EDIT = (By.CSS_SELECTOR, "i[contains(class(), 'fas fa-edit')]")
    DELETE = (By.CSS_SELECTOR, "i[contains(class(), 'fas fa-times')]")

    def add_employee(self, first_name="Alpha", last_name="Beta", dependents=0):
        add_employee_btn = self.find_element(ADD_EMPLOYEE_BTN)
        first_name_fld = self.find_element(FIRST_NAME_FLD)
        last_name_fld = self.find_element(LAST_NAME_FLD)
        dependents_fld = self.find_element(DEPENDENTS_FLD)
        add_btn = self.find_element(ADD_BTN)
        
        add_employee_btn.click()
        first_name_fld.send_keys(first_name)
        last_name_fld.send_keys(last_name)
        dependents_fld.send_keys(dependents)
        add_btn.click()
