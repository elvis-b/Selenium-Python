import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def setup():
    options = ChromeOptions()

    # Disable notification pop-ups
    prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def navigate_to_myntra(driver):
    driver.get("https://www.myntra.com")

    # Wait until the page's document.readyState is "complete"
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

def search_for_bluetooth_headphones(driver):
    search_box = driver.find_element(By.CLASS_NAME, "desktop-searchBar")
    search_box.click()
    time.sleep(2)
    search_box.send_keys("Bluetooth headphones")
    search_box.send_keys(Keys.RETURN) # we use Enter as there is no Search button that we can click

def sort_by_whats_new(driver):
    actions = ActionChains(driver)

    # Hover over the "Sort by" container
    sort_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sort-sortBy"))
    )
    actions.move_to_element(sort_container).perform()

    # Wait for the "What's New" option to be clickable
    whats_new_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[contains(., "What\'s New")]'))
    )

    actions.move_to_element(whats_new_option).perform()
    time.sleep(1)
    whats_new_option.click()

    WebDriverWait(driver, 15).until(
        EC.url_contains("sort=new")
    )

    # Optional: Wait for product list to refresh
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-base"))
    )

def filter_by_brand_jbl(driver):
    brand_filter = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'JBL')]"))
    )
    brand_filter.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("JBL")
    )

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-base"))
    )

def validate_first_item_is_jbl(driver):
    time.sleep(5)
    first_item = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "(//ul[@class='results-base']//li[@class='product-base'][1]//h3")) # We get the brand of the first product
    )
    brand_name = first_item.text
    assert "JBL" in brand_name.upper(), f"Expected 'JBL' in the brand name, but got: {brand_name}"
    print(f"First item brand: {brand_name}")

def test_automation_myntra(setup):
    navigate_to_myntra(setup)
    search_for_bluetooth_headphones(setup)
    sort_by_whats_new(setup)
    filter_by_brand_jbl(setup)
    validate_first_item_is_jbl(setup)