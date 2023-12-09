import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
nom = driver.find_element(By.ID, 'userName')
nom.send_keys("Abraham")

email = driver.find_element(By.ID,'userEmail').send_keys("abraham@gmail.com")
direccion = driver.find_element(By.ID, 'currentAddress').send_keys("ignacio allende 4000")
extra = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys("hola")

driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
boton = driver.find_element(By.ID, 'submit').click()

# Para mantener la ventana abierta durante unos segundos antes de cerrarla
time.sleep(5)

driver.close()