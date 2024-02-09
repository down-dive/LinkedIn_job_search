from selenium import webdriver
import pytest
import time

# Fixture to create a WebDriver instance for testing
@pytest.fixture
def driver():
    # URL for the initial page before switching to the iframe
    url = "https://www.linkedin.com/"
    
    driver = webdriver.Chrome(executable_path='drivers/macos/chromedrivermac')
    
    # Navigate to the URL
    driver.get(url)
    
     # Wait for 2 seconds (adjust as needed)
    time.sleep(2)
    
    # Yield the WebDriver instance to the test function
    yield driver
    
    # Close the WebDriver instance after the test is complete
    driver.close()
    
    
    

