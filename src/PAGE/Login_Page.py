from selenium.webdriver.common.by import By
from src.PAGE.Utils.Common import ActionElement

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

    def login_role_vendor(self,username, password):
        self.driver.get(self.url)
        self.element_send_keys(self.username_txt_box, username)
        self.element_send_keys(self.password_txt_box, password)
        self.element_click(self.btn_login)

    def assert_text_home_title_vendor(self):
       return self.element_get_text(self.home_title_vendor)

    def login_role_admin(self, username, password):
        self.driver.get(self.url)
        self.element_send_keys(self.username_txt_box, username)
        self.element_send_keys(self.password_txt_box, password)
        self.element_click(self.btn_login)

    def assert_text_home_title_admin(self):
        return self.element_get_text(self.home_title_admin)
    
    def assert_text_login_failed(self):
        return self.element_get_text(self.text_login_vendor_failed)
    
    
    
    
    


    
