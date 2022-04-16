from pytest import fail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
import time
import sys
from config import chromePath



options = webdriver.ChromeOptions()

options.add_argument(chromePath)

# addition from  blog
options.add_argument('headless')
options.add_argument( "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36")
options.add_argument("remote-debugging-port=3333")


s='./chromedriver'
driver = webdriver.Chrome(s,options=options)
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(10)
time.sleep(10)



# search_box = WebDriverWait(driver,500).until(
#     EC.presence_of_element_located((By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]'))
# )


contact = 'Meal'
searchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchBox.send_keys(contact)
searchBox.send_keys(Keys.ENTER)

time.sleep(5)
driver.implicitly_wait(2)
msg = '--rebotting Bot'
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
# driver.implicitly_wait(20)
msg_box.send_keys(msg)
msg_box.send_keys(Keys.ENTER)
driver.implicitly_wait(5)

print('DONE')
driver.implicitly_wait(30)

driver.close()



