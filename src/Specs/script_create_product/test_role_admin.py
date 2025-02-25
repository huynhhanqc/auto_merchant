import os
from dotenv import load_dotenv
from faker import Faker
from src.pages.page_login.login_page import LogInPage
from src.pages.menu_page import MenuMC
from src.pages.create_product_page.info_page import TabInFo
from src.pages.create_product_page.image_page import TabImage
from src.pages.create_product_page.document_page import TabDocument
from src.drivers.webdriver_factory import WebdriverFactory
import logging
from selenium.common.exceptions import TimeoutException 
from src.utils.log_capture import log_capture

load_dotenv()
user_name = os.getenv("USER_ROLE_ADMIN")
pass_word = os.getenv("PASS_ROLE_ADMIN")

class TestCreateProductRoleAdmin(WebdriverFactory):
    def test_create_product_role_admin_success(self):
        fake = Faker()
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_mc = MenuMC(driver)
        info = TabInFo(driver)
        image = TabImage(driver)
        document = TabDocument(driver)
        try:
            logging.info("🔹 Bắt đầu đăng nhập tài khoản Admin")
            login_Page.login_role_admin(user_name,pass_word)
            menu_mc.click_Create_Product()
            assert menu_mc.assert_title_home_create_product() == "Add New Product"
            info.send_keys_name_product(fake.text())
            info.send_keys_vendor_product_name(fake.text())
            info.send_keys_bar_code()
            info.click_on_brand()
            info.send_keys_vendor_product_code()
            info.send_keys_vender_price()
            info.send_keys_mar_price()
            info.send_keys_hasaki_price()
            info.send_keys_leng_th()
            info.send_keys_width()
            info.send_keys_height()
            info.send_keys_weight()
            info.click_on_Shelf_Life_product()
            info.click_expiration_date_formatting_admin()
            info.click_ip_expiration_date_formatting()
            info.click_save_next()
            logging.info("🔹 Tải lên hình ảnh")
            image.send_keys_upload_image()
            image.click_save_next_image()
            logging.info("🔹 Nhập thông tin tài liệu")
            document.click_Announcement_Date()
            document.send_keys_Announcement_Code()
            document.send_keys_Announcement_Document()
            document.click_save_next_document()
            document.click_Btn_request_approve()
            document.accept_alert()
            assert info.assert_text_status_product_success() == "Waiting Approve"
            info.click_btn_approve_product()
            info.accept_alert()
            info.get_bar_code()
            if info.assert_text_status_product_approved_admin() == "Approved":
                assert True
            elif info.assert_text_status_product_completed() == "Completed":
                assert True
            else:
                assert False
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

