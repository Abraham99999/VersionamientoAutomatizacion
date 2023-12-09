import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
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

        element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/span/div/div[1]/div/input")))
        try:
            element.send_keys("rick88")
            allure.attach(driver.get_screenshot_as_png(), name="Ingresar usuario", attachment_type=AttachmentType.PNG)

            button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.form-ingresar")))
            button.click()
            contrasena = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'password')]")))

        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), name="Error inesperado", attachment_type=AttachmentType.PNG)

        contrasena.send_keys("testing34")

        allure.attach(driver.get_screenshot_as_png(), name="Ingresar contraseña", attachment_type=AttachmentType.PNG)

        continuar_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='button'][contains(.,'Continuar')]")))
        continuar_button.click()

        llavero = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div/form/div/div[1]/span/div/div[1]/div/input")))
        llavero.send_keys("99999999")
        allure.attach(driver.get_screenshot_as_png(), name="Ingresar token", attachment_type=AttachmentType.PNG)
        boton_autorizar = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div[2]/div/div/form/div/div[2]/button")))
        # Hacer clic en el botón "Autorizar"
        boton_autorizar.click()
        # Menú hamburguesa

        hamburguesa = wait.until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='open lnu']")))
        hamburguesa.click()
        allure.attach(driver.get_screenshot_as_png(), name="Seleccionar menú hamburguesa", attachment_type=AttachmentType.PNG)

        opctransferencia = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@translate-en,'My transfers') or contains(@translate-es,'Mis transferencias')]")))
        opctransferencia.click()
        allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Transferencia", attachment_type=AttachmentType.PNG)

        opcrealizartran = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Realizar una transferencia")))
        allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Realizar una transferencia",attachment_type=AttachmentType.PNG)
        opcrealizartran.click()

        driver.implicitly_wait(1)
        montos = ["1.00", "0.80", "0.90"]
        for i in range(len(montos)):
            boton_rapidas = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mifel-btn-primary")))
            allure.attach(driver.get_screenshot_as_png(), name="Seleccionar Propias",attachment_type=AttachmentType.PNG)
            boton_rapidas.click()

            driver.implicitly_wait(1)

            input_cuenta = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form-control")))
            input_cuenta.send_keys("5264760096356901")
            #allure.attach(driver.get_screenshot_as_png(), name="Se ingresa la cuenta", attachment_type=AttachmentType.PNG)

            boton_validar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mifel-btn-primary")))
            boton_validar.click()

            label_banco = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mifel-dropdown--label')))
            time.sleep(3)
            driver.execute_script("window.scrollBy(0, 550)")

            input_nombre = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@title,'Nombre')]")))
            input_nombre.send_keys("Abraham")
            allure.attach(driver.get_screenshot_as_png(), name="Ingresar el Nombre", attachment_type=AttachmentType.PNG)
            time.sleep(1)
            #driver.execute_script("window.scrollBy(500, 800)")

            boton_continuar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mifel-btn-primary")))
            boton_continuar.click()
            time.sleep(1)
            input_monto = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form-control")))
            input_monto.send_keys((montos[i]))
            allure.attach(driver.get_screenshot_as_png(), name="Ingresar monto", attachment_type=AttachmentType.PNG)
            time.sleep(1)
            # input_monto.send_keys(Keys.ENTER)

            boton_cont = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mifel-btn-primary")))
            boton_cont.click()
            time.sleep(1)
            tokenauz = wait.until(EC.presence_of_element_located((By.NAME, "Contraseña token")))
            tokenauz.send_keys("999999")
            #time.sleep(1)
            try:

                boton_autorizar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mifel-btn-primary")))
                boton_autorizar.click()
            except TimeoutException:
                # El pop-up de error apareció, captura de pantalla con Allure
                allure.attach(driver.get_screenshot_as_png(), name="Error al procesar datos",attachment_type=AttachmentType.PNG)
            except Exception as e:
                # Otro tipo de error, también captura de pantalla
                allure.attach(driver.get_screenshot_as_png(), name="Error inesperado",attachment_type=AttachmentType.PNG)
                allure.attach(driver.get_screenshot_as_png(), name="Error inesperado",
                              attachment_type=AttachmentType.PNG)
        boton_cerrar_sesion = wait.until(EC.presence_of_element_located((By.XPATH, "//p[text()='Sí, cerrar sesión']")))
        boton_cerrar_sesion.click()

    def tearDown(self):
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()
