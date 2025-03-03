import os
from time import sleep
from dotenv import load_dotenv
from faker import Faker
from src.pages.create_work_schedule_page.create_work_schedule_page import CreateWorkSchedule
from src.pages.page_login.login_page import LogInPage
from src.drivers.webdriver_factory import WebdriverFactory
import logging
from selenium.common.exceptions import TimeoutException 
from src.utils.log_capture import log_capture

load_dotenv()
user_name = os.getenv("USER_ROLE_ADMIN")
pass_word = os.getenv("PASS_ROLE_ADMIN")

class TestCreateWorkSchedule (WebdriverFactory):
    def test_create_work_schedule_inline_success(self):
        driver = self.driver
        login_page = LogInPage(driver)
        create_schedule = CreateWorkSchedule(driver)
        try:
            login_page.login_role_admin(user_name, pass_word)
            create_schedule.go_to_url()
            create_schedule.click_select_Vendor()
            create_schedule.click_work_type()
            create_schedule.click_select_pgpb()
            create_schedule.click_working_date()
            create_schedule.click_select_random_shift()
            create_schedule.click_btn_save()
        except TimeoutException as e:
            logging.error(f"⏳ The element is not visible or clickable during the timeout.: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False, "The element is not displayed or cannot be clicked."
        except Exception as e:
            logging.error(f"🚨 Unexpected error when testing.: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False