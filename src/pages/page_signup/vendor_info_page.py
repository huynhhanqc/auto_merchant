import logging
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
from faker import Faker
from time import sleep

class VendorInfo(ActionElement):
    contact_name = (By.ID, "contact_name")
    company_name = (By.ID, "company_name")
    registration_number = (By.ID, "registration_number")
    address = (By.ID, "address")
    vendor_description = (By.ID, "description")
    btn_continue = (By.XPATH, "//button[normalize-space()='Tiếp tục']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_contact_name(self):
        fake = Faker()
        try:
            contact_name = fake.name()
            self.element_send_keys(self.contact_name, contact_name)
        except Exception as e:
            logging.error(f"An error occurred while entering the contact name: {e}")
            raise

    def input_company_name(self):
        fake = Faker()
        try:
            company_name = fake.name_male()
            self.element_send_keys(self.company_name, company_name)
        except Exception as e:
            logging.error(f"An error occurred while entering the company name: {e}")
            raise

    def input_registration_number(self):
        fake = Faker()
        try:
            registration_number = fake.random_number(digits=10)
            self.element_send_keys(self.registration_number, registration_number)
        except Exception as e:
            logging.error(f"An error occurred while entering the registration number: {e}")
            raise

    def input_address(self):
        fake = Faker()
        try:
            address = fake.address()
            self.element_send_keys(self.address, address)
        except Exception as e:
            logging.error(f"An error occurred while entering the address: {e}")
            raise

    def input_vendor_description(self):
        fake = Faker()  
        try:
            vendor_description = fake.text(max_nb_chars=150)
            self.element_send_keys(self.vendor_description, vendor_description)
        except Exception as e:
            logging.error(f"An error occurred while entering the vendor description: {e}")
            raise

    def click_btn_continue(self):
        try:
            self.element_click(self.btn_continue)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the continue button: {e}")
            raise
