import logging
from time import sleep
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement

class QuotationMuilti(ActionElement):
    url_create_quotation = "https://test-merchant.hasaki.vn/quotation/detail"
    select_time = [By.XPATH, "//*[@id='receivingTime']"]
    set_time = (By.XPATH, "//*[@class='flatpickr-day 'and text()='29']")
    quotation_type = (By.XPATH, "//*[@aria-labelledby='select2-quotationType-container']/parent::*")
    type_tester = (By.XPATH, "(//li[text()='Tester']/parent::*)[1]")
    type_gift = (By.XPATH, "//li[text()='Gift']")
    require_vat = (By.XPATH, "//*[@id='quotationConfig']/parent::*")
    note = (By.XPATH, "//*[@id='quotationNote']")
    store = (By.XPATH, "//*[@id='select2-store_1-container']/parent::*")
    product_sku = (By.XPATH, "//*[text()='Search for a product']/parent::span")
    input_sku = (By.XPATH, "//input[@role='searchbox']")
    accept_sku = (By.XPATH, "//*[text()='206500009']")
    btn_save = (By.ID, "btnSaveQuotationDetail")
    pup_ok = (By.XPATH, "//*[text()='OK']")
    btn_res_quest = (By.XPATH, "//a[contains(text(),'Request to confirm')]")
    text_status = (By.XPATH, "//span[@class='position-relative badge badge-warning']")
    company = (By.XPATH, "//span[@class='select2-selection select2-selection--single form-select form-select-solid']")
    company2_accept = (By.XPATH, "//li[contains(text(),'Cty Hasaki Beauty & Clinic')]")
    company4_accept = (By.XPATH, "//li[contains(text(),'Cty Mastige')]")

    # Quotation All Store
    multi_stores = [By.XPATH, "//*[@role='option'and text()='MULTI STORES']"]
    zone_bd = (By.XPATH, "//*[text()='Hồ Chí Minh']")
    check_box_all_stores = (By.XPATH, "//label[contains(text(),'Check All')]")
    btn_use_store = (By.XPATH, "//*[@id='btnUseStore']")
    btn_allocate = (By.XPATH, "//*[@onclick='openAllocateQtyModal(1)']")
    btn_close_allocate = (By.XPATH, "//button[text()='Close']")
    sales_allocation_by_order = (By.XPATH, "//input[@id='allocationMethod_2']")
    text_mutil_store = (By.XPATH, "//*[text()='Multi Store']")

    def __init__(self, driver_, excel_reader):
        super().__init__(driver_)
        self.driver = driver_
        self.excel_reader = excel_reader

    def go_to_create_quotation(self):
        try:
            self.driver.get(self.url_create_quotation)
        except Exception as e:
            logging.error(f"An error occurred while navigating to the URL: {e}")

    def click_set_time(self):
        try:
            self.element_click(self.select_time)
            self.element_click(self.set_time)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'set_time': {e}")

    def click_type_tester(self):
        try:
            self.element_click(self.quotation_type)
            self.element_click(self.type_tester)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'type_tester': {e}")

    def click_company_id2(self):
        try:
            self.element_click(self.company)
            self.element_click(self.company2_accept)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'company': {e}")

    def click_company_id4(self):
        try:
            self.element_click(self.company)
            self.element_click(self.company4_accept)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'company': {e}")

    def click_type_gift(self):
        try:
            self.element_click(self.quotation_type)
            self.element_click(self.type_gift)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'type_gift': {e}")

    def click_require_vat(self):
        try:
            self.element_click(self.require_vat)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'require_vat': {e}")

    def send_keys_note(self, note):
        try:
            self.element_send_keys(self.note, note)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'note': {e}")

    def click_select_store_multi(self):
        try:
            self.element_click(self.store)
            self.element_click(self.multi_stores)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'store': {e}")

    def click_input_sku(self):
        try:
            self.element_click(self.product_sku)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'product_sku': {e}")

    def send_keys_sku_file(self):
        column_letter = "A" 
        num_values = 1  
        try:
            random_skus = self.excel_reader.get_random_values(column_letter, num_values)
            for sku in random_skus:
                self.element_send_keys(self.input_sku, sku)
                sleep(1)
                self.click_accept_sku(sku)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'input_sku': {e}")

    def click_accept_sku(self, sku):
        try:
            sku_locator = (By.XPATH, f"//*[text()='{sku}']")
            self.element_click(sku_locator)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'accept_sku': {e}")

    def click_zone_bd(self):
        try:
            self.element_click(self.zone_bd)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'zone_bd': {e}")

    def click_check_box_all_stores(self):
        try:
            self.element_click(self.check_box_all_stores)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'check_box_all_stores': {e}")

    def click_btn_use_store(self):
        try:
            self.element_click(self.btn_use_store)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_use_store': {e}")

    def click_btn_allocate(self):
        try:
            self.element_click(self.btn_allocate)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_allocate': {e}")

    def click_btn_close_allocate(self):
        try:
            self.element_click(self.btn_close_allocate)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_close_allocate': {e}")

    def click_sales_allocation_by_order(self):
        try:
            self.element_click(self.sales_allocation_by_order)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'sales_allocation_by_order': {e}")

    def click_btn_save(self):
        try:
            self.element_click(self.btn_save)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_save': {e}")

    def click_pop_ok(self):
        try:
            self.element_click(self.pup_ok)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'pup_ok': {e}")

    def click_btn_res_quest(self):
        try:
            self.element_click(self.btn_res_quest)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_res_quest': {e}")

    def assert_text_status(self):
        try:
            waiting_approve_text = self.element_get_text(self.text_status)
            if waiting_approve_text == "Waiting For Confirm\nM":
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"An error occurred while getting the text of 'text_status': {e}")

    def assert_text_mutil_store(self):
        try:
            count_store = self.element_get_text(self.text_mutil_store)
            if count_store == "Multi Store(23 STORES)":
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"An error occurred while getting the text of 'text_mutil_store': {e}")


