import logging
import os
from time import sleep
from selenium.webdriver.common.by import By
from src.utils.common import ActionElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



class VendorCerTiFiCate(ActionElement):

    dropzone_area = (By.CLASS_NAME, "dz-message.needsclick")  # Khu vực hiển thị để nhấp
    file_input = (By.CSS_SELECTOR, "input.dz-hidden-input[type='file']")
    btn_summit = (By.XPATH, "//span[@class='indicator-label']")
    text_success = (By.XPATH, "//h2[contains(text(),'Bạn đã hoàn tất đăng ký')]")
    text_error = (By.XPATH, "//div[@id='swal2-html-container' and text()='Xin lỗi, có vẻ như có một số lỗi được phát hiện, vui lòng thử lại.']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _upload_file_to_dropzone(self, dropzone_id, file_path):
        """Hàm phụ nội bộ để xử lý tải lên file cho một dropzone cụ thể"""
        try:
            wait = WebDriverWait(self.driver, 10)
            dropzone_container = wait.until(
                EC.presence_of_element_located((By.ID, dropzone_id)),
                message=f"Khu vực dropzone với ID {dropzone_id} không tìm thấy"
            )
            dropzone_element = dropzone_container.find_element(*self.dropzone_area)
            dropzone_element.click()
            file_input_element = wait.until(
                EC.presence_of_element_located(self.file_input),
                message="Phần tử input file không tìm thấy"
            )
            self.driver.execute_script(
                "arguments[0].style.visibility = 'visible'; "
                "arguments[0].style.position = 'relative'; "
                "arguments[0].style.height = '100px'; "
                "arguments[0].style.width = '200px';",
                file_input_element
            )
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Tệp không tồn tại tại: {file_path}")
            file_input_element.send_keys(file_path)
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".dz-success")),
                message=f"Tải lên file cho dropzone {dropzone_id} không thành công"
            )
            print(f"Tải lên file {file_path} cho dropzone {dropzone_id} thành công")
        except Exception as e:
            logging.error(f"Lỗi khi tải lên file cho dropzone {dropzone_id}: {e}")
            raise
    
    def upload_certificate_of_business_registration(self):
        file_path = "/Users/mac/File_Test/product_media_27340e042a50f229f3fb0bcb7f7aa0a1.pdf"  
        self._upload_file_to_dropzone("kt_dropzonejs_1", file_path)
        sleep(2)
        
    def upload_product_announcement_sheet(self):
        file_path = "/Users/mac/File_Test/168111037851370.jpg"  
        self._upload_file_to_dropzone("kt_dropzonejs_2", file_path)
        sleep(2)

    def upload_genuine_distribution_authorization(self):
        file_path = "/Users/mac/File_Test/ProductTest.xlsx" 
        self._upload_file_to_dropzone("kt_dropzonejs_3", file_path)
        sleep(2)

    def click_btn_summit(self):
        try:
            self.element_click(self.btn_summit)
            sleep(3)
        except Exception as e:
            logging.error(f"An error occurred while clicking the summit button: {e}")
            raise   

    def check_text_success(self):
        try:
            success_text = self.element_get_text(self.text_success)
            error_text = self.element_get_text(self.text_error)
            if error_text == "Xin lỗi, có vẻ như có một số lỗi được phát hiện, vui lòng thử lại.":
                assert False, f"Đã phát hiện lỗi: {error_text}"
            else :
                assert success_text == "Bạn đã hoàn tất đăng ký"
        except AssertionError as e:
            logging.error(f"Lỗi kiểm tra text: {e}")
            raise