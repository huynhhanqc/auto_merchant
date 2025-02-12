from src.PAGE.Login_Page import LogInPage
from time import sleep
import pytest
from src.SPECS.BaseTest import BaseFixture
import logging
from selenium.common.exceptions import TimeoutException 
from src.PAGE.Utils.Log_capture import Log_CapTure 

@pytest.mark.skip(reason="no reason")
class TestSignIn(BaseFixture):
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
            Log_CapTure(driver, "Timeout_Error")
            assert False
        
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            Log_CapTure(driver, "Unexpected_Error")
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
            Log_CapTure(driver, "Timeout_Error")
            assert False
        
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            Log_CapTure(driver, "Unexpected_Error")
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
            Log_CapTure(driver, "Timeout_Error")
            assert False
        
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            Log_CapTure(driver, "Unexpected_Error")
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
            Log_CapTure(driver, "Timeout_Error")
            assert False
        
        except Exception as e:
            logging.error(f"🚨 Lỗi không mong muốn: {str(e)}")
            Log_CapTure(driver, "Unexpected_Error")
            assert False
