from time import sleep
import unittest
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateQuotation_Page.create_quotation_page import Create_Quotation
from src.SETUP.WebDriver_Setup import WebDriverSetup


class TestCreateQuotationSigle(WebDriverSetup):
    def test_create_quotation(self):
        driver = self.driver
        loginMC_page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        create_quotation = Create_Quotation(driver)
        loginMC_page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_create_quotation()
        sleep(1)
        create_quotation.click_type_gift()
        create_quotation.click_select_store_multi()
        sleep(2)
        create_quotation.click_zone_bd()
        create_quotation.click_btn_use_store()
        create_quotation.click_product_sku()
        create_quotation.send_keys_sku(100190112)
        sleep(1)
        create_quotation.click_accept_sku()
        create_quotation.click_btn_save()
        sleep(1)
        create_quotation.click_pop_ok()
        sleep(1)
        create_quotation.click_btn_res_quest()
        driver.switch_to.alert.accept()
        assert create_quotation.assert_text_status() == "Waiting For Confirm\nM"

    def test_create_quotation_type_normal_multi(self):
        driver = self.driver
        loginMC_page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        create_quotation = Create_Quotation(driver)
        loginMC_page.login_role_vendor("truonghan1506", "150699")
        sleep(1)
        menu_MC.click_create_quotation()
        sleep(1)
        create_quotation.click_select_store_multi()
        sleep(1)
        create_quotation.click_check_box_all_stores()
        create_quotation.click_btn_use_store()
        create_quotation.click_product_sku()
        create_quotation.send_keys_sku(100190112)
        sleep(1)
        create_quotation.click_accept_sku()
        create_quotation.click_btn_save()
        sleep(1)
        create_quotation.click_pop_ok()
        sleep(1)
        create_quotation.click_btn_res_quest()
        driver.switch_to.alert.accept()
        sleep(1)
        assert create_quotation.assert_text_status() == "Waiting For Confirm\nM"
        sleep(1)
        assert create_quotation.assert_text_mutil_store() == "Multi Store(64 STORES)"
    










