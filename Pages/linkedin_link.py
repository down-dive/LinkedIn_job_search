from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (assuming Chrome)
driver = webdriver.Chrome('drivers/macos/chromedrivermac')

job_titles = ["Quality Assurance Engineer", "Automation engineer", "energy sector"]
job_locations = ["Cupertino, CA", "Sunnyvale, CA", 'remote']
# keywords = ["python", "selenium", "API", "JS", "JavaScript", "SeleniumWebDriver", "Postman", "PostgreSQL", "SQL"]
keywords = ["engineer"]

data_dictionary = {

}

def link():
    try:
        # Iterate through job titles and locations
        for job_title in job_titles:
            for job_location in job_locations:
                # Modify the job title and location in the URL
                # modified_url = f'https://www.linkedin.com/jobs/{job_title.lower().replace(" ", "-")}-jobs-{job_location.lower().replace(", ", "-")}/'
                modified_url = 'https://www.linkedin.com/jobs/sqa-engineer-jobs-cupertino-ca?position=1&pageNum=0'

                # Open the modified URL
                driver.get(modified_url)
                wait = WebDriverWait(driver, 10)
                time.sleep(5)
                print("I am loading the page")

                # Maximize or expand the browser window
                # driver.maximize_window()
                # print("I am expanding the page")

                # #change the date filter
                # wait.until(
                #     EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Date posted filter. Any Time filter is currently applied. Clicking this button displays all Date posted filter options." ]'))
                # ).click()
                # time.sleep(5)
                # wait.until(
                #     EC.element_to_be_clickable((By.XPATH, '//label[contains(text(),"Past Week")]'))
                # ).click()
                # wait.until(
                #     EC.element_to_be_clickable((By.XPATH, "//*[@class='filter__submit-button']"))
                # ).click()
                # print("I am changing the date filter") 

                # Clicking on each job title on the page

                # Wait for the title to be present on the page
                titles = wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@data-tracking-control-name="public_jobs_jserp-result_search-card"]'))
                )

                # Sort elements based on their position
                # sorted_titles = sorted(titles, key=lambda e: e.location_once_scrolled_into_view['y'])

                # Iterate through each element, scroll to it, and click
                # Wait for the first element to be clickable
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-tracking-control-name="public_jobs_jserp-result_search-card"]')))

                # Find all elements matching the given XPath
                # titles = driver.find_elements(By.XPATH, '//*[@data-tracking-control-name="public_jobs_jserp-result_search-card"]')

                # Iterate through the elements and click on each one
                # for index, title in enumerate(titles):
                #     title.click()
                #     print(f"I am clicking on title {index + 1}")
                #     time.sleep(3)

                #     # Expands the page
                #     expand_button_locator = (By.XPATH, '//*[@aria-label="Show more, visually expands previously read content above"]')
                #     wait.until(EC.element_to_be_clickable(expand_button_locator)).click()
                #     print("I am expanding the page")
                #     time.sleep(3)

                #     # Extract the text content of the page
                #     job_describtion_extracted = driver.find_element(By.XPATH, "//div[@class='show-more-less-html__markup relative overflow-hidden']").text
                #     title = driver.find_element(By.XPATH, "//a[@class='topcard__link']").text
                #     # company = driver.find_element(By.XPATH, "//div[@class='show-more-less-html__markup relative overflow-hidden']").text
                #     # location = driver.find_element(By.XPATH, "//div[@class='show-more-less-html__markup relative overflow-hidden']").text
                #     # print(job_describtion_extracted)
                #     print(title)

                #     # Check if all keywords are present in the page text
                #     all_keywords_present = all(keyword.lower() in job_describtion_extracted.lower() for keyword in keywords)

                #     # Print the result
                #     if all_keywords_present:
                #             print("All keywords are present in the text.")
                #     else:
                #             print("Not all keywords are present in the text.") 

                 # Expands the page
                expand_button_locator = (By.XPATH, '//*[@aria-label="Show more, visually expands previously read content above"]')
                wait.until(EC.element_to_be_clickable(expand_button_locator)).click()
                print("I am expanding the page")
                time.sleep(3)

                # Extract the text content of the page

                job_title_extracted = driver.find_element(By.XPATH, "//a[@class='topcard__link']").text
                print(job_title_extracted)
                data_dictionary['title'] = job_title_extracted
                company_extracted = driver.find_element(By.XPATH, "//a[@class='topcard__org-name-link topcard__flavor--black-link']").text
                print(company_extracted)
                data_dictionary['company'] = company_extracted
                location_extracted = driver.find_element(By.XPATH, "//span[@class='topcard__flavor topcard__flavor--bullet']").text
                data_dictionary['location'] = location_extracted
                print(location_extracted)
                job_describtion_extracted = driver.find_element(By.XPATH, "//div[@class='show-more-less-html__markup relative overflow-hidden']").text
                data_dictionary['describtion'] = job_describtion_extracted
                print(data_dictionary)



    except Exception as e:
        print(f"An exception occurred: ", e)

    #     finally:
    #         # Close the browser
    #         driver.quit()

    # def write_to_document(description, output_path):
    #     if description:
    #         document = Document()
    #         document.add_paragraph(description)
    #         document.save(output_path)
    #         print(f"Description written to {output_path}")
    #     else:
    #         print("Not all keywords found on the web page.")

        print("I am at the end")
        time.sleep(2)
        driver.quit()

        