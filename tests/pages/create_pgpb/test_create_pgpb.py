import os
from time import sleep
from dotenv import load_dotenv
from faker import Faker
from src.pages.page_login.login_page import LogInPage
from src.pages.create_pgpb_page.add_pgpb_page import CreatePgPb
from src.drivers.webdriver_factory import WebdriverFactory
import logging
from selenium.common.exceptions import TimeoutException 
from src.utils.log_capture import log_capture
from tests.pages.create_pgpb.assertions.create_pgbp_assertions import CreatePgbpbAssertions

load_dotenv()
user_name = os.getenv("USER_ROLE_ADMIN")
pass_word = os.getenv("PASS_ROLE_ADMIN")

class TestCreatePgPbRoleAdmin (WebdriverFactory):
    def test_create_pg_inline_success(self):
        driver = self.driver
        login_page = LogInPage(driver)
        add_pg = CreatePgPb(driver)
        assertions = CreatePgbpbAssertions(driver)
        try:
            logging.info("🔹 Bắt đầu đăng nhập tài khoản Admin")
            login_page.login_role_admin(user_name, pass_word)
            sleep(2)
            add_pg.go_to_url()
            add_pg.click_select_Vendor()
            sleep(1)
            add_pg.click_select_Brand()
            add_pg.click_select_Work_Type_Inline()
            add_pg.send_keys_full_name()
            add_pg.send_keys_personal_Email()
            add_pg.send_keys_id_Number()
            add_pg.send_keys_phone()
            add_pg.click_select_Location()
            add_pg.send_keys_image_Avatar()
            add_pg.send_keys_image_front_side_cmnd()
            add_pg.send_keys_image_back_side_cmnd()
            add_pg.click_btn_Save()
            sleep(1)
            assert assertions.verify_inactive_status(), "In-active status verification failed"
            add_pg.click_btn_Request_to_Active()
            assert assertions.verify_waiting_approve_status(), "Waiting approve status verification failed"
            sleep(1)
            add_pg.click_btn_Approve()
            assert assertions.verify_active_status(), "Active status verification failed"
            add_pg.get_staff_id()
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False
        
    def test_create_pg_not_line_success(self):
        fake = Faker()
        driver = self.driver
        login_page = LogInPage(driver)
        add_pg = CreatePgPb(driver)
        assertions = CreatePgbpbAssertions(driver)
        try:
            logging.info("🔹 Bắt đầu đăng nhập tài khoản Admin")
            login_page.login_role_admin(user_name, pass_word)
            sleep(2)
            add_pg.go_to_url()
            add_pg.click_select_Vendor()
            sleep(1)
            add_pg.click_select_Brand()
            add_pg.click_select_Work_Type_Not_Line()
            add_pg.send_keys_full_name()
            add_pg.send_keys_personal_Email()
            add_pg.send_keys_id_Number()
            add_pg.send_keys_phone()
            add_pg.click_select_Location()
            add_pg.send_keys_note("PG Auto")
            add_pg.send_keys_image_Avatar()
            add_pg.send_keys_image_front_side_cmnd()
            add_pg.send_keys_image_back_side_cmnd()
            add_pg.click_btn_Save()
            assert assertions.verify_active_status(), "Active status verification failed"
            add_pg.get_id_number()
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False
