from pages.login_page import LoginPage
import json

with open("config/config.json") as f:
    config = json.load(f)

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(config['login']['username'], config['login']['password'])
    assert login_page.is_success_message_displayed(), "Login success message not found"
