from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
wait = WebDriverWait(driver, 10)     #espera a que cargue la pagina para poder encontrar el elemento
t=1

nom = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'Full Name')]")))  #le da la condicion de que haya visibilidad del elemento para seleccionarlo
nom.send_keys("Franco")
time.sleep(t)


mail= wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'userEmail')]")))
mail.send_keys("aaabbb@gmail.com")
time.sleep(t)

dire = wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='currentAddress']")))
dire.send_keys("aaa 123")
time.sleep(t)

dire2=wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[contains(@id,'permanentAddress')]")))
dire2.send_keys("bbb 123")
time.sleep(t)

driver.execute_script("window,scrollTo(0,300)")  #scrollea
time.sleep(2)


submit = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id,'submit')]")))
submit.click()
time.sleep(t)







driver.close()
