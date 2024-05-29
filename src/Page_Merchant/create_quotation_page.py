from selenium.webdriver.common.by import By


class Create_Quotation:
    def __init__(self, driver):
        self.driver = driver

        self.select_time = [By.XPATH, "//*[@id='receivingTime']"]
        self.set_time = (By.XPATH, "//*[@class='flatpickr-day 'and text()='29']")
        self.quotation_type = (By.XPATH, "//*[@aria-labelledby='select2-quotationType-container']/parent::*")
        self.type_tester = (By.XPATH, "(//li[text()='Tester']/parent::*)[1]")
        self.type_gift = (By.XPATH, "//li[text()='Gift']")
        self.require_vat = (By.XPATH, "//*[@id='quotationConfig']/parent::*")
        self.note = (By.XPATH, "//*[@id='quotationNote']")
        self.store = (By.XPATH, "//*[@id='select2-store_1-container']/parent::*")
        self.product_sku = (By.XPATH, "//*[text()='Search for a product']/parent::span")
        self.input_sku = (By.XPATH, "//input[@role='searchbox']")
        self.accept_sku = (By.XPATH, "//*[text()='100190112']")
        self.btn_save = (By.ID, "btnSaveQuotationDetail")
        self.pup_ok = (By.XPATH, "//*[text()='OK']")
        self.btn_res_quest = (By.XPATH, "//div[@class='card-toolbar']//a[3]")

        # Quotation All Store
        self.multi_stores = [By.XPATH, "//*[@role='option'and text()='MULTI STORES']"]
        self.zone_bd = (By.XPATH, "//*[text()=' Bình Dương ']")
        self.btn_use_store = (By.XPATH, "//*[@id='btnUseStore']")
        self.btn_allocate = (By.XPATH, "//*[@onclick='openAllocateQtyModal(1)']")
        self.btn_close_allocate = (By.XPATH, "//button[text()='Close']")
        self.sales_allocation_by_order = (By.XPATH, "//input[@id='allocationMethod_2']")

    def click_select_time(self):
        self.driver.find_element(*self.select_time).click()

    def click_set_time(self):
        self.driver.find_element(*self.set_time).click()

    def click_quotation_type(self):
        self.driver.find_element(*self.quotation_type).click()

    def click_type_tester(self):
        self.driver.find_element(*self.type_tester).click()

    def click_type_gift(self):
        self.driver.find_element(*self.type_gift).click()

    def click_require_vat(self):
        self.driver.find_element(*self.require_vat).click()

    def input_note(self, note):
        self.driver.find_element(*self.note).send_keys(note)

    def select_store(self):
        self.driver.find_element(*self.store).click()

    def click_product_sku(self):
        self.driver.find_element(*self.product_sku).click()

    def click_input_sku(self, sku):
        self.driver.find_element(*self.input_sku).send_keys(sku)

    def click_accept_sku(self):
        self.driver.find_element(*self.accept_sku).click()

    def click_multi_stores(self):
        self.driver.find_element(*self.multi_stores).click()

    def click_zone_bd(self):
        self.driver.find_element(*self.zone_bd).click()

    def click_btn_use_store(self):
        self.driver.find_element(*self.btn_use_store).click()

    def click_btn_allocate(self):
        self.driver.find_element(*self.btn_allocate).click()

    def click_btn_close_allocate(self):
        self.driver.find_element(*self.btn_close_allocate).click()

    def click_sales_allocation_by_order(self):
        self.driver.find_element(*self.sales_allocation_by_order).click()

    def click_btn_save(self):
        self.driver.find_element(*self.btn_save).click()

    def click_pop_ok(self):
        self.driver.find_element(*self.pup_ok).click()

    def click_btn_res_quest(self):
        self.driver.find_element(*self.btn_res_quest).click()







