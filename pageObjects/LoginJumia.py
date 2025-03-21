from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class KilimallBase:

    def __init__(self, driver):
        self.driver = driver
      

class LoginJumia(KilimallBase):

    username_element = "account"
    password_element = "password"
    loginbutton = "div.search-button"
    sbutton='//*[@id="pc__search-input"]/div[2]'
    searchtext=".van-field__control"    
    infbx="div.info-box"
    
    descrelement="p.product-title"
    # priceselement = "div.product-price"
    priceselement = ".product-price[data-v-c039e353]"
   

    def setUsername(self,username):
        self.driver.find_element(By.NAME, self.username_element).send_keys(username)
       
    def setPassword(self,password):
        
        self.driver.find_element(By.NAME,self.password_element).send_keys(password,Keys.ENTER)
      

    def entertextitem(self,searchterm):
        self.driver.find_element(By.CSS_SELECTOR, self.searchtext).send_keys(searchterm,Keys.ENTER)
        
        
    def submitsearch(self):
         
        self.driver.find_element(By.XPATH, self.sbutton).click()
    # def getitemprices(self):
    #     infobox =self.driver.find_elements(By.CSS_SELECTOR,self.infbx)
    #     iteminfo = self.driver.find_elements(By.CSS_SELECTOR,self.descrelement)
    #     allprices = self.driver.find_elements(By.CSS_SELECTOR, self.priceselement)


    #     for price in allprices:
            
    #         print (price.text)

    def getitemprices(self):
        # Locate the elements
        infobox = self.driver.find_elements(By.CSS_SELECTOR, self.infbx)  # Not used yet, but keeping it for context
        iteminfo = self.driver.find_elements(By.CSS_SELECTOR, self.descrelement)  # Descriptions
        allprices = self.driver.find_elements(By.CSS_SELECTOR, self.priceselement)  # Prices

        # Ensure both lists have the same length to avoid index errors
        if len(iteminfo) != len(allprices):
            print("Warning: Number of descriptions and prices don't match!")
            return

        
        for description, price in zip(iteminfo, allprices):

            print(f"{description.text}: {price.text}")


    
  
    
