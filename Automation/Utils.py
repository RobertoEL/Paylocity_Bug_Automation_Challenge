from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, url, username, password, timeout=10):
    driver.get(url)

    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.NAME, "Username"))
    )

    driver.find_element(By.NAME, "Username").send_keys(username)
    driver.find_element(By.NAME, "Password").send_keys(password, Keys.ENTER)

    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    print("Login successful")


def add_employee(driver, first_name, last_name, dependants, timeout=10, adding=True):
    if adding:
        driver.find_element(By.ID, "add").click()

    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.NAME, "firstName"))
    )

    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "firstName").send_keys(first_name)
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys(last_name)
    driver.find_element(By.NAME, "dependants").clear()
    driver.find_element(By.NAME, "dependants").send_keys(dependants)

    if adding:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.ID, "addEmployee"))
        )

        driver.find_element(By.ID, "addEmployee").click()
    else:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.ID, "updateEmployee"))
        )

        driver.find_element(By.ID, "updateEmployee").click()

    print(f"Employee submitted: {first_name} {last_name}, {dependants}")


def employee_exists(driver, first_name, last_name, dependants, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.NAME, "firstName"))
    )

    rows = driver.find_elements(
        By.XPATH,
        f"""
        //table//tr[
            td[normalize-space()='{first_name}']
            and td[normalize-space()='{last_name}']
            and td[normalize-space()='{dependants}']
        ]
        """
    )
    return bool(rows)


def edit_employee(driver, first_name, last_name, dependants, new_first_name, new_last_name, new_dependants, timeout=10):
    all_rows = driver.find_elements(By.XPATH, "//table//tr")
    rows = driver.find_elements(
        By.XPATH,
        f"""
                //table//tr[
                    td[normalize-space()='{first_name}']
                    and td[normalize-space()='{last_name}']
                    and td[normalize-space()='{dependants}']
                ]
                """
    )

    if rows:
        row = rows[0]
        row_number = all_rows.index(row)
    else:
        print("No matching row found")

    edit_button = driver.find_elements(By.XPATH, f'//*[@id="employeesTable"]/tbody/tr[{row_number}]/td[9]/i[1]')[0]
    edit_button.click()

    add_employee(driver, new_first_name, new_last_name, new_dependants, timeout=10, adding=False)

    print("Editing employee...")


def delete_employee(driver, first_name, last_name, dependants, timeout=10):
    all_rows = driver.find_elements(By.XPATH, "//table//tr")
    rows = driver.find_elements(
        By.XPATH,
        f"""
            //table//tr[
                td[normalize-space()='{first_name}']
                and td[normalize-space()='{last_name}']
                and td[normalize-space()='{dependants}']
            ]
            """
    )

    if rows:
        row = rows[0]
        row_number = all_rows.index(row)
    else:
        print("No matching row found")

    delete_button = driver.find_element(By.XPATH, f'//*[@id="employeesTable"]/tbody/tr[{row_number}]/td[9]/i[2]')
    delete_button.click()

    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.ID, "deleteEmployee"))
    )

    confirm_delete_button = driver.find_element(By.ID, "deleteEmployee")
    confirm_delete_button.click()

    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.ID, "deleteEmployee"))
    )

    print("Deleting employee...")
