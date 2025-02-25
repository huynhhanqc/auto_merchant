import pytest
from src.drivers.webdriver_factory import WebdriverFactory
from time import sleep
import logging
from selenium.common.exceptions import TimeoutException 
from src.pages.page_signup.account_info_page import AccountInfo
from src.pages.page_signup.vendor_info_page import VendorInfo
from src.pages.page_signup.vendor_certificate_page import VendorCerTiFiCate
from src.utils.log_capture import log_capture 


# @pytest.mark.skip(reason="no reason")
class TestSignUp(WebdriverFactory):
     def test_sign_up_success(self):
        driver = self.driver
        account_info = AccountInfo(driver)
        vendor_info = VendorInfo(driver)
        vendor_certificate = VendorCerTiFiCate(driver)
        try:
            account_info.open_page_sign_up()
            account_info.click_new_sign_up()
            account_info.input_user_name()
            account_info.input_email()
            account_info.input_phone_number()
            account_info.input_password()
            account_info.input_confirm_password()
            account_info.click_btn_continue()
            vendor_info.input_contact_name()
            vendor_info.input_company_name()
            vendor_info.input_registration_number()
            vendor_info.input_address()
            vendor_info.input_vendor_description()
            vendor_info.click_btn_continue()
            vendor_certificate.upload_certificate_of_business_registration()
            vendor_certificate.upload_product_announcement_sheet()
            vendor_certificate.upload_genuine_distribution_authorization()
            vendor_certificate.click_btn_summit()
            vendor_certificate.check_text_success()
            log_capture(driver, "Create Success")
        except TimeoutException as e:
            logging.error(f"⏳ Lỗi timeout xảy ra: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False
            

