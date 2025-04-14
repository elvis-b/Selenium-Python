import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def setup():
    options = ChromeOptions()
    options.add_argument("--start-maximized")  # Maximizes the window
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(2)  # Implicit wait for 2 seconds
    yield driver  # Provide the driver to the test
    driver.quit()  # Cleanup after the test

def navigate_to_amazon(driver):
    driver.get("https://www.amazon.in")

def click_todays_deals(driver):
    todays_deals = driver.find_element(By.LINK_TEXT, "Today's Deals")
    todays_deals.click()

def click_clearance(driver):
    clearance_link = driver.find_element(By.XPATH, "//a[@aria-label='Clearance']")
    clearance_link.click()

def click_watches(driver):
    watches_link = driver.find_element(By.XPATH, "//img[@src='https://m.media-amazon.com/images/G/31/img21/Fashion/Event/Jan-ART/Event-page/Clearance_Store_Refresh/Fashion/ClearanceStore_Fashion_04._SY530_QL85_.jpg']")
    watches_link.click()

def select_get_it_tomorrow(driver): #Selecting Get It by Tomorrow instead of Get It Today as "get it today" does not appear as an option
    get_it_tomorrow_checkbox = driver.find_element(By.XPATH, "//span[text()='Get It by Tomorrow']")
    get_it_tomorrow_checkbox.click()

def validate_results_message(driver):
    results_message = driver.find_element(By.XPATH, "//h2[text()='Results']")
    assert results_message.is_displayed(), "Results message not displayed."

def validate_first_item_name(driver):
    first_item = driver.find_element(By.XPATH, "//div[@class='s-main-slot s-result-list s-search-results sg-row']//div[@role='listitem'][1]")
    item_name = first_item.text
    assert "Watch" in item_name, f"Expected 'Watch' in the item name, but got: {item_name}"
    print(f"First item name: {item_name}")

def test_automation_2(setup):
    navigate_to_amazon(setup)
    click_todays_deals(setup)
    click_clearance(setup)
    click_watches(setup)
    select_get_it_tomorrow(setup)

    # Validate results message
    validate_results_message(setup)

    # Validate the first item's name contains "Watch"
    validate_first_item_name(setup)