import os
import time

class BasePage(object):
    MSG = "Hello Gauge"

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        self.driver.find_element(*element).click()

    def set_text(self, element, text):
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(text)

    def get_text(self, element):
        return self.driver.find_element(*element).text

    def get_title(self):
        return self.driver.title

    def scroll_to_element(self, locator):
        target = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView()', target)

    def wait(self, timeout):
        time.sleep(timeout)
