from selenium.webdriver.common.by import By


class Create_Quotation_Excel:
    def __init__(self, driver):
        self.driver = driver
        self.Select_Type = (By.XPATH, "//*[@aria-labelledby='select2-quotationType-container']/parent::*")
        self.Type_Tester = (By.XPATH, "(//li[text()='Tester']/parent::*)[1]")
        self.Require_Vat = (By.XPATH, "//*[@id='quotationConfig']/parent::*")
        self.Note = (By.XPATH, "//*[@id='quotationNote']")
        self.Upload_Excel = (By.ID, "excelFile")
        self.Import_by_Sku = (By.XPATH, "//div[@class='import-type']//label[text()='Import by sku']")
        self.Import_by_Barcode = (By.XPATH, "//div[@class='import-type']//label[text()='Import by barcode']")
        self.Btn_Validate = (By.XPATH, "//*[text()='Validate File']/parent::*")
        self.Btn_Save_Quotation = (By.XPATH, "//*[@id='saveQuotation']")
        self.Btn_OK = (By.XPATH, "//button[text()='OK']")
        self.Btn_Request = (By.XPATH, "//*[text()='Request to confirm']")

    def click_Type_Tester(self):
        self.driver.find_element(*self.Select_Type).click()
        self.driver.find_element(*self.Type_Tester).click()

    def input_Upload_Excel_Barcode(self):
        self.driver.find_element(*self.Upload_Excel).send_keys("c:\\Users\\HASAKI\\Documents\\File_Data_Test\\File_Auto_Barcode.xlsx")

    def input_Upload_Excel_Sku(self):
        self.driver.find_element(*self.Upload_Excel).send_keys("c:\\Users\\HASAKI\\Documents\\File_Data_Test\\File_Auto_Sku.xlsx")
    
    def click_Btn_Validate(self):
        self.driver.find_element(*self.Btn_Validate).click()

    def click_Btn_Save_Quotation(self):
        self.driver.find_element(*self.Btn_Save_Quotation).click()
    
    def click_Btn_OK(self):
        self.driver.find_element(*self.Btn_OK).click()

    def click_Btn_Request(self):
        self.driver.find_element(*self.Btn_Request).click()

    def assert_text_value_price_barcode(self):
        text_price = self.driver.find_element(By.XPATH, "//*[text()='1,824,440 đ']").text
        assert text_price == "1,824,440 đ", "Passed"

    def assert_text_value_price_sku(self):
        text_price = self.driver.find_element(By.XPATH, "//*[text()='2,674,440 đ']").text
        assert text_price == "2,674,440 đ", "Passed"

    def click_Import_by_Sku(self):
        self.driver.find_element(*self.Import_by_Sku).click()
    


