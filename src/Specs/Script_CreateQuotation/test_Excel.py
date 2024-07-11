from time import sleep
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateQuotation_Page.Excel_page import Create_Quotation_Excel
from src.SPECS.BaseTest import BaseFixture


class TestCreateQuotationExcel(BaseFixture):
    def test_File_Barcode_Type_Tester_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Excel.click_Type_Tester()
        Excel.send_keys_Note()
        Excel.send_keys_Upload_Excel_Barcode()
        sleep(1)
        Excel.click_Btn_Validate()
        sleep(1)
        Excel.accept_alert()
        sleep(1)
        Excel.click_Btn_Save_Quotation()
        sleep(2)
        Excel.click_Btn_OK()
        sleep(1)
        # Excel.click_Btn_Request()
        # Excel.accept_alert() 
        # assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        # assert Excel.assert_text_type_tester_quotation() == "Tester"      

    def test_File_Sku_Type_Tester_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        sleep(1)
        Excel.click_Type_Tester()
        Excel.send_keys_Note()
        sleep(1)
        Excel.click_Import_by_Sku()
        sleep(1)
        Excel.send_keys_Upload_Excel_Sku()
        sleep(1)
        Excel.click_Btn_Validate()
        sleep(1)
        Excel.accept_alert()
        Excel.click_Btn_Save_Quotation()
        sleep(1)
        Excel.click_Btn_OK()
        sleep(1)
        # Excel.click_Btn_Request()
        # sleep(4)
        # Excel.accept_alert()
        # sleep(1)
        # assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 

    def test_File_Barcode_Type_Gift_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Excel.click_Type_Gift()
        Excel.send_keys_Note()
        Excel.send_keys_Upload_Excel_Barcode()
        Excel.click_Btn_Validate()
        sleep(2)
        Excel.accept_alert()
        sleep(1)
        Excel.click_Btn_Save_Quotation()
        sleep(1)
        Excel.click_btn_Yes_Gift()
        sleep(2)
        Excel.click_Btn_OK()
        sleep(1)
        # Excel.click_Btn_Request()
        # Excel.accept_alert()
        # sleep(1)
        # assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        # assert Excel.assert_text_type_gift_quotation() == "Gift"
        # assert Excel.assert_text_total_price() == "0 đ"
       
    def test_File_Sku_Type_Gift_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        sleep(1)
        Excel.click_Type_Gift()
        Excel.send_keys_Note()
        Excel.click_Import_by_Sku()
        Excel.send_keys_Upload_Excel_Sku()
        Excel.click_Btn_Validate()
        sleep(1)
        Excel.accept_alert()
        sleep(1)
        Excel.click_Btn_Save_Quotation()
        sleep(2)
        Excel.click_btn_Yes_Gift()
        sleep(2)
        Excel.click_Btn_OK()
        sleep(1)
        # Excel.click_Btn_Request()
        # Excel.accept_alert()
        # assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        # assert Excel.assert_text_type_gift_quotation() == "Gift"
        # assert Excel.assert_text_total_price() == "0 đ"
        

    def test_File_Barcode_Type_Normal_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Excel.send_keys_Note()
        Excel.send_keys_Upload_Excel_Barcode()
        Excel.click_Btn_Validate()
        sleep(1)
        Excel.accept_alert()
        sleep(1)
        Excel.click_Btn_Save_Quotation()
        sleep(2)
        Excel.click_Btn_OK()
        sleep(1)
        # Excel.click_Btn_Request()
        # Excel.accept_alert()
        # assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        # assert Excel.assert_text_type_normal_quotation() == "Normal"

    def test_File_Sku_Type_Normal_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Excel.send_keys_Note()
        Excel.click_Import_by_Sku()
        Excel.send_keys_Upload_Excel_Sku()
        Excel.click_Btn_Validate()
        sleep(1)
        Excel.accept_alert()
        sleep(1)
        Excel.click_Btn_Save_Quotation()
        sleep(2)
        Excel.click_Btn_OK()
        sleep(1)
        # Excel.click_Btn_Request()
        # Excel.accept_alert()
        # assert Excel.assert_text_status_quotation() == "Waiting For Confirm\nM" 
        # assert Excel.assert_text_type_normal_quotation() == "Normal"

    def test_File_Barcode_Type_Normal_Non_VAT_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Excel.click_Require_Vat()
        Excel.send_keys_Note()
        Excel.send_keys_Upload_Excel_Barcode()
        Excel.click_Btn_Validate()
        assert Excel.assert_text_error_Require_Vat() == "Require VAT Product:"

    def test_File_Sku_Type_Normal_Non_VAT_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Excel.click_Require_Vat()
        Excel.send_keys_Note()
        Excel.click_Import_by_Sku()
        Excel.send_keys_Upload_Excel_Sku()
        Excel.click_Btn_Validate()
        assert Excel.assert_text_error_Require_Vat() == "Require VAT Product:"







  




    



    
