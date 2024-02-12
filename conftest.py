from selenium import webdriver
import pytest
import time

# Fixture to create a WebDriver instance for testing
@pytest.fixture
def driver():
    # URL for the login page 
    # url = "https://www.linkedin.com/"
    
    # url without login
    url = "https://www.linkedin.com/jobs/sqa-engineer-jobs-cupertino-ca?position=1&pageNum=0"
    
    driver = webdriver.Chrome(executable_path='drivers/macos/chromedrivermac')
    
    # Navigate to the URL
    driver.get(url)
    
     # Wait for 2 seconds (adjust as needed)
    time.sleep(2)
    
    # Yield the WebDriver instance to the test function
    yield driver
    
    # Close the WebDriver instance after the test is complete
    driver.close()
    
    
    

