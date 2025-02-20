import time
import logging

def log_capture(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  
    filename = f"ScreenShort/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename) 
    logging.info(f"📸 Đã chụp ảnh lỗi: {filename}")