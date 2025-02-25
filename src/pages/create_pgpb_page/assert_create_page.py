import logging
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AssertCreatePG (ActionElement):

    text_status_Inactive = (By.XPATH, "//*[@class='badge badge-secondary' and contains(text(), 'In-Active')]")
    text_status_Waiting_Approve = (By.XPATH, "//*[@class='badge badge-warning' and contains(text(), 'Waiting for Approve')]")
    text_status_Active = (By.XPATH, "//*[@class='badge badge-success' and contains(text(), 'Active')]")
    text_staff_id = (By.ID, "staff_id")
    text_id_Number = (By.ID, "cmnd")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def is_text_present(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return False
        
    def get_staff_id(self):
        try:
            staff_id_value = self.element_get_attribute(self.text_staff_id, "value")
            if staff_id_value is not None:
                print(f"Giá trị của staff_id: {staff_id_value}")
            else:
                print("Không tìm thấy giá trị của staff_id.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

    def get_id_Number(self):
        try:
            id_number_value = self.element_get_attribute(self.text_id_Number, "value")
            if id_number_value is not None:
                print(f"Giá trị của id_Number: {id_number_value}")
            else:
                print("Không tìm thấy giá trị của id_Number.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
    
    def check_active_status(self):
        try:
            active_text = self.is_text_present(self.text_status_Inactive)
            if active_text == "Active":
                assert True, "Text 'Active' is present on the UI."
            else:
                assert False, "Text 'Active' is not present on the UI."
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            self.get_id_Number()
    
    def check_waiting_approve_status(self):
        try:
            waiting_text = self.is_text_present(self.text_status_Inactive)
            if waiting_text == "Waiting for Approve":
                assert True, "Text 'Waiting for Approve' is present on the UI."
            else:
                assert False, "Text 'Waiting for Approve' is not present on the UI."
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            self.get_id_Number()

    def check_inactive_status(self):
        try:
            inactive_text = self.is_text_present(self.text_status_Inactive)
            if inactive_text == "Inactive":
                assert True, "Text 'Inactive' is present on the UI."
            else:
                assert False, "Text 'Inactive' is not present on the UI."
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            self.get_id_Number()