import logging
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement


class LogInPage(ActionElement):
    url = "https://test-merchant.hasaki.vn/login"
    username_txt_box = (By.NAME, 'username')
    password_txt_box = (By.ID, 'password')
    btn_login = (By.ID, 'kt_sign_in_submit')
    home_title_vendor = (By.XPATH, "//h1[normalize-space()='Dashboard']")
    home_title_admin = (By.XPATH, "//h1[normalize-space()='Welcome to Hasaki']")
    text_login_vendor_failed = (By.XPATH, "//div[@class='alert alert-danger flashSession']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_role_vendor(self, username, password):
        try:
            self.driver.get(self.url)
            self.element_send_keys(self.username_txt_box, username)
            self.element_send_keys(self.password_txt_box, password)
            self.element_click(self.btn_login)
        except Exception as e:
            logging.error(f"An error occurred while logging in: {e}")
            raise

    def assert_text_home_title_vendor(self):
        try:
            return self.element_get_text(self.home_title_vendor)
        except Exception as e:
            logging.error(f"An error occurred while getting the home title: {e}")
            raise

    def login_role_admin(self, username, password):
        try:
            self.driver.get(self.url)
            self.element_send_keys(self.username_txt_box, username)
            self.element_send_keys(self.password_txt_box, password)
            self.element_click(self.btn_login)
        except Exception as e:
            logging.error(f"An error occurred while logging in: {e}")
            raise

    def assert_text_home_title_admin(self):
        try:
            return self.element_get_text(self.home_title_admin)
        except Exception as e:
            logging.error(f"An error occurred while getting the home title: {e}")
            raise

    def assert_text_login_failed(self):
        try:
            return self.element_get_text(self.text_login_vendor_failed)
        except Exception as e:
            logging.error(f"An error occurred while getting the login failed text: {e}")
            raise
