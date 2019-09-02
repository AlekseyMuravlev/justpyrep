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

links = ['https://rostov.tele2.ru/','https://msk.tele2.ru/']
for link in links:
    
    driver.get(link);

    time.sleep(1) # Let the user actually see something!


    tariffs = driver.find_elements_by_css_selector('div.ssc-tariff-box') #get all RND tarifs

    print (link +' tariffs amount' + str(len(tariffs))) #see the number of tarifs
         
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


    print(tnamel[linm])
    print(pricez[linm])
    i=0
    k=0
    linm+=1
for tnama in tnamel[0]:
    i=0
    while tnama != tnamel[1][i]:
        i+=1
    if pricez[0][k] > pricez[1][i]:
        print("Цена в Ростове на тариф " + tnama + " выше")
    else:
        print("Цена в Москве на тариф " + tnama + " выше")
    kuku = tnamel[1].pop(i)
    kuku = pricez[1].pop(i)
    k+=1
i = 0
if len(tnamel[1])>0:
    print("В Москве есть следующие тарифы, которых нет в Ростове:")
    for tnama in tnamel[1]:
         print(tnama + ' за ' + str(pricez[1][i]) + ' руб')
         i +=1
         
    
#print ('MSK tarifs' + str(len(tariffs[1]))) #see the number of tarifs
time.sleep(5) # Let the user actually see something!
driver.quit()
