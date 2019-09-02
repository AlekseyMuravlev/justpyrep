from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
try:
    driver = webdriver.Chrome('C:\Intel\chromedriver.exe',chrome_options=options)
except Exception:
    exp+=1
#driver.implicitly_wait(40) 
#driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('https://rostov.tele2.ru/');
time.sleep(1) # Let the user actually see something!

actions = ActionChains(driver)
mendiv = driver.find_element_by_xpath('//div[@class="dropdown-menu-container"]/ul[@class="dropdown-menu"]')
liq = mendiv.find_elements_by_tag_name("li")
liqun = len(liq)
print(liqun)
tenk = True
i=1
k=0
j=0
exp = 0

while tenk:
    time.sleep(5)
    try:
        mendiv = driver.find_element_by_xpath('//div[@class="dropdown-menu-container"]')
        try:
            menli = mendiv.find_element_by_xpath('//ul[@class="dropdown-menu"]/li['+str(i)+']')
            ActionChains(driver).move_to_element(menli).perform()
            print('i = ' + str(i))
            #time.sleep(2)
           
            #sbhr = menli.find_elements_by_tag_name('li')
            
            try:
               dmu = menli.find_elements_by_class_name('submenu-col')

               smt = dmu[k].find_elements_by_class_name('submenu-title')
               if smt[0].text == "Часто интересуются":
                   k=0
                   j=0
                   i+=1
               else:
                   
                   
                   try:
                       ahr = dmu[k].find_elements_by_tag_name('a')
                       ahr[j].click()
                       j+=1
                       time.sleep(5)
                       driver.back()
                        
                   except Exception: 
                       print(smt[0].text)
                       print('k = ' + str(k))
                       print(len(dmu))
                       print(dmu[k].text)
                       k+=1
                       j=0
               
            except Exception:          
                k=0
                j=0
                i+=1

        except Exception:
            tenk = False
    

    except Exception:
        exp+=1
        print(exp)
   
print('Prepare to exit')
time.sleep(10)
driver.quit()
