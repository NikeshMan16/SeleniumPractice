"""20.	Automate a dynamic search box.
o	Enter a search term in a search bar and select an autocomplete suggestion dynamically."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from urls import url_auto

driver = webdriver.Chrome()
driver.get("https://www.google.co.uk/")
wait = WebDriverWait(driver,5)

search_field = wait.until(EC.visibility_of_element_located((By.ID,'APjFqb')))
search_field.send_keys('selenium')

suggestion_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'ul[role="listbox"]')))

suggestions = suggestion_box.find_elements(By.CSS_SELECTOR,'li span')

for suggestion in suggestions:
    print(suggestion.text)
    if "selenium python" in suggestion.text.lower():
        suggestion.click()
        break

wait.until(EC.title_contains("selenium python"))

driver.quit()

