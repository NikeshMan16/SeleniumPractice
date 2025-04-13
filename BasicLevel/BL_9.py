"""9.	Interact with a dropdown menu.
o	Select an option from a dropdown using three different methods:
	By Index
	By Visible Text
	By Value"""
import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from urls import url_automation

driver = webdriver.Chrome()
driver.get(url_automation)

element = driver.find_element(By.ID, 'country')
driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth'});",element)

dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_index(3)
print("The value is selected by index")
time.sleep(2)
dropdown.select_by_visible_text('Canada')
time.sleep(2)
print("The value has been selected by visible text")


