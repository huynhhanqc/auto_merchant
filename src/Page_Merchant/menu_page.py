from selenium.webdriver.common.by import By


class Menu_MC:
    def __init__(self, driver):
        self.driver = driver
        self.menu_quotation = (By.XPATH, "//*[text()='Quotation']/parent::a")
        self.create_quotation = (By.XPATH, "//*[text()='Create Quotation']/parent::a")
        self.Create_Quotation_Excel = (By.XPATH, "//*[text()='Create Quotation by Excel']/parent::a")

    def click_menu_quotation(self):
        self.driver.find_element(*self.menu_quotation).click()

    def click_create_quotation(self):
        self.driver.find_element(*self.create_quotation).click()

    def click_Create_Quotation_Excel(self):
        self.driver.find_element(*self.Create_Quotation_Excel).click()
