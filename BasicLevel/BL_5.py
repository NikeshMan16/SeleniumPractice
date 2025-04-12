"""5.	Extract text from a webpage.
o	Navigate to "https://example.com".
o	Print all the text present inside a specific <div> element."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasicLevel.urls import url_example

driver = webdriver.Chrome()
driver.get(url_example)
wait = WebDriverWait(driver, 5)

box_text = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/p[1]'))).text

print(f"The text in the paragraph is {box_text}")



