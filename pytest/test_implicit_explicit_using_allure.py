import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Wikipedia Search")
@allure.story("Search for 'Selenium'")
def test_wikipedia_search(driver):
    with allure.step("Open Wikipedia homepage"):
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()
    
    with allure.step("wait untill the search input is visible"):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "searchInput"))
        )

    with allure.step("Enter search term and submit"):
       search_box = driver.find_element(By.ID, "searchInput")
       search_box.send_keys("Selenium")
    with allure.step("Verify the search term was entered correctly"):
       assert search_box.get_attribute("value") == "Selenium", "Text input failed"
       print("✅ Text input successful")
       search_box.submit()
