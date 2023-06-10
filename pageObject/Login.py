import time

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as Ec


class Loginpage:
    click_login_XPATH = (By.XPATH,"//a[normalize-space()='Login']")
    Text_Email_XPATH = (By.XPATH,"//input[@id='email']")
    Text_Password_XPATH = (By.XPATH,"//input[@id='password']")
    Enter_Login_XPATH = (By.XPATH,"//button[@type='submit']")
    Click_Menu_Button_XPATH = (By.XPATH,"//a[@role='button']")
    Click_Logout_CSS = (By.CSS_SELECTOR,"a[href='https://automation.credence.in/logout']")

    def __init__(self,driver):
        self.driver = driver

    def  Click_Login_Page(self):
        self.driver.find_element(*Loginpage.click_login_XPATH).click()

    def Enter_Email(self,email):
        self.driver.find_element(*Loginpage.Text_Email_XPATH).send_keys(email)
    def Enter_Password(self,password):
        self.driver.find_element(*Loginpage.Text_Password_XPATH).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Loginpage.Enter_Login_XPATH).click()

    def Click_Menu_Button(self):
        self.driver.find_element(*Loginpage.Click_Menu_Button_XPATH).click()
        time.sleep(2)

    def Click_Logout(self):
        self.driver.find_element(*Loginpage.Click_Logout_CSS).click()
        # time.sleep(5)

    def Login_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*Loginpage.Click_Menu_Button_XPATH)
            # self.driver.find_element(*Loginpage.click_logout_XPATH)
            return True
        except Ec:
            return False



    #
    # def title(self):
    #     try:
    #         self.driver.implicitly_wait(10)
    #         title = self.driver.title
    #         return title
    #     except Ec:
    #         title = self.driver.title
    #         return title
    #
