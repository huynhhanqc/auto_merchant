import time
from src.Page_Merchant.login_page import SignInPage
from src.Page_Merchant.menu_page import Menu_MC
from src.Page_Merchant.quotation_xslx_page import Create_Quotation_Excel
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_create_quotation_xlsx():
    driver = webdriver.Chrome()
    loginMC_page = SignInPage(driver)
    menu_MC = Menu_MC(driver)
    Quotation_Excel = Create_Quotation_Excel(driver)
    loginMC_page.login_page()
    driver.maximize_window()
    time.sleep(1)
    menu_MC.click_menu_quotation()
    time.sleep(1)
    menu_MC.click_Create_Quotation_Excel()
    Quotation_Excel.click_Select_Type()
    Quotation_Excel.click_Type_Tester()
    Quotation_Excel.input_Upload_Excel("C:\\Users\\HASAKI\\Downloads\\quotation-template.xlsx")
    Quotation_Excel.click_Btn_Validate()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    Quotation_Excel.click_Btn_Save_Quotation()
    time.sleep(1)
    Quotation_Excel.click_Btn_OK()
    time.sleep(1)
    Quotation_Excel.click_Btn_Request()
    driver.switch_to.alert.accept()
    elementnumber = driver.find_element(By.XPATH, "//*[text()='1,502,220 đ']")
    actual_number = elementnumber.text
    elementTxt = driver.find_element(By.XPATH, "//*[text()='Tester']")
    actual_Txt = elementTxt.text
    expected_number = "1,502,220 đ"
    expected_Txt = "Tester"
    assert actual_number == expected_number, f"expected number: {expected_number}, Actual number: {actual_number}"
    assert actual_Txt == expected_Txt, f"expected Txt: {expected_Txt}, Actual number: {actual_Txt}"
  




    



    
