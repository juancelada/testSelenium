from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
time.sleep(2)

driver.get("https://asijira.buenosaires.gob.ar/secure/Dashboard.jspa")
time.sleep(2)

driver.get("https://www.youtube.com")

driver.back()
time.sleep(2)
driver.execute_script("window.history.go(-1)")
time.sleep(2)
