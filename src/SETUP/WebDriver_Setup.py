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
            self.driver.close()
            self.driver.quit()