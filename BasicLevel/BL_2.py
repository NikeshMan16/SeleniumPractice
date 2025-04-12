"""2.	Find an element using different locators.
o	Locate a search input field using ID, Name, XPath, and CSS Selector.
o	Enter "Selenium WebDriver" in the search field and submit the form."""
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from BasicLevel.urls import url_automation

driver = webdriver.Chrome()
driver.get(url_automation)

wait = WebDriverWait(driver, 5)  # Wait condition for the elements

input_field = wait.until(EC.visibility_of_element_located((By.ID,'name')))
input_field.send_keys("Selenium Webdriver")
time.sleep(2)  # To check the entered field



