from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginJumia:
    username = "account"
    password = "password"
    loginbutton = "div.search-button"
    sbutton='//*[@id="pc__search-input"]/div[2]'
    searchtext=".van-field__control"    
    infbx="div.info-box"
    descrelement="p.product-title"
    priceselement = "div.product-price"


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.NAME, self.username).click()
        self.driver.find_element(By.NAME, self.username).send_keys(username)
    def setPassword(self,password):
        
        self.driver.find_element(By.NAME,self.password).send_keys(password)
        self.driver.find_element(By.NAME,self.password).send_keys(Keys.ENTER)
    def entertextitem(self,searchterm):
        Stxt = self.driver.find_element(By.CSS_SELECTOR, self.searchtext)
        
        Stxt.send_keys(searchterm + Keys.ENTER)
        
    def submitsearch(self):
         
        self.driver.find_element(By.XPATH, self.sbutton).click()
    def getitemprices(self):
        infobox =self.driver.find_elements(By.CSS_SELECTOR,self.infbx)
        iteminfo = self.driver.find_elements(By.CSS_SELECTOR,self.descrelement)
        allprices = self.driver.find_elements(By.CSS_SELECTOR, self.priceselement)


        for iteminfo in infobox:
            print (iteminfo.text)


        # itemsfound = [itemsfound.text for itemsfound in infobox]
        
        # print(itemsfound)

        # infnprices = [infobox.text for infobox in iteminfo]
        # print (infnprices)
        # itinfo = [itinfo.text for itinfo in iteminfo]
        # print(itinfo)
        # prices = [prices.text for prices in allprices]

        # print(prices)
        
        



        # prices = [ prices.text for prices in allprices]
        # print(prices)
        # return prices


    
  
    
