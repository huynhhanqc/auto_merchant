from time import sleep
from faker import Faker
from src.SETUP.WebDriver_Setup import WebDriverSetup
from src.PAGE.Login_Page import LogInPage
from src.PAGE.Menu_Page import Menu_MC
from src.PAGE.CreateProduct_Page.New_Product_Tab_Info_Page import Tab_InFo
from src.PAGE.CreateProduct_Page.New_Product_Tab_Image_Page import Tab_Image
from src.PAGE.CreateProduct_Page.New_Product_Tab_Document_Page import Tab_Document

class TestCreateProduct(WebDriverSetup):
    def test_create_product_role_vendor_Success(self):
        fake = Faker()
        driver = self.driver
        login_Page = LogInPage(driver)
        menu_mc = Menu_MC(driver)
        tab_info = Tab_InFo(driver)
        tab_image = Tab_Image(driver)
        tab_document = Tab_Document(driver)
        login_Page.login_role_vendor("truonghan1506","150699")
        sleep(2)
        menu_mc.click_Create_Product()   
        assert menu_mc.get_title_home_create_product() == "Add New Product"
        sleep(1)
        tab_info.enter_name_product(fake.text())
        tab_info.enter_vendor_product_name(fake.text())
        tab_info.enter_bar_code(fake.postcode())
        tab_info.click_select_brand()
        sleep(1)
        tab_info.click_input_brand()
        tab_info.input_vendor_product_code(fake.postcode())
        tab_info.input_vender_price(fake.postcode())
        tab_info.input_mar_price(fake.postcode())
        tab_info.input_hasaki_price(fake.postcode())
        tab_info.input_leng_th()
        tab_info.input_width()
        tab_info.input_height()
        tab_info.input_weight()
        tab_info.click_expiration_date_formatting_vendor()
        sleep(1)
        tab_info.click_ip_expiration_date_formatting()
        tab_info.click_save_next()
        driver.implicitly_wait(2)
        tab_image.input_upload_image()
        sleep(2)
        tab_image.click_save_next_image()
        tab_document.select_Announcement_Date()
        tab_document.click_accept_date()
        tab_document.input_Announcement_Code()
        tab_document.input_Announcement_Document()
        sleep(2)
        tab_document.click_save_next_document()
        tab_document.click_Btn_request_approve()
        sleep(1)
        driver.switch_to.alert.accept()
        sleep(2)
        assert tab_info.get_text_status_product_success() == "Waiting Approve"



