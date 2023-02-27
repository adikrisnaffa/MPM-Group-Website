from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Buka browser Chrome
browser = webdriver.Chrome()

# Buka website https://www.saucedemo.com/
browser.get("https://www.saucedemo.com/")

# Tunggu hingga page load selesai
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.ID, "login_button_container")))

# Hitung waktu fully loaded
start_time = time.time()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
end_time = time.time()
fully_loaded_time = end_time - start_time

# Cek apakah fully loaded time kurang dari 10 detik
if fully_loaded_time < 10:
    print("Fully loaded time < 10 detik")
else:
    print("Fully loaded time >= 10 detik")

# Tutup browser
browser.quit()
