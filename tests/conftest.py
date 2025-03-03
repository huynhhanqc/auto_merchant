import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from datetime import datetime


@pytest.fixture(scope="class")
def setup_teardown(request):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--disable-extensions')  
        chrome_options.add_argument('--ignore-certificate-errors')  
        chrome_options.add_argument('--window-size=1920,1080')  
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
        driver.implicitly_wait(10)  
        request.cls.driver = driver
        logging.info("Chrome driver initialized successfully in normal mode")
        yield driver  
    except WebDriverException as e:
        logging.error(f"Failed to initialize Chrome driver: {e}")
        raise
    finally:
        try:
            driver.quit()
            logging.info("Chrome driver closed successfully")
        except Exception as e:
            logging.warning(f"Error closing Chrome driver: {e}")
    driver.quit()

@pytest.fixture(scope="class")
def chrome_driver_headless(request):
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless=new')  
            chrome_options.add_argument('--window-size=1920,1080') 
            chrome_options.add_argument('--no-sandbox') 
            chrome_options.add_argument('--disable-dev-shm-usage')  
            chrome_options.add_argument('--ignore-certificate-errors')  
            service = Service(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(
                service=service,
                options=chrome_options
            )
            driver.implicitly_wait(10) 
            request.cls.driver = driver
            yield driver 
        except WebDriverException as e:
            logging.error(f"Failed to initialize Chrome driver: {e}")
            raise
        finally:
            try:
                driver.quit()
                logging.info("Chrome driver closed successfully")
            except Exception as e:
                logging.warning(f"Error closing Chrome driver: {e}")
        driver.quit()

# Fixture cho Firefox
@pytest.fixture(scope="class")
def firefox_driver_headless(request):
    try:
        firefox_options = Options()
        firefox_options.add_argument('--headless') 
        firefox_options.add_argument('--width=1920') 
        firefox_options.add_argument('--height=1080') 
        firefox_options.add_argument('--no-sandbox') 
        firefox_options.add_argument('--disable-dev-shm-usage')  
        firefox_options.add_argument('--ignore-certificate-errors')  
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(
            service=service,
            options=firefox_options
        )
        driver.implicitly_wait(10)  
        yield driver
    except WebDriverException as e:
        logging.error(f"Failed to initialize Firefox driver: {e}")
        raise
    finally:
        try:
            driver.quit()
            logging.info("Firefox driver closed successfully")
        except Exception as e:
            logging.warning(f"Error closing Firefox driver: {e}")
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
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        report_dir = "reporthtml"
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)  
        report_path = os.path.join(report_dir, f"report_{timestamp}.html")
        config.option.htmlpath = report_path
        logger = logging.getLogger(__name__)
        logger.info(f"Configured HTML report path: {report_path}")
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to configure HTML report: {e}")
        raise

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart():
    if os.path.exists("pytest.log"):
        os.remove("pytest.log")


