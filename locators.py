
from selenium.webdriver.common.by import By

#Filter locators:
class DateFilterLocators:
    
    ANYTIME_BUTTON = (By.XPATH, '//*[@aria-label="Date posted filter. Any Time filter is currently applied. Clicking this button displays all Date posted filter options." ]')
    PAST_WEEK_BUTTON = (By.XPATH, '//label[contains(text(),"Past Week")]')
    DONE_BUTTON = (By.XPATH, "//*[@class='filter__submit-button']")
    