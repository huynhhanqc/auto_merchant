from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By


class SignInPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.username_txt_box = (By.NAME, 'username')
        self.password_txt_box = (By.ID, 'password')
        self.login_btn = (By.ID, 'kt_sign_in_submit')

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_txt_box).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txt_box).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()





