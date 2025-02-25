import logging
import random
import re
import string
from time import sleep
from faker import Faker
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement


class AccountInfo(ActionElement):
    url = "https://test-merchant.hasaki.vn/login"
    new_sign_up = (By.XPATH, "//a[normalize-space()='Đăng ký tài khoản mới.']")
    user_name = (By.ID, "username")
    email = (By.ID, "email")
    phone_number = (By.ID, "phone")
    password = (By.ID, "password")
    confirm_password = (By.ID, "confirm-password")
    btn_continue = (By.XPATH, "//button[normalize-space()='Tiếp tục']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page_sign_up(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            logging.error(f"An error occurred while opening the sign-up page: {e}")
            raise

    def click_new_sign_up(self):
        try:
            self.element_click(self.new_sign_up)
        except Exception as e:
            logging.error(f"An error occurred while clicking the new sign-up button: {e}")
            raise

    def input_user_name(self):
        fake = Faker()
        try:
            username = fake.user_name().replace(" ", "")
            self.element_send_keys(self.user_name, username)
            print(f"\nACCOUNT: >>>>>>>>>>>>>>>>>>>>>>: {username}")
        except Exception as e:
            logging.error(f"An error occurred while entering the username: {e}")
            raise
    
    def input_email(self):
        fake = Faker()
        try:
            mail = fake.email()
            self.element_send_keys(self.email, mail)
        except Exception as e:
            logging.error(f"An error occurred while entering the email: {e}")
            raise

    def input_phone_number(self):
        try:
            valid_prefixes = [
                "032", "033", "034", "035", "036", "037", "038", "039",
                "056", "058", "059", "070", "076", "077", "078", "079",
                "080", "081", "082", "083", "084", "085", "086", "088", "089",
                "090", "091", "092", "093", "094", "096", "097", "098", "099"
            ]
            prefix = random.choice(valid_prefixes)
            random_number = ''.join(str(random.randint(0, 9)) for _ in range(7))
            phone_number = f"{prefix}{random_number}"
            self.element_send_keys(self.phone_number, phone_number)
        except Exception as e:
            logging.error(f"An error occurred while entering the phone number: {e}")
            raise

    def input_password(self):
        try:
            special_chars = "@$%!"
            first_char = random.choice(string.ascii_uppercase)
            length = 10  
            num_special = 2 
            num_digits = 2 
            num_lower = length - num_special - num_digits 
            special_part = ''.join(random.choice(special_chars) for _ in range(num_special))
            digit_part = ''.join(random.choice(string.digits) for _ in range(num_digits))
            lower_part = ''.join(random.choice(string.ascii_lowercase) for _ in range(num_lower))
            remaining_chars = special_part + digit_part + lower_part
            remaining_chars = ''.join(random.sample(remaining_chars, len(remaining_chars)))
            password_number = first_char + remaining_chars
            self.element_send_keys(self.password, password_number)
            print(f"PASSWORD:  >>>>>>>>>>>>>>>>>>>>>>: {password_number}")
        except Exception as e:
            logging.error(f"An error occurred while entering the password: {e}")
            raise

    def input_confirm_password(self):
        try:
            confirpassword = self.element_get_attribute(self.password, "value")
            self.element_send_keys(self.confirm_password, confirpassword)
        except Exception as e:
            logging.error(f"An error occurred while entering the confirm password: {e}")
            raise

    def click_btn_continue(self):
        try:
            self.element_click(self.btn_continue)
            sleep(2)
        except Exception as e:
            logging.error(f"An error occurred while clicking the continue button: {e}")
            raise


