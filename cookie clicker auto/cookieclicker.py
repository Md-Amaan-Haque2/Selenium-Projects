from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

lang_XPATH = "//*[contains(text(), 'English')]"

WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.XPATH , lang_XPATH))
)

language = driver.find_element(By.XPATH , lang_XPATH)

language.click()

cookie_id = "bigCookie"
base = "product"
base_price = "productPrice"

WebDriverWait(driver, 5).until(
    
  EC.presence_of_element_located((By.ID , cookie_id))

)

cookie = driver.find_element(By.ID , cookie_id)

while True:
    
    cookie.click()
    cookie_count = driver.find_element(By.ID , "cookies").text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",",""))


    for i in range(6):
        
          cursor_price = driver.find_element(By.ID , base_price + str(i)).text.replace(",","")

          if not cursor_price.isdigit():
            continue

          cursor_price = int(cursor_price)

          if cookie_count >= cursor_price:
            cursor = driver.find_element(By.ID , base + str(i))
            cursor.click()
            break
