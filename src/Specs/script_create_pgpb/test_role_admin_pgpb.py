import os
from time import sleep
from dotenv import load_dotenv
from faker import Faker
from src.pages.login_page import LogInPage
from src.pages.create_pgpb_page.add_pgpb_page import CreatePgPb
from src.drivers.webdriver_factory import WebdriverFactory
import logging
from selenium.common.exceptions import TimeoutException 
from src.utils.log_capture import log_capture
from src.pages.create_pgpb_page.assert_create_page import AssertCreatePG

load_dotenv()
user_name = os.getenv("USER_ROLE_ADMIN")
pass_word = os.getenv("PASS_ROLE_ADMIN")

class TestCreatePgPbRoleAdmin (WebdriverFactory):
    def test_create_pg_inline_success(self):
        fake = Faker()
        driver = self.driver
        login_page = LogInPage(driver)
        add_pg = CreatePgPb(driver)
        assert_create_pg = AssertCreatePG(driver)
        try:
            logging.info("🔹 Bắt đầu đăng nhập tài khoản Admin")
            login_page.login_role_admin(user_name, pass_word)
            sleep(2)
            add_pg.go_to_url()
            add_pg.click_select_Vendor()
            sleep(1)
            add_pg.click_select_Brand()
            add_pg.click_select_Work_Type_Inline()
            add_pg.send_keys_full_name(fake.name())
            add_pg.send_keys_personal_Email(fake.email())
            add_pg.send_keys_id_Number()
            add_pg.send_keys_phone()
            add_pg.click_select_Location()
            add_pg.send_keys_image_Avatar()
            add_pg.send_keys_image_front_side_cmnd()
            add_pg.send_keys_image_back_side_cmnd()
            add_pg.click_btn_Save()
            assert_create_pg.check_inactive_status
            sleep(1)
            add_pg.click_btn_Request_to_Active()
            sleep(1)
            assert_create_pg.check_waiting_approve_status()
            add_pg.click_btn_Approve()
            assert_create_pg.check_active_status()
            sleep(3)
            assert_create_pg.get_staff_id()
            assert_create_pg.get_id_Number()
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
        assert_create_pg = AssertCreatePG(driver)
        try:
            logging.info("🔹 Bắt đầu đăng nhập tài khoản Admin")
            login_page.login_role_admin(user_name, pass_word)
            sleep(2)
            add_pg.go_to_url()
            add_pg.click_select_Vendor()
            sleep(1)
            add_pg.click_select_Brand()
            add_pg.click_select_Work_Type_Not_Line()
            add_pg.send_keys_full_name(fake.name())
            add_pg.send_keys_personal_Email(fake.email())
            add_pg.send_keys_id_Number()
            add_pg.send_keys_phone()
            add_pg.click_select_Location()
            add_pg.send_keys_note("PG Auto")
            add_pg.send_keys_image_Avatar()
            add_pg.send_keys_image_front_side_cmnd()
            add_pg.send_keys_image_back_side_cmnd()
            add_pg.click_btn_Save()
            assert_create_pg.check_active_status()
            assert_create_pg.get_id_Number()
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False
