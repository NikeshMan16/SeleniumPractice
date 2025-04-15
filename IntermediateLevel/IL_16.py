"""16.	Extract and validate data from a web table.
o	Find a specific row and column value inside a table."""
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from urls import url_auto

driver = webdriver.Chrome()
driver.get(url_auto)
driver.maximize_window()

table = driver.find_element(By.XPATH, "//table[@name='BookTable']")

rows = table.find_elements(By.XPATH, ".//tbody/tr")

target_book = "Learn JS"
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if cells and cells[0].text.strip() == target_book:
        book = cells[0].text
        author = cells[1].text
        subject = cells[2].text
        price = cells[3].text
        print(f"Book: {book}, Author: {author}, Subject: {subject}, Price: {price}")
        break
else:
    print(f"'{target_book}' not found in the table.")

driver.quit()