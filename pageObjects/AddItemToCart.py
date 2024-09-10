from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AddItemToCart:
    cart =""
    itemprices = ".product-item .info-box .product-price[data-v-75a3da00]"
    def __init__(self, driver):
        self.driver = driver

    def ClickCart(self):
        print("Cart Clicked")
        pass
    def ItemAdded(self):
        print("Item added to cart")
        pass
    def allPrices(self):
        combinedprices=self.driver.find_elements(By.CSS_SELECTOR, self.itemprices)
        print(combinedprices)

