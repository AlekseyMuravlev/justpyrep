from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
import time

def EventWait(event):
    ch=True 
    while ch:               #Check until loaded 
        try:
           event
           ch=False
        except Exception:
           ch=True

driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://rostov.tele2.ru/')
time.sleep(1) # Let the user actually see something!

ch=True 
while ch:               #Check until loaded 
    try:
       offer = driver.find_element_by_css_selector('iframe.flocktory-widget') #open offer
       ch=False
    except Exception:
       ch=True
ch=True 
while ch:               #Check until loaded 
    try:
        offer.click()
        oid = offer.get_attribute('id')
        ch=False
    except Exception:
       ch=True
ch=True 
while ch:               #Check until loaded 
    try:
        framer = driver.find_element_by_id(oid)
        ch=False
    except Exception:
       ch=True


driver.switch_to.frame(framer)

phone =driver.find_element_by_xpath("//form[@class='form js-form']/div/input[@id='tel']")
print(phone.get_attribute('innerHTML'))
#driver.find_element_by(By.xpath("//input[@id='tel']"))

phone.send_keys("9044482842")
#user=driver.find_element_by_id('name')
user =driver.find_element_by_xpath("//form[@class='form js-form']/div/input[@id='name']")

user.send_keys("Aleksey");
time.sleep(6)
el=driver.find_element_by_xpath("//button[@class='widget__link js-to-intro no-outline']")
el.click()


time.sleep(5) # Let the user actually see something!
driver.quit()
