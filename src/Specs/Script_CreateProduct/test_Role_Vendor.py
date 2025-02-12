from time import sleep
from faker import Faker
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateProduct_Page.Info_Page import Tab_InFo
from src.PAGE.CreateProduct_Page.Image_Page import Tab_Image
from src.PAGE.CreateProduct_Page.Document_Page import Tab_Document
from src.SPECS.BaseTest import BaseFixture
import logging
from selenium.common.exceptions import TimeoutException 
from src.PAGE.Utils.Log_capture import Log_CapTure 


class TestCreateProductRoleVendor(BaseFixture):
    def test_create_product_role_vendor_Success(self):
        fake = Faker()
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_mc = Menu_MC(driver)
        info = Tab_InFo(driver)
        image = Tab_Image(driver)
        document = Tab_Document(driver)
        try:
            login_Page.login_role_vendor("truonghan1506", "150699")
            sleep(2)
            menu_mc.click_Create_Product()
            assert menu_mc.assert_title_home_create_product() == "Add New Product"
            sleep(1)
            info.send_keys_name_product(fake.text())
            info.send_keys_vendor_product_name(fake.text())
            info.send_keys_bar_code(fake.postcode())
            info.click_on_brand()
            info.send_keys_vendor_product_code(fake.postcode())
            info.send_keys_vender_price(fake.postcode())
            info.send_keys_mar_price(fake.postcode())
            info.send_keys_hasaki_price(fake.postcode())
            info.send_keys_leng_th()
            info.send_keys_width()
            info.send_keys_height()
            info.send_keys_weight()
            info.click_expiration_date_formatting_vendor()
            sleep(1)
            info.click_ip_expiration_date_formatting()
            info.click_save_next()
            sleep(2)
            image.send_keys_upload_image()
            sleep(2)
            image.click_save_next_image()
            document.click_Announcement_Date()
            document.send_keys_Announcement_Code()
            document.send_keys_Announcement_Document()
            sleep(2)
            document.click_save_next_document()
            document.click_Btn_request_approve()
            sleep(1)
            document.accept_alert()
            sleep(2)
            assert info.assert_text_status_product_success() == "Waiting Approve"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            Log_CapTure(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            Log_CapTure(driver, "Unexpected_Error")
            assert False


