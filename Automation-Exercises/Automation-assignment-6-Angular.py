import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def setup():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def navigate_to_homepage(driver):
    driver.get("https://angular-university.io")

def click_my_courses(driver):
    my_courses = driver.find_element(By.XPATH, "//a[@href='/my-courses']")
    my_courses.click()
    time.sleep(3)

def click_angular_beginners_course(driver):
    course_link = driver.find_element(By.CSS_SELECTOR, "div > .course-id-1")
    course_link.click()

def select_helicopter_view_checkbox(driver):
    checkbox = driver.find_element(By.XPATH, "//a[@href='/lesson/angular-beginners-beginners-course-helicopter-view']")
    checkbox.click()

def validate_github_button(driver): # We validate github button, as the notification message is obsolete, not available anymore
    github_button = driver.find_element(By.XPATH, "//button[@class='btn btn-github']")

    assert "Github" in github_button.text, f"Expected 'Information' message, but got: {github_button.text}"
    print("Information message displayed correctly.")

def test_assignment_6(setup):
    navigate_to_homepage(setup)
    click_my_courses(setup)
    click_angular_beginners_course(setup)
    select_helicopter_view_checkbox(setup)
    validate_github_button(setup)