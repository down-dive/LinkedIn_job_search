from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from dotenv import load_dotenv
from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values(".env")

# Access the environment variables
username = env_vars["USERNAME"]
password = env_vars["PASSWORD"]

import os
import time

list_titles = ["Quality Assurance Engineer", "Automation engineer"]
list_locations = ["Cupertino, CA", "Sunnuvale, CA"]
# from webdriver_factory import WebDriverFactory

class LoginPage:
    def __init__(self):
        self.driver = WebDriverFactory.get_driver()
        # Other page initialization code

def login():

    driver = webdriver.Chrome('drivers/macos/chromedrivermac')
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.linkedin.com')
 
    # locating email tab and entering the email
    driver.find_element(By.ID, 'session_key').send_keys(username)
    print("I am here")
    # time.sleep(5)

    driver.find_element(By.ID, 'session_password').send_keys(password)
    print("I am here 2")
    # time.sleep(5)

    # clicking submit button
    # driver.find_element(By.XPATH, "//*[ text() = ‘Sign in’ ]").click()
    driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']").click()
    print("I am here 3")
    # time.sleep(5)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@title='Jobs']"))).click()
    # driver.find_element(By.XPATH, "//*[@title='Jobs']").click()
    print("I am here 4")
    # time.sleep(5)

    # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="organization-title"]'))).send_keys("Quality Assurance Engineer")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="organization-title"]')))
    # driver.find_element(By.XPATH, '//*[@autocomplete="organization-title"]').send_keys("Quality Assurance Engineer")
    # time.sleep(5)

    # Locate the input field using its ID (replace 'your_input_id' with the actual ID)
    input_title = driver.find_element(By.XPATH, '//*[@autocomplete="organization-title"]')
    input_location = driver.find_element(By.XPATH, '//*[@autocomplete="address-level2"]')


    # Use a for loop to send each item for logged in account
    for title, location in zip(list_titles, list_locations):

        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="organization-title"]')))
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="address-level2"]')))
        input_title.clear()  # Clear the input title before sending a new item
        input_location.clear()  # Clear the input location before sending a new item

        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="organization-title"]')))
        input_title.send_keys(title)
        # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="address-level2"]')))
        input_location.send_keys(location)

        # Optionally, send an Enter key press for both input fields
        input_title.send_keys(Keys.ENTER)
        input_location.send_keys(Keys.ENTER)

        # Optional: Wait for a brief moment to observe the result or perform additional actions
        time.sleep(2)   

    # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="address-level2"]'))).send_keys("Cupertino, CA")
    # driver.find_element(By.XPATH, '//*[@autocomplete="address-level2"]').send_keys("Cupertino, CA")
    # time.sleep(5)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@autocomplete="address-level2"]'))).send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, '//*[@autocomplete="address-level2"]').send_keys(Keys.ENTER)
    # print("I am here 5")

    time.sleep(5)





 

