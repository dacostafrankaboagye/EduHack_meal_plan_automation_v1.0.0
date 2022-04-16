
from selenium import webdriver
from selenium.webdriver.common.by import By



def id_info():  
    # get the ID from the database
    
    #using txt file as a test
    
    with open('ListOfID.txt', 'r') as IDList:
        for i in IDList:
            id = i.strip()
            #implementation(driver=driver, id=id)
            print(id)


id_info()


'''

def perform_operation(driver):
    try:
        with open('db.txt','a') as dbT:
            for i in range(1,7): # will they have more than 7 items???
                ab = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[4]/div/table/tbody/tr['+str(i)+']')
                dbT.write('==')
                for j in ab:
                    #dbT.write((j.get_attribute('innerText')).replace('    ','') ) 
                    dbT.write(str((j.get_attribute('innerText'))))  
    except:
        print('Nil')


'''


def implementation(driver,id):
    #id = '70722023' # the id
    id_tb = driver.find_element_by_class_name('search-by-id')
    id_tb.send_keys(id)
    login = driver.find_element_by_class_name("search-by-id-btn")
    login.submit()
    #driver.close()
    driver.implicitly_wait(5)
    try:
        with open('db.txt','a') as dbT:
            for i in range(1,7): # will they have more than 7 items???
                ab = driver.find_elements(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[4]/div/table/tbody/tr['+str(i)+']')
                dbT.write('==')
                for j in ab:
                    #dbT.write((j.get_attribute('innerText')).replace('    ','') ) 
                    
                    dbT.write(str((j.get_attribute('innerText')))) 
                     
    except:
        print('Nil')
    driver.close()
