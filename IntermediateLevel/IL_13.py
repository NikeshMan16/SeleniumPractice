"""13.	Perform mouse hover action.
o	Hover over a menu item and click a submenu option."""
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from urls import url_auto

driver = webdriver.Chrome()
driver.get(url_auto)
wait = WebDriverWait(driver, 5)
hover_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'dropbtn')))

actions = ActionChains(driver)
actions.move_to_element(hover_button).perform()

option = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="HTML3"]/div[1]/div/div/a[1]')))
option.click()
time.sleep(2)

