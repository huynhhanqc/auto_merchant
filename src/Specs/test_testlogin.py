from src.PAGE.Utils import ReadFile
from selenium import webdriver
import pytest

@pytest.mark.skip(reason="nor reason")
def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
