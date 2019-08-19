from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://rostov.tele2.ru/');
time.sleep(1) # Let the user actually see something!

tarifs = driver.find_elements_by_css_selector('div.ssc-tariff-box')

print ("Тарифов на странице")
print (len(tarifs))
ln = len(tarifs)
i=0
exp=0
while i < ln:
    contr = tarifs.pop(0)
    
    
    try:
         contr.find_element_by_css_selector('img.hit-image')
  
         print('Хит тариф - ' + contr.find_element_by_css_selector('div.tariff-title').find_element_by_tag_name('span').find_element_by_tag_name('span').get_attribute('innerHTML'))
    except Exception:
         exp+=1
         #print(contr.find_element(By.XPATH, '//div[@class="tariff-title"]/span/span''').get_attribute('innerHTML'))
    i+=1
driver.quit()
