from time import sleep
import unittest
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateQuotation_Page.quotation_xslx_page import Create_Quotation_Excel
from src.SETUP.WebDriver_Setup import WebDriverSetup


class TestCreateQuotationExcel(WebDriverSetup, unittest.TestCase):
    def test_File_Barcode_Type_Tester_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Quotation_Excel.click_Type_Tester()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.send_keys_Upload_Excel_Barcode()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        Quotation_Excel.accept_alert()
        sleep(1)
        Quotation_Excel.click_Btn_Save_Quotation()
        sleep(2)
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        Quotation_Excel.accept_alert() 
        assert Quotation_Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        assert Quotation_Excel.assert_text_type_tester_quotation() == "Tester"      

    def test_File_Sku_Type_Tester_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        sleep(1)
        Quotation_Excel.click_Type_Tester()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.click_Import_by_Sku()
        Quotation_Excel.send_keys_Upload_Excel_Sku()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        Quotation_Excel.accept_alert()
        Quotation_Excel.click_Btn_Save_Quotation()
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        sleep(4)
        Quotation_Excel.accept_alert()
        driver.save_screenshot("src\\ScreenShort\\image2.png")
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        Quotation_Excel.accept_alert()
        sleep(1)
        assert Quotation_Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 

    def test_File_Barcode_Type_Gift_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Quotation_Excel.click_Type_Gift()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.send_keys_Upload_Excel_Barcode()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        Quotation_Excel.accept_alert()
        sleep(1)
        Quotation_Excel.click_Btn_Save_Quotation()
        sleep(1)
        Quotation_Excel.click_btn_Yes_Gift()
        sleep(2)
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        Quotation_Excel.accept_alert()
        sleep(1)
        assert Quotation_Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        assert Quotation_Excel.assert_text_type_gift_quotation() == "Gift"
        assert Quotation_Excel.assert_text_total_price() == "0 đ"
       
    def test_File_Sku_Type_Gift_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        sleep(1)
        Quotation_Excel.click_Type_Gift()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.click_Import_by_Sku()
        Quotation_Excel.send_keys_Upload_Excel_Sku()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        Quotation_Excel.accept_alert()
        sleep(1)
        Quotation_Excel.click_Btn_Save_Quotation()
        sleep(2)
        Quotation_Excel.click_btn_Yes_Gift()
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        Quotation_Excel.accept_alert()
        assert Quotation_Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        assert Quotation_Excel.assert_text_type_gift_quotation() == "Gift"
        assert Quotation_Excel.assert_text_total_price() == "0 đ"
        

    def test_File_Barcode_Type_Normal_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.send_keys_Upload_Excel_Barcode()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        Quotation_Excel.accept_alert()
        sleep(1)
        Quotation_Excel.click_Btn_Save_Quotation()
        sleep(2)
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        Quotation_Excel.accept_alert()
        assert Quotation_Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        assert Quotation_Excel.assert_text_type_normal_quotation() == "Normal"

    def test_File_Sku_Type_Normal_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.click_Import_by_Sku()
        Quotation_Excel.send_keys_Upload_Excel_Sku()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        Quotation_Excel.accept_alert()
        sleep(1)
        Quotation_Excel.click_Btn_Save_Quotation()
        sleep(2)
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        Quotation_Excel.accept_alert()
        assert Quotation_Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        assert Quotation_Excel.assert_text_type_normal_quotation() == "Normal"

    def test_File_Barcode_Type_Normal_Non_VAT_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Quotation_Excel.click_Require_Vat()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.send_keys_Upload_Excel_Barcode()
        Quotation_Excel.click_Btn_Validate()
        assert Quotation_Excel.assert_text_error_Require_Vat() == "Require VAT Product:"

    def test_File_Sku_Type_Normal_Non_VAT_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Quotation_Excel.click_Require_Vat()
        Quotation_Excel.send_keys_Note()
        Quotation_Excel.click_Import_by_Sku()
        Quotation_Excel.send_keys_Upload_Excel_Sku()
        Quotation_Excel.click_Btn_Validate()
        assert Quotation_Excel.assert_text_error_Require_Vat() == "Require VAT Product:"







  




    



    
