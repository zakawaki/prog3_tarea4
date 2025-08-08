import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    
    # Configuración automática del ChromeDriver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def screenshot(browser, request):
    """Fixture para capturas de pantalla"""
    def _take_screenshot(step_name):
        test_name = request.node.name
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{screenshots_dir}/{test_name}_{step_name}_{timestamp}.png"
        browser.save_screenshot(filename)
        print(f"\nScreenshot saved: {filename}")
    
    return _take_screenshot