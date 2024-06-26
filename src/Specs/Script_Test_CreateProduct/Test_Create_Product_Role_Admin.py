from time import sleep
import unittest
from faker import Faker
from src.SETUP.WebDriver_Setup import WebDriverSetup
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateProduct_Page.New_Product_Tab_Info_Page import Tab_InFo
from src.PAGE.CreateProduct_Page.New_Product_Tab_Image_Page import Tab_Image
from src.PAGE.CreateProduct_Page.New_Product_Tab_Document_Page import Tab_Document


class TestCreateProductRoleAdmin(WebDriverSetup, unittest.TestCase): 
    def test_create_product_role_admin_Success(self):   
        fake = Faker()
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_mc = Menu_MC(driver)
        tab_info = Tab_InFo(driver)
        tab_image = Tab_Image(driver)
        tab_document = Tab_Document(driver)
        login_Page.login_role_admin("admin","123123")
        sleep(2)
        menu_mc.click_Create_Product()   
        assert menu_mc.assert_title_home_create_product() == "Add New Product"
        sleep(1)
        tab_info.send_keys_name_product(fake.text())
        tab_info.send_keys_vendor_product_name(fake.text())
        tab_info.send_keys_bar_code(fake.postcode())
        sleep(1)
        tab_info.click_on_brand()
        sleep(1)
        tab_info.send_keys_vendor_product_code(fake.postcode())
        tab_info.send_keys_vender_price(fake.postcode())
        tab_info.send_keys_mar_price(fake.postcode())
        tab_info.send_keys_hasaki_price(fake.postcode())
        tab_info.send_keys_leng_th()
        tab_info.send_keys_width()
        tab_info.send_keys_height()
        tab_info.send_keys_weight()
        tab_info.click_expiration_date_formatting_admin()
        sleep(1)
        tab_info.click_ip_expiration_date_formatting()
        tab_info.click_save_next()
        driver.implicitly_wait(3)
        tab_image.send_keys_upload_image()
        sleep(2)
        tab_image.click_save_next_image()
        tab_document.click_Announcement_Date()
        tab_document.send_keys_Announcement_Code()
        tab_document.send_keys_Announcement_Document()
        sleep(2)
        tab_document.click_save_next_document()
        tab_document.click_Btn_request_approve()
        sleep(1)
        tab_document.accept_alert()
        sleep(2)
        assert tab_info.assert_text_status_product_success() == "Waiting Approve"
        tab_info.click_btn_approve_product()
        sleep(1)
        tab_info.accept_alert()
        sleep(2)
        if tab_info.assert_text_status_product_approved_admin() == "Approved":
            assert True
        elif tab_info.assert_text_status_product_completed() == "Completed":
            assert True
            driver.save_screenshot("src\\ScreenShort\\image.png")
        else:
            driver.save_screenshot("src\\ScreenShort\\image.png")
            assert False
            
    




