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

@pytest.mark.standard_user
def test_standard_user(context):
# Login
    username = context.find_element(By.ID, "user-name")
    password = context.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button = context.find_element(By.ID, "login-button")
    login_button.click()
    print(context.find_element(By.XPATH, '//span[@class="title"]').text)

# Select product
    inventory_item = context.find_element(By.XPATH, "//div[@class='inventory_list']//div[@class='inventory_item'][1]")
    inventory_item.click()


# Add product to cart
    add_to_cart_button = context.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()


# Checkout
    shopping_cart_link = context.find_element(By.ID, "shopping_cart_container")
    shopping_cart_link.click()
    checkout_button = context.find_element(By.ID, "checkout")
    checkout_button.click()

# Fill out checkout information
    first_name = context.find_element(By.ID, "first-name")
    last_name = context.find_element(By.ID, "last-name")
    postal_code = context.find_element(By.ID, "postal-code")
    first_name.send_keys("Adikrisna")
    last_name.send_keys("Nugraha")
    postal_code.send_keys("12345")

# Continue to next page
    continue_button = context.find_element(By.ID, "continue")
    continue_button.click()
    time.sleep(5)

# Complete order
    finish_button = context.find_element(By.ID, "finish")
    finish_button.click()
    time.sleep(5)

# Verify order confirmation
    confirmation_message = WebDriverWait(context, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='THANK YOU FOR YOUR ORDER']")))
    assert confirmation_message.is_displayed()
    time.sleep(5)