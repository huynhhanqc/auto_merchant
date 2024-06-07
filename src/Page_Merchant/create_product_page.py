from faker import Faker
from selenium.webdriver.common.by import By

class CreateProduct:
    def __init__(self, driver):
        self.driver = driver
        # Tab Product Info
        self.name_product = (By.ID, "name")
        self.vendor_product = (By.ID, "venprod_name")
        self.bar_code = (By.ID, "barcode")
        self.select_brand = (By.XPATH, "//span[@role='combobox']")
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
        self.select_expiration_date_formatting = (By.XPATH, "(//*[@role='combobox'])[3]")
        self.ip_expiration_date_formatting = (By.XPATH, "(//*[@role='option' and contains(text(),'DD/MM/YY')])[2]")
        self.save_next = (By.ID, "btnSaveProductDetail")   
        # Tab Images
        self.upload_image = (By.XPATH, "//*[@id='kt_tab_pane_5']")

    # Action tab Product Info
    def enter_name_product(self):
        fake_data = Faker()
        self.driver.find_element(*self.name_product).send_keys(fake_data.name())

    def enter_vendor_product_name(self):
        fake_data = Faker()
        self.driver.find_element(*self.vendor_product).send_keys(fake_data.name())

    def enter_bar_code(self):
        fake_data = Faker()
        self.driver.find_element(*self.bar_code).send_keys(fake_data.postcode())

    def click_select_brand(self):
        self.driver.find_element(*self.select_brand).click()

    def click_input_brand(self):
        self.driver.find_element(*self.input_brand).click()

    def input_vendor_product_code(self):
        fake_data = Faker()
        self.driver.find_element(*self.vendor_product_code).send_keys(fake_data.postcode())

    def input_vender_price(self):
        fake_data = Faker()
        self.driver.find_element(*self.vender_price).send_keys(fake_data.postcode())

    def input_mar_price(self):
        fake_data = Faker()
        self.driver.find_element(*self.mar_price).send_keys(fake_data.postcode())

    def input_hasaki_price(self):
        fake_data = Faker()
        self.driver.find_element(*self.hasaki_price).send_keys(fake_data.postcode())

    def input_leng_th(self):
        self.driver.find_element(*self.leng_th).send_keys(1)

    def input_width(self):
        self.driver.find_element(*self.width).send_keys(1)

    def input_height(self):
        self.driver.find_element(*self.height).send_keys(1)

    def input_weight(self):
        self.driver.find_element(*self.weight).send_keys(1)

    def click_expiration_date_formatting(self):
        self.driver.find_element(*self.select_expiration_date_formatting).click()

    def click_ip_expiration_date_formatting(self):
        self.driver.find_element(*self.ip_expiration_date_formatting).click()

    def click_save_next(self):
        self.driver.find_element(*self.save_next).click()

    # Action Tab Images
    def click_upload_image(self):
        self.driver.find_element(*self.upload_image).click()


    def input_upload_image(self):
        self.driver.find_element(*self.upload_image).send_keys("c:/Users/HASAKI/Downloads/hinh-nen-3d-cho-may-tinh-dep_111406086.jpg")

    
    