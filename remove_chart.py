from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

@pytest.mark.remove
def test_remove(context):
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

# Remove
    remove_button = context.find_element(By.ID,"remove-sauce-labs-backpack")
    remove_button.click()
    assert "removed_cart_item" in context.page_source