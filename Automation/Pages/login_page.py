from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Account/Login"
    USERNAME_INPUT = (By.ID, "input[id='Username']")
    PASSWORD_INPUT = (By.ID, "input[id='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.open_url(self.URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
