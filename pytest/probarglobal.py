import unittest

import allure
import pytest
from selenium import webdriver
from Funciones.Funciones import Funciones_Globales
from allure_commons.types import AttachmentType


class base_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        t = 0

    def test1(self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/",1)
       # f.Texto_Xpath("//input[contains(@id,'user-name')]","Abraham", 3)

        f.Texto_ID("user-name", "Abraham Aguila", 0)
        allure.attach(driver.get_screenshot_as_png(), name="ingresa usuario", attachment_type=AttachmentType.PNG)
        f.Texto_Xpath("//input[contains(@id,'password')]", "admin123", 0)
        allure.attach(driver.get_screenshot_as_png(),name="ingresa contraseña", attachment_type=AttachmentType.PNG)
        driver.close()

    def test2(self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://www.saucedemo.com/",1)
        f.Texto_Xpath("//input[contains(@id,'user-name')]","Jose", 0)
        allure.attach(driver.get_screenshot_as_png(), name="ingresa usuario2", attachment_type=AttachmentType.PNG)
        f.Texto_Xpath("//input[contains(@id,'password')]", "admin123", 0)
        allure.attach(driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
        allure.attach(driver.get_screenshot_as_png(), name="ingresa contraseña2", attachment_type=AttachmentType.PNG)
        #f.Texto_ID("user-name", "Abraham", 3)

