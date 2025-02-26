from src.drivers.webdriver_factory import WebdriverFactory
from src.pages.page_login.login_page import LogInPage
import pytest
from src.utils.log_capture import log_capture 

@pytest.mark.skip(reason="no reason")
@pytest.mark.parametrize("username, password, expected_result", [
    ("truonghan1506", "150699", True),
    ("truonghan1506", "1506999", False),
    ("nonexistentuser", "admin1", False)
])

class TestSignIn(WebdriverFactory):
    def test_login(self, username, password, expected_result):
        driver = self.driver
        sign_in = LogInPage(driver)
        sign_in.go_to_url()
        sign_in.input_username(username)
        sign_in.input_password(password)
        sign_in.click_btn_login()
        if sign_in.get_text_home_title_vendor == "Welcome to Hasaki":
            assert expected_result == True
        else:
            assert expected_result == False

            
