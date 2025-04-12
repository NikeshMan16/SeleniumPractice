"""8.	Check if a checkbox is selected or not.
o	Locate a checkbox, click it, and verify if it is selected."""

from selenium import webdriver
from selenium.webdriver.common.by import By

from urls import url_automation

driver = webdriver.Chrome()
driver.get(url_automation)

monday = driver.find_element(By.ID, 'monday')
sunday = driver.find_element(By.ID,'sunday')
monday.click()

if monday.is_selected() is True:
    print("Monday checkbox is selected")
else:
    print("Not selected")

