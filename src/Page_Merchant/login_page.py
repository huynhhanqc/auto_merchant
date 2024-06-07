from selenium.webdriver.common.by import By
from faker import Faker
import time


class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://test-merchant.hasaki.vn/login"
        self.username_txt_box = (By.NAME, 'username')
        self.password_txt_box = (By.ID, 'password')
        self.login_btn = (By.ID, 'kt_sign_in_submit')

    def login_page(self):
        self.driver.get(self.url)
        self.driver.find_element(*self.username_txt_box).send_keys("truonghan1506")
        self.driver.find_element(*self.password_txt_box).send_keys("150699")
        self.driver.find_element(*self.login_btn).click()
