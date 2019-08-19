from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:\Intel\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://rostov.tele2.ru/');
time.sleep(1) # Let the user actually see something!
tarif = driver.find_element_by_css_selector('div.tariff-info-item')
try:
    stro=tarif.find_element_by_tag_name('strong')
    print(stro.get_attribute('innerHTML'))
except:
    print('No deal')
driver.quit()
