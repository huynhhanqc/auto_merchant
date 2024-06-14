from selenium.webdriver.common.by import By

class LogInPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://test-merchant.hasaki.vn/login"
        self.username_txt_box = (By.NAME, 'username')
        self.password_txt_box = (By.ID, 'password')
        self.login_btn = (By.ID, 'kt_sign_in_submit')
        self.home_title_vendor = (By.XPATH, "//h1[normalize-space()='Dashboard']")
        self.home_title_admin = (By.XPATH, "//h1[normalize-space()='Welcome to Hasaki']")
        self.text_login_vendor_failed = (By.XPATH, "//div[@class='alert alert-danger flashSession']")    
    def login_role_vendor(self,username, password):
        self.driver.get(self.url)
        self.driver.find_element(*self.username_txt_box).send_keys(username)
        self.driver.find_element(*self.password_txt_box).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def get_home_title_vendor(self):
        return self.driver.find_element(*self.home_title_vendor).text

    def login_role_admin(self, username, password):
        self.driver.get(self.url)
        self.driver.find_element(*self.username_txt_box).send_keys(username)
        self.driver.find_element(*self.password_txt_box).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def get_home_title_admin(self):
        return self.driver.find_element(*self.home_title_admin).text
    
    def get_text_login_failed(self):
        return self.driver.find_element(*self.text_login_vendor_failed).text
    


    
