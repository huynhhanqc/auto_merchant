from src.SETUP.WebDriver_Setup import WebDriverSetup
from src.PAGE.Login_Page import LogInPage
from time import sleep


class TestSignIn(WebDriverSetup):
    def test_login_role_vendor_success(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        Sign_In.login_role_vendor("truonghan1506", "150699")
        sleep(1)
        assert Sign_In.assert_text_home_title_vendor() == "Dashboard"

    def test_login_role_admin_success(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        Sign_In.login_role_admin("admin", "123123")
        sleep(1)
        assert Sign_In.assert_text_home_title_admin() == "Welcome to Hasaki"

    def test_login_role_vendor_failed(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        Sign_In.login_role_vendor("truonghan", "326")
        sleep(1)
        assert Sign_In.assert_text_login_failed() == "Tên người dùng hoặc mật khẩu không đúng !"

    def test_login_role_admin_failed(self):
        driver = self.driver
        Sign_In = LogInPage(driver)
        Sign_In.login_role_admin("admin", "123")
        sleep(1)
        assert Sign_In.assert_text_login_failed() == "Tên người dùng hoặc mật khẩu không đúng !"

        
        

        
        