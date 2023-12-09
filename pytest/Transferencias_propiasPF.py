import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Agrega esta línea
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType
from Funciones.Funciones import Funciones_Globales

class btest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @allure.feature("Navegador y Sistema Operativo")
    @allure.story("Chrome en Windows 10")

    def test1_transferencia(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://mifel.net/qa-banca-electronica-pf/", 3)
        wait = WebDriverWait(driver, 10)

        autenticacion = Funciones_Globales(driver)
        autenticacion.ingresar_usuario("rick88")
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.form-ingresar")))
        button.click()

        autenticacion = Funciones_Globales(driver)
        autenticacion.ingresar_contrasena("testing34")
        continuar_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='button'][contains(.,'Continuar')]")))
        continuar_button.click()


        llavero = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div/form/div/div[1]/span/div/div[1]/div/input")))
        llavero.send_keys("99999999")
        allure.attach(driver.get_screenshot_as_png(), name="Ingresar token", attachment_type=AttachmentType.PNG)
        boton_autorizar = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[2]/div/div/form/div/div[2]/button")))
        # Hacer clic en el botón "Autorizar"
        boton_autorizar.click()
        #Menú hamburguesa

        hamburguesa = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='open lnu']")))
        hamburguesa.click();
        allure.attach(driver.get_screenshot_as_png(), name="Seleccionar menú hamburguesa", attachment_type=AttachmentType.PNG)

        opctransferencia = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@translate-en,'My transfers') or contains(@translate-es,'Mis transferencias')]")))
        opctransferencia.click();
        allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Transferencia", attachment_type=AttachmentType.PNG)

        opcrealizartran = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Realizar una transferencia")))
        allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Realizar una transferencia",attachment_type=AttachmentType.PNG)
        opcrealizartran.click()

        driver.implicitly_wait(1)
        montos = ["0.70", "0.80", "0.90", "0.70", "0.80", "0.90", "0.70", "0.80", "0.90", "0.70"]
        for i in range(len(montos)):
            #  allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Realizar Transferencia", attachment_type=AttachmentType.PNG)
            boton_propias = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/section/div/div[2]/div/div[2]/div[2]/div[1]/button[2]")))
            # Haz clic en el botón "Propias"
            allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Propias",attachment_type=AttachmentType.PNG)
            boton_propias.click()

            # Esperar 1 segundo
            driver.implicitly_wait(1)
            allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Cuenta",attachment_type=AttachmentType.PNG)
            # Btn seleccionar cuenta
            selCuenta = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Cuenta Básica Nómina')]")))
            # Hacer clic en el elemento
            selCuenta.click()
            #Esperar a que aparezaca el botón Continuar
            elemento_continuar = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Continuar')]")))

            # Ingresar monto
            inputMonto = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='Monto a transferir']")))
            inputMonto.send_keys(montos[i])
            allure.attach(driver.get_screenshot_as_png(), name="Ingresar Monto"+montos[i], attachment_type=AttachmentType.PNG)
            driver.implicitly_wait(1)
            # Captura btnContinuar
            boton_continuar = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='mifel-btn transfer-amount__button mifel-btn-primary mifel-btn-block']")))
            # Hacer clic en el botón
            boton_continuar.click()

            # Agregar un tiempo de espera de 5 segundos
            driver.implicitly_wait(1)

            # BtnConfirmar
            botnconfirmar = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Confirmar')]")))
            # Hacer clic en el botón "Confirmar"
            allure.attach(driver.get_screenshot_as_png(), name="Confirmar",attachment_type=AttachmentType.PNG)
            botnconfirmar.click()
            allure.attach(driver.get_screenshot_as_png(), name="err", attachment_type=AttachmentType.PNG)
            driver.implicitly_wait(5)
            #Esperar al texto "Trasferencia"
            exitosa = wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="voucher"]/section[1]/section/span'),'¡Transferencia exitosa!'))
            allure.attach(driver.get_screenshot_as_png(), name="Transferencia Exitosa",attachment_type=AttachmentType.PNG)
            time.sleep(4)
            # Desplazar el scroll hacia abajo (por ejemplo, 500 píxeles)
            driver.execute_script("window.scrollBy(0, 550)")

            time.sleep(1)
            # Localizar y dar clic en el botón "Nueva transferencia"
            btnnuevatransfer = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Nueva transferencia')]")))
            # Hacer clic en el botón "Nueva Transferencia"
            btnnuevatransfer.click()
            time.sleep(1)

            # Espera hasta que la imagen sea visible
        imagen_element = wait.until(EC.presence_of_element_located((By.XPATH,"//img[@src='https://d3vtsr5ffy4e4a.cloudfront.net/uploads/4bdb4c62-ac38-4bf9-8480-cdc8ceaa1d8b/original/icon-logout.svg']")))
        # Hace clic en la imagen
        imagen_element.click()

        # Espera hasta que el botón "Sí, cerrar sesión" sea clickable
        boton_cerrar_sesion = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Sí, cerrar sesión']")))

        # Hace clic en el botón "Sí, cerrar sesión"
        boton_cerrar_sesion.click()

    def tearDown(self):
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()
