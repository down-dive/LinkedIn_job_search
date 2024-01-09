from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

def landing():
    
    driver = webdriver.Chrome('drivers/macos/chromedrivermac')

    driver.get('https://www.linkedin.com')

   