from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.




i=0
k=0
linm=0

exp=0

pricez=[[],[]]

tnamel=[[],[]]

links = ['https://rostov.tele2.ru/','https://rostov.tele2.ru/nastroy-tariff']
for link in links:
    
    driver.get(link);

    time.sleep(1) # Let the user actually see something!


    tariffs = driver.find_elements_by_css_selector('div.ssc-tariff-box') #get all  tariffs

 
         
     #
    for i in tariffs:         #title name loop
        ch=True
        while ch:               #Check until loaded 
                try:
                    tariftitle = i.find_element_by_css_selector('div.tariff-title').text
                    while tariftitle == '': # if tariftitle hidden swipe to find
                           tariftitle = i.find_element_by_css_selector('div.tariff-title').text
                           swipe=driver.find_element_by_css_selector('div.swiper-arrow-next')
                           swipe.click()
                    ch=False
                except Exception:
                   ch=True
        tnamel[linm].append(tariftitle)
        ch=True 
        while ch:               #Check until loaded 
                try:
                    pri=i.find_element_by_css_selector('span.price')
                    ch=False
                except Exception:
                   ch=True
        pricez[linm].append(pri.text)
        print(tariftitle)



    i=0
    k=0
    linm+=1
print("Тарифы/возможность настроить")
for tnama in tnamel[0]:
    for i in range(len(tnamel[1])):
        if tnama == tnamel[1][i]:
             print(tnama + "/да")

#print ('MSK tarifs' + str(len(tariffs[1]))) #see the number of tarifs
time.sleep(5) # Let the user actually see something!
driver.quit()
