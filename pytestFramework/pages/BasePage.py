from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This is parent of all pages"""

class BasePage :
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_enabled()

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.text

    def findElementsSizeBy(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return len(element)

    def is_present(self, by_locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).is_displayed()
