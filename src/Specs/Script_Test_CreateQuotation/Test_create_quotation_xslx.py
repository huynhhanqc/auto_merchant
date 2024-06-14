from time import sleep
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateQuotation_Page.quotation_xslx_page import Create_Quotation_Excel
from selenium.webdriver.common.by import By
from src.SETUP.WebDriver_Setup import WebDriverSetup

class TestCreateQuotationExcel(WebDriverSetup):
    def test_File_Barcode_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506", "150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        Quotation_Excel.click_Type_Tester()
        Quotation_Excel.input_Upload_Excel_Barcode()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        driver.switch_to.alert.accept()
        sleep(1)
        Quotation_Excel.click_Btn_Save_Quotation()
        sleep(1)
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        driver.switch_to.alert.accept()
        Quotation_Excel.assert_text_value_price_barcode()
        

    def test_File_Sku_Success(self):
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        Quotation_Excel = Create_Quotation_Excel(driver)
        login_Page.login_role_vendor("truonghan1506", "150699")
        sleep(1)
        menu_MC.click_Create_Quotation_Excel()
        sleep(1)
        Quotation_Excel.click_Type_Tester()
        Quotation_Excel.click_Import_by_Sku()
        Quotation_Excel.input_Upload_Excel_Sku()
        Quotation_Excel.click_Btn_Validate()
        sleep(1)
        driver.switch_to.alert.accept()
        sleep(1)
        Quotation_Excel.click_Btn_Save_Quotation()
        sleep(1)
        Quotation_Excel.click_Btn_OK()
        sleep(1)
        Quotation_Excel.click_Btn_Request()
        driver.switch_to.alert.accept()
        Quotation_Excel.assert_text_value_price_sku()


  




    



    
