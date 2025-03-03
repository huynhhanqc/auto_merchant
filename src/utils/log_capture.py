from datetime import datetime
import os
import time
import logging
from PIL import Image


def log_capture_full(driver, test_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True) 
    temp_dir = os.path.join(screenshot_dir, "temp")
    os.makedirs(temp_dir, exist_ok=True)
    try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        viewport_height = driver.execute_script("return window.innerHeight")
        scroll_pos = 0
        screenshots = []
        while scroll_pos < total_height:
            driver.execute_script(f"window.scrollTo(0, {scroll_pos});")
            time.sleep(0.5) 
            temp_filename = os.path.join(temp_dir, f"part_{scroll_pos}.png")
            driver.save_screenshot(temp_filename)
            screenshots.append(Image.open(temp_filename))
            scroll_pos += viewport_height
        if screenshots:
            widths, heights = zip(*(img.size for img in screenshots))
            total_height = sum(heights)
            max_width = max(widths)
            full_screenshot = Image.new('RGB', (max_width, total_height))
            y_offset = 0
            for img in screenshots:
                full_screenshot.paste(img, (0, y_offset))
                y_offset += img.size[1]
            filename = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
            full_screenshot.save(filename, 'PNG')
            logging.info(f"📸 Đã chụp toàn bộ trang lỗi: {filename}")
            for temp_file in os.listdir(temp_dir):
                os.remove(os.path.join(temp_dir, temp_file))
            os.rmdir(temp_dir)
    except Exception as e:
        logging.error(f"Failed to take full page screenshot: {e}")
        raise

def log_capture(driver, test_name):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  
    filename = f"ScreenShort/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename) 
    logging.info(f"📸 Đã chụp ảnh lỗi: {filename}")