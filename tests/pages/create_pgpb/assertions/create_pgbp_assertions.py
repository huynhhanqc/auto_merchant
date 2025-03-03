import logging
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
from selenium.webdriver.support import expected_conditions as EC
from src.pages.create_pgpb_page.add_pgpb_page import CreatePgPb


class CreatePgbpbAssertions():

    def __init__(self, driver):
        self.page = CreatePgPb(driver)

    def verify_active_status(self):
        """Kiểm tra trạng thái 'Active' trên UI."""
        status_text = self.page.get_status_text("active")
        try:
            assert status_text == "Active", f"Expected 'Active', but got '{status_text}'"
            logging.info("Verified 'Active' status successfully")
            return True
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            return False

    def verify_waiting_approve_status(self):
        """Kiểm tra trạng thái 'Waiting for Approve' trên UI."""
        status_text = self.page.get_status_text("waiting_approve")
        try:
            assert status_text == "Waiting for Approve", f"Expected 'Waiting for Approve', but got '{status_text}'"
            logging.info("Verified 'Waiting for Approve' status successfully")
            return True
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            return False

    def verify_inactive_status(self):
        """Kiểm tra trạng thái 'In-Active' trên UI."""
        status_text = self.page.get_status_text("inactive")
        try:
            assert status_text == "In-Active", f"Expected 'In-Active', but got '{status_text}'"
            logging.info("Verified 'In-Active' status successfully")
            return True
        except AssertionError as e:
            logging.error(f"Assertion error: {e}")
            return False