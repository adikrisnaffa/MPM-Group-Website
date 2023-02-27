from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading

def run_test(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Login to the website
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()


# Start 100 threads to simulate 100 concurrent users
threads = []
for i in range(100):
    username = "user" + str(i+1)
    password = "password" + str(i+1)
    t = threading.Thread(target=run_test, args=(username, password))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
