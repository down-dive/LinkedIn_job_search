from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from .common import CommonOps

import time
import csv
import sys

job_titles = ["Quality Assurance Engineer", "Automation engineer", "energy sector"]
job_locations = ["Cupertino, CA", "Sunnyvale, CA", 'remote']
keywords = ["engineer", "python", "selenium", "API", "JS", "JavaScript", "SeleniumWebDriver", "Postman", "PostgreSQL", "SQL"]
# keywords = ["engineer"]

data_dictionary = {}

def write_data_to_csv(data_dict):
    if data_dict:
        # Write the dictionary data to a CSV file
        csv_file_path = "output_data.csv"
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write header if needed
            csv_writer.writerow(['Key', 'Value'])

            # Write data from the dictionary to the CSV file
            for key, value in data_dict.items():
                csv_writer.writerow([key, value])

        print(f"Data has been written to {csv_file_path}")
    else:
        print("No data has been written to the CSV file, the dictionary is empty")
        
        
class LinkedInPage(CommonOps):
    
    ANYTIME_BUTTON = (By.XPATH, '//*[@aria-label[contains(., "Date posted filter")]]')
    PAST_WEEK_BUTTON = (By.XPATH, '//label[contains(text(),"Past Week")]')
    DONE_BUTTON = (By.XPATH, "//*[@class='filter__submit-button']")
    TITLES = (By.XPATH, '//*[@data-tracking-control-name="public_jobs_jserp-result_search-card"]')
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def apply_date_filter(self):
        print(" I am on date filter")

        self.wait_for(self.ANYTIME_BUTTON).click()

        self.wait_for(self.PAST_WEEK_BUTTON).click()

        self.wait_for(self.DONE_BUTTON).click()

        
    def click_job_title(self):
        print("I am on titles")
        # Clicking on each job title on the page
        
        self.wait_for(self.TITLES)
        time.sleep(5)
        print(len(self.TITLES))

   
        print("Titles are located")
        
        for index in range(len(self.TITLES)):
            if index < len(self.TITLES):
                print(len(self.TITLES))
                try:
                    # TITLES = self.driver.find_elements(By.XPATH, '//*[@data-tracking-control-name="public_jobs_jserp-result_search-card"]')
                    # print("I am self")
                    title = self.TITLES[index]
                    # element_present = EC.presence_of_element_located((By.XPATH, f'(//*[@data-tracking-control-name="public_jobs_jserp-result_search-card"])[{index + 1}]'))
                    # WebDriverWait(driver, timeout).until(element_present)

                    # title.click()
                    # print(f"I am clicking on title {index + 1}")
                    # current_url = self.driver.current_url
                    # print("Current Webpage URL:", current_url)

                    expand_button_locator = (By.XPATH, '//*[@aria-label="Show more, visually expands previously read content above"]')
                    self.wait.until(EC.element_to_be_clickable(expand_button_locator)).click()
                    print("I am expanding the page")

                    job_title_extracted = self.driver.find_element(By.XPATH, "//a[@class='topcard__link']").text
                    company_extracted = self.driver.find_element(By.XPATH, "//a[@class='topcard__org-name-link topcard__flavor--black-link']").text
                    location_extracted = self.driver.find_element(By.XPATH, "//span[@class='topcard__flavor topcard__flavor--bullet']").text
                    job_description_extracted = self.driver.find_element(By.XPATH, "//div[@class='show-more-less-html__markup relative overflow-hidden']").text

                    found_keywords = [keyword for keyword in keywords if keyword.lower() in job_description_extracted.lower()]

                    if found_keywords:
                        print("Success: Found the following keyword(s):", ', '.join(found_keywords))
                        data_dictionary['title'] = job_title_extracted
                        data_dictionary['company'] = company_extracted
                        data_dictionary['location'] = location_extracted
                        data_dictionary['keywords'] = found_keywords
                        # data_dictionary['link'] = current_url
                        data_dictionary['description'] = job_description_extracted
                    else:
                        print("Not all keywords are present in the text.")

                except (TimeoutException, StaleElementReferenceException) as e:
                    print(f"Exception occurred: {e}. Reloading the page...")
                    self.driver.refresh()
                    expand_button_locator = (By.XPATH, '//*[@aria-label="Show more, visually expands previously read content above"]')
                    self.wait.until(EC.element_to_be_clickable(expand_button_locator)).click()
                    print("I am expanding the page")
                    job_title_extracted = self.driver.find_element(By.XPATH, "//a[@class='topcard__link']").text
                    company_extracted = self.driver.find_element(By.XPATH, "//a[@class='topcard__org-name-link topcard__flavor--black-link']").text
                    location_extracted = self.driver.find_element(By.XPATH, "//span[@class='topcard__flavor topcard__flavor--bullet']").text
                    job_description_extracted = self.driver.find_element(By.XPATH, "//div[@class='show-more-less-html__markup relative overflow-hidden']").text
                    
                    found_keywords = [keyword for keyword in keywords if keyword.lower() in job_description_extracted.lower()]

                    if found_keywords:
                        print("Success: Found the following keyword(s):", ', '.join(found_keywords))
                        data_dictionary['title'] = job_title_extracted
                        data_dictionary['company'] = company_extracted
                        data_dictionary['location'] = location_extracted
                        data_dictionary['keywords'] = found_keywords
                        # data_dictionary['link'] = current_url
                        data_dictionary['description'] = job_description_extracted
                    else:
                        print("Not all keywords are present in the text.")


