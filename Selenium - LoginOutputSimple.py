from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('https://rostov.tele2.ru/')

time.sleep(1) # Let the user actually see something!




##
actions = ActionChains(driver) #take driver actions
##
ch=True 
while ch:               #Check until loaded 
    try:
       login = driver.find_element_by_xpath("//div[@class='action login-action-new hidden-lg']") #login
       ch=False
    except Exception:
       ch=True
       while ch:               #Check until loaded 
            try:
               login = driver.find_element_by_xpath("//div[@class='action login-action-new visible-lg-inline-block']") #open offer
               ch=False
            except Exception:
               ch=True
login.click()

time.sleep(10)
divfra = driver.find_element_by_xpath("//div[@class='iframe-top-padding']") #select login by pass
ifras = divfra.find_elements_by_tag_name('iframe')
ifra = ifras[0]
driver.switch_to.frame(ifra)
##ch=True 
##while ch:               #Check until loaded 
##    try:
pwo = driver.find_element_by_xpath("//ul[@class='payment-options-double']/li[2]") #select login by pass
##       ch=False
##    except Exception:
##       ch=True
pwo.click()
##time.sleep(3)

formact = driver.find_element_by_xpath("//form[@class='active']")   #NUMBER&PASS ARE HERE.
elem = formact.find_element_by_name("pNumber")
elem.send_keys('9040000000')
time.sleep(2)
elem = formact.find_element_by_name("password")
elem.send_keys('Tele2TestNumber')
time.sleep(2)
formact.submit()



ch=True 
while ch:               #Check until loaded 
    try:
       login = driver.find_element_by_xpath("//div[@class='action login-action-new hidden-lg']") #login
       login.click()
       print(1)
       ch=False
    except Exception:
       ch=True
       while ch:               #Check until loaded 
            try:
               login = driver.find_element_by_xpath("//div[@class='action login-action-new visible-lg-inline-block with-action-popup']") #open offer
               actions.move_to_element(login).perform()
               print("2")
               ch=False
            except Exception:
               ch=True
actions.move_to_element(login).perform()
time.sleep(10)

ch=True 
while ch:               #Check until loaded # two types of menu
    try:
       actions.move_to_element(login).perform()
    
       print(driver.find_element_by_xpath("//div[@class='profile-popup_balance profile-popup_block']").text)
       driver.find_element_by_xpath("//ul[@class='profile-popup_menu profile-popup_block']/li[2]").click()
             
       wch=True
       while wch:
             try:
                aa = driver.find_element_by_xpath("//div[@class='remnants-table']")
                print(aa.text)
                wch=False
             except Exception:
                wch=True
       driver.back()
       time.sleep(5)
       wch=True
       while wch:               #Check until loaded 
             try:
                   login = driver.find_element_by_xpath("//div[@class='action login-action-new visible-lg-inline-block with-action-popup']") #open offer
                   print("2")
                   wch=False
             except Exception:
                   print("3")
                   wch=True
       login = driver.find_element_by_xpath("//div[@class='action login-action-new visible-lg-inline-block with-action-popup']")
       ActionChains(driver).move_to_element(login).perform()
       print("4")
       pwo = driver.find_element_by_xpath("//ul[@class='profile-popup_menu profile-popup_block']/li[4]")    
       time.sleep(2)
       pwo.click()
     
       ch=False
    except Exception: #menu in the compact site 
       ch=True
       try:
         print(driver.find_element_by_xpath("//div[@class='widget-box dashboard-balance']").text)
         remains = driver.find_element_by_xpath("//section[@class='dashboard-packages box-link-holder_with-small-title']/a[@class='box-link-holder hidden-xs']")
         remains.click()
         wch=True
         while wch:
             try:
                aa = driver.find_element_by_xpath("//div[@class='remnants-table']")
                print(aa.text)
                wch=False
             except Exception:
                wch=True
         driver.back()
         wch=True
         while wch:
             try:
               pwo = driver.find_element_by_xpath("//ul[@class='advanced-box unstyled-list']/li[2]/div/a[@class='box-link-advanced with-absolute-pseudo-right-arrow']") #
               pwo.click()
               wch= False
             except Exception:
               wch=True
         ch=False
         
       except Exception:
         ch=True


#pwo.click()
for i in range(12):
    ch=True 
    while ch:               #Check until loaded 
        try:
           expan = driver.find_element_by_xpath("//div[@class='expenses-category']") 
           #print(expan.get_attribute('innerHTML'))
           time.sleep(1)           
           print(expan.text)
           ch=False
        except Exception:
           ch=True

    try:
        step = driver.find_element_by_xpath("//a[@class='prev icon-left-arrow']")
        step.click()
    except Exception:
           ch=True
    

time.sleep(15) # Let the user actually see something!
driver.quit()
