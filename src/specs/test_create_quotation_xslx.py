import time
from src.Page_Merchant.loginMC_page import SignInPage
from src.Page_Merchant.menu_page import Menu_MC
from src.Page_Merchant.quotation_xslx_page import Create_Quotation_Excel
from selenium import webdriver


def test_create_quotation_xlsx():
    driver = webdriver.Chrome()
    loginMC_page = SignInPage(driver)
    menu_MC = Menu_MC(driver)
    Quotation_Excel = Create_Quotation_Excel(driver)
    loginMC_page.open_page("https://test-merchant.hasaki.vn/login")
    driver.maximize_window()
    loginMC_page.enter_username("truonghan1506")
    loginMC_page.enter_password("150699")
    loginMC_page.click_login()
    time.sleep(1)
    menu_MC.click_menu_quotation()
    time.sleep(1)
    menu_MC.click_Create_Quotation_Excel()
    Quotation_Excel.click_Select_Type()
    Quotation_Excel.click_Type_Tester()
    time.sleep(1)









