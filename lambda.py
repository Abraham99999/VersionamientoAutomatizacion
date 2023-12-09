# test_example_lambda.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_search_on_google_lambda():
    username = "abraham.aguilar"
    access_key = "11zXovIoS0XOaHRsQwQqnvkwUyn6wN9LpyxgmIfIRVBEv8xv6B"

    capabilities = {
        "build": "PyCharm Integration",
        "browserName": "chrome",
        "version": "latest",
        "platform": "WIN10",
        "name": "test_search_on_google_lambda"
    }

    driver = webdriver.Remote(
        command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
        capabilities=capabilities  # Cambiado de desired_capabilities a capabilities
    )

    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("LambdaTest")
    search_box.send_keys(Keys.RETURN)
    assert "LambdaTest" in driver.title
    driver.quit()
