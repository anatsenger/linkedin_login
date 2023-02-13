import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginLinkedin:
    def __init__(self, user: str, password: str):
        self.context = {
            'user': '//*[@id="session_key"]',
            'password': '//*[@id="session_password"]',
            'submit': '//*[@id="main-content"]/section[1]/div/div/form/button'
        }
        self.driver = webdriver.Chrome 
        self.user = user
        self.password = password

    def get_driver(self) -> webdriver:
        return self.driver

    def driver_open(self):
        driver = self.get_driver()
        self.driver = driver()
        self.get_driver().get('https://www.linkedin.com/')

    def user_element(self) -> WebElement or None:
        try:
            return self.get_driver().find_element(By.XPATH, self.context['user'])
        except Exception as e:
            print(e)
            return None

    def password_element(self) -> WebElement or None:
        try:
            return self.get_driver().find_element(By.XPATH, self.context['password'])
        except Exception as e:
            print(e)
            return None

    def submit_element(self) -> WebElement or None:
        try:
            return self.get_driver().find_element(By.XPATH, self.context['submit'])
        except Exception as e:
            print(e)
            return None


    def user_action(self):
        user = self.user_element()
        if user is not None:
            user.click()
            user.send_keys('anathaissenger@hotmail.com')
            time.sleep(1)


    def password_action(self):
        password = self.password_element()
        if password is not None:
            password.click()
            password.send_keys('')
            time.sleep(1)

    def submit_action(self):
        submit = self.submit_element()
        if submit is not None:
            submit.click()
            breakpoint()
