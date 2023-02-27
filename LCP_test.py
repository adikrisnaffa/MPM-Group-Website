import time
import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Fungsi untuk mengukur LCP
@pytest.mark.test_lcp
def test_lcp(context):
    lcp_script = """const observer = new PerformanceObserver((list) => {
                          for (const entry of list.getEntries()) {
                            if (entry.name === 'largest-contentful-paint') {
                              console.log(entry.startTime);
                            }
                          }
                        });
                    observer.observe({type: 'largest-contentful-paint', buffered: true});
                    """
    context.execute_script(lcp_script)
    time.sleep(5)