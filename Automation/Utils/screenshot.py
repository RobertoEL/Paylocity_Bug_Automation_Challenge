import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    reports_dir = "reports/screenshots"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(reports_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(file_path)
    return file_path
