"""15.	Handle a file upload scenario.
o	Automate a file upload using Selenium WebDriver."""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from urls import url_auto

driver = webdriver.Chrome()
driver.get(url_auto)
wait = WebDriverWait(driver,5)
file_path = r"C:\Users\nikes\OneDrive\Desktop\SeleniumPracticeCodingQuestions.docx"

single_file_upload  =wait.until(EC.visibility_of_element_located((By.ID,'singleFileInput')))
file_upload_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="singleFileForm"]/button')))

driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});",single_file_upload)
time.sleep(1.5)
single_file_upload.send_keys(file_path)
file_upload_button.click()
if wait.until(EC.visibility_of_element_located((By.ID,'singleFileStatus'))).is_displayed():
    print("Upload file has been successful")
else:
    print("Upload file failed.")


