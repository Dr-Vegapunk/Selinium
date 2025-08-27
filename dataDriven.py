from selenium import webdriver
from selenium.webdriver.common.by import By
import csv, time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

with open("data.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        username = line["username"]
        password = line["password"]

        # Clear and enter username
        user_input = driver.find_element(By.ID, "user-name")
        user_input.clear()
        user_input.send_keys(username)

        # Clear and enter password
        pass_input = driver.find_element(By.ID, "password")
        pass_input.clear()
        pass_input.send_keys(password)

        # Click login button
        driver.find_element(By.ID, "login-button").click()

        # Check if inventory page is reached
        assert "inventory" in driver.current_url, f"Login failed for user {username}"

        time.sleep(2)  # Small wait to stabilize

        # Log out to prepare for next login attempt
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)

driver.quit()
