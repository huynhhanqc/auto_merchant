from selenium.webdriver.common.by import By
from src.PAGE.CreateQuotation_Page.ActionElment import ActionElement


class Tab_InFo(ActionElement):

    name_product = (By.ID, "name")
    text_input_name_product_none = (By.XPATH, "//div[@data-field='name']")
    vendor_product = (By.ID, "venprod_name")
    bar_code = (By.ID, "barcode")
    select_brand = (By.XPATH, "//*[@aria-controls='select2-brand_id-container']")
    options_brand = (By.XPATH, "//li[contains(text(),'LA ROCHE-POSAY')]")
    vendor_product_code = (By.ID, "venprod_code")   
    vender_price = (By.ID, "venprod_price")
    mar_price = (By.ID, "market_price")
    hasaki_price = (By.ID, "price")
    discount_Offline = (By.ID, "discountOffline")   
    discount_Online = (By.ID, "discountOnline")
    leng_th = (By.ID, "plength")
    width = (By.ID, "width")
    height = (By.ID, "height")
    weight = (By.ID, "weight")
    select_expiration_date_formatting_vendor = (By.XPATH, "(//*[@role='combobox'])[3]")
    ip_expiration_date_formatting = (By.XPATH, "(//*[@role='option' and contains(text(),'DD/MM/YY')])[2]")
    save_next = (By.ID, "btnSaveProductDetail")   
    text_status_product_success = (By.XPATH, "//*[text()='Waiting Approve']")
    text_already_exists = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible fade show']")
        #Role Admin
    select_expiration_date_formatting_admin = (By.XPATH, "//span[@aria-labelledby='select2-product_expiration_date_format-container']/parent::span")
    btn_approve_product = (By.XPATH, "//button[normalize-space()='Approve']")
    text_status_product_approved_admin = (By.XPATH, "//*[text()='Approved']")
    text_status_product_completed = (By.XPATH, "//*[text()='Completed']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def send_keys_name_product(self,text_name):
        self.element_send_keys(self.name_product, text_name)

    def get_text_input_name_product_failed(self):
        return self.element_get_text(self.text_input_name_product_none)

    def send_keys_vendor_product_name(self,text_name):
        self.element_send_keys(self.vendor_product, text_name)

    def send_keys_bar_code(self, number):
        self.element_send_keys(self.bar_code, number)

    def clear_bar_code(self):
        self.element_clear(self.bar_code)

    def click_on_brand(self):
        self.element_click(self.select_brand)
        self.element_click(self.options_brand)

    def send_keys_vendor_product_code(self, number):
        self.element_send_keys(self.vendor_product_code, number)

    def send_keys_vender_price(self, number):
        self.element_send_keys(self.vender_price, number)

    def send_keys_mar_price(self, number):
        self.element_send_keys(self.mar_price, number)

    def send_keys_hasaki_price(self, number):
        self.element_send_keys(self.hasaki_price, number)

    def send_keys_leng_th(self):
        self.element_send_keys(self.leng_th, 1)

    def send_keys_width(self):
        self.element_send_keys(self.width, 2)

    def send_keys_height(self):
        self.element_send_keys(self.height, 3)

    def send_keys_weight(self):
        self.element_send_keys(self.weight, 4)

    def click_expiration_date_formatting_vendor(self):
        self.element_click(self.select_expiration_date_formatting_vendor)

    def click_ip_expiration_date_formatting(self):
        self.element_click(self.ip_expiration_date_formatting)

    def click_save_next(self):
        self.element_click(self.save_next)

    def assert_text_status_product_success(self):
        return self.element_get_text(self.text_status_product_success)
    
    def assert_text_already_exists(self):
        return self.element_get_text(self.text_already_exists)

    #Role Admin
    def click_btn_approve_product(self):
        self.element_click(self.btn_approve_product)

    def click_expiration_date_formatting_admin(self):
        self.element_click(self.select_expiration_date_formatting_admin)

    def assert_text_status_product_approved_admin(self):
        return self.element_get_text(self.text_status_product_approved_admin)

    def assert_text_status_product_completed(self):
        return self.element_get_text(self.text_status_product_completed)