"""12.	Handle multiple browser windows.
o	Click on a link that opens in a new tab and switch to it.
o	Extract its title and close it."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import url_auto

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get(url_auto)
original_window =driver.current_window_handle
# element = (By.XPATH,'//*[@id="HTML4"]/div[1]/button')
#
# driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth'});",element)
button_new = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="HTML4"]/div[1]/button')))
button_new.click()

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Extract the title from new window
print("Title is:", driver.title)
driver.close()
driver.switch_to.window(original_window)





