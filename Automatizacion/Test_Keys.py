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

nom = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@placeholder,'Full Name')]")))  #le da la condicion de que haya visibilidad del elemento para seleccionarlo
nom.send_keys("Franco")
time.sleep(1)
nom.send_keys(Keys.TAB + "francoduepre@gmail.com" + Keys.TAB + "aaa123" + Keys.TAB + "bbb 123" + Keys.TAB + Keys.ENTER)
time.sleep(2)


#se hace topdo directo del primer cuadro de texto y se le va haceindo tab 











driver.close()
