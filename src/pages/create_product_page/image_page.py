import logging
from time import sleep
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement

class TabImage(ActionElement):

    upload_image = (By.XPATH, "(//input[@type='file' and @class='dz-hidden-input'])[1]")
    save_next_image = (By.XPATH, "//button[@id='btnSaveProductDetail']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def send_keys_upload_image(self):
        try:
            self.element_send_keys_path(self.upload_image, "/Users/mac/File_Test/168111037851370.jpg")
            sleep(3)
        except Exception as e:
            logging.error(f"An error occurred while uploading the image: {e}")

    def click_save_next_image(self):
        try:
            for _ in range(2): 
                if self.element_click(self.save_next_image):
                    return
            sleep(1) 
            logging.warning("Failed to click 'save_next_image' after 2 attempts.")
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'save_next_image': {e}")
        