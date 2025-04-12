"""6.	Verify an element’s presence on the page.
o	Check if a button exists on the page before clicking it."""

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import url_automation

driver = webdriver.Chrome()
driver.get(url_automation)
wait = WebDriverWait(driver,5)
try:
    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'wikipedia-search-button')))
    button.click()
    print("Button has been clicked")
except TimeoutException:
    print("Failed to locate the element")

