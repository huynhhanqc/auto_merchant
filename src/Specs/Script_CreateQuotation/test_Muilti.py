from time import sleep
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateQuotation_Page.Muilti_page import Quotation_Muilti
from src.SPECS.BaseTest import BaseFixture


class TestCreateQuotationSigle(BaseFixture):
    def test_create_quotation(self):
        driver = self.driver
        loginMC_page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        muilti = Quotation_Muilti(driver)
        loginMC_page.login_role_vendor("truonghan1506","150699")
        sleep(1)
        menu_MC.click_create_quotation()
        sleep(1)
        muilti.click_type_gift()
        muilti.click_select_store_multi()
        sleep(2)
        muilti.click_zone_bd()
        muilti.click_btn_use_store()
        muilti.click_product_sku()
        muilti.send_keys_sku(100190112)
        sleep(1)
        muilti.click_accept_sku()
        muilti.click_btn_save()
        sleep(1)
        muilti.click_pop_ok()
        sleep(1)
        # muilti.click_btn_res_quest()
        # driver.switch_to.alert.accept()
        # assert muilti.assert_text_status() == "Waiting For Confirm\nM"

    def test_create_quotation_type_normal_multi(self):
        driver = self.driver
        loginMC_page = LogInPage(driver)
        menu_MC = Menu_MC(driver)
        muilti = Quotation_Muilti(driver)
        loginMC_page.login_role_vendor("truonghan1506", "150699")
        sleep(1)
        menu_MC.click_create_quotation()
        sleep(1)
        muilti.click_select_store_multi()
        sleep(1)
        muilti.click_check_box_all_stores()
        muilti.click_btn_use_store()
        muilti.click_product_sku()
        muilti.send_keys_sku(100190112)
        sleep(1)
        muilti.click_accept_sku()
        muilti.click_btn_save()
        sleep(1)
        muilti.click_pop_ok()
        sleep(1)
        # muilti.click_btn_res_quest()
        # driver.switch_to.alert.accept()
        # sleep(1)
        # assert muilti.assert_text_status() == "Waiting For Confirm\nM"
        # sleep(1)
        # assert muilti.assert_text_mutil_store() == "Multi Store(64 STORES)"
    










