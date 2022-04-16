import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
options.headless = True

s=Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(5)
time.sleep(10)
print('Scan :: ')
input('Done: ')
print('logged')


contact = 'Meal'
searchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchBox.send_keys(contact)
searchBox.send_keys(keys.ENTER)

driver.implicitly_wait(5)
time.sleep(5)
msg = '..Testing_Meal_Bot..'
msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
msg_box.send_keys(msg)
msg_box.send_keys(keys.ENTER)

print('DONE')
                