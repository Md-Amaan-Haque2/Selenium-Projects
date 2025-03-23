from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Sort of works like a proxy server
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://workspace.google.com/intl/en-US/gmail/")


WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='button button--medium header__aside__button button--desktop button--tablet button--mobile']"))
  )

sign_in_button = driver.find_element(By.XPATH, "//*[@class='button button--medium header__aside__button button--desktop button--tablet button--mobile']")
sign_in_button.click()

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.ID , "identifierId"))
  )

sign_user = driver.find_element(By.ID , "identifierId")
sign_user.clear()
sign_user.send_keys("" + Keys.RETURN) ## provide your mail

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.NAME , "Passwd"))
  )

sign_pass = driver.find_element(By.NAME , "Passwd")
sign_pass.clear()
time.sleep(0.5)
sign_pass.send_keys("" + Keys.RETURN)## provide the password for the given mail

WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.XPATH , "//*[@class='T-I T-I-KE L3']"))
  )

compose_but = driver.find_element(By.XPATH , "//*[@class='T-I T-I-KE L3']")
compose_but.click()

WebDriverWait(driver,10).until(
  EC.presence_of_element_located((By.ID , ":tx"))
)

sender = driver.find_element(By.ID , ":tx")
sender.send_keys("")## provide the recipient mail
time.sleep(6)

subject = driver.find_element(By.ID , ":q7")
subject.send_keys("Automated mail")
time.sleep(1)

body = driver.find_element(By.ID , ":rm")
body.send_keys("first automated mail by selenium")
time.sleep(1)

send = driver.find_element(By.ID , ":pw")
time.sleep(1)
send.click()


driver.quit()
