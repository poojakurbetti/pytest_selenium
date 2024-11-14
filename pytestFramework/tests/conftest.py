import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        service = Service(executable_path='/Users/poojak/Desktop/Drivers/chromedriver')
        options = webdriver.ChromeOptions()
        web_driver = webdriver.Chrome()
        # web_driver = webdriver.Chrome(executable_path="/Users/poojak/Desktop/Drivers/chromedriver")
    if request.param == "firefox":
        service = Service(executable_path='/Users/poojak/Desktop/Drivers/geckodriver')
        options = webdriver.FirefoxOptions()
        web_driver = webdriver.Firefox(service=service, options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()
