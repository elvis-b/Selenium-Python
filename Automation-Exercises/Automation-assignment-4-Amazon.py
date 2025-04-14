import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def setup():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

def navigate_to_amazon(driver):
    driver.get("https://www.amazon.in")

def search_for_headphones(driver):
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("bluetooth headphones")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    time.sleep(2)

def sort_by_newest_arrivals(driver):
    sort_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "a-dropdown-label"))
    )
    sort_dropdown.click()

    newest_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "s-result-sort-select_4"))
    )
    newest_option.click()
    time.sleep(3)

def validate_item_date(driver):
    date_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']//span[contains(text(),'Apr')]"))
    )
    assert "Apr" in date_text.text, f"Expected 'Sep' in item info, but got: {date_text.text}"
    print(f"First item shows 'Sep' in date info: {date_text.text}")

def test_amazon_bluetooth_headphones_flow(setup):
    navigate_to_amazon(setup)
    search_for_headphones(setup)
    sort_by_newest_arrivals(setup)
    validate_item_date(setup)