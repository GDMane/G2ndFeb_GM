from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

print ('Updated from server side ..!')
print('Hello ....!')


driver = webdriver.Chrome('E:\Ganesh\Drivers\chromedriver.exe')
driver.get("http://toolsqa.com/automation-practice-form/")

driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element_by_id("photo").click()
time.sleep(1)
os.system('E:\\Ganesh\\autoitTest.au3')
time.sleep(1)
