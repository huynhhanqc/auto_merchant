from src.SPECS.Script_CreateProduct.Test_Role_Admin import TestCreateProductRoleAdmin
from src.SPECS.Script_CreateProduct.Test_Role_Vendor import TestCreateProductRoleVendor

from src.SPECS.Script_CreateQuotation.Test_Muilti import TestCreateQuotationSigle
from src.SPECS.Script_CreateQuotation.Test_Excel import TestCreateQuotationExcel
import unittest

TC1=unittest.TestLoader().loadTestsFromTestCase(TestCreateProductRoleAdmin)
TC2=unittest.TestLoader().loadTestsFromTestCase(TestCreateProductRoleVendor)

TC3=unittest.TestLoader().loadTestsFromTestCase(TestCreateQuotationSigle)
TC4=unittest.TestLoader().loadTestsFromTestCase(TestCreateQuotationExcel)

createproductTestCase=unittest.TestSuite([TC1, TC2]) 
quotatitonTestCase=unittest.TestSuite([TC3, TC4])
alltests=unittest.TestSuite([TC1,TC2,TC3,TC4])

unittest.TextTestRunner().run(alltests)