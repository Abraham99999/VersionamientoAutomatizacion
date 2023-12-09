import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones_Globales
from selenium.webdriver import ActionChains


def test_login1():
    global driver
    driver = webdriver.Chrome()
    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", 2)
    driver.maximize_window()
