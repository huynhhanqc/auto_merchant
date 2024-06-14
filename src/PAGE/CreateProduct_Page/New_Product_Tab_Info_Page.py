from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Tab_InFo:
    def __init__(self, driver):
        self.driver = driver
        self.name_product = (By.ID, "name")
        self.text_input_name_product_none = (By.XPATH, "//div[@data-field='name']")
        self.vendor_product = (By.ID, "venprod_name")
        self.bar_code = (By.ID, "barcode")
        self.select_brand = (By.XPATH, "//*[text()='Select Brand']")
        self.input_brand = (By.XPATH, "//li[contains(text(),'BIODERMA')]")
        self.vendor_product_code = (By.ID, "venprod_code")   
        self.vender_price = (By.ID, "venprod_price")
        self.mar_price = (By.ID, "market_price")
        self.hasaki_price = (By.ID, "price")
        self.discount_Offline = (By.ID, "discountOffline")   
        self.discount_Online = (By.ID, "discountOnline")
        self.leng_th = (By.ID, "plength")
        self.width = (By.ID, "width")
        self.height = (By.ID, "height")
        self.weight = (By.ID, "weight")
        self.select_expiration_date_formatting_vendor = (By.XPATH, "(//*[@role='combobox'])[3]")
        self.ip_expiration_date_formatting = (By.XPATH, "(//*[@role='option' and contains(text(),'DD/MM/YY')])[2]")
        self.save_next = (By.ID, "btnSaveProductDetail")   
        self.text_status_product_success = (By.XPATH, "//span[@class='position-relative ms-2 badge badge badge-warning']")
        #Role Admin
        self.select_expiration_date_formatting_admin = (By.XPATH, "//span[@aria-labelledby='select2-product_expiration_date_format-container']/parent::span")
        self.btn_approve_product = (By.XPATH, "//button[normalize-space()='Approve']")
        self.text_status_product_approved_admin = (By.XPATH, "//span[@class='position-relative ms-2 badge badge badge-success']")

    def enter_name_product(self,text_name):
        self.driver.find_element(*self.name_product).send_keys(text_name)

    def get_text_input_name_product_failed(self):
        return self.driver.find_element(*self.text_input_name_product_none).text

    def enter_vendor_product_name(self,text_name):
        self.driver.find_element(*self.vendor_product).send_keys(text_name)

    def enter_bar_code(self, number):
        self.driver.find_element(*self.bar_code).send_keys(number)

    def click_select_brand(self):
        self.driver.find_element(*self.select_brand).click()

    def click_input_brand(self):
        self.driver.find_element(*self.input_brand).click()

    def input_vendor_product_code(self, number):
        self.driver.find_element(*self.vendor_product_code).send_keys(number)

    def input_vender_price(self, number):
        self.driver.find_element(*self.vender_price).send_keys(number)

    def input_mar_price(self, number):
        self.driver.find_element(*self.mar_price).send_keys(number)

    def input_hasaki_price(self, number):
        self.driver.find_element(*self.hasaki_price).send_keys(number)

    def input_leng_th(self):
        self.driver.find_element(*self.leng_th).send_keys(1)

    def input_width(self):
        self.driver.find_element(*self.width).send_keys(1)

    def input_height(self):
        self.driver.find_element(*self.height).send_keys(1)

    def input_weight(self):
        self.driver.find_element(*self.weight).send_keys(1)

    def click_expiration_date_formatting_vendor(self):
        self.driver.find_element(*self.select_expiration_date_formatting_vendor).click()

    def click_ip_expiration_date_formatting(self):
        self.driver.find_element(*self.ip_expiration_date_formatting).click()

    def click_save_next(self):
        self.driver.find_element(*self.save_next).click()

    def get_text_status_product_success(self):
        return self.driver.find_element(*self.text_status_product_success).text
    
    #Role Admin
    def click_btn_approve_product(self):
        self.driver.find_element(*self.btn_approve_product).click()

    def click_expiration_date_formatting_admin(self):
        self.driver.find_element(*self.select_expiration_date_formatting_admin).click()

    def get_text_status_product_approved_admin(self):
        return self.driver.find_element(*self.text_status_product_approved_admin).text
