from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CommonOps:

    # Initialize CommonOps with a WebDriver instance and a WebDriverWait with a default timeout of 10 seconds  
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10) 
        
    # Wait for the presence of an element identified by the given locator    
    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))
    
    # Wait for an element to be clickable based on the given locator
    def wait_for_clickable(self, locator):
        return self._wait.until(ec.element_to_be_clickable(locator))

    # Find and return a single element based on the given locator
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    # Attach a file 
    def attach_file(self, file_path):
        # Execute JavaScript to set the value of the hidden file input
        self.driver.execute_script('''
            var fileInput = document.querySelector("input[type='file']");
            fileInput.style.display = 'block';  // Make the input visible (if needed)
            fileInput.value = arguments[0];
        ''', file_path)