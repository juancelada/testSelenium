from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://testingqarvn.com.es/prueba-de-campos-checkbox/")
driver.maximize_window()
driver.implicitly_wait(10)
t=3

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(@id,'wsf-1-label-36-row-1')]")))
btn1.click()

btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(@id,'wsf-1-label-36-row-2')]")))
btn2.click()


time.sleep(t)
driver.close()
