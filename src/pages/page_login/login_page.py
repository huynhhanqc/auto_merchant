import logging
from time import sleep
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement

class LogInPage(ActionElement):
    url = "https://test-merchant.hasaki.vn/login"
    username_txt_box = (By.NAME, 'username')
    password_txt_box = (By.ID, 'password')
    btn_login = (By.ID, 'kt_sign_in_submit')
    home_title_vendor = (By.XPATH, "//h1[normalize-space()='Dashboard']")
    home_title_admin = (By.XPATH, "//h1[normalize-space()='Welcome to Hasaki']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def login_role_vendor(self, username, password):
        try:
            self.go_to_url()
            self.element_send_keys(self.username_txt_box, username)
            self.element_send_keys(self.password_txt_box, password)
            self.element_click(self.btn_login)
        except Exception as e:
            logging.error(f"An error occurred during login: {e}")
            raise

    def login_role_admin(self, username, password):
        try:
            self.go_to_url()
            self.element_send_keys(self.username_txt_box, username)
            self.element_send_keys(self.password_txt_box, password)
            self.element_click(self.btn_login)
        except Exception as e:
            logging.error(f"An error occurred during login: {e}")
            raise

    def go_to_url(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            logging.error(f"An error occurred while opening the login page: {e}")
            raise

    def input_username(self, username):
        try:
            self.element_send_keys(self.username_txt_box, username)
        except Exception as e:
            logging.error(f"An error occurred while entering the username: {e}")
            raise

    def input_password(self, password):
        try:
            self.element_send_keys(self.password_txt_box, password)
        except Exception as e:
            logging.error(f"An error occurred while entering the password: {e}")
            raise
        
    def click_btn_login(self):
        try:
            self.element_click(self.btn_login)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the login button: {e}")
            raise

    def get_text_login_failed(self):
        try:
            return self.element_get_text(self.text_login_vendor_failed)
        except Exception as e:
            logging.error(f"An error occurred while getting the login failed text: {e}")
            raise
    
    def get_text_home_title_vendor(self):
        try:
            return self.element_get_text(self.home_title_admin)
        except Exception as e:
            logging.error(f"An error occurred while getting the home title vendor text: {e}")
            raise