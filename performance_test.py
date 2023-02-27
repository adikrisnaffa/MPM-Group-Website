import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Fungsi untuk mengukur waktu loading
def test_performance(context):
    context.get("https://www.saucedemo.com/inventory.html")
    start_time = time.time()
    context.find_element(By.CLASS_NAME,"inventory_item").click()
    end_time = time.time()
    assert end_time - start_time < 10
