from selenium.webdriver.common.by import By
from src.PAGE.CreateQuotation_Page.ActionElment import ActionElement

class Tab_Document(ActionElement):

    Announcement_Date = (By.XPATH, "//*[@id='announce_date']")
    accept_date = (By.XPATH, "//span[@class='flatpickr-day ' and text()='29']")
    Announcement_Code = (By.XPATH, "//*[@id='announce_code']")
    Announcement_Document = (By.XPATH, "(//input[@type='file' and @class='dz-hidden-input'])[2]")
    Btn_request_approve = (By.XPATH, "//button[normalize-space()='Request to approve']")
    save_next_document = (By.XPATH, "//button[@id='btnSaveProductDetail']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_Announcement_Date(self):
        self.element_click(self.Announcement_Date)
        self.element_click(self.accept_date)

    def send_keys_Announcement_Code(self):
        self.element_send_keys(self.Announcement_Code, "TEST1999")

    def send_keys_Announcement_Document(self):
        self.driver.find_element(*self.Announcement_Document).send_keys("c:\\Users\\HASAKI\\Downloads\\Quy_tac_tao_Task_tren_Hasaki_Project_-_ver_1.1.pdf")
    
    def click_save_next_document(self):
        self.element_click(self.save_next_document)

    def click_Btn_request_approve(self):
        self.element_click(self.Btn_request_approve)