"""10.	Retrieve all links from a webpage.
o	Print all hyperlinks (<a> tags) available on a webpage."""

from selenium import webdriver
from selenium.webdriver.common.by import By

from urls import url_automation

driver = webdriver.Chrome()
driver.get(url_automation)

hyperlinks = driver.find_elements(By.TAG_NAME,'a')

for hyperlink in hyperlinks:
    print(f"{hyperlink.text} \n")



