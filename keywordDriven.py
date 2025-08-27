from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv, time

def perform_action(driver, keyword, locator, value):
    if keyword == "enter-text":
        element = driver.find_element(By.ID, locator)
        element.clear()
        element.send_keys(value)

    elif keyword == "click":
        element = driver.find_element(By.ID, locator)
        element.click()

    elif keyword == "logout":
    # Only logout if we're on the inventory page
     if "inventory" in driver.current_url:
        try:
            wait = WebDriverWait(driver, 10)

            # Wait for menu button and click it
            menu_button = wait.until(
                EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
            )
            menu_button.click()

            # Wait until logout link is clickable
            logout_link = wait.until(
                EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
            )
            logout_link.click()
            print("✅ Logged out successfully.")

            # 🔑 Wait until login page loads again
            wait.until(EC.presence_of_element_located((By.ID, "user-name")))

        except Exception as e:
            print(f"⚠️ Could not log out: {e}")
        else:
            print("⚠️ Not on inventory page, skipping logout.")

    elif keyword == "enter-text":
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located((By.ID, locator))
        )
        element.clear()
        element.send_keys(value)

    elif keyword == "assert-url":
        assert value in driver.current_url, f"❌ Assertion failed! '{value}' not in {driver.current_url}"

    else:
        print(f"⚠️ Unknown keyword: {keyword}")

# Start browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

with open("keyword.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        keyword = line["keyword"]
        locator = line["locator"]
        value = line["value"]

        perform_action(driver, keyword, locator, value)
        time.sleep(1)

time.sleep(3)
driver.quit()
