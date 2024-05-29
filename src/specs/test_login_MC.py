import time
from src.Page_Merchant.loginMC_page import SignInPage
from selenium import webdriver


def test_create_quotation():
    print("hello Nhi nhung nhay")
    driver = webdriver.Chrome()
    loginMC_page = SignInPage(driver)
    loginMC_page.open_page("https://test-merchant.hasaki.vn/login")
    driver.maximize_window()
    loginMC_page.enter_username("truonghan1506")
    loginMC_page.enter_password("150699")
    loginMC_page.click_login()
    time.sleep(1)


