from selenium import webdriver
import time


driver = webdriver.Chrome('E:\Ganesh\Drivers\chromedriver.exe')
driver.get("http://toolsqa.com/automation-practice-form/")

driver.execute_script("window.scrollTo(0, 1000)")

driver.find_element_by_class_name('form-horizontal').find_element_by_link_text('Test File to Download').click()