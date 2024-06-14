from selenium.webdriver.common.by import By


class Menu_MC:
    def __init__(self, driver):
        self.driver = driver
        self.menu_quotation = (By.XPATH, "//*[text()='Quotation']/parent::a")
        self.create_quotation = (By.XPATH, "//*[text()='Create Quotation']/parent::a")
        self.Create_Quotation_Excel = (By.XPATH, "//*[text()='Create Quotation by Excel']/parent::a")
        self.menu_product = (By.XPATH, "//*[text()='Products']/parent::a")
        self.Create_Product = (By.XPATH, "//*[text()='Add New Product']/parent::a")
        self.title_home_create_product = (By.XPATH, "//*[text()='Add New Product']")

    def get_title_home_create_product(self):
        return self.driver.find_element(*self.title_home_create_product).text

    def click_create_quotation(self):
        self.driver.find_element(*self.menu_quotation).click()
        self.driver.find_element(*self.create_quotation).click()

    def click_Create_Quotation_Excel(self):
        self.driver.find_element(*self.menu_quotation).click()
        self.driver.find_element(*self.Create_Quotation_Excel).click()

    def click_Create_Product(self):
        self.driver.find_element(*self.menu_product).click()
        self.driver.find_element(*self.Create_Product).click()
