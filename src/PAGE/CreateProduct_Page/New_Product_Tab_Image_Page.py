from selenium.webdriver.common.by import By

class Tab_Image:
    def __init__(self, driver):
        self.driver = driver
        self.upload_image = (By.XPATH, "(//input[@type='file' and @class='dz-hidden-input'])[1]")
        self.save_next_image = (By.XPATH, "//button[@id='btnSaveProductDetail']")

    def input_upload_image(self):
        self.driver.find_element(*self.upload_image).send_keys("c:\\Users\\HASAKI\\Downloads\\hinh-nen-3d-cho-may-tinh-dep_111406086.jpg")

    def click_save_next_image(self):
        self.driver.find_element(*self.save_next_image).click()
