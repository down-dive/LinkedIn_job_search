from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CommonOps:
        
    # Wait for the presence of an element identified by the given locator    
    def wait_for(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    
    # Wait for an element to be clickable based on the given locator
    def wait_for_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    # Find and return a single element based on the given locator
    def find(self, locator):
        return self.driver.find_element(*locator)
    