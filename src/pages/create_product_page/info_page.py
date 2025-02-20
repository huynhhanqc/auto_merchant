import logging
import random
import string
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement


class TabInFo(ActionElement):
    name_product = (By.ID, "name")
    text_input_name_product_none = (By.XPATH, "//div[@data-field='name']")
    vendor_product = (By.ID, "venprod_name")
    bar_code = (By.ID, "barcode")
    select_brand = (By.XPATH, "//*[@aria-controls='select2-brand_id-container']")
    options_brand = (By.XPATH, "//ul[contains(@class, 'select2-results__options')]")
    vendor_product_code = (By.ID, "venprod_code")
    vender_price = (By.XPATH, "//input[@id='venprod_price']")
    mar_price = (By.XPATH, "//input[@id='market_price']")
    hasaki_price = (By.XPATH, "//input[@id='price']")
    discount_Offline = (By.ID, "discountOffline")
    discount_Online = (By.ID, "discountOnline")
    leng_th = (By.XPATH, "//input[@id='plength']")
    width = (By.XPATH, "//input[@id='width']")
    height = (By.XPATH, "//input[@id='height']")
    weight = (By.XPATH, "//input[@id='weight']")
    product_Shelf_Life = (By.XPATH, "//span[@aria-labelledby='select2-product_shelf_life_month-container']/parent::span") 
    options_Shelf_Life = (By.XPATH,"//ul[contains(@class, 'select2-results__options')]")
    select_expiration_date_formatting_vendor = (By.XPATH, "(//*[@role='combobox'])[3]")
    ip_expiration_date_formatting = (By.XPATH, "(//*[@role='option' and contains(text(),'DD/MM/YY')])[2]")
    save_next = (By.XPATH, "//button[@id='btnSaveProductDetail']")
    text_status_product_success = (By.XPATH, "//*[text()='Waiting Approve']")
    text_already_exists = (By.XPATH, "//div[@class='alert alert-danger alert-dismissible fade show']")
    #Role Admin
    select_expiration_date_formatting_admin = (
        By.XPATH, "//span[@aria-labelledby='select2-product_expiration_date_format-container']/parent::span")
    btn_approve_product = (By.XPATH, "//button[normalize-space()='Approve']")
    text_status_product_approved_admin = (By.XPATH, "//*[text()='Approved']")
    text_status_product_completed = (By.XPATH, "//*[text()='Completed']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        

    def send_keys_name_product(self, text_name, length=30):
        try:
            if len(text_name) >= length:
                name = text_name[:length]
            else:
                remaining_length = length - len(text_name)
                characters = string.ascii_letters
                random_string = ''.join(random.choice(characters) for _ in range(remaining_length))
                name = f"{text_name}{random_string}"
            self.element_send_keys(self.name_product, name)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'name_product': {e}")
            raise

    def send_keys_vendor_product_name(self, text_name, length=30):
        try:
            if len(text_name) >= length:
                name = text_name[:length]
            else:
                remaining_length = length - len(text_name)
                characters = string.ascii_letters
                random_string = ''.join(random.choice(characters) for _ in range(remaining_length))
                name = f"{text_name}{random_string}"
            self.element_send_keys(self.vendor_product, name)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'vendor_product': {e}")
            raise

    def send_keys_bar_code(self):
        try:
            code = ''.join(str(random.randint(0, 9)) for _ in range(12))
            self.element_send_keys(self.bar_code, code)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'bar_code': {e}")
            raise

    def clear_bar_code(self):
        try:
            self.element_clear(self.bar_code)
        except Exception as e:
            logging.error(f"An error occurred while clearing 'bar_code': {e}")
            raise

    def click_on_brand(self):
        try:
            self.element_click(self.select_brand)
            options = self.get_options(self.options_brand)
            random_option = random.choice(options)
            random_option.click()
        except Exception as e:
            logging.error(f"An error occurred while clicking on 'select_brand': {e}")
            raise

    def send_keys_vendor_product_code(self):
        try:
            code = ''.join(str(random.randint(0, 9)) for _ in range(7))
            self.element_send_keys(self.vendor_product_code, code)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'vendor_product_code': {e}")
            raise

    def send_keys_vender_price(self, number):
        try:
            self.element_send_keys(self.vender_price, number)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'vender_price': {e}")
            raise

    def send_keys_mar_price(self, number):
        try:
            self.element_send_keys(self.mar_price, number)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'mar_price': {e}")
            raise

    def send_keys_hasaki_price(self, number):
        try:
            self.element_send_keys(self.hasaki_price, number)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'hasaki_price': {e}")
            raise

    def send_keys_leng_th(self):
        try:
            self.element_send_keys(self.leng_th, 1)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'leng_th': {e}")
            raise

    def send_keys_width(self):
        try:
            self.element_send_keys(self.width, 2)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'width': {e}")
            raise

    def send_keys_height(self):
        try:
            self.element_send_keys(self.height, 3)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'height': {e}")
            raise

    def send_keys_weight(self):
        try:
            self.element_send_keys(self.weight, 4)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'weight': {e}")
            raise

    def click_on_Shelf_Life_product(self):
        try:
            self.element_click(self.product_Shelf_Life)
            options = self.get_options(self.options_Shelf_Life)
            random_option = random.choice(options)
            random_option.click()
        except Exception as e:
            logging.error(f"An error occurred while clicking on 'product_Shelf_Life': {e}")
            raise

    def click_expiration_date_formatting_vendor(self):
        try:
            self.element_click(self.select_expiration_date_formatting_vendor)
        except Exception as e:
            logging.error(f"An error occurred while clicking on 'select_expiration_date_formatting_vendor': {e}")
            raise

    def click_ip_expiration_date_formatting(self):
        try:
            self.element_click(self.ip_expiration_date_formatting)
        except Exception as e:
            logging.error(f"An error occurred while clicking on 'ip_expiration_date_formatting': {e}")
            raise

    def click_save_next(self):
        try:
            self.element_click(self.save_next)
        except Exception as e:
            logging.error(f"An error occurred while clicking on 'save_next': {e}")
            raise

    def assert_text_status_product_success(self):
        try:
            return self.element_get_text(self.text_status_product_success)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_status_product_success': {e}")
            raise

    def assert_text_already_exists(self):
        try:
            return self.element_get_text(self.text_already_exists)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_already_exists': {e}")
            raise

    #Role Admin
    def click_btn_approve_product(self):
        try:
            self.element_click(self.btn_approve_product)
        except Exception as e:
            logging.error(f"An error occurred while clicking on 'btn_approve_product': {e}")
            raise

    def click_expiration_date_formatting_admin(self):
        try:
            self.element_click(self.select_expiration_date_formatting_admin)
        except Exception as e:
            logging.error(f"An error occurred while clicking on 'select_expiration_date_formatting_admin': {e}")
            raise

    def assert_text_status_product_approved_admin(self):
        try:
            return self.element_get_text(self.text_status_product_approved_admin)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_status_product_approved_admin': {e}")
            raise

    def assert_text_status_product_completed(self):
        try:
            return self.element_get_text(self.text_status_product_completed)
        except Exception as e:
            logging.error(f"An error occurred while getting text from 'text_status_product_completed': {e}")
            raise

    def get_bar_code(self):
        try:
            id_number_value = self.element_get_attribute(self.bar_code, "value")
            print(f"Giá trị của Barcode: {id_number_value}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
    