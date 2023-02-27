import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Fungsi untuk mengukur FCP
@pytest.mark.test_fcp
def test_fcp(context):
    script = """
    var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {};
    var timings = performance.timing || {};
    return timings.responseStart - timings.navigationStart;
    """
    fcp_time = context.execute_script(script)
    assert fcp_time < 1000
