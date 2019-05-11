from getgauge.python import step, before_scenario, Messages, DataStoreFactory

from utils.page_factory import PageFactory


# --------------------------
# Gauge step implementations
# --------------------------

@step("The word <word> has <number> vowels.")
def assert_no_of_vowels_in(word, number):
    PageFactory.vowels_page.assert_no_of_vowels_in(word, number)


@step("Vowels in English language are <vowels>.")
def assert_default_vowels(given_vowels):
    PageFactory.vowels_page.assert_default_vowels(given_vowels)


@step("Almost all words have vowels <table>")
def assert_words_vowel_count(table):
    PageFactory.vowels_page.assert_table(table)