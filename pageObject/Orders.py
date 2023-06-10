import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class OrderP:

    click_apple_macbook = (By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']")
    click_add = (By.XPATH,"//input[@value='Add to Cart']")
    Dropdown_item = (By.XPATH,"//tbody/tr[1]/td[3]/select[1]")
    Continue_Shoping_XPATH = (By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    Click_Apple_Ipad = (By.XPATH,"//h3[normalize-space()='Apple iPad Retina']")
    Click_Add_TO_Cart = (By.XPATH,"//input[@value='Add to Cart']")
    Dropdown_item1 = (By.XPATH,"//tbody/tr[2]/td[3]/select[1]")
    Continue_Shoping1_XPATH = (By.XPATH,"//a[@class='btn btn-primary btn-lg']")
    click_Electric_Guitar = (By.XPATH,"//h3[normalize-space()='Electric Guitar']")
    click_Add_to_Cart1 = (By.XPATH,"//input[@value='Add to Cart']")
    Dropdown_list = (By.XPATH,"//tbody/tr[3]/td[3]/select[1]")
    Cheakout_XPATH = (By.XPATH,"//a[@class='btn btn-success btn-lg']")
    First_Name_XPATH = (By.XPATH,"//input[@id='first_name']")
    Last_Name_XPATH = (By.XPATH,"//input[@id='last_name']")
    Phone_Number = (By.XPATH,"//input[@id='phone']")
    Address_XPATH = (By.XPATH,"//textarea[@id='address']")
    ZipCode_XPATH = (By.XPATH,"//input[@id='zip']")
    Dropdown_state_List =(By.XPATH,"//select[@id='state']")
    Text_Owner_Name_XPATH = (By.XPATH,"//input[@id='owner']")
    Text_Cvv_XPATH = (By.XPATH,"//input[@id='cvv']")
    Text_Card_Number = (By.XPATH,"//input[@id='cardNumber']")
    DropDown_Year_XPATH = (By.XPATH,"//select[@id='exp_year']")
    Dropdown_Month_XPATH = (By.XPATH,"//select[@id='exp_month']")
    Click_Continue_Cheakout = (By.XPATH,"//button[@id='confirm-purchase']")





    def __init__(self,driver):
        self.driver = driver

    def click_Macbook(self):
        self.driver.find_element(*OrderP.click_apple_macbook).click()

    def click_Add(self):
        self.driver.find_element(*OrderP.click_add).click()


    def Dropdown_Click(self,item):
        Item = Select(self.driver.find_element(*OrderP.Dropdown_item))
        Item.select_by_index(3)

    def Continue_Shoping(self):
        self.driver.find_element(*OrderP.Continue_Shoping_XPATH).click()
        # time.sleep(3)
    def  Apple_Ipad(self):
        self.driver.find_element(*OrderP.Click_Apple_Ipad).click()

    def click_Add_to_Cart(self):
        self.driver.find_element(*OrderP.Click_Add_TO_Cart).click()

    def  Dropdown_handle(self,item1):
        Item1 = Select(self.driver.find_element(*OrderP.Dropdown_item1))
        Item1.select_by_index(2)

    def  Click_Continue(self):
        self.driver.find_element(*OrderP.Continue_Shoping1_XPATH).click()

    def  Click_Elelctic_Guitar(self):
        self.driver.find_element(*OrderP.click_Electric_Guitar).click()

    def CLick_Addcart(self):
        self.driver.find_element(*OrderP.click_Add_to_Cart1).click()

    def Dropdown(self,item2):
        Iten2 = Select(self.driver.find_element(*OrderP.Dropdown_list))
        Iten2.select_by_index(4)

    def Cheakout_list(self):
        self.driver.find_element(*OrderP.Cheakout_XPATH).click()

    def Enter_FirstName(self,firstname):
        self.driver.find_element(*OrderP.First_Name_XPATH).send_keys(firstname)
    def Enter_LastName(self,lastname):
        self.driver.find_element(*OrderP.Last_Name_XPATH).send_keys(lastname)

    def Enter_Phone(self,phone):
        self.driver.find_element(*OrderP.Phone_Number).send_keys(phone)
    def Enter_Adress(self,address):
        self.driver.find_element(*OrderP.Address_XPATH).send_keys(address)

    def Enter_Zipcode(self,zipcode):
        self.driver.find_element(*OrderP.ZipCode_XPATH).send_keys(zipcode)

    def Dropdown_State(self,state):
        State = Select(self.driver.find_element(*OrderP.Dropdown_state_List))
        State.select_by_visible_text("Delhi")

    def Enter_OwnerName(self,ownername):
        self.driver.find_element(*OrderP.Text_Owner_Name_XPATH).send_keys(ownername)
    def Enter_Cvv(self,cvv):
        self.driver.find_element(*OrderP.Text_Cvv_XPATH).send_keys(cvv)

    def Enter_CardNumber(self,cardnumber):
        self.driver.find_element(*OrderP.Text_Card_Number).send_keys(cardnumber)

    def Enter_ExpiryYear(self,expiryyear):
        ExpireYear = Select(self.driver.find_element(*OrderP.DropDown_Year_XPATH))
        ExpireYear.select_by_visible_text("2028")


    def Enter_ExpiryMonth(self,expirymonth):
        ExpireMonth = Select(self.driver.find_element(*OrderP.Dropdown_Month_XPATH))
        ExpireMonth.select_by_visible_text("May")


    def Click_ContinueCheakout(self):
        self.driver.find_element(*OrderP.Click_Continue_Cheakout).click()







