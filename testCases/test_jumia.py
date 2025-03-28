import pytest
from pageObjects.LoginJumia import LoginJumia
from pageObjects.SearchItemJumia import SearchItemJumia
# from pageObjects.AddItemToCart import AddItemToCart
from pageObjects.GetPricesJumia import GetPricesJumia
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from utilities.readCredentials import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_J01:
    # baseurl = "https://www.kilimall.co.ke/login"

    searchterm=ReadConfig.getSearchitem()
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    
        
    

    logger=LogGen.loggen()
    # searchterm="Hennesy"

    # mdriver=webdriver.Chrome()

    @pytest.mark.regression

    def test_KilimallLogin(self):
      
                
        # self.driver = setup
       
        self.driver.get(self.baseurl)
        # time.sleep(5)

        self.lp=LoginJumia(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.logger.info("Loggin in with password and username successful") 
        time.sleep(10)

        
        self.lp.entertextitem(self.searchterm)
        
        self.logger.info("Item to search entered")
        
        self.lp.submitsearch()
        time.sleep(5)
        self.logger.info("-----waiting for results----")
        time.sleep(10)
        self.logger.info("---------getting item prices-----------")
        self.lp.getitemprices()


class Test_J02:
    




    
   

        
        
