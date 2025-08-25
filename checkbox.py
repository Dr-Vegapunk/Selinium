from selenium import webdriver;
from selenium.webdriver.common.by import By;
import time

driver1 = webdriver.Chrome();
driver1.get("https://the-internet.herokuapp.com/checkboxes");  

driver2 = webdriver.Chrome();
driver2.get("https://the-internet.herokuapp.com/download");

driver3= webdriver.Chrome();
driver3.get("https://the-internet.herokuapp.com/upload");

checkbox1 = driver1.find_element(By.XPATH, "//input[@type='checkbox'][1]");
checkbox2 = driver1.find_element(By.XPATH, "//input[@type='checkbox'][2]");

download = driver2.find_element(By.LINK_TEXT, "SomeFile.txt");
download2 = driver2.find_element(By.LINK_TEXT, "kote.jpg");

upload = driver3.find_element(By.ID, "file-upload");

# checkbox1.click();
checkbox2.click();
download.click();
download2.click();


print("Checkbox 1 is selected:", checkbox1.is_selected());
print("Checkbox 2 is selected:", checkbox2.is_selected());

time.sleep(5); # Wait for 5 seconds to see the result

driver1.quit();

driver2.quit();
