from selenium.webdriver.common.by import By
from src.PAGE.Utils.Common import ActionElement

class Tab_Image(ActionElement):
    upload_image = (By.XPATH, "(//input[@type='file' and @class='dz-hidden-input'])[1]")
    save_next_image = (By.XPATH, "//button[@id='btnSaveProductDetail']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def send_keys_upload_image(self):
        self.element_send_keys_path(self.upload_image, "c:\\Users\\HASAKI\\Downloads\\hinh-nen-3d-cho-may-tinh-dep_111406086.jpg")

    def click_save_next_image(self):
        self.element_click(self.save_next_image)
