import time

import pytest

from pageObject import Orders
from pageObject.Login import Loginpage
from pageObject.Orders import OrderP
from utilites.Logger import LogGenerator
from utilites.Readproperties import Readconfig


class Test_AddCart:

    url = Readconfig.geturl()
    Email = Readconfig.getemail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_Add_to_Cart003(self,setup):

        self.driver = setup
        self.driver.get(self.url)
        self.lp = Loginpage(self.driver)
        self.lp.Click_Login_Page()
        self.lp.Enter_Email(self.Email)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.oa = OrderP(self.driver)
        self.oa.click_Macbook()
        self.oa.click_Add()
        self.oa.Dropdown_Click(2)
        self.oa.Continue_Shoping()
        # time.sleep(2)
        self.oa.Apple_Ipad()
        self.oa.click_Add_to_Cart()
        self.oa.Dropdown_handle(3)
        self.oa.Click_Continue()
        self.oa.Click_Elelctic_Guitar()
        self.oa.CLick_Addcart()
        self.oa.Dropdown(4)
        self.oa.Cheakout_list()
        self.oa.Enter_FirstName('Ganesh')
        self.oa.Enter_LastName('Kumar')
        self.oa.Enter_Phone("9032929393")
        self.oa.Enter_Adress("New Adarsh Nagar Khandwa")
        self.oa.Enter_Zipcode("340934")
        self.oa.Dropdown_State("Delhi")
        self.oa.Enter_OwnerName("RajAryan")
        self.oa.Enter_Cvv("257")
        self.oa.Enter_CardNumber("4716")
        self.oa.Enter_CardNumber("1089")
        self.oa.Enter_CardNumber("9971")
        self.oa.Enter_CardNumber("6531")
        self.oa.Enter_ExpiryYear("2022")
        self.oa.Enter_ExpiryMonth("June")
        self.oa.Click_ContinueCheakout()
        if self.driver.title == "CredKart":
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Credance\\Screenshot\\test_Add_to_Cart003.py-Pass.png")
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Credance\\Screenshot\\test_Add_to_Cart003.py-Fail.png")
            assert False



















