from src.SPECS.Script_Test_CreateProduct.Test_Create_Product_Role_Admin import TestCreateProductRoleAdmin
from src.SPECS.Script_Test_CreateProduct.Test_Create_Product_Role_Vendor import TestCreateProductRoleVendor

from src.SPECS.Script_Test_CreateQuotation.Test_create_quotation import TestCreateQuotationSigle
from src.SPECS.Script_Test_CreateQuotation.Test_create_quotation_xslx import TestCreateQuotationExcel
import unittest

TC1=unittest.TestLoader().loadTestsFromTestCase(TestCreateProductRoleAdmin)
TC2=unittest.TestLoader().loadTestsFromTestCase(TestCreateProductRoleVendor)

TC3=unittest.TestLoader().loadTestsFromTestCase(TestCreateQuotationSigle)
TC4=unittest.TestLoader().loadTestsFromTestCase(TestCreateQuotationExcel)

createproductTestCase=unittest.TestSuite([TC1, TC2]) 
quotatitonTestCase=unittest.TestSuite([TC3, TC4])

unittest.TextTestRunner().run(createproductTestCase)