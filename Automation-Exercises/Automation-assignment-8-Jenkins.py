import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import re


@pytest.fixture
def setup():
    options = FirefoxOptions()
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def navigate_to_jenkins(driver):
    driver.get("https://www.jenkins.io")

def click_documentation(driver):
    documentation_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/doc/']"))
    )
    documentation_button.click()

def click_guided_tour(driver):
    guided_tour = driver.find_element(By.LINK_TEXT, "Guided Tour") #//a[contains(text(), 'Guided Tour')]
    guided_tour.click()

def click_was_this_page_helpful(driver):
    helpful_link = driver.find_element(By.XPATH, "//a[@href='#feedback']")
    helpful_link.click()

def select_yes_radio(driver):
    yes_radio = driver.find_element(By.XPATH, "//input[@value='Yes']")
    yes_radio.click()

def enter_sum_and_submit(driver):
    math_label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ssTestLabel"))
    )
    math_text = math_label.text

    # Use regex to extract the numbers
    numbers = list(map(int, re.findall(r'\d+', math_text)))
    if len(numbers) == 2:
        total = numbers[0] + numbers[1]
    else:
        raise ValueError(f"Expected two numbers to sum, but found: {numbers}")

    # Fill in the calculated sum
    answer_input = driver.find_element(By.NAME, "ssTestValue")
    answer_input.clear()
    answer_input.send_keys(str(total))

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit_button.click()

def validate_thank_you_message(driver):
    # Wait until the element is visible
    thank_you = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'thank-you-for-your-feedback'))
    )

    assert thank_you.is_displayed(), "Thank you message not displayed."
    print("Feedback submitted successfully!")

def test_assignment_8(setup):
    navigate_to_jenkins(setup)
    click_documentation(setup)
    click_guided_tour(setup)
    click_was_this_page_helpful(setup)
    select_yes_radio(setup)
    enter_sum_and_submit(setup)
    validate_thank_you_message(setup)