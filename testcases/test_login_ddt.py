import time

import pytest

from pageObject.Login import Loginpage
from utilites import XLutils
from utilites.Readproperties import Readconfig
import openpyxl


class Test_Login_DDT:
    url = Readconfig.geturl()
    # email  = Readconfig.getemail()
    # password = Readconfig.getpassword()
    path = "C:\\Users\\mukes\\PycharmProjects\\Credance\\testcases\\TestData\\Loginnew.xlsx"

    @pytest.mark.sanity
    def test_loginddt(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Loginpage(self.driver)
        self.lp.Click_Login_Page()
        self.rows = XLutils.getrowCount(self.path,'Sheet1')
        Status_List = []
        for r in range(2,self.rows+1):
            self.email = XLutils.readData(self.path,'Sheet1',r,2)
            self.password = XLutils.readData(self.path,'Sheet1',r,3)
            self.lp.Enter_Email(self.email)
            self.lp.Enter_Password(self.password)
            self.lp.Click_Login()
            if self.lp.Login_Status()==True:
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Credance\\Screenshot\\test_login_ddt.py-pass.png")
                self.lp.Click_Menu_Button()
                self.lp.Click_Logout()
                self.lp = Loginpage(self.driver)
                self.lp.Click_Login_Page()
                Status_List.append("Pass")
                XLutils.writeData(self.path,'Sheet1' ,r ,4,"Pass")
            else:
                Status_List.append("Fail")
                XLutils.writeData(self.path,'Sheet1', r,4,"Fail")
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Credance\\Screenshot\\test_login_ddt.py-fail.png")
        print(Status_List)
        # if "Fail" not in Status_List:
        #     assert True
        # else:
        #     assert False
        # self .driver.close()







