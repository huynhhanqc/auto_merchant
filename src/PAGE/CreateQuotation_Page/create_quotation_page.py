from selenium.webdriver.common.by import By
from src.PAGE.CreateQuotation_Page.ActionElment import ActionElement


class Create_Quotation(ActionElement):

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
    accept_sku = (By.XPATH, "//*[text()='100190112']")
    btn_save = (By.ID, "btnSaveQuotationDetail")
    pup_ok = (By.XPATH, "//*[text()='OK']")
    btn_res_quest = (By.XPATH, "//div[@class='card-toolbar']//a[3]")
    text_status = (By.XPATH, "//span[@class='position-relative badge badge-warning']")

    # Quotation All Store
    multi_stores = [By.XPATH, "//*[@role='option'and text()='MULTI STORES']"]
    zone_bd = (By.XPATH, "//*[text()=' Bình Dương ']")
    btn_use_store = (By.XPATH, "//*[@id='btnUseStore']")
    btn_allocate = (By.XPATH, "//*[@onclick='openAllocateQtyModal(1)']")
    btn_close_allocate = (By.XPATH, "//button[text()='Close']")
    sales_allocation_by_order = (By.XPATH, "//input[@id='allocationMethod_2']")



    def __init__(self, driver_):
        super().__init__(driver_)
        self.driver = driver_

    def click_set_time(self):
        self.element_click(self.select_time)
        self.element_click(self.set_time)

    def click_type_tester(self):
        self.element_click(self.quotation_type)
        self.element_click(self.type_tester)

    def click_type_gift(self):
        self.element_click(self.quotation_type)
        self.element_click(self.type_gift)

    def click_require_vat(self):
        self.element_click(self.require_vat)

    def send_keys_note(self, note):
        self.element_send_keys(self.note, note)

    def click_select_store(self):
        self.element_click(self.store)

    def click_product_sku(self):
        self.element_click(self.product_sku)

    def send_keys_sku(self, sku):
        self.element_send_keys(self.input_sku, sku)

    def click_accept_sku(self):
        self.element_click(self.accept_sku)

    def click_multi_stores(self):
        self.element_click(self.multi_stores)

    def click_zone_bd(self):
        self.element_click(self.zone_bd)

    def click_btn_use_store(self):
        self.element_click(self.btn_use_store)

    def click_btn_allocate(self):
        self.element_click(self.btn_allocate)

    def click_btn_close_allocate(self):
        self.element_click(self.btn_close_allocate)

    def click_sales_allocation_by_order(self):
        self.element_click(self.sales_allocation_by_order)

    def click_btn_save(self):
        self.element_click(self.btn_save)

    def click_pop_ok(self):
        self.element_click(self.pup_ok)

    def click_btn_res_quest(self):
        self.element_click(self.btn_res_quest)

    def assert_text_status(self):
        return self.element_get_text(self.text_status)

    







