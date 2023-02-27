from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.logout
def test_logout(context):
# Login
    username = context.find_element(By.ID, "user-name")
    password = context.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button = context.find_element(By.ID, "login-button")
    login_button.click()
    print(context.find_element(By.XPATH, '//span[@class="title"]').text)

# Logout
    menu = context.find_element(By.ID, 'react-burger-menu-btn')
    menu.click()
    logout = context.find_element(By.ID, 'logout_sidebar_link')
    logout.click()