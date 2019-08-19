from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://rostov.tele2.ru/');
time.sleep(1) # Let the user actually see something!


tarifs = driver.find_elements_by_css_selector('div.ssc-tariff-box') #get all tarifs 
print (len(tarifs)) #see the number of tarifs
ln = len(tarifs)    
i=0
exp=0

pricez=[0,0]

tnamel=[]
 #

while i<ln:         #title name loop
    contr=tarifs[i] #get the list of tarif names
    tariftitle = contr.find_element_by_css_selector('div.tariff-title').find_element_by_tag_name('span').find_element_by_tag_name('span').get_attribute('innerHTML')
    tnamel.append(tariftitle)
    i+=1
i=0
k=0
while len(tnamel)>0 :

    ch=True 
    while ch:               #Check until loaded 
        try:
           tarifs = driver.find_elements_by_css_selector('div.ssc-tariff-box')
           if len(tarifs)<ln:
               ch=True
           else:
               ch=False
        except Exception:
           ch=True
    i=0
    tt=tnamel.pop(0)
    while i<ln:
        contr=tarifs[i]
        ch=True 
        while ch:               #Check until loaded 
                try:
                    tarifs = driver.find_elements_by_css_selector('div.ssc-tariff-box')
                    contr=tarifs[i]
                    if len(tarifs)<ln:
                        ch=True
                    else:
                       ch=False
                except Exception:
                       ch=True
        tariftitle = contr.find_element_by_css_selector('div.tariff-title').find_element_by_tag_name('span').find_element_by_tag_name('span').get_attribute('innerHTML')
        if tariftitle == tt:
            ch=True 
            while ch:               #Check until loaded 
                    try:
                        pri=contr.find_element_by_css_selector('span.price')
                        ch=False
                    except Exception:
                       ch=True
            pricez[0]=int(pri.get_attribute('innerHTML'))
            print(tariftitle)
            ch=True 
            while ch:               #Check until loaded 
                try:
                    tarifs = driver.find_elements_by_css_selector('div.ssc-tariff-box')
                    contr=tarifs[i]
                    if len(tarifs)<ln:
                        ch=True
                    else:
                       ch=False
                except Exception:
                       ch=True

            ch=True 
            while ch:               #Check until loaded 
                    try:
                       pri.click()
                       ch=False
                    except Exception:
                       ch=True
                       chq=True    
                       
                       while chq:               #Check until loaded #sometimes you just need to swipe it out
                            try:
                       swipe=driver.find_element_by_css_selector('div.swiper-arrow-next')
                       swipe.click()
                               chq=False
                            except Exception:
                               chq=True

            ch = True
            while ch:
                try:
                    price=driver.find_element_by_css_selector('div.price-wrap').find_element_by_tag_name('span').find_element_by_tag_name('span').get_attribute('innerHTML')
                    print(price)
                    pricez[1]=int(price)
                    ch = False
                except Exception:
                    ch = True
            if pricez[0]==pricez[1]:
                print('Main and info Prices are correct!')
                driver.back()
            else:
                print(tariftitle+' inner/outer price mistake')    
            
 #       time.sleep(3)
        i+=1

time.sleep(5) # Let the user actually see something!
driver.quit()
