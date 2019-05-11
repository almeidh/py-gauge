from selenium.webdriver.common.by import By
from getgauge.python import Messages
from pages.base_page import BasePage


class VowelsPage(BasePage):
    AngularMSG = BasePage.MSG + "from Angular Page"
    vowels = ["a", "e", "i", "o", "u"]

    def number_of_vowels(self, word):
        return len([elem for elem in list(word) if elem in self.vowels])

    def assert_no_of_vowels_in(self, word, number):
        assert str(number) == str(self.number_of_vowels(word))

    def assert_default_vowels(self, given_vowels):
        Messages.write_message("Given vowels are {0}".format(given_vowels))
        assert given_vowels == "".join(self.vowels)

    def assert_table(self, table):
        actual = [str(self.number_of_vowels(word)) for word in table.get_column_values_with_name("Word")]
        expected = [str(count) for count in table.get_column_values_with_name("Vowel Count")]
        assert expected == actual
