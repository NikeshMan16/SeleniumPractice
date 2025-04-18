"""1.	Launch a browser and navigate to a URL.
o	Open Chrome and navigate to "https://example.com".
o	Print the page title and URL in the console."""

from selenium import webdriver

from BasicLevel.urls import url_automation

driver = webdriver.Chrome()

driver.get(url_automation)
page_tile = driver.title
url_link = driver.current_url

print(f"The page title of website is {page_tile}")
print(f"The url of the website is {driver.current_url}")
