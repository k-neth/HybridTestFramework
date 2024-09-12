from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class GetPricesJumia:
    mainwrapperCSSSELECTOR=".listings"
    miniwrapperPriceCSSSelector="div.product-price"
    searchinputID = "van-field-10-input"

    def __init__(self, driver):
        self.driver=driver

    def getprices(self,searchterm):
        self.driver.find_element(By.ID, self.searchinputID).send_keys(searchterm + Keys.ENTER)
        # allprices = self.driver.find_elements(By.CSS_SELECTOR, self.miniwrapperPriceCSSSelector)
        # allprices.text
        # for item in allprices:
        #     return item
            

