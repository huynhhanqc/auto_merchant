import unittest
from selenium import webdriver


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.implicitly_wait(10)
        driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            self.driver.quit()

    # def setUp(self):
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("--window-size=1920,1080")
    #     options.add_argument("--disable-extensions")
    #     options.add_argument("--proxy-server='direct://'")
    #     options.add_argument("--proxy-bypass-list=*")
    #     options.add_argument("--start-maximized")
    #     options.add_argument('--headless')
    #     options.add_argument('--disable-gpu')
    #     options.add_argument('--disable-dev-shm-usage')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--ignore-certificate-errors')
    #     self.driver = webdriver.Chrome(options=options)
        


