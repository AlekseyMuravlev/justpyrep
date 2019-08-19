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
actions = ActionChains(driver) #take driver actions

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

rules=driver.find_element_by_xpath("//a[@class='js-rules']")
ruhre = rules.get_attribute('href')
driver.execute_script("window.open('" + ruhre + "', '_blank')")
perso=driver.find_element_by_xpath("//a[@class='js-personal']")
pehref = perso.get_attribute('href')
driver.execute_script("window.open('" + pehref + "', '_blank')")

ch=True 
while ch:               #Check until OPENED RULES
    try:
       driver.switch_to.window(driver.window_handles[2])
       ch=False
    except Exception:
       ch=True
time.sleep(10) 
driver.save_screenshot("screenshot_rules.png")
ch=True 
while ch:               #Check until PERSONAL DATA 
    try:
       driver.switch_to.window(driver.window_handles[1])
       ch=False
    except Exception:
       ch=True
time.sleep(10) 
driver.save_screenshot("screenshot_personal_data.png")




time.sleep(10) # Let the user actually see something!
driver.quit()
