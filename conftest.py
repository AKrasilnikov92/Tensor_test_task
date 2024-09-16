import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    
    option = Options()
    option.add_argument("--start-maximized")
    option.add_experimental_option("detach", True)
        
    driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()