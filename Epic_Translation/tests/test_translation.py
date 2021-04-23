###############################################################################
# 
# test_translation.py
#
# Authors: Epic Systems Preternship Team
# Date:    April 20, 2021
#
# test_translation.py provides unit tests to check the accuracy of the
# translation script as compared to the sample data.
# 
###############################################################################

from .context import translation
import unittest


class TestTranslationMethods(unittest.TestCase):
    '''Test translation methods'''

    def test_call_api(self):
        phrase = translation.call_translate_api("as directed", "ES")
        self.assertEqual(phrase, "come se indica")
        phrase = translation.call_translate_api("come se indica", "EN")
        self.assertEqual(phrase, "as directed")

    def test_eng_to_esp_words(self):
        self.assertEqual('method call', 'expected result')

    def test_esp_to_eng_words(self):
        self.assertEqual('method call', 'expected result')

    def test_eng_to_esp_sentence(self):
        self.assertEqual('method call', 'expected result')
    
    def test_esp_to_eng_sentence(self):
        self.assertEqual('method call', 'expected result')
    
    def test_api_translation(self):
        self.assertEqual('method call', 'expected result')


if __name__ == '__main__':
    unittest.main()
