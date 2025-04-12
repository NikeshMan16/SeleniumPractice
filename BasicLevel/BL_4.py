"""4.	Handle a simple alert pop-up.
o	Open a webpage with an alert box.
o	Accept or dismiss the alert."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from BasicLevel.urls import url_automation

driver = webdriver.Chrome()
wait = WebDriverWait(driver,5)
driver.get(url_automation)

alert_button = wait.until(EC.visibility_of_element_located((By.ID,'alertBtn')))
alert_button.click()
alert = driver.switch_to.alert

print("Alert is:", alert.text)
alert.accept()