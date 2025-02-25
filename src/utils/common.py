from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException


class ActionElement:
    def __init__(self, driver):
        self.driver = driver

    def element_send_keys(self, locator, keys):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            ).send_keys(keys) 
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while sending keys to the element: {e}")
            raise

    def wait_for_page_load(self):
        try:
            WebDriverWait(self.driver, 20).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while waiting for the page to load: {e}")
            raise
        
    def element_click(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while clicking the element: {e}")
            raise

    def element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while clicking the element: {e}")
            raise
    
    def find_element(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while finding the element: {e}")
            raise

    def element_get_text(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            ).text
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while getting the text: {e}")
            raise
    
    def element_get_attribute(self, locator, attribute):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            ).get_attribute(attribute)
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while getting the attribute: {e}")
            raise
    
    def get_options(self, locator):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while getting the options: {e}")
            raise
    
    def refresh_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while refreshing the element: {e}")
            raise
    
    def switch_to_frame(self, frame_locator):
        try:
            frame = WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it(frame_locator)
            )
            return frame
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while switching to the frame: {e}")
            raise
    
    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while switching to the default content: {e}")
            raise
    
    def element_clear(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            ).clear()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while clearing the element: {e}")
            raise

    def accept_alert(self):
        try:
            self.driver.switch_to.alert.accept()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while accepting the alert: {e}")
            raise

    def element_send_keys_path(self, locator, file_path):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            element.send_keys(file_path)
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as e:
            logging.error(f"An error occurred while sending keys to the element: {e}")
            raise

    