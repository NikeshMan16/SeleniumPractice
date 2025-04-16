from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3/text()')

    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)

    def get_error_message(self):
        self.wait.until(EC.visibility_of_element_located(self.error_message))
        return self.get_text(self.error_message)

class DashboardPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.heading = (By.CLASS_NAME,'app_logo')

    def check_dashboard_heading_shown(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.heading))
            return True
        except TimeoutException:
            return False




