from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .common import CommonOps

class LoginPage(CommonOps):
    
    LOGIN_EMAIL_INPUT = (By.ID, 'session_key')
    LOGIN_PASSWORD_INPUT = (By.ID, 'session_password')
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")
    DASHBOARD_ITEM = (By.XPATH, "//*[@title='Jobs']")

    def login(self, username, password):
    
        # locating email tab and entering the email
        self.find(self.LOGIN_EMAIL_INPUT).send_keys(username)
        print("I am here")
        # time.sleep(5)
        
        # locating password tab and entering the password
        self.find(self.LOGIN_PASSWORD_INPUT).send_keys(password)
        print("I am here 2")
        # time.sleep(5)

        # clicking submit button
        self.find(self.SUBMIT_BUTTON).click()
        print("I am here 3")
        time.sleep(5)

    # Check if the Dashboard menu item is displayed, indicating a successful login
    def login_success(self):
        return self.find(self.DASHBOARD_ITEM).is_displayed()       






    

