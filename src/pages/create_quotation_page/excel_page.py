from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
import logging
from time import sleep


class Create_Quotation_Excel(ActionElement):
    
    url_create_excel = "https://test-merchant.hasaki.vn/quotation/import"
    Select_Type = (By.XPATH, "//*[@aria-labelledby='select2-quotationType-container']/parent::*")
    Type_Tester = (By.XPATH, "//li[text()='Tester']")
    Type_Gift = (By.XPATH, "//li[text()='Gift']")
    Require_Vat = (By.XPATH, "//*[@id='quotationConfig']/parent::*")
    Note = (By.XPATH, "//*[@id='quotationNote']")
    Upload_Excel = (By.ID, "excelFile")
    Import_by_Sku = (By.XPATH, "//div[@class='import-type']//label[text()='Import by sku']")
    Import_by_Barcode = (By.XPATH, "//div[@class='import-type']//label[text()='Import by barcode']")
    Btn_Validate = (By.XPATH, "//*[@id='btnUploadQuotationTemplate']")
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
    company = (By.XPATH, "//span[@class='select2-selection select2-selection--single form-select form-select-solid']")
    company_accept = (By.XPATH, "//li[contains(text(),'Cty Hasaki Beauty & Clinic')]")
    text_code_quotation = (By.XPATH, "//strong[normalize-space()='Code :']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_excel_page(self):
        try:
            self.driver.get(self.url_create_excel)
        except Exception as e:
            logging.error(f"An error occurred while navigating to the URL: {e}")
            raise

    def click_Type_Tester(self):
        try:
            self.element_click(self.Select_Type)
            self.element_click(self.Type_Tester)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Type_Tester': {e}")
            raise

    def click_Type_Gift(self):
        try:
            self.element_click(self.Select_Type)
            self.element_click(self.Type_Gift)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Type_Gift': {e}")
            raise

    def click_company(self):
        try:
            self.element_click(self.company)
            self.element_click(self.company_accept)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'company': {e}")
            raise

    def click_Require_Vat(self):
        try:
            self.element_click(self.Require_Vat)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Require_Vat': {e}")
            raise

    def send_keys_Note(self):
        try:
            self.element_send_keys(self.Note, "Test by HASAKI")
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'Note': {e}")
            raise

    def send_keys_Upload_Excel_Barcode(self):
        try:
            self.element_send_keys(self.Upload_Excel, "/Users/mac/File_Test/quotation-Barcode.xlsx")
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'Upload_Excel_Barcode': {e}")
            raise

    def click_Import_by_Sku(self):
        try:
            self.element_click(self.Import_by_Sku)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Import_by_Sku': {e}")
            raise

    def send_keys_Upload_Excel_Sku(self):
        try:
            self.element_send_keys(self.Upload_Excel, "/Users/mac/File_Test/quotation-SKU.xlsx")
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'Upload_Excel_Sku': {e}")
            raise
    
    def click_Btn_Validate(self):
        try:
            self.element_click(self.Btn_Validate)
            sleep(3)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Btn_Validate': {e}")
            raise

    def click_Btn_Save_Quotation(self):
        try:
            self.element_click(self.Btn_Save_Quotation)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Btn_Save_Quotation': {e}")
            raise
    
    def click_btn_ok(self):
        try:
            self.element_click(self.Btn_OK)
            sleep(3)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Btn_OK': {e}")
            raise

    def click_btn_Yes_Gift(self):
        try:
            self.element_click(self.btn_Yes_Gift)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_Yes_Gift': {e}")
            raise

    def click_Btn_Request(self):
        try:
            self.element_click(self.Btn_Request)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Btn_Request': {e}")
            raise

    def assert_text_error_Require_Vat(self):
        try:
            return self.element_get_text(self.text_error_Require_Vat)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_error_Require_Vat': {e}")
            raise

    def assert_text_status_quotation(self):
        try:
            return self.element_get_text(self.text_status_quotation)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_status_quotation': {e}")
            raise

    def assert_text_type_tester_quotation(self):
        try:
            return self.element_get_text(self.text_type_tester_quotation)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_type_tester_quotation': {e}")
            raise

    def assert_text_type_gift_quotation(self):
        try:
            return self.element_get_text(self.text_tpye_gift_quotation)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_tpye_gift_quotation': {e}")
            raise
    
    def assert_text_total_price(self):
        try:
            return self.element_get_text(self.text_total_price)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_total_price': {e}")
            raise
    
    def assert_text_type_normal_quotation(self):
        try:
            return self.element_get_text(self.text_type_normal_quotation)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_type_normal_quotation': {e}")
            raise

    def get_text_code(self):
        try:
            code = self.element_get_text(self.text_code_quotation, "text")
            print(f"Giá trị của staff_id: {code}")
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_code': {e}")
            raise
    
    


