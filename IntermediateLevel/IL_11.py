"""11.	Automate Login Functionality.
o	Open a login page, enter username and password, click login, and verify the result."""



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import url_sauce

driver = webdriver.Chrome()
driver.get(url_sauce)

login_username = "standard_user"
login_password = "secret_sauce"
wait = WebDriverWait(driver, 5)

username_field = wait.until(EC.visibility_of_element_located((By.ID,'user-name')))
username_field.send_keys(login_username)

password_field = wait.until(EC.visibility_of_element_located((By.ID,'password')))
password_field.send_keys(login_password)

submit_button = wait.until(EC.element_to_be_clickable((By.ID,'login-button')))
submit_button.click()

if "inventory.html" in driver.current_url:
    print("Login Successful")
else:
     print("Login has Failed")