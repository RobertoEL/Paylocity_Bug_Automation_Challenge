import string

from selenium import webdriver
from Utils import *
import random

# === Config ===
LOGIN_URL = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login"
USERNAME = "TestUser854"
PASSWORD = "n7{A1l)0NM!u"
FIRST_NAME = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
LAST_NAME = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
DEPENDANTS = rand_int = random.randint(0, 32)

# === Start Browser ===
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Login
    login(driver, LOGIN_URL, USERNAME, PASSWORD)

except Exception as e:
    print("Login failed:", e)

try:
    # Add an employee
    add_employee(driver, FIRST_NAME, LAST_NAME, DEPENDANTS)

    # Verify the new employee entry
    if employee_exists(driver, FIRST_NAME, LAST_NAME, DEPENDANTS):
        print("Employee added successfully.")
    else:
        print("Employee not found.")

except Exception as e:
    print("Error adding the employee:", e)

try:
    # Delete the employee
    delete_employee(driver, FIRST_NAME, LAST_NAME, DEPENDANTS)

    # Verify the employee was deleted
    if not employee_exists(driver, FIRST_NAME, LAST_NAME, DEPENDANTS):
        print("Employee deleted successfully.")
    else:
        print("Employee was found.")

except Exception as e:
    print("Error deleting the employee:", e)

finally:
    # Clean up
    driver.quit()
