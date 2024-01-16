from selenium import webdriver
from Pages.linkedin_page import LinkedInPage


def main():
    # Initialize the WebDriver (assuming Chrome)
    driver = webdriver.Chrome('drivers/macos/chromedrivermac')

    # Create an instance of LinkedInPage
    linkedin_page = LinkedInPage(driver)

    job_titles = ["Quality Assurance Engineer", "Automation engineer", "energy sector"]
    job_locations = ["Cupertino, CA", "Sunnyvale, CA", 'remote']
    keywords = ["engineer", "python", "selenium", "API", "JS", "JavaScript", "SeleniumWebDriver", "Postman", "PostgreSQL", "SQL"]
    data_dictionary = {}

    try:
        modified_url = 'https://www.linkedin.com/jobs/sqa-engineer-jobs-cupertino-ca?position=1&pageNum=0'
        driver.get(modified_url)
        print("I am loading the page")

        driver.maximize_window()
        print("I am expanding the page")
        
        # Specify job title and the location
        linkedin_page.navigate_to_jobs("software-engineer", "san-francisco")

        # Apply date filter using LinkedInPage instance
        linkedin_page.apply_date_filter()
        
        linkedin_page.click_job_title()

        # Continue with the rest of your logic using LinkedInPage instance

    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        # Close the WebDriver
        driver.quit()
