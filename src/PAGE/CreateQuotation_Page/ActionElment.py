from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ActionElement:
    def __init__(self, driver):
        self.driver = driver

    def element_send_keys(self, locator, text):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def element_click(self, locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def element_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def element_get_text(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        ).text
    def element_clear(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        ).clear()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()