from selenium.webdriver.common.by import By
from src.PAGE.Utils.Common import ActionElement


class Menu_MC(ActionElement):

    menu_quotation = (By.XPATH, "//*[text()='Quotation']/parent::a")
    create_quotation = (By.XPATH, "//*[text()='Create Quotation']/parent::a")
    Create_Quotation_Excel = (By.XPATH, "//*[text()='Create Quotation by Excel']/parent::a")
    menu_product = (By.XPATH, "//*[text()='Products']/parent::a")
    Create_Product = (By.XPATH, "//*[text()='Add New Product']/parent::a")
    title_home_create_product = (By.XPATH, "//*[text()='Add New Product']")

    def __init__(self, driver_):
        super().__init__(driver_)
        self.driver = driver_

    def assert_title_home_create_product(self):
        return self.element_get_text(self.title_home_create_product)

    def click_create_quotation(self):
        self.element_click(self.menu_quotation)
        self.element_click(self.create_quotation)

    def click_Create_Quotation_Excel(self):
        self.element_click(self.menu_quotation)
        self.element_click(self.Create_Quotation_Excel)

    def click_Create_Product(self):
        self.element_click(self.menu_product)
        self.element_click(self.Create_Product)
