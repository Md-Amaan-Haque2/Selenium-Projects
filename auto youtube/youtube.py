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

driver.get("https://www.youtube.com/")

driver.maximize_window()

WebDriverWait(driver,5).until(
  EC.presence_of_element_located((By.NAME, "search_query"))
)

search = driver.find_element(By.NAME , "search_query")
search.clear()
search.send_keys("Selenium Tutorials"+ Keys.RETURN)

time.sleep(6)

WebDriverWait(driver,5).until(
  EC.presence_of_element_located((By.PARTIAL_LINK_TEXT , "Selenium Tutorial for Beginners using Python"))
)

video_finder = driver.find_element(By.PARTIAL_LINK_TEXT , "Selenium Tutorial for Beginners using Python")
video_finder.send_keys(Keys.RETURN)

time.sleep(1)

WebDriverWait(driver,120).until(
  EC.presence_of_element_located((By.ID , "skip-button:2"))
)

skip_button = driver.find_element(By.ID , "skip-button:2")

time.sleep(5)

skip_button.click()

WebDriverWait(driver,5).until(
  EC.presence_of_element_located((By.ID , "simplebox-placeholder"))
)

comment_section = driver.find_element(By.ID , "simplebox-placeholder")
comment_section.click()

WebDriverWait(driver,5).until(
  EC.presence_of_element_located((By.PARTIAL_LINK_TEXT , "Sign in"))
)

signin_button = driver.find_element(By.PARTIAL_LINK_TEXT , "Sign in")

time.sleep(2)

signin_button.click()


WebDriverWait(driver,5).until(
  EC.presence_of_element_located((By.ID , "identifierId"))
)

email_user = driver.find_element(By.ID , "identifierId")
email_user.clear()

time.sleep(1)

email_user.send_keys(""+ Keys.RETURN)## enter your account email

WebDriverWait(driver,5).until(
  EC.presence_of_element_located((By.NAME , "Passwd"))
)

email_pass = driver.find_element(By.NAME , "Passwd")
email_pass.clear()

time.sleep(1)

email_pass.send_keys("" + Keys.RETURN)## enter your mail password

ele = WebDriverWait(driver,5)

time.sleep(8)


try:
    ele.until(EC.presence_of_element_located((By.ID, "skip-button:2")))
    skip_button2 = driver.find_element(By.ID , "skip-button:2")
    time.sleep(5)
    skip_button2.click()

    
    ele.until(EC.presence_of_element_located((By.ID , "simplebox-placeholder")))
    comment_section = driver.find_element(By.ID , "simplebox-placeholder")
    comment_section.click()
    time.sleep(1)
    ele.until(EC.presence_of_element_located((By.ID , "contenteditable-root")))
    comment_write = driver.find_element(By.ID , "contenteditable-root")
    comment_write.send_keys("what a nice lecture by you!")

except:
    ele.until(EC.presence_of_element_located((By.ID, "simplebox-placeholder")))
    comment_section = driver.find_element(By.ID , "simplebox-placeholder")
    comment_section.click()
    time.sleep(1)
    ele.until(EC.presence_of_element_located((By.ID , "contenteditable-root")))
    comment_write = driver.find_element(By.ID , "contenteditable-root")
    comment_write.send_keys("what a nice lecture by you!") 

time.sleep(1)


sub_button = driver.find_element(By.ID , "subscribe-button-shape")
sub_button.click()

time.sleep(1)

subbed_button = driver.find_element(By.XPATH , "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading-trailing']")
subbed_button.click()

time.sleep(1)

sub_notif_but = driver.find_element(By.XPATH , "//*[@class='style-scope ytd-menu-service-item-renderer']")
sub_notif_but.click()

time.sleep(1)

like_but = driver.find_element(By.XPATH , "//*[@class='ytLikeButtonViewModelHost']")
like_but.click()

time.sleep(10)

driver.quit()