import time
from src.Page_Merchant.login_page import SignInPage
from src.Page_Merchant.menu_page import Menu_MC
from src.Page_Merchant.create_product_page import CreateProduct
from selenium import webdriver

def test_create_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    login_pageMC = SignInPage(driver)
    menu_mc = Menu_MC(driver)
    create_product = CreateProduct(driver)
    login_pageMC.login_page()
    menu_mc.click_menu_product()
    time.sleep(3)
    menu_mc.click_Create_Product()
    time.sleep(1)
    create_product.enter_name_product()
    create_product.enter_vendor_product_name()
    create_product.enter_bar_code()
    time.sleep(1)
    create_product.click_select_brand()
    time.sleep(1)
    create_product.click_input_brand()
    create_product.input_vendor_product_code()
    create_product.input_vender_price()
    create_product.input_mar_price()
    create_product.input_hasaki_price()
    create_product.input_leng_th()
    create_product.input_width()
    create_product.input_height()
    create_product.input_weight()
    time.sleep(1)
    create_product.click_expiration_date_formatting()
    time.sleep(1)
    create_product.click_ip_expiration_date_formatting()
    # create_product.click_save_next()
    # # create_product.click_upload_image()
    # time.sleep(1)
    # create_product.input_upload_image()
    # time.sleep(5)


