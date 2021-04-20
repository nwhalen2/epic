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

sys.path.insert(0, '~/epic/Epic_Translation/src/translation/')

import translation
import unittest


class TestTranslationMethods(unittest.TestCase):
    '''Test translation methods'''

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
