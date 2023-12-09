import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones_Globales():

    def __init__(self, driver):
        self.driver=driver

    def Tiempo(self, tie):
        t=time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.maximize_window()
        self.driver.get(Url)

        t= time.sleep(Tiempo)
        return t

    def Texto_Xpath(self,xpath,texto,Tiempo):
        val=self.driver.find_element(By.XPATH,xpath)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def Texto_ID(self,ID,texto,Tiempo):
        val=self.driver.find_element(By.ID,ID)
        val.clear()
        val.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def ingresar_usuario(self, usuario):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/span/div/div[1]/div/input")))
        element.send_keys(usuario)
        #allure.attach(self.driver.get_screenshot_as_png(), name="Ingresar usuario", attachment_type=AttachmentType.PNG)


    def ingresar_contrasena(self, contrasena):

        contrasena_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'password')]")))
        contrasena_element.send_keys(contrasena)
        #allure.attach(self.driver.get_screenshot_as_png(), name="Ingresar contraseña", attachment_type=AttachmentType.PNG)

