from selenium.webdriver.common.by import By

class Tab_Document:
    def __init__(self, driver):
        self.driver = driver
        self.Announcement_Date = (By.XPATH, "//*[@id='announce_date']")
        self.accept_date = (By.XPATH, "//span[@class='flatpickr-day ' and text()='29']")
        self.Announcement_Code = (By.XPATH, "//*[@id='announce_code']")
        self.Announcement_Document = (By.XPATH, "(//input[@type='file' and @class='dz-hidden-input'])[2]")
        self.Btn_request_approve = (By.XPATH, "//button[normalize-space()='Request to approve']")
        self.save_next_document = (By.XPATH, "//button[@id='btnSaveProductDetail']")

    def select_Announcement_Date(self):
        self.driver.find_element(*self.Announcement_Date).click()

    def click_accept_date(self):
        self.driver.find_element(*self.accept_date).click()

    def input_Announcement_Code(self):
        self.driver.find_element(*self.Announcement_Code).send_keys("TEST123567")

    def input_Announcement_Document(self):
        self.driver.find_element(*self.Announcement_Document).send_keys("c:\\Users\\HASAKI\\Downloads\\Quy_tac_tao_Task_tren_Hasaki_Project_-_ver_1.1.pdf")
    
    def click_save_next_document(self):
        self.driver.find_element(*self.save_next_document).click()

    def click_Btn_request_approve(self):
        self.driver.find_element(*self.Btn_request_approve).click()