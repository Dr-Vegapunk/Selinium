from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
import time


options = Options()
driver = webdriver.Chrome(options=options)  
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
