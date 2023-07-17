from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://testingqarvn.com.es/combobox/")
driver.maximize_window()
driver.implicitly_wait(10)
t=3

driver.execute_script("window,scrollTo(0,500)")
sistSelect = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'wsf-1-field-53')]")))
ds=Select(sistSelect)


ds.select_by_visible_text("Windows")


time.sleep(t)
driver.close()
