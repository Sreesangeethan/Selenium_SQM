from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://lms.aps.rjt.ac.lk/login")

from selenium.webdriver.common.by import By

# Locate input fields
username_input = driver.find_element(By.ID, "username")  # Replace "username" with the actual ID or locator
password_input = driver.find_element(By.ID, "password")  # Replace "password" with the actual ID or locator

# Enter valid credentials
username_input.send_keys("testuser")  # Replace with actual username
password_input.send_keys("password123")  # Replace with actual password

# Locate and click the login button
login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

import time

# Delay to allow page loading or use WebDriverWait for a better approach
time.sleep(3)

# Check for successful login
try:
    # Check presence of element that only appears upon successful login
    welcome_message = driver.find_element(By.ID, "welcomeMessage")  # Replace "welcomeMessage" with the actual ID or locator
    print("Login successful!")
except:
    print("Login failed!")

