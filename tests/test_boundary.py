import pytest
from selenium import webdriver
import os
from datetime import datetime

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Opcional para ejecución sin UI
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)  # Espera implícita global
    yield driver
    driver.quit()

@pytest.fixture
def take_screenshot(browser):
    """Fixture para capturas de pantalla"""
    def _take_screenshot(test_name):
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{screenshots_dir}/{test_name}_{timestamp}.png"
        browser.save_screenshot(filename)
        print(f"\nScreenshot saved: {filename}")
    return _take_screenshot