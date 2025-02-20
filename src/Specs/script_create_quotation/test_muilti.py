import os
from time import sleep
from dotenv import load_dotenv
import pytest
from src.pages.login_page import LogInPage
from src.pages.create_quotation_page.muilti_page import QuotationMuilti
from src.drivers.webdriver_factory import  WebdriverFactory
from src.utils.log_capture import log_capture
import logging
from selenium.common.exceptions import TimeoutException
from src.handleFile.handle_excel import ExcelReader

load_dotenv()
user_name = os.getenv("USER_ROLE_MERCHANT")
pass_word = os.getenv("PASS_ROLE_MERCHANT")

@pytest.fixture(scope="function")
def excel_reader():
    file_path = '/Users/mac/Downloads/Product.xlsx' 
    sheet_name = 'Prod'
    return ExcelReader(file_path, sheet_name)

class TestCreateQuotationSigle(WebdriverFactory):
    def test_create_quotation(self, excel_reader):
        driver = self.driver
        loginMC_page = LogInPage(driver)
        muilti = QuotationMuilti(driver, excel_reader)
        try:
            loginMC_page.login_role_vendor(user_name, pass_word)
            sleep(1)
            muilti.go_to_create_quotation()
            sleep(1)
            muilti.click_type_gift()
            muilti.click_company()
            muilti.click_select_store_multi()
            sleep(2)
            muilti.click_zone_bd()
            muilti.click_btn_use_store()
            muilti.click_input_sku()
            muilti.send_keys_sku_file()
            sleep(1)
            muilti.click_btn_save()
            sleep(1)
            muilti.click_pop_ok()
            sleep(1)
            muilti.click_btn_res_quest()
            sleep(2)
            muilti.accept_alert()
            assert muilti.assert_text_status() == "Waiting For Confirm\nM"
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
            sleep(1)
            muilti.go_to_create_quotation()
            sleep(1)
            muilti.click_company()
            sleep(1)
            muilti.click_select_store_multi()
            sleep(1)
            muilti.click_check_box_all_stores()
            muilti.click_btn_use_store()
            muilti.click_input_sku()
            muilti.send_keys_sku_file()
            sleep(1)
            muilti.click_btn_save()
            sleep(1)
            muilti.click_pop_ok()
            sleep(1)
            muilti.click_btn_res_quest()
            sleep(1)
            muilti.accept_alert()
            sleep(1)
            assert muilti.assert_text_status() == "Waiting For Confirm\nM"
            sleep(1)
            assert muilti.assert_text_mutil_store() == "Multi Store(22 STORES)"
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    










