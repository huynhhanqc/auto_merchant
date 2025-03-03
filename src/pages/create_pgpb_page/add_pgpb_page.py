import logging
import os
import re
from faker import Faker
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
import random
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class CreatePgPb (ActionElement): 

    url_Create_Pg = "https://test-merchant.hasaki.vn/promoter/pg-draft/create"
    select_Vendor = (By.ID, "select2-vendor_id-container")
    options_Vendor = (By.XPATH, "//*[@role='option' and contains(text(),'V190064 - Thương Mại Song Hằng')]")
    btn_btnAddPromoter = (By.ID, "btnAddPromoter")
    select_Brand = (By.XPATH, "//span[@class='select2-selection select2-selection--multiple form-select form-select-solid discount-condition-brand']")
    options_Brand = (By.XPATH, "//ul[@id='select2-brand_id-results']/li")
    select_Work_Type = (By.ID, "work_type")
    options_Work_Type_Not_Line = (By.XPATH, "//select[@id='work_type']/option")
    option_Inline = (By.XPATH, "//option[@value='inline']")
    full_name = (By.ID, "name")
    personal_Email = (By.ID, "personal_email")
    id_Number = (By.ID, "cmnd")
    phone = (By.ID, "phone")   
    select_City = (By.XPATH, "//*[@aria-describedby='select2-zone_code-container']") 
    options_City = (By.XPATH, "//span[@class='select2-results']")
    select_Location = (By.XPATH, "(//span[@class='select2-selection select2-selection--multiple form-select form-select-solid']/parent::span)[2]")
    options_Location = (By.XPATH, "//ul[@id='select2-loc_id-results']/li")
    note = (By.ID, "note")
    image_Avatar = (By.XPATH, "//input[@name='avatar']")
    image_front_side_cmnd = (By.XPATH, "//input[@name='front_side_cmnd']")
    image_back_side_cmnd = (By.XPATH, "//input[@name='back_side_cmnd']")
    btn_Save = (By.XPATH, "//button[normalize-space()='Save']")
    btn_Request_to_Active = (By.XPATH, "//button[normalize-space()='Request to active']")
    btn_Yes_Request_to_Active = (By.XPATH, "//button[normalize-space()='Yes']")
    btn_Approve = (By.XPATH, "//button[normalize-space()='Approve']")
    btn_Accept_Approved = (By.XPATH, "//button[@type='button'][normalize-space()='Approve']")
    avatar_preview_xpath = (By.XPATH, "//div[@id='avatar']//div[@class='image-input-wrapper w-125px h-125px']")
    fontside_preview_xpath = (By.XPATH, "//div[@id='front_side']//div[@class='image-input-wrapper w-125px h-125px']")
    backside_preview_xpath = (By.XPATH, "//div[@id='back_side']//div[@class='image-input-wrapper w-125px h-125px']")
    text_status_Inactive = (By.XPATH, "//*[@class='badge badge-secondary' and contains(text(), 'In-Active')]")
    text_status_Waiting_Approve = (By.XPATH, "//*[@class='badge badge-warning' and contains(text(), 'Waiting for Approve')]")
    text_status_Active = (By.XPATH, "//*[@class='badge badge-success' and contains(text(), 'Active')]")
    text_staff_id = (By.ID, "staff_id")
    text_id_Number = (By.ID, "cmnd")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_url(self):
        try:
            self.driver.get(self.url_Create_Pg)
        except Exception as e:
            logging.error(f"An error occurred while navigating to the URL: {e}")
            raise

    def click_btnAddPromoter(self):
        try:
            self.element_click(self.btn_btnAddPromoter)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_btnAddPromoter': {e}")
            raise

    def click_select_Vendor (self):
        try:
            self.element_click(self.select_Vendor)
            self.element_click(self.options_Vendor)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'select_Vendor': {e}")
            raise

    def click_select_Brand(self, min_options=1, max_options=3):
        selected_options = []
        for _ in range(max_options):
            try:
                self.element_click(self.select_Brand)
                options = self.get_options(self.options_Brand)
                available_options = [option for option in options if option.text not in selected_options]
                if len(available_options) >= min_options:
                    option = random.choice(available_options)
                    option.click()
                    selected_options.append(option.text)
                else:
                    break
            except StaleElementReferenceException:
                logging.error("StaleElementReferenceException occurred. Retrying...")
                continue

    def click_select_Work_Type_Inline(self):
        try:
            self.element_click(self.select_Work_Type)
            self.element_click(self.option_Inline)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'select_Work_Type_Inline': {e}")
            raise

    def click_select_Work_Type_Not_Line(self):
        try:
            self.element_click(self.select_Work_Type)
            options = self.get_options(self.options_Work_Type_Not_Line)
            options_to_exclude_by_value = ["Select Type", "inline"]
            available_options = [option for option in options if option.text not in options_to_exclude_by_value]
            if len(available_options) >= 6:
                selected_options = random.sample(available_options, 6)
                for option in selected_options:
                    option.click()
            else:
                logging.error("Not enough options to select 6 after excluding the specified options.")
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'select_Work_Type_Not_Line': {e}")
            raise

    def send_keys_full_name(self):
        fake = Faker ()
        try:
            name = fake.name()
            self.element_send_keys(self.full_name, name)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'full_name': {e}")
            raise

    def send_keys_personal_Email(self):
        fake = Faker ()
        try:
            email = fake.email()
            self.element_send_keys(self.personal_Email, email)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'personal_Email': {e}")
            raise

    def send_keys_id_Number(self):
        try:
            id_number = ''.join(str(random.randint(0, 9)) for _ in range(12))
            self.element_send_keys(self.id_Number, id_number)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'id_Number': {e}")
            raise

    def send_keys_phone(self):
        try:
            prefixes = ['09', '08', '07', '05', '03']
            prefix = random.choice(prefixes)
            random_number = ''.join(str(random.randint(0, 9)) for _ in range(8))
            phone_number = f"{prefix}{random_number}"
            self.element_send_keys(self.phone, phone_number)
        except Exception as e:
            logging.error(f"An error occurred while sending keys to 'phone': {e}")
            raise

    def click_select_City(self):
        self.element_click(self.select_City)
        options = self.get_options(self.options_City)
        random_option = random.choice(options)
        random_option.click()

    def click_select_Location(self, min_options=2, max_options=3):
        selected_options = []
        for _ in range(max_options):
            try:
                self.element_click(self.select_Location)
                options = self.get_options(self.options_Location)
                available_options = [option for option in options if option.text not in selected_options]
                if len(available_options) >= min_options:
                    option = random.choice(available_options)
                    option.click()
                    selected_options.append(option.text)
                else:
                    break
            except StaleElementReferenceException:
                logging.error("StaleElementReferenceException occurred. Retrying...")
                continue

    def send_keys_note(self, text):
        self.element_send_keys(self.note, text)

    def is_image_loaded(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            style = element.get_attribute("style")
            if not style:
                return False
            background_image_match = re.search(r'url\("([^"]+)"\)', style)
            if background_image_match:
                image_url = background_image_match.group(1)
                logging.info(f"Found image URL in background-image: {image_url}")
                return bool(image_url and "test-merchant.hasaki.vn" in image_url)  
            return False
        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"Image not loaded for locator {locator}: {e}")
            return False

    def send_keys_image_Avatar(self):
        image_directory = "/Users/mac/AvatarPG"
        try:
            image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
            if image_files:
                selected_image = random.choice(image_files)
                image_path = os.path.join(image_directory, selected_image)
                self.element_send_keys_path(self.image_Avatar, image_path)
                sleep(2)
            if self.is_image_loaded(self.avatar_preview_xpath):
                style = self.find_element(*self.avatar_preview_xpath).get_attribute("style")
                background_image_match = re.search(r'url\("([^"]+)"\)', style)
                if background_image_match:
                    image_url = background_image_match.group(1)
                    logging.info(f"Verified avatar loaded with URL: {image_url}")
                    assert "test-merchant.hasaki.vn" in image_url, "Avatar URL does not match expected domain"
                logging.info("Avatar successfully uploaded and loaded.")
                return True
            else:
                raise Exception("Avatar upload failed: Image not loaded correctly.")
        except Exception as e:
            logging.error(f"Lỗi trong quá trình tải ảnh lên: {e}")

    def send_keys_image_front_side_cmnd(self):
        try:
            self.element_send_keys_path(self.image_front_side_cmnd, "/Users/mac/CccdPG/3_1733110493_bb8cef1271ce54dac7ea11a6eb8d0b92.jpeg")
            sleep(1)
            if not self.is_image_loaded(self.fontside_preview_xpath):
                raise Exception("Image ID Number Font Side không được tải lên thành công.")
        except Exception as e:
            logging.error(f"Lỗi trong quá trình tải ảnh lên: {e}")

    def send_keys_image_back_side_cmnd(self):
        try:
            self.element_send_keys_path(self.image_back_side_cmnd, "/Users/mac/CccdPG/3_1733110493_bb8cef1271ce54dac7ea11a6eb8d0b92.jpeg")
            sleep(1)
            if not self.is_image_loaded(self.backside_preview_xpath):
                raise Exception("Image ID Number Font Side không được tải lên thành công.")
        except Exception as e:
            logging.error(f"Lỗi trong quá trình tải ảnh lên: {e}")

    def click_btn_Save(self):
        try:
            self.element_click(self.btn_Save)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_Save': {e}")
            raise

    def click_btn_Request_to_Active(self):
        try:
            self.element_click(self.btn_Request_to_Active)
            sleep(1)
            self.element_click(self.btn_Yes_Request_to_Active)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_Request_to_Active': {e}")
            raise

    def click_btn_Approve(self):
        try:
            self.element_click(self.btn_Approve)
            sleep(1)
            self.element_click(self.btn_Accept_Approved)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_Approve': {e}")
            raise 

    def is_text_present(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return False

    def get_staff_id(self):
        try:
            text_id = self.element_get_attribute(self.text_staff_id, "value")
            print(f"\nStaff ID : {text_id}")
        except Exception as e:
            logging.error(f"An error occurred while getting staff_id: {e}")
            return None

    def get_id_number(self):
        try:
            id_number = self.element_get_attribute(self.text_id_Number, "value") 
            print(f"\nID Number : {id_number}")
        except Exception as e:
            logging.error(f"An error occurred while getting id_number: {e}")
            return None
        
    def get_status_text(self, status_type):
        locators = {
            "inactive": self.text_status_Inactive,
            "waiting_approve": self.text_status_Waiting_Approve,
            "active": self.text_status_Active
        }
        locator = locators.get(status_type.lower(), None)
        if locator:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )
                return element.text
            except (NoSuchElementException, TimeoutException) as e:
                logging.error(f"Failed to get status text for {status_type}: {e}")
                return None
        return None

    
    


        