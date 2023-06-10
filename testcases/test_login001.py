import pytest

from pageObject.Login import Loginpage
from utilites.Logger import LogGenerator
from utilites.Readproperties import Readconfig


class Test_Login:
    url = Readconfig.geturl()
    email = Readconfig.getemail()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    @pytest.mark.sanity
    def test_title_page(self,setup):
        self.driver = setup
        if self.driver.title == "CredKart":
            print("title is visible")
            assert True
        else:
            assert False

    @pytest.mark.sanity
    def test_login002(self,setup):
        self.driver = setup
        self.log.info("Startes test case 002 testing")
        self.log.info("opening browser")
        self.driver.get(self.url)
        self.log.info("GO to this Url page" + self.url)
        self.lp = Loginpage(self.driver)
        self.lp.Click_Login_Page()
        self.log.info("click login page")
        self.lp.Enter_Email(self.email)
        self.log.info("Entering the Email" + self.email )
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password" + self.password)
        self.lp.Click_Login()
        self.log.info("clickl the login button")
        if self.driver.title == "CredKart":
            self.lp.Click_Menu_Button()
            self.log.info("click the Menu Button")
            self.lp.Click_Logout()
            self.log.info("click the logout Buttion")
            assert True
        else:
            assert False


