from selenium import webdriver;
from selenium.webdriver.common.by import By;

driver= webdriver.Chrome();
driver.get("https://www.saucedemo.com/");
driver.maximize_window(); # Maximize the browser window

driver.find_element(By.ID, "user-name").send_keys("standard_user");
driver.find_element(By.ID, "password").send_keys("secret_sauce");

#from x-path
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce");


driver.find_element(By.ID, "login-button").click();

assert "inventor" in driver.current_url, "Login failed, inventory page not reached";

driver.implicitly_wait(10); # Wait for elements to load
#wait to seen login successfully then close the browser
driver.find_element(By.ID, "react-burger-menu-btn").click();