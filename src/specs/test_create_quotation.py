import time
from src.Page_Merchant.loginMC_page import SignInPage
from src.Page_Merchant.menu_page import Menu_MC
from src.Page_Merchant.create_quotation_page import Create_Quotation
from selenium import webdriver


def test_create_quotation():
    driver = webdriver.Chrome()
    loginMC_page = SignInPage(driver)
    menu_MC = Menu_MC(driver)
    create_quotation = Create_Quotation(driver)
    loginMC_page.login_page()
    driver.maximize_window()
    time.sleep(1)
    menu_MC.click_menu_quotation()
    time.sleep(1)
    menu_MC.click_create_quotation()
    time.sleep(1)
    create_quotation.click_quotation_type()
    create_quotation.click_type_gift()


