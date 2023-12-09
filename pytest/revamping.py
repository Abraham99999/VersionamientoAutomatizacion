import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # Agrega esta línea
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from Funciones.Funciones import Funciones_Globales
from allure_commons.types import AttachmentType

class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        t = 5
        # Configuración de opciones de Chrome
        chrome_options = Options()


        # Preferencias para deshabilitar ciertos elementos en la página
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.notifications": 2,
            "profile.managed_default_content_settings.stylesheets": 2,
            "profile.managed_default_content_settings.cookies": 2,
            "profile.managed_default_content_settings.javascript": 1,
            "profile.managed_default_content_settings.plugins": 1,
            "profile.managed_default_content_settings.popups": 2,
            "profile.managed_default_content_settings.geolocation": 2,
            "profile.managed_default_content_settings.media_stream": 2
        }

        chrome_options.add_experimental_option("prefs", prefs)

        # Otros argumentos
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--enable-logging --v=1')

        # Inicializa el navegador Chrome con las opciones configuradas
        self.driver = webdriver.Chrome(options=chrome_options)

    def test1_validaHeader(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.mifel.com.mx/cert-personas", 6)
        # Espera hasta que el elemento esté presente en la página (puedes ajustar el tiempo según sea necesario)
        wait = WebDriverWait(driver, 10)
        usr = wait.until(EC.presence_of_element_located((By.ID, "user_session_username")))
        # Ingresa el texto en el campo de entrada
        usr.send_keys("abraham.aguilar@mifel.com.mx")

        pswd = wait.until(EC.presence_of_element_located((By.ID, "user_session_password")))
        # Ingresa el texto en el campo de contraseña
        pswd.send_keys("R4z3r2305@#/")
        time.sleep(100)
        btnIngresar = wait.until(EC.presence_of_element_located((By.ID, "submit_button")))
        # Hace clic en el botón
        btnIngresar.click()

        time.sleep(100)
        driver.quit()
