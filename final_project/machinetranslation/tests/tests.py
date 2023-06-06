import unittest #Python unit testing framework
from translator import english_to_french
from translator import french_to_english

class TestMethods(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


    def test_english_to_french_null(self):
        value = english_to_french('Bonjour')
        message = "Test value is not none."
        self.assertIsNotNone(value, message)


    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


    def test_french_to_english_null(self):
        value = None
        message = "Test value is not none."
        self.assertIsNone(value, message)


if __name__ == '__main__':
    unittest.main()
