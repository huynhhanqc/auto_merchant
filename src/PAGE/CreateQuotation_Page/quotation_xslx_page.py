from selenium.webdriver.common.by import By
from src.PAGE.CreateQuotation_Page.ActionElment import ActionElement


class Create_Quotation_Excel(ActionElement):
    
    Select_Type = (By.XPATH, "//*[@aria-labelledby='select2-quotationType-container']/parent::*")
    Type_Tester = (By.XPATH, "(//li[text()='Tester']/parent::*)[1]")
    Type_Gift = (By.XPATH, "//li[text()='Gift']")
    Require_Vat = (By.XPATH, "//*[@id='quotationConfig']/parent::*")
    Note = (By.XPATH, "//*[@id='quotationNote']")
    Upload_Excel = (By.ID, "excelFile")
    Import_by_Sku = (By.XPATH, "//div[@class='import-type']//label[text()='Import by sku']")
    Import_by_Barcode = (By.XPATH, "//div[@class='import-type']//label[text()='Import by barcode']")
    Btn_Validate = (By.XPATH, "//*[text()='Validate File']/parent::*")
    Btn_Save_Quotation = (By.XPATH, "//*[@id='saveQuotation']")
    Btn_OK = (By.XPATH, "//button[contains(text() ,'OK')]")
    Btn_Request = (By.XPATH, "//*[text()='Request to confirm']")
    text_error_Require_Vat = (By.XPATH, "//b[normalize-space()='Require VAT Product:']")
    btn_Yes_Gift = (By.XPATH, "//button[normalize-space()='Yes']")
    text_status_quotation = (By.XPATH, "//span[contains(text(),'Waiting For Confirm')]")  
    text_type_tester_quotation = (By.XPATH, "//*[text()='Tester']")  
    text_tpye_gift_quotation = (By.XPATH, "//span[normalize-space()='Gift']")
    text_type_normal_quotation = (By.XPATH, "//*[text()='Normal']")
    text_total_price = (By.XPATH, "//span[@id='selected-product-total-price']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_Type_Tester(self):
        self.element_click(self.Select_Type)
        self.element_click(self.Type_Tester)

    def click_Type_Gift(self):
        self.element_click(self.Select_Type)
        self.element_click(self.Type_Gift)

    def click_Require_Vat(self):
        self.element_click(self.Require_Vat)

    def send_keys_Note(self):
        self.element_send_keys(self.Note, "Test by HASAKI")

    def send_keys_Upload_Excel_Barcode(self):
        self.element_send_keys(self.Upload_Excel, "c:\\Users\\HASAKI\\Documents\\File_Data_Test\\File_Auto_Barcode.xlsx")

    def click_Import_by_Sku(self):
        self.element_click(self.Import_by_Sku)

    def send_keys_Upload_Excel_Sku(self):
        self.element_send_keys(self.Upload_Excel, "c:\\Users\\HASAKI\\Documents\\File_Data_Test\\File_Auto_Sku.xlsx")
    
    def click_Btn_Validate(self):
        self.element_click(self.Btn_Validate)

    def click_Btn_Save_Quotation(self):
        self.element_click(self.Btn_Save_Quotation)
    
    def click_Btn_OK(self):
        self.element_click(self.Btn_OK)

    def click_btn_Yes_Gift(self):
        self.element_click(self.btn_Yes_Gift)

    def click_Btn_Request(self):
        self.element_click(self.Btn_Request)

    def assert_text_error_Require_Vat(self):
        return self.element_get_text(self.text_error_Require_Vat)
    
    def assert_text_status_quotation(self):
        return self.element_get_text(self.text_status_quotation)
    
    def assert_text_type_tester_quotation(self):
        return self.element_get_text(self.text_type_tester_quotation)
    
    def assert_text_type_gift_quotation(self):
        return self.element_get_text(self.text_tpye_gift_quotation)
    
    def assert_text_total_price(self):
        return self.element_get_text(self.text_total_price)
    
    def assert_text_type_normal_quotation(self):
        return self.element_get_text(self.text_type_normal_quotation)

    
    


