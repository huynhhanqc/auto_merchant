import os
from dotenv import load_dotenv
from src.pages.login_page import LogInPage
from src.pages.create_quotation_page.excel_page import Create_Quotation_Excel
from src.drivers.webdriver_factory import WebdriverFactory
import logging
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import NoSuchElementException
from src.utils.log_capture import log_capture 

load_dotenv()
user_name = os.getenv("USER_ROLE_MERCHANT")
pass_word = os.getenv("PASS_ROLE_MERCHANT")

class TestCreateQuotationExcel(WebdriverFactory):
    def test_File_Barcode_Type_Tester_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.click_Type_Tester()
            Excel.send_keys_Note()
            Excel.send_keys_Upload_Excel_Barcode()
            Excel.click_Btn_Validate()
            Excel.accept_alert()
            Excel.click_Btn_Save_Quotation()
            Excel.click_btn_ok()
            Excel.click_Btn_Request()
            Excel.accept_alert() 
            assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
            assert Excel.assert_text_type_tester_quotation() == "Tester"      
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_File_Sku_Type_Tester_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.click_Type_Tester()
            Excel.send_keys_Note()
            Excel.click_Import_by_Sku()
            Excel.send_keys_Upload_Excel_Sku()
            Excel.click_Btn_Validate()
            Excel.accept_alert()
            Excel.click_Btn_Save_Quotation()
            Excel.click_btn_ok()
            Excel.click_Btn_Request()
            Excel.accept_alert()
            assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_File_Barcode_Type_Gift_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.click_Type_Gift()
            Excel.send_keys_Note()
            Excel.send_keys_Upload_Excel_Barcode()
            Excel.click_Btn_Validate()
            Excel.accept_alert()
            Excel.click_Btn_Save_Quotation()
            Excel.click_btn_Yes_Gift()
            Excel.click_btn_ok()
            Excel.click_Btn_Request()
            Excel.accept_alert()
            assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
            assert Excel.assert_text_type_gift_quotation() == "Gift"
            assert Excel.assert_text_total_price() == "0 đ"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_File_Sku_Type_Gift_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.click_Type_Gift()
            Excel.send_keys_Note()
            Excel.click_Import_by_Sku()
            Excel.send_keys_Upload_Excel_Sku()
            Excel.click_Btn_Validate()
            Excel.accept_alert()
            Excel.click_Btn_Save_Quotation()
            Excel.click_btn_Yes_Gift()
            Excel.click_btn_ok()
            Excel.click_Btn_Request()
            Excel.accept_alert()
            assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
            assert Excel.assert_text_type_gift_quotation() == "Gift"
            assert Excel.assert_text_total_price() == "0 đ"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False
        except NoSuchElementException as e:
            logging.error(f"🚨 Element not found: {str(e)}")
            log_capture(driver, "Element_Not_Found")
            assert False<e

    def test_File_Barcode_Type_Normal_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.send_keys_Note()
            Excel.send_keys_Upload_Excel_Barcode()
            Excel.click_Btn_Validate()
            Excel.accept_alert()
            Excel.click_Btn_Save_Quotation()
            Excel.click_btn_ok()
            Excel.click_Btn_Request()
            Excel.accept_alert()
            assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
            assert Excel.assert_text_type_normal_quotation() == "Normal"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_File_Sku_Type_Normal_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.send_keys_Note()
            Excel.click_Import_by_Sku()
            Excel.send_keys_Upload_Excel_Sku()
            Excel.click_Btn_Validate()
            Excel.accept_alert()
            Excel.click_Btn_Save_Quotation()
            Excel.click_btn_ok()
            Excel.click_Btn_Request()
            Excel.accept_alert()
            assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
            assert Excel.assert_text_type_normal_quotation() == "Normal"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_File_Barcode_Type_Normal_Non_VAT_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.click_Require_Vat()
            Excel.send_keys_Note()
            Excel.send_keys_Upload_Excel_Barcode()
            Excel.click_Btn_Validate()
            assert Excel.assert_text_error_Require_Vat() == "Require VAT Product:"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_File_Sku_Type_Normal_Non_VAT_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        Excel = Create_Quotation_Excel(driver)
        try:
            login_Page.login_role_vendor(user_name, pass_word)
            Excel.go_to_excel_page()
            Excel.click_company()
            Excel.click_Require_Vat()
            Excel.send_keys_Note()
            Excel.click_Import_by_Sku()
            Excel.send_keys_Upload_Excel_Sku()
            Excel.click_Btn_Validate()
            assert Excel.assert_text_error_Require_Vat() == "Require VAT Product:"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

