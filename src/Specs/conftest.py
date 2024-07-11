from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setUp_and_teaDown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield 
    driver.quit()

# def setUp(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--window-size=1920,1080")
#         options.add_argument("--disable-extensions")
#         options.add_argument("--proxy-server='direct://'")
#         options.add_argument("--proxy-bypass-list=*")
#         options.add_argument("--start-maximized")
#         options.add_argument('--headless')
#         options.add_argument('--disable-gpu')
#         options.add_argument('--disable-dev-shm-usage')
#         options.add_argument('--no-sandbox')
#         options.add_argument('--ignore-certificate-errors')
#         self.driver = webdriver.Chrome(options=options)