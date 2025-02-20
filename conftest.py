from selenium import webdriver
import pytest
from datetime import datetime


@pytest.fixture(scope="class")
def setup_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver 
    yield driver 
    driver.quit()

@pytest.fixture(scope="class")
def chrome_driver_headless(request):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--ignore-certificate-errors')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        request.cls.driver = driver
        yield driver 
        driver.quit()

# Fixture cho Firefox
@pytest.fixture(scope="class")
def firefox_driver_headless(request):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--kiosk")  
    options.add_argument("--disable-gpu") 
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Firefox(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

# Fixture cho Edge
@pytest.fixture(scope="class")
def edge_driver_headless(request):
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")  
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--ignore-certificate-errors") 
    options.use_chromium = True 
    driver = webdriver.Edge(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

#Config report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"reporthtml/report_{timestamp}.html"
    config.option.htmlpath = report_path


