import unittest

from translator import english_to_french, french_to_english

class TestCases(unittest.TestCase):
    """
    Class to run test cases for translation
    """
    def test_english_to_french(self):
        """
        Function to test the function english_to_french
        """
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")
    
    def test_french_to_english(self):
        """
        Function to test the function french_to_english
        """
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")
    
unittest.main()
