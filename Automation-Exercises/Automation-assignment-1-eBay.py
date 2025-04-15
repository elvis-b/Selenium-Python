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
    search_box = driver.find_element(By.CSS_SELECTOR, "form > div:nth-child(1) input")
    submit_button = driver.find_element(By.CLASS_NAME, "gh-search-button__label")
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

def validate_newly_listed_date(driver):
    date_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 's-item__dynamic.s-item__listingDate'))
    )
    assert "Apr" in date_text.text, f"Expected 'Apr' in item info, but got: {date_text.text}"
    print(f"First item shows 'Apr' in date info: {date_text.text}")

def test_automation_1(setup):
    navigate_to_ebay(setup)
    search_for_keyword(setup, "Selenium")
    click_buy_it_now(setup)
    select_time_newly_listed(setup)
    validate_newly_listed_date(setup)
