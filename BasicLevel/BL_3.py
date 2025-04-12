"""3.	Click a button and verify navigation.
o	Click on a "Login" button and verify if the user is redirected to the login page."""
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait

from BasicLevel.urls import url_saucedemo

driver = webdriver.Chrome()
driver.get(url_saucedemo)
login_username = "standard_user"
login_password = "secret_sauce"
wait = WebDriverWait(driver,5)

username_field = wait.until(EC.visibility_of_element_located((By.ID,'user-name')))
username_field.send_keys(login_username)

password_field = wait.until(EC.visibility_of_element_located((By.ID,'password')))
password_field.send_keys(login_password)

submit_button = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))
submit_button.click()
time.sleep(2)

if driver.current_url == "https://www.saucedemo.com/inventory.html":
    print("Successful Login")


