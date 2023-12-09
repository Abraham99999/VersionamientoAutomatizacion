from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.options import Options as ChromeOptions

class LTAutomate(unittest.TestCase):
    def setUp(self):
        username = "{abraham.aguilar}"
        accessToken = "{11zXovIoS0XOaHRsQwQqnvkwUyn6wN9LpyxgmIfIRVBEv8xv6B}"
        gridUrl = "https://abraham.aguilar:11zXovIoS0XOaHRsQwQqnvkwUyn6wN9LpyxgmIfIRVBEv8xv6B@hub.lambdatest.com/wd/hub"

        capabilities = {
            'platform': "Windows 10",
            'browserName': "Chrome",
            'version': "119.0",
            "resolution": "1024x768",
            "name": "LambdaTest python google search test",
            "build": "LambdaTest python google search build",
            "network": True,
            "video": True,
            "visual": True,
            "console": True,
        }

        # URL: https://{username}:{accessToken}@hub.lambdatest.com/wd/hub
        url = gridUrl

        print("Initiating remote driver on platform: " + capabilities["platform"] + " browser: " + capabilities["browserName"] + " version: " + capabilities["version"])

        # Crear el driver con opciones
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--no-sandbox')  # Necesario para ejecución en entorno remoto como LambdaTest

        self.driver = webdriver.Remote(
            command_executor=url,
            options=chrome_options,
        )

    def test_search_in_google(self):
        driver = self.driver
        print("Driver initiated successfully.  Navigate url")
        driver.get("https://www.google.com.mx/")
        time.sleep(3)

        driver.execute_script("lambda-status=passed")
        print("Requesting to mark test: pass")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
