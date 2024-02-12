import pytest
from Pages.login_page import LoginPage
from Pages.linkedin_page import LinkedInPage
import time
# from dotenv import load_dotenv
from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values(".env")

# Access the environment variables
username = env_vars["USERNAME"]
password = env_vars["PASSWORD"]

# Fixture to log in and return LoginPage instance
# @pytest.fixture
# def logged_in_form(driver):
#     form = LoginPage(driver)
#     form.login(username, password)
#     return form

# Test for valid authentication using the logged_in_form fixture
# def test_valid_authentication(logged_in_form):
#     assert logged_in_form.login_success(), "Login unsuccessful"

def test_linkedin_search(driver):
    linkedinPage = LinkedInPage(driver)
    
    linkedinPage.apply_date_filter()