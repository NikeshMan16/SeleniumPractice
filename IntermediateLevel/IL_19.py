"""19.	Validate whether an image is loaded correctly.
o	Fetch the src attribute of an <img> tag and verify the image URL."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests

from urls import url_ecom

driver = webdriver.Chrome()
driver.get(url_ecom)
wait = WebDriverWait(driver, 5)

img = driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div/div[2]/div[2]/a/img')

img_src = img.get_attribute("src")
print(f'Img src: {img_src}')

#Validation the URL with HTTP request
response = requests.get(img_src)

if response.status_code == 200:
    print("Image URL valid and image loaded correctly.")
else:
    print("image URL broken or url invalid")

driver.quit()