from selenium.webdriver.common.by import By


class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://test-merchant.hasaki.vn/login"
        self.username_txt_box = (By.NAME, 'username')
        self.password_txt_box = (By.ID, 'password')
        self.login_btn = (By.ID, 'kt_sign_in_submit')

    def login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_txt_box).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txt_box).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_btn).click()


