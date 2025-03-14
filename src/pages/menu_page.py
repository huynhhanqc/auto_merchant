from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
import logging


class MenuMC(ActionElement):

    menu_quotation = (By.XPATH, "//*[text()='Quotation']/parent::a")
    create_quotation = (By.XPATH, "//*[text()='Create Quotation']/parent::a")
    Create_Quotation_Excel = (By.XPATH, "//*[text()='Create Quotation by Excel']/parent::a")
    menu_product = (By.XPATH, "//*[text()='Products']/parent::a")
    Create_Product = (By.XPATH, "//*[text()='Add New Product']/parent::a")
    title_home_create_product = (By.XPATH, "//*[text()='Add New Product']")
    menu_PgPb = (By.ID, "menu-item-promoter")
    list_PgPb_Draft = (By.ID, "indexPgDraft")

    def __init__(self, driver_):
        super().__init__(driver_)
        self.driver = driver_

    def assert_title_home_create_product(self):
        try:
            return self.element_get_text(self.title_home_create_product)
        except Exception as e:
            logging.error(f"An error occurred while getting the title: {e}")
            raise

    def click_create_quotation(self):
        try:
            self.element_click(self.menu_quotation)
            self.element_click(self.create_quotation)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'create_quotation': {e}")
            raise

    def click_Create_Quotation_Excel(self):
        try:
            self.element_click(self.menu_quotation)
            self.element_click(self.Create_Quotation_Excel)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Create_Quotation_Excel': {e}")
            raise

    def click_Create_Product(self):
        try:
            self.element_click(self.menu_product)
            self.element_click(self.Create_Product)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'Create_Product': {e}")
            raise

    def click_Menu_PgPb(self):
        try:
            self.element_click(self.menu_PgPb)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'menu_PgPb': {e}")
            raise

    def click_list_PgPb_Draft(self):
        try:
            self.element_click(self.list_PgPb_Draft)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'list_PgPb_Draft': {e}")
            raise

