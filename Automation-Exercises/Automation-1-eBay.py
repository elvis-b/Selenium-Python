import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup(request):
    options = Options()
    options.add_argument("--start-maximized")  # Maximizes the window
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(2)
    yield driver  # Provide the driver to the test
    driver.quit()  # Cleanup after the test

def navigate_to_ebay(driver):
    driver.get("https://www.ebay.com")

def search_for_keyword(driver, keyword="Selenium"):
    search_box = driver.find_element(By.XPATH, "//input[@title='Search']")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_box.send_keys(keyword)
    submit_button.click()

def click_buy_it_now(driver):
    buy_it_now = driver.find_element(By.XPATH, "//div[@class='fake-tabs srp-format-tabs']//span[contains(text(),'Buy It Now')]")
    buy_it_now.click()

def select_time_newly_listed(driver):
    best_match_option = driver.find_element(By.XPATH, "//button[@aria-label='Sort selector. Best Match selected.']")
    best_match_option.click()

    newly_listed_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Time: newly listed']"))
    )
    newly_listed_option.click()


def newly_listed_date(driver):
    try:
        # Wait for the date elements to be visible
        listed_dates = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 's-item__dynamic.s-item__listingDate'))
        )

        # Filter out the dates that contain "Apr"
        apr_dates = []
        for date_element in listed_dates:
            bold_date_element = date_element.find_element(By.CLASS_NAME, 'BOLD')
            date_text = bold_date_element.text

            if "Apr" in date_text:
                apr_dates.append(date_text)

        if apr_dates:
            # Assert if the first "Apr" date is found
            first_apr_date = apr_dates[0]
            print(f"First Apr date: {first_apr_date}")
            return first_apr_date
        else:
            print("No 'Apr' dates found.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def test_automation_1(setup):
    navigate_to_ebay(setup)
    search_for_keyword(setup, "Selenium")
    click_buy_it_now(setup)
    select_time_newly_listed(setup)
    first_item_date = newly_listed_date(setup)

    # Print and assert that the first item's date contains "Apr"
    assert first_item_date and "Apr" in first_item_date, "No item date found or 'Apr' is missing."
    print(f"First item date: {first_item_date}")
