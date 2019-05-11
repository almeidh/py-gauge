from getgauge.python import before_suite, after_suite
from selenium import webdriver

from pages.vowels_page import VowelsPage
from pages.angular_page import AngularPage


class PageFactory:
    driver = webdriver.Chrome("D:\Workspace\py-gauge\drivers\chromedriver.exe")
    vowels_page = VowelsPage(driver)
    angular_page = AngularPage(driver)


@before_suite
def init():
    PageFactory.driver.get("https://angularjs.org")

@after_suite
def close():
    PageFactory.driver.close()
