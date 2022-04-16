


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


chromePath = "user-data-dir=C:\\Users\\Frank\\AppData\\Local\\Programs\\Python\\Python310\\MypyFiles\\WebDrivers\\cookies"

chromeOptions = Options()
chromeOptions.add_argument(chromePath)
#chromeOptions.add_argument('headless')
# tut


driver = webdriver.Chrome('./chromedriver', options=chromeOptions)

driver.get("http://web.whatsapp.com")

print ("Loading Page")

while not driver.find_elements_by_class_name("_3hKpJ"):
    time.sleep(1)

print ("Page Loaded")

driver.implicitly_wait(10)
contact = 'Meal'
searchBar = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
searchBar.send_keys(contact)
searchBar.send_keys(Keys.ENTER)

msg=""

time.sleep(2)
driver.implicitly_wait(10)
inputBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
with open('fileToCall.txt') as ms:
    for i in ms:
        data = i.strip()
        msg = msg + data + ' '

inputBox.send_keys(msg)
driver.implicitly_wait(20)
inputBox.send_keys('\ue007')



#driver.close()





