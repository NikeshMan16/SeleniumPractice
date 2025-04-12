"""7.	Capture a screenshot of a webpage.
o	Take a screenshot after navigating to a website and save it as a PNG file."""
import time

from selenium import webdriver

from urls import url_example

driver = webdriver.Chrome()
driver.get(url_example)
time.sleep(2)
driver.save_screenshot("BasicLevel/ss.png")

