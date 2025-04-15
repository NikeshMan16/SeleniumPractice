"""17.	Automate double-click action.
o	Perform a double-click on a button and verify the resulting action."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from urls import url_auto

driver = webdriver.Chrome()
driver.get(url_auto)
driver.maximize_window()
wait = WebDriverWait(driver,5)
actions = ActionChains(driver)
field1 = driver.find_element(By.ID,'field1')
field2 = driver.find_element(By.ID,'field2')

double_click_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="HTML10"]/div[1]/button')))
actions.double_click(double_click_button).perform()

if field1.get_attribute("value") == field2.get_attribute("value"):
    print("Double click successful as text copied")
else:
    print("Double click failed as text not copied")


driver.quit()