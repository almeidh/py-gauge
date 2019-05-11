from selenium.webdriver.common.by import By
from getgauge.python import Messages
from pages.base_page import BasePage

class AngularPageLocators:
    GREETING_INPUT = (By.CSS_SELECTOR, 'input[ng-model="yourName"]')
    FINAL_GREETING = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[2]/div/h1')


class AngularPage(BasePage, AngularPageLocators):
    app_title = "AngularJS — Superheroic JavaScript MVW Framework"
    correct_greeting = "Hello Almeid!"
    

    def assert_title(self, taken_title):
        Messages.write_message("Verifying correct title")
        assert str(taken_title) == str(self.app_title)

    def assert_greeting(self, taken_greeting):
        assert taken_greeting == self.correct_greeting
