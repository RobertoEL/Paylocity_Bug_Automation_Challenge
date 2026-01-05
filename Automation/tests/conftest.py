import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import json
from datetime import datetime
from selenium.common.exceptions import WebDriverException
from utils.driver_factory import create_driver
from utils.logger import create_logger
from utils.screenshot import take_screenshot

with open("config/config.json") as f:
    config = json.load(f)

logger = create_logger()

@pytest.fixture
def browser(request):
    browser_name = config.get("browser", "chrome")
    timeout = config.get("timeout", 10)

    logger.info(f"Starting browser: {browser_name}")
    driver = create_driver(browser_name)
    driver.implicitly_wait(timeout)

    yield driver

    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_path = take_screenshot(driver, test_name)
        logger.info(f"Screenshot saved: {screenshot_path}")

    logger.info("Closing browser")
    driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
