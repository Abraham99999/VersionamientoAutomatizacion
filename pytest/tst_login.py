from selenium import webdriver
from Funciones.Funciones import Funciones_Globales


def test_login1():
    global driver
    driver = webdriver.Chrome()
    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
    driver.maximize_window()


import allure
import pytest
from selenium import webdriver
from Funciones.Funciones import Funciones_Globales
from allure_commons.types import AttachmentType


class componentes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        t = 0

    def cerarpopup(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://www.mifel.com.mx/", 2)

        cerrar = self.driver.find_element(By.XPATH, '//button[contains(text(),"X")]').click()
        allure.attach(driver.get_screenshot_as_png(), name="cerrar popup", attachment_type=AttachmentType.PNG)
        driver.close()

    def elementos(self):
        driver = self.driver
        element_para_ti = driver.find_element_by_link_text("Para ti")
        element_empresas = driver.find_element_by_link_text("Empresas")
        element_banca_privada = driver.find_element_by_link_text("Banca Privada")
        element_banca_digital = driver.find_element_by_link_text("Banca Digital")

    if element_para_ti and element_empresas and element_banca_privada and element_banca_digital:
        print("Los textos 'Para ti', 'Empresas', 'Banca Privada' y 'Banca Digital' se encuentran en la página.")
    else:
        print("Alguno de los textos no se encuentra en la página.")