from datetime import datetime
import logging
from time import sleep
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement


class TabDocument(ActionElement):

    Announcement_Date = (By.XPATH, "//*[@id='announce_date']")
    Announcement_Code = (By.XPATH, "//*[@id='announce_code']")
    Announcement_Document = (By.XPATH, "(//input[@type='file' and @class='dz-hidden-input'])[2]")
    Btn_request_approve = (By.XPATH, "//button[normalize-space()='Request to approve']")
    save_next_document = (By.XPATH, "//button[@id='btnSaveProductDetail']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_Announcement_Date(self):
        current_date = datetime.now().strftime("%d")
        try:
            self.element_click(self.Announcement_Date)
            current_date_locator = (By.XPATH, f"//span[text()='{current_date}']")
            self.element_click(current_date_locator)
        except Exception as e:
            logging.error(f"An error occurred while clicking the current date: {e}")

    def send_keys_Announcement_Code(self):
        try:
            self.element_send_keys(self.Announcement_Code, "247961/24/CBMP-QL1")
        except Exception as e:
            logging.error(f"An error occurred while sending keys to Announcement Code: {e}")

    def send_keys_Announcement_Document(self):
        try:
            self.element_send_keys_path(self.Announcement_Document, "/Users/mac/File_Test/product_media_27340e042a50f229f3fb0bcb7f7aa0a1.pdf")
            sleep(3)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to Announcement Document: {e}")
        
    def click_save_next_document(self):
        try:
            self.element_click(self.save_next_document)
        except Exception as e:
            logging.error(f"An error occurred while clicking the save next document: {e}")

    def click_Btn_request_approve(self):
        try:
            self.element_click(self.Btn_request_approve)
        except Exception as e:
            logging.error(f"An error occurred while clicking the request approve: {e}")