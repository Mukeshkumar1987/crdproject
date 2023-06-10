import time

import pytest

from pageObject.Login import Loginpage
from utilites.Readproperties import Readconfig


class Test_Login_Params:

    url = Readconfig.geturl()
    Email = Readconfig.getemail
    password = Readconfig.getpassword()

    @pytest.mark.sanity
    def test_login_params(self,setup,getDataforogin):
        self.driver = setup

        self.driver.get(self.url)
        self.lp = Loginpage(self.driver)
        self.lp.Click_Login_Page()
        self.lp.Enter_Email(getDataforogin[0])
        self.lp.Enter_Password(getDataforogin[1])
        self.lp.Click_Login()
        if self.lp.Login_Status() == True:
            if getDataforogin[2] == "Pass":
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Credance\\Screenshot\\test_params.py-pass.png")
                self.lp.Click_Menu_Button()
                self.lp.Click_Logout()
                assert True
            else:
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Credance\\Screenshot\\test_params.py-fail.png")

                assert False
        else:
            if getDataforogin[2] == "Fail":
                assert True

            else:
                self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Credance\\Screenshot\\test_params.py-fail.png")

                assert False
        self.driver.close()




