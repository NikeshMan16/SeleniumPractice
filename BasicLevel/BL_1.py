"""1.	Launch a browser and navigate to a URL.
o	Open Chrome and navigate to "https://example.com".
o	Print the page title and URL in the console."""

from selenium import webdriver

driver = webdriver.Chrome()
url_to_fetch ="https://example.com"

driver.get(url_to_fetch)
page_tile = driver.title
url_link = driver.current_url

print(f"The page title of website is {page_tile}")
print(f"The url of the website is {driver.current_url}")
