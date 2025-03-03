import logging
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
import random
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

from src.utils.log_capture import log_capture


class CreateWorkSchedule(ActionElement):

    url_create_work_schedule = "https://test-merchant.hasaki.vn/promoter/work-schedule/create"
    select_Vendor = (By.ID, "select2-vendor_id-container")
    options_Vendor = (By.XPATH, "//*[@role='option' and contains(text(),'V190064 - Thương Mại Song Hằng')]")
    work_type = (By.XPATH, "//input[@id='workType']")
    select_pgpb = (By.ID, "select2-staff_id-container")
    options_pgpb = (By.XPATH, "//ul[@id='select2-staff_id-results']/li")
    date_picker_trigger = (By.XPATH, "//input[contains(@class, 'form-control') and contains(@class, 'form-control input') and @type='text' and @placeholder='Working Date']")
    calendar_container = (By.CLASS_NAME, "flatpickr-calendar")
    day_element = (By.XPATH, "//span[contains(@class, 'flatpickr-day ')]")  
    next_month_button = (By.XPATH, "//span[@class='flatpickr-next-month']")
    select_shift = (By.ID, "select2-shift_id-container")
    options_shift = (By.XPATH, "//ul[@id='select2-shift_id-results']/li")
    option_hc32 = (By.XPATH, "(//*[contains(text(),'HC 32 (PG - 09:00:00-22:00:00)')])[2]")
    btn_save = (By.XPATH, "//button[@class='btn btn-primary btn-sm ml-2 btnSaveWorkSchedule']")
    #Detail Schedule Inline Time In/Out
    select_store_32 = (By.XPATH, "//span[@id='select2-inlineMultiLocation_1-container']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_url(self):
        try:
            self.driver.get(self.url_create_work_schedule)
        except Exception as e:
            logging.error(f"An error occurred while navigating to the URL: {e}")
            raise

    def click_select_Vendor(self):
        try:
            self.element_click(self.select_Vendor)
            self.element_click(self.options_Vendor)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'select_Vendor': {e}")
            raise
    
    def click_work_type(self):
        try:
            self.element_click(self.work_type)
            sleep(2)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'work_type': {e}")
            raise

    def click_select_pgpb(self):
        try:
            self.element_click(self.select_pgpb)
            sleep(1)
            options = self.get_options(self.options_pgpb)
            available_options = [
                option for option in options 
                if option.text.strip() and option.text.strip() != "Select PG/PB"
            ]
            if not available_options:
                raise ValueError("No valid options available after excluding 'Select PG/PB'")
            option = random.choice(available_options)
            self.element_click(option)
            sleep(1)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'select_pgpb': {e}")
            raise

    def click_working_date(self):
        try:
            self.element_click(self.date_picker_trigger)
            days = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.day_element)
            )
            nearest_day = None
            for day in days:
                classes = day.get_attribute("class").split()
                if ("flatpickr-disabled" not in classes and "prevMonthDay" not in classes and "selected" not in classes):
                    day_text = day.text.strip()
                    if day_text and day_text.isdigit():  
                        nearest_day = day
                        break  
            if nearest_day is None:
                raise ValueError("No selectable date found in the calendar")
            self.element_click((By.XPATH, f"//span[@class='{nearest_day.get_attribute('class')}'][text()='{nearest_day.text.strip()}']"))
            sleep(1)
            return True
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'working_date': {e}")
            raise

    def click_select_random_shift(self):
        try:
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    self.element_click(self.select_shift)
                    break
                except StaleElementReferenceException as e:
                    if attempt < max_attempts - 1:
                        logging.warning(f"Attempt {attempt + 1} failed to click select_shift, retrying... Error: {e}")
                        sleep(1)  
                        continue
                    logging.error(f"Failed to click select_shift after {max_attempts} attempts: {e}")
                    raise
            options = self.get_options(self.options_shift)
            options_to_exclude_by_value = ["HC 32 (PG - 09:00:00-22:00:00)"]
            available_options = [option for option in options if option.text.strip() not in options_to_exclude_by_value]
            self.element_click(random.choice(available_options))
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'select_shift': {e}")
            raise

    def click_option_hc32(self):
        try:
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    self.element_click(self.select_shift)
                    break
                except StaleElementReferenceException as e:
                    if attempt < max_attempts - 1:
                        logging.warning(f"Attempt {attempt + 1} failed to click select_shift, retrying... Error: {e}")
                        sleep(1)  
                        continue
                    logging.error(f"Failed to click select_shift after {max_attempts} attempts: {e}")
                    raise
            options = self.find_element(self.option_hc32)
            ActionChains(self.driver).move_to_element(options).click().perform()
        except Exception as e:
            logging.error(f"Unexpected error while selecting option 'HC 32': {e}")
            raise

    def click_btn_save(self):
        try:
            self.element_click(self.btn_save)
        except Exception as e:
            logging.error(f"An error occurred while clicking the 'btn_save': {e}")
            raise
    