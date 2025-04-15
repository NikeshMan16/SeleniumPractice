"""14.	Drag and drop an element.
o	Automate a drag-and-drop action on a webpage."""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from urls import url_auto

driver = webdriver.Chrome()
driver.get(url_auto)
wait = WebDriverWait(driver,5)

source = wait.until(EC.visibility_of_element_located((By.ID,'draggable')))
destination = wait.until(EC.visibility_of_element_located((By.ID,'droppable')))

driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});",source)

actions = ActionChains(driver)
actions.drag_and_drop(source,destination).perform()
time.sleep(2)

time.sleep(2)
msg_box = driver.find_element(By.XPATH,'//*[@id="droppable"]/p').text
if msg_box == "Dropped!":
    print("The items has been dragged and dropped!")
else:
    print("Failed to drag and drop the element.")