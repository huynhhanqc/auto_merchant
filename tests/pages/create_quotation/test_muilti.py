import os
from dotenv import load_dotenv
import pytest
from src.pages.page_login.login_page import LogInPage
from src.pages.create_quotation_page.muilti_page import QuotationMuilti
from src.drivers.webdriver_factory import  WebdriverFactory
from src.utils.log_capture import log_capture
import logging
from selenium.common.exceptions import TimeoutException
from src.handle_file.file_handler import ExcelReader

load_dotenv()
user_name = os.getenv("USER_ROLE_MERCHANT")
pass_word = os.getenv("PASS_ROLE_MERCHANT")

@pytest.fixture(scope="function")
def excel_reader():
    file_path = '/Users/mac/File_Test/ProductTest.xlsx' 
    sheet_name = 'Product'
    return ExcelReader(file_path, sheet_name)

class TestCreateQuotationSigle(WebdriverFactory):
    def test_create_quotation_success(self, excel_reader):
        driver = self.driver
        login_in = LogInPage(driver)
        muilti = QuotationMuilti(driver, excel_reader)
        try:
            login_in.login_role_vendor(user_name, pass_word)
            muilti.go_to_create_quotation()
            muilti.click_type_gift()
            muilti.click_company_id4()
            muilti.click_select_store_multi()
            muilti.click_zone_bd()
            muilti.click_btn_use_store()
            muilti.click_input_sku()
            muilti.send_keys_sku_file()
            muilti.click_btn_save()
            muilti.click_pop_ok()
            muilti.click_btn_res_quest()
            muilti.accept_alert()
            muilti.assert_text_status()
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_create_quotation_type_normal_multi(self, excel_reader):
        driver = self.driver
        loginMC_page = LogInPage(driver)
        muilti = QuotationMuilti(driver,excel_reader )
        try:
            loginMC_page.login_role_vendor(user_name, pass_word)
            muilti.go_to_create_quotation()
            muilti.click_company_id4()
            muilti.click_select_store_multi()
            muilti.click_check_box_all_stores()
            muilti.click_btn_use_store()
            muilti.click_input_sku()
            muilti.send_keys_sku_file()
            muilti.click_btn_save()
            muilti.click_pop_ok()
            muilti.click_btn_res_quest()
            muilti.accept_alert()
            muilti.assert_text_status()
            muilti.assert_text_mutil_store()
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    










