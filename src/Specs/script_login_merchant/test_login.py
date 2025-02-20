from src.drivers.webdriver_factory import WebdriverFactory
from src.pages.login_page import LogInPage
from time import sleep
import pytest
import logging
from selenium.common.exceptions import TimeoutException 
from src.utils.log_capture import log_capture 

@pytest.mark.skip(reason="no reason")

class TestSignIn(WebdriverFactory):
    def __init__(self):
        self.driver = None

    def test_login_role_vendor_success(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        try:
            Sign_In.login_role_vendor("truonghan1506", "150699")
            sleep(1)
            assert Sign_In.assert_text_home_title_vendor() == "Dashboard"
        except TimeoutException as e:
            logging.error(f"⏳ Lỗi timeout xảy ra: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_login_role_admin_success(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        try:
            Sign_In.login_role_admin("admin", "123123")
            sleep(1)
            assert Sign_In.assert_text_home_title_admin() == "Welcome to Hasaki"
        except TimeoutException as e:
            logging.error(f"⏳ Lỗi timeout xảy ra: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_login_role_vendor_failed(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        try:
            Sign_In.login_role_vendor("truonghan", "326")
            sleep(1)
            assert Sign_In.assert_text_login_failed() == "Tên người dùng hoặc mật khẩu không đúng !"
        except TimeoutException as e:
            logging.error(f"⏳ Lỗi timeout xảy ra: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False

    def test_login_role_admin_failed(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        try:
            Sign_In.login_role_admin("admin", "123")
            sleep(1)
            assert Sign_In.assert_text_login_failed() == "Tên người dùng hoặc mật khẩu không đúng !"
        except TimeoutException as e:
            logging.error(f"⏳ Lỗi timeout xảy ra: {str(e)}")
            log_capture(driver, "Timeout_Error")
            assert False
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            log_capture(driver, "Unexpected_Error")
            assert False
