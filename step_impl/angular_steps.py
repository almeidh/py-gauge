from getgauge.python import step, before_scenario, Messages, DataStoreFactory

from utils.page_factory import PageFactory


# --------------------------
# Gauge step implementations
# --------------------------

@step("Application title is correct")
def check_title():
    title = PageFactory.angular_page.get_title()
    PageFactory.angular_page.assert_title(title)

@step("Add new greeting for user <name>")
def add_greeting(name):
    PageFactory.angular_page.scroll_to_element(PageFactory.angular_page.GREETING_INPUT)
    PageFactory.angular_page.set_text(PageFactory.angular_page.GREETING_INPUT, name)

@step("Check user greeting")
def verify_correct_greeting():
    greeting = PageFactory.angular_page.get_text(PageFactory.angular_page.FINAL_GREETING)
    PageFactory.angular_page.assert_greeting(greeting)
