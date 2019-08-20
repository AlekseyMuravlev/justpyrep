from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('https://more.tele2.ru/')
ch=True
time.sleep(1) # Let the user actually see something!


##while ch:               #Check until loaded 
##    try:
imgs = driver.find_elements_by_tag_name('img') #open offer
##       ch=False
##    except Exception:
##        ch=True

for im in imgs:
    print(im.get_attribute('src'))

time.sleep(10) # Let the user actually see something!
driver.quit()
